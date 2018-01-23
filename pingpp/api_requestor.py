# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import calendar
import datetime
import platform
import time

import pingpp
from pingpp import error, http_client, version, util, six
from pingpp.six.moves.urllib.parse import urlencode, urlsplit, urlunsplit
from pingpp.pingpp_response import PingppResponse


def _encode_datetime(dttime):
    if dttime.tzinfo and dttime.tzinfo.utcoffset(dttime) is not None:
        utc_timestamp = calendar.timegm(dttime.utctimetuple())
    else:
        utc_timestamp = time.mktime(dttime.timetuple())

    return int(utc_timestamp)


def _encode_nested_dict(key, data, fmt='%s[%s]'):
    d = {}
    for subkey, subvalue in six.iteritems(data):
        d[fmt % (key, subkey)] = subvalue
    return d


def _api_encode(data):
    for key, value in six.iteritems(data):
        key = util.utf8(key)
        if value is None:
            continue
        elif hasattr(value, 'pingpp_id'):
            yield (key, value.pingpp_id)
        elif isinstance(value, list) or isinstance(value, tuple):
            for sv in value:
                if isinstance(sv, dict):
                    subdict = _encode_nested_dict(key, sv, fmt='%s[][%s]')
                    for k, v in _api_encode(subdict):
                        yield (k, v)
                else:
                    yield ("%s[]" % (key,), util.utf8(sv))
        elif isinstance(value, dict):
            subdict = _encode_nested_dict(key, value)
            for subkey, subvalue in _api_encode(subdict):
                yield (subkey, subvalue)
        elif isinstance(value, datetime.datetime):
            yield (key, _encode_datetime(value))
        else:
            yield (key, util.utf8(value))


def _build_api_url(url, query):
    scheme, netloc, path, base_query, fragment = urlsplit(url)

    if base_query:
        query = '%s&%s' % (base_query, query)

    return urlunsplit((scheme, netloc, path, query, fragment))


def _get_utc_timestamp():
    return str(int(time.time()))


class APIRequestor(object):

    def __init__(self, key=None, client=None, api_base=None, api_version=None):
        self.api_base = api_base or pingpp.api_base
        self.api_key = key
        self.api_version = api_version or pingpp.api_version

        from pingpp import verify_ssl_certs as verify
        from pingpp import proxy
        from pingpp import ca_bundle

        self._client = client or http_client.new_default_http_client(
            verify_ssl_certs=verify, proxy=proxy, ca_bundle=ca_bundle)

    def request(self, method, url, params=None, headers=None):
        rbody, rcode, rheaders, my_api_key = self.request_raw(
            method.lower(), url, params, headers)
        resp = self.interpret_response(rbody, rcode, rheaders)
        return resp, my_api_key

    def handle_error_response(self, rbody, rcode, resp, rheaders):
        try:
            error_data = resp['error']
        except (KeyError, TypeError):
            raise error.APIError(
                "Invalid response object from API: %r (HTTP response code "
                "was %d)" % (rbody, rcode),
                rbody, rcode, resp)

        err = self.specific_api_error(
            rbody, rcode, resp, rheaders, error_data)

        raise err

    def specific_api_error(self, rbody, rcode, resp, rheaders, error_data):
        util.log_info(
            'Ping++ API error received',
            error_code=error_data.get('code'),
            error_type=error_data.get('type'),
            error_message=error_data.get('message'),
            error_param=error_data.get('param'),
        )

        if rcode in [400, 404]:
            raise error.InvalidRequestError(
                error_data.get('message'), error_data.get('param'),
                error_data.get('code'), rbody, rcode, resp, rheaders)
        elif rcode == 401:
            raise error.AuthenticationError(
                error_data.get('message'), rbody, rcode, resp, rheaders)
        elif rcode == 402:
            raise error.ChannelError(
                error_data.get('message'), error_data.get('param'),
                error_data.get('code'), rbody, rcode, resp, rheaders)
        elif rcode == 403:
            raise error.RateLimitError(
                error_data.get('message'), rbody, rcode, resp, rheaders)
        else:
            raise error.APIError(
                error_data.get('message'), rbody, rcode, resp, rheaders)

    def request_headers(self, api_key, method):
        user_agent = 'Pingpp/v1 PythonBindings/%s' % (version.VERSION,)

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
            'User-Agent': user_agent,
            'Authorization': 'Bearer %s' % (api_key,),
            'Accept-Language': pingpp.accept_language,
            'Content-Type': 'application/json; charset=UTF-8',
        }

        if self.api_version is not None:
            headers['Pingplusplus-Version'] = self.api_version

        return headers

    def request_raw(self, method, url, params=None, supplied_headers=None):
        """
        Mechanism for issuing an API call
        """

        if self.api_key:
            my_api_key = self.api_key
        else:
            from pingpp import api_key
            my_api_key = api_key

        if my_api_key is None:
            raise error.AuthenticationError(
                'No API key provided. (HINT: set your API key using '
                '"pingpp.api_key = <API-KEY>"). You can generate API keys '
                'from the Ping++ web interface.  '
                'See https://www.pingxx.com/api for details.')

        abs_url = '%s%s' % (self.api_base, url)
        request_uri = url

        if method == 'get' or method == 'delete':
            if params:
                encoded_params = urlencode(list(_api_encode(params or {})))
                abs_url = _build_api_url(abs_url, encoded_params)
                request_uri = _build_api_url(url, encoded_params)
            post_data = None
        elif method == 'post' or method == 'put':
            post_data = util.json.dumps(params).encode("utf-8")
        else:
            raise error.APIConnectionError(
                'Unrecognized HTTP method %r.  This may indicate a bug in the '
                'Ping++ bindings. ' % (method,))

        headers = self.request_headers(my_api_key, method)

        if supplied_headers is not None:
            for key, value in six.iteritems(supplied_headers):
                headers[key] = value

        request_utc_timestamp = _get_utc_timestamp()
        headers['Pingplusplus-Request-Timestamp'] = request_utc_timestamp
        rsa_data = self.get_rsa_verify_data(
            post_data, request_uri, int(request_utc_timestamp))
        util.log_debug('Signing data', data=rsa_data)

        privkey = self.get_private_key()
        if privkey is not None:
            headers['Pingplusplus-Signature'] = self.rsa_sign(
                privkey, rsa_data)

        rbody, rcode, rheaders = self.execute_request_with_retry(
            method, abs_url, headers, post_data)

        return rbody, rcode, rheaders, my_api_key

    def execute_request_with_retry(self, method, abs_url, headers, post_data):
        retry_count = 0
        rbody, rcode, rheaders = self.execute_request(
            method, abs_url, headers, post_data)

        if pingpp.bad_gateway_match:
            from pingpp import max_network_retries, network_retry_delay
            while retry_count < max_network_retries and rcode == 502:
                retry_count += 1
                time.sleep(network_retry_delay)
                rbody, rcode, rheaders = self.execute_request(
                    method, abs_url, headers, post_data)

        return rbody, rcode, rheaders

    def execute_request(self, method, abs_url, headers, post_data):
        util.log_info('Request to Ping api', method=method, path=abs_url)
        util.log_debug(
            'Post details',
            post_data=post_data, api_version=self.api_version)

        rbody, rcode, rheaders = self._client.request(
            method, abs_url, headers, post_data)

        util.log_info(
            'Ping++ API response', path=abs_url, response_code=rcode)
        util.log_debug('API response body', body=rbody)

        return rbody, rcode, rheaders

    def interpret_response(self, rbody, rcode, rheaders):
        try:
            if hasattr(rbody, 'decode'):
                rbody = rbody.decode('utf-8')
            resp = PingppResponse(rbody, rcode, rheaders)
        except Exception:
            raise error.APIError(
                "Invalid response body from API: %s "
                "(HTTP response code was %d)" % (rbody, rcode),
                rbody, rcode, rheaders)
        if not (200 <= rcode < 300):
            self.handle_error_response(rbody, rcode, resp.data, rheaders)

        return resp

    def get_private_key(self):
        from pingpp import private_key
        if private_key is not None:
            return private_key.strip()

        from pingpp import private_key_path
        if private_key_path is not None:
            f = open(private_key_path, "r")
            pingpp.private_key = f.read()
            f.close()
            return pingpp.private_key.strip()
        return None

    def rsa_sign(self, private_key, data):
        from Crypto.PublicKey import RSA
        from Crypto.Signature import PKCS1_v1_5
        from Crypto.Hash import SHA256
        from base64 import b64encode

        rsa_key = RSA.importKey(private_key)
        sign = PKCS1_v1_5.new(rsa_key).sign(SHA256.new(data.encode()))
        return b64encode(sign)

    def get_rsa_verify_data(self, body, uri, timestamp):
        verify_data = [body.decode()] if body else []
        verify_data.extend([uri, repr(timestamp)])
        return "".join(verify_data)
