# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from pingpp import six


class PingppError(Exception):

    def __init__(self, message=None, http_body=None, http_status=None,
                 json_body=None, headers=None):
        super(PingppError, self).__init__(message)

        if http_body and hasattr(http_body, 'decode'):
            try:
                http_body = http_body.decode('utf-8')
            except BaseException:
                http_body = ('<Could not decode body as utf-8.>')

        self._message = message
        self.http_body = http_body
        self.http_status = http_status
        self.json_body = json_body
        self.headers = headers or {}

    def __unicode__(self):
        return self._message

    if six.PY3:
        def __str__(self):
            return self.__unicode__()
    else:
        def __str__(self):
            return unicode(self).encode('utf-8')


class APIError(PingppError):
    pass


class APIConnectionError(PingppError):
    pass


class ChannelError(PingppError):

    def __init__(self, message, param, code, http_body=None,
                 http_status=None, json_body=None, headers=None):
        super(ChannelError, self).__init__(
            message, http_body, http_status, json_body,
            headers)
        self.param = param
        self.code = code


class InvalidRequestError(PingppError):

    def __init__(self, message, param, code=None, http_body=None,
                 http_status=None, json_body=None, headers=None):
        super(InvalidRequestError, self).__init__(
            message, http_body, http_status, json_body,
            headers)
        self.param = param
        self.code = code


class AuthenticationError(PingppError):
    pass


class RateLimitError(PingppError):
    pass
