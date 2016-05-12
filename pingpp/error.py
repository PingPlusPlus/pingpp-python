# -*- coding: utf-8 -*-
# Exceptions


class PingppError(Exception):

    def __init__(self, message=None, http_body=None, http_status=None,
                 json_body=None):
        super(PingppError, self).__init__(message)

        self.http_body = http_body

        self.http_status = http_status
        self.json_body = json_body


class APIError(PingppError):
    pass


class APIConnectionError(PingppError):
    pass


class ChannelError(PingppError):

    def __init__(self, message, param, code, http_body=None,
                 http_status=None, json_body=None):
        super(ChannelError, self).__init__(
            message, http_body, http_status, json_body)
        self.param = param
        self.code = code


class InvalidRequestError(PingppError):

    def __init__(self, message, param, http_body=None,
                 http_status=None, json_body=None):
        super(InvalidRequestError, self).__init__(
            message, http_body, http_status, json_body)
        self.param = param


class AuthenticationError(PingppError):
    pass
