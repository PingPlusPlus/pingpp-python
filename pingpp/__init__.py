# -*- coding: utf-8 -*-
# Ping++ Python
# Configurations

api_key = None
api_base = 'https://api.pingxx.com'
verify_ssl_certs = True
accept_language = None
private_key_path = None
private_key = None
app_id = None

from pingpp.error import (  # noqa
    PingppError,
    APIError,
    APIConnectionError,
    AuthenticationError,
    ChannelError,
    InvalidRequestError)

from pingpp.resource import (  # noqa
    Charge,
    RedEnvelope,
    Event,
    Transfer,
    Customs,
    BatchRefund,
    BatchTransfer,
    Identification,
    )

from pingpp.version import VERSION  # noqa
from pingpp.api_requestor import APIRequestor  # noqa
from pingpp.resource import (  # noqa
    convert_to_pingpp_object,
    PingppObject,
    PingppObjectEncoder,
    APIResource,
    ListObject,
    SingletonAPIResource,
    ListableAPIResource,
    CreateableAPIResource,
    UpdateableAPIResource,
    DeletableAPIResource)
from pingpp.util import json, logger  # noqa
from pingpp.wxpub_oauth import WxpubOauth  # noqa

api_version = VERSION
