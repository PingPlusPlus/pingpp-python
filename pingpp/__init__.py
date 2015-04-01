# Ping++ Python bindings
# Configuration variables

api_key = None
api_base = 'https://api.pingxx.com'
verify_ssl_certs = True

from pingpp.error import (
    PingppError, APIError, APIConnectionError, AuthenticationError, CardError,
    InvalidRequestError)

from pingpp.resource import Charge
from pingpp.resource import RedEnvelope

from pingpp.version import VERSION
from pingpp.api_requestor import APIRequestor
from pingpp.resource import (
    convert_to_pingpp_object, PingppObject, PingppObjectEncoder,
    APIResource, ListObject, SingletonAPIResource, ListableAPIResource,
    CreateableAPIResource, UpdateableAPIResource, DeletableAPIResource)

from pingpp.wxpub_oauth import WxpubOauth

api_version = VERSION
