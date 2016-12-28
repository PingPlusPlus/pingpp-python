# -*- coding: utf-8 -*-

import calendar
import datetime
import platform
import time
import urllib
import urlparse
import warnings

import pingpp
from pingpp import error, http_client, version, util


def _encode_datetime(dttime):
    if dttime.tzinfo and dttime.tzinfo.utcoffset(dttime) is not None:
        utc_timestamp = calendar.timegm(dttime.utctimetuple())
    else:
        utc_timestamp = time.mktime(dttime.timetuple())

    return int(utc_timestamp)


def _api_encode(data):
    for key, value in data.iteritems():
        key = util.utf8(key)
        if value is None:
            continue
        elif hasattr(value, 'pingpp_id'):
            yield (key, value.pingpp_id)
        elif isinstance(value, list) or isinstance(value, tuple):
            for subvalue in value:
                yield ("%s[]" % (key,), util.utf8(subvalue))
        elif isinstance(value, dict):
            subdict = dict(('%s[%s]' % (key, subkey), subvalue) for
                           subkey, subvalue in value.iteritems())
            for subkey, subvalue in _api_encode(subdict):
                yield (subkey, subvalue)
        elif isinstance(value, datetime.datetime):
            yield (key, _encode_datetime(value))
        else:
            yield (key, util.utf8(value))


def _get_utc_timestamp():
    return str(int(time.time()))


def _build_api_url(url, query):
    scheme, netloc, path, base_query, fragment = urlparse.urlsplit(url)

    if base_query:
        query = '%s&%s' % (base_query, query)

    return urlparse.urlunsplit((scheme, netloc, path, query, fragment))


class APIRequestor(object):

    def __init__(self, key=None, client=None):
        self.api_key = key

        from pingpp import verify_ssl_certs

        self._client = client or http_client.new_default_http_client(
            verify_ssl_certs=verify_ssl_certs)

    @classmethod
    def api_url(cls, url=''):
        warnings.warn(
            'The `api_url` class method of APIRequestor is '
            'deprecated and will be removed.',
            DeprecationWarning)
        return '%s%s' % (pingpp.api_base, url)

    @classmethod
    def _deprecated_encode(cls, stk, key, value):
        warnings.warn(
            'The encode_* class methods of APIRequestor are deprecated and '
            'will be removed.',
            DeprecationWarning, stacklevel=2)
        stk.extend(_api_encode({key: value}))

    @classmethod
    def encode_dict(cls, stk, key, value):
        cls._deprecated_encode(stk, key, value)

    @classmethod
    def encode_list(cls, stk, key, value):
        cls._deprecated_encode(stk, key, value)

    @classmethod
    def encode_datetime(cls, stk, key, value):
        cls._deprecated_encode(stk, key, value)

    @classmethod
    def encode_none(cls, stk, key, value):
        cls._deprecated_encode(stk, key, value)

    @classmethod
    def encode(cls, d):
        """
        Internal: encode a string for url representation
        """
        warnings.warn(
            'The `encode` class method of APIRequestor is deprecated and '
            'will be removed.',
            DeprecationWarning)
        return urllib.urlencode(list(_api_encode(d)))

    @classmethod
    def build_url(cls, url, params):
        warnings.warn(
            'The `build_url` class method of APIRequestor is deprecated and '
            'will be removed.',
            DeprecationWarning)
        return _build_api_url(url, cls.encode(params))

    def request(self, method, url, params=None):
        rbody, rcode, my_api_key = self.request_raw(
            method.lower(), url, params)
        resp = self.interpret_response(rbody, rcode)
        return resp, my_api_key

    def handle_api_error(self, rbody, rcode, resp):
        try:
            err = resp['error']
        except (KeyError, TypeError):
            raise error.APIError(
                "Invalid response object from API: %r (HTTP response code "
                "was %d)" % (rbody, rcode),
                rbody, rcode, resp)

        if rcode in [400, 404]:
            raise error.InvalidRequestError(
                err.get('message'), err.get('param'), rbody, rcode, resp)
        elif rcode == 401:
            raise error.AuthenticationError(
                err.get('message'), rbody, rcode, resp)
        elif rcode == 402:
            raise error.ChannelError(
                err.get('message'), err.get('param'),
                err.get('code'), rbody, rcode, resp)
        else:
            raise error.APIError(err.get('message'), rbody, rcode, resp)

    def request_raw(self, method, url, params=None):
        """
        Mechanism for issuing an API call
        """

        from pingpp import api_version
        from pingpp import accept_language
        my_accept_language = accept_language
        request_utc_timestamp = _get_utc_timestamp()
        if self.api_key:
            my_api_key = self.api_key
        else:
            from pingpp import api_key
            my_api_key = api_key

        if my_api_key is None:
            raise error.AuthenticationError(
                'No API key provided. (HINT: set your API key using '
                '"pingpp.api_key = <API-KEY>"). You can generate API keys '
                'from the Ping++ web interface.  See https://pingxx.com '
                'for details.')

        abs_url = '%s%s' % (pingpp.api_base, url)

        encoded_params = urllib.urlencode(list(_api_encode(params or {})))

        if method == 'get' or method == 'delete':
            if params:
                abs_url = _build_api_url(abs_url, encoded_params)
            post_data = None
        elif method == 'post' or method == 'put':
            post_data = util.json.dumps(params).encode("utf-8")
        else:
            raise error.APIConnectionError(
                'Unrecognized HTTP method %r.  This may indicate a bug in the '
                'Ping++ bindings. ' % (method,))

        ua = {
            'bindings_version': version.VERSION,
            'lang': 'python',
            'publisher': 'pingpp',
            'httplib': self._client.name,
        }
        for attr, func in [['lang_version', platform.python_version],
                           ['platform', platform.platform],
                           ['uname', lambda: ' '.join(platform.uname())]]:
            try:
                val = func()
            except Exception as e:
                val = "!! %s" % (e,)
            ua[attr] = val

        headers = {
            'X-Pingpp-Client-User-Agent': util.json.dumps(ua),
            'User-Agent':
                'Pingplusplus/v1 PythonBindings/%s' % (version.VERSION,),
            'Authorization': 'Bearer %s' % (my_api_key,),
            'Accept-Language': my_accept_language,
            'Pingplusplus-Request-Timestamp': request_utc_timestamp
        }

        if method == "get" or method == "delete":
            post_data = None
            build_url = self.build_url(url, params)
        else:
            build_url = url

        rsa_data = self.get_rsa_verify_data(body=post_data, uri=build_url, timestamp=int(request_utc_timestamp))

        headers['Content-Type'] = 'application/json;charset=UTF-8'
        privkey = self.get_private_key()
        if privkey is not None:
            headers['Pingplusplus-Signature'] = self.rsa_sign(
                privkey, rsa_data)

        if api_version is not None:
            headers['Pingplusplus-Version'] = api_version

        rbody, rcode = self._client.request(
            method, abs_url, headers, post_data)

        util.logger.info(
            'API request to %s returned (response code, response body) of '
            '(%d, %r)',
            abs_url, rcode, rbody)
        return rbody, rcode, my_api_key

    def interpret_response(self, rbody, rcode):
        try:
            if hasattr(rbody, 'decode'):
                rbody = rbody.decode('utf-8')
            resp = util.json.loads(rbody)
        except Exception:
            raise error.APIError(
                "Invalid response body from API: %s "
                "(HTTP response code was %d)" % (rbody, rcode),
                rbody, rcode)
        if not (200 <= rcode < 300):
            self.handle_api_error(rbody, rcode, resp)
        return resp

    # Deprecated request handling.  Will all be removed in 2.0
    def _deprecated_request(self, impl, method, url, headers, params):
        warnings.warn(
            'The *_request functions of APIRequestor are deprecated and '
            'will be removed in version 2.0. Please use the client classes '
            ' in `pingpp.http_client` instead',
            DeprecationWarning, stacklevel=2)

        method = method.lower()

        if method == 'get' or method == 'delete':
            if params:
                url = self.build_url(url, params)
            post_data = None
        elif method == 'post' or method == 'put':
            post_data = self.encode(params)
        else:
            raise error.APIConnectionError(
                'Unrecognized HTTP method %r.  This may indicate a bug in the '
                'Ping++ bindings. ' % (method,))

        client = impl(verify_ssl_certs=self._client._verify_ssl_certs)
        return client.request(method, url, headers, post_data)

    def _deprecated_handle_error(self, impl, *args):
        warnings.warn(
            'The handle_*_error functions of APIRequestor are deprecated and '
            'will be removed in version 2.0. Please use the client classes '
            ' in `pingpp.http_client` instead',
            DeprecationWarning, stacklevel=2)

        client = impl(verify_ssl_certs=self._client._verify_ssl_certs)
        return client._handle_request_error(*args)

    def requests_request(self, meth, abs_url, headers, params):
        from pingpp.http_client import RequestsClient
        return self._deprecated_request(RequestsClient, meth, abs_url,
                                        headers, params)

    def handle_requests_error(self, err):
        from pingpp.http_client import RequestsClient
        return self._deprecated_handle_error(RequestsClient, err)

    def pycurl_request(self, meth, abs_url, headers, params):
        from pingpp.http_client import PycurlClient
        return self._deprecated_request(PycurlClient, meth, abs_url,
                                        headers, params)

    def handle_pycurl_error(self, err):
        from pingpp.http_client import PycurlClient
        return self._deprecated_handle_error(PycurlClient, err)

    def urlfetch_request(self, meth, abs_url, headers, params):
        from pingpp.http_client import UrlFetchClient
        return self._deprecated_request(UrlFetchClient, meth, abs_url,
                                        headers, params)

    def handle_urlfetch_error(self, err, abs_url):
        from pingpp.http_client import UrlFetchClient
        return self._deprecated_handle_error(UrlFetchClient, err, abs_url)

    def urllib2_request(self, meth, abs_url, headers, params):
        from pingpp.http_client import Urllib2Client
        return self._deprecated_request(Urllib2Client, meth, abs_url,
                                        headers, params)

    def handle_urllib2_error(self, err, abs_url):
        from pingpp.http_client import Urllib2Client
        return self._deprecated_handle_error(Urllib2Client, err)

    def get_private_key(self):
        from pingpp import private_key_path, private_key
        if private_key is not None:
            return private_key.strip()
        if private_key_path is not None:
            pingpp.private_key = open(private_key_path, "r").read()
            return pingpp.private_key.strip()
        return None

    def rsa_sign(self, private_key, data):
        from Crypto.PublicKey import RSA
        from Crypto.Signature import PKCS1_v1_5
        from Crypto.Hash import SHA256
        from base64 import b64encode
        rsa_key = RSA.importKey(private_key)
        signer = PKCS1_v1_5.new(rsa_key)
        digest = SHA256.new(data.encode())
        sign = signer.sign(digest)

        return b64encode(sign)

    def get_rsa_verify_data(self, body, uri, timestamp):
        verify_data = [body.decode()] if body else []
        verify_data.extend([uri, repr(timestamp)])
        return "".join(verify_data)
