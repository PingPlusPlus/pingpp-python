# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

# Ping++ Python
# Configurations

api_key = None
api_base = 'https://api.pingxx.com'
verify_ssl_certs = True
api_version = None
accept_language = None
private_key_path = None
private_key = None
app_id = None
max_network_retries = 1
bad_gateway_match = True
connect_timeout = 30
timeout = 80
proxy = None
network_retry_delay = 0.5
ca_bundle = None

# Set to either 'debug' or 'info', controls console logging
log = None

# Resource
from pingpp.api_resources import *  # noqa

from pingpp.wxpub_oauth import WxpubOauth  # noqa

from pingpp.error import (  # noqa
    PingppError,
    APIError,
    APIConnectionError,
    AuthenticationError,
    ChannelError,
    InvalidRequestError)

# DEPRECATED: These imports will be moved out of the root pingpp namespace
# in the future

from pingpp.version import VERSION  # noqa
from pingpp.api_requestor import APIRequestor  # noqa

from pingpp.pingpp_object import PingppObject  # noqa
from pingpp.api_resources.abstract import (  # noqa
    APIResource,
    SingletonAPIResource,
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
    DeletableAPIResource)

from pingpp.util import (  # noqa
    convert_to_pingpp_object,
    json,
    logger)
