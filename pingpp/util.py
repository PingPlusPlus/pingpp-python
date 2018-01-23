# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import hmac
import io
import logging
import sys
import os
import re

import pingpp
from pingpp import six

PINGPP_LOG = os.environ.get('PINGPP_LOG')

logger = logging.getLogger('pingpp')

__all__ = [
    'io',
    'parse_qsl',
    'json',
    'utf8',
    'log_info',
    'log_debug',
    'logfmt',
]

try:
    from pingpp.six.moves.urllib.parse import parse_qsl
except ImportError:
    # Python < 2.6
    from cgi import parse_qsl

try:
    import json
except ImportError:
    json = None

if not (json and hasattr(json, 'loads')):
    try:
        import simplejson as json
    except ImportError:
        if not json:
            raise ImportError(
                "Ping++ requires a JSON library, such as simplejson. "
                "HINT: Try installing the "
                "python simplejson library via 'pip install simplejson' or "
                "'easy_install simplejson'.")
        else:
            raise ImportError(
                "Ping++ requires a JSON library with the same interface as "
                "the Python 2.6 'json' library.  You appear to have a 'json' "
                "library with a different interface.  Please install "
                "the simplejson library.  HINT: Try installing the "
                "python simplejson library via 'pip install simplejson' "
                "or 'easy_install simplejson'.")


def utf8(value):
    if six.PY2 and isinstance(value, unicode):
        return value.encode('utf-8')
    else:
        return value


def is_appengine_dev():
    return ('APPENGINE_RUNTIME' in os.environ and
            'Dev' in os.environ.get('SERVER_SOFTWARE', ''))


def _console_log_level():
    if pingpp.log in ['debug', 'info']:
        return pingpp.log
    elif PINGPP_LOG in ['debug', 'info']:
        return PINGPP_LOG
    else:
        return None


def log_debug(message, **params):
    msg = logfmt(dict(message=message, **params))
    if _console_log_level() == 'debug':
        print(msg, file=sys.stderr)
    logger.debug(msg)


def log_info(message, **params):
    msg = logfmt(dict(message=message, **params))
    if _console_log_level() in ['debug', 'info']:
        print(msg, file=sys.stderr)
    logger.info(msg)


def _test_or_live_environment():
    if pingpp.api_key is None:
        return
    match = re.match(r'sk_(live|test)_', pingpp.api_key)
    if match is None:
        return
    return match.groups()[0]


def logfmt(props):
    def fmt(key, val):
        # Handle case where val is a bytes or bytesarray
        if six.PY3 and hasattr(val, 'decode'):
            val = val.decode('utf-8')
        # Check if val is already a string to avoid re-encoding into
        # ascii. Since the code is sent through 2to3, we can't just
        # use unicode(val, encoding='utf8') since it will be
        # translated incorrectly.
        if not isinstance(val, six.string_types):
            val = six.text_type(val)
        if re.search(r'\s', val):
            val = repr(val)
        # key should already be a string
        if re.search(r'\s', key):
            key = repr(key)
        return u'{key}={val}'.format(key=key, val=val)
    return u' '.join([fmt(key, val) for key, val in sorted(props.items())])


# Borrowed from Django's source code
if hasattr(hmac, 'compare_digest'):
    # Prefer the stdlib implementation, when available.
    def secure_compare(val1, val2):
        return hmac.compare_digest(utf8(val1), utf8(val2))
else:
    def secure_compare(val1, val2):
        """
        Returns True if the two strings are equal, False otherwise.
        The time taken is independent of the number of characters that match.
        For the sake of simplicity, this function executes in constant time
        only when the two strings have the same length. It short-circuits when
        they have different lengths.
        """
        val1, val2 = utf8(val1), utf8(val2)
        if len(val1) != len(val2):
            return False
        result = 0
        if six.PY3 and isinstance(val1, bytes) and isinstance(val2, bytes):
            for x, y in zip(val1, val2):
                result |= x ^ y
        else:
            for x, y in zip(val1, val2):
                result |= ord(x) ^ ord(y)
        return result == 0


OBJECT_CLASSES = {}


def load_object_classes():
    # This is here to avoid a circular dependency
    from pingpp import api_resources

    global OBJECT_CLASSES

    OBJECT_CLASSES = {
        # data structures
        api_resources.ListObject.OBJECT_NAME: api_resources.ListObject,

        # business objects
        api_resources.BalanceBonus.OBJECT_NAME: api_resources.BalanceBonus,
        api_resources.BalanceTransaction.OBJECT_NAME:
            api_resources.BalanceTransaction,
        api_resources.BalanceTransfer.OBJECT_NAME:
            api_resources.BalanceTransfer,
        api_resources.BatchRefund.OBJECT_NAME: api_resources.BatchRefund,
        api_resources.BatchTransfer.OBJECT_NAME: api_resources.BatchTransfer,
        api_resources.BatchWithdrawal.OBJECT_NAME:
            api_resources.BatchWithdrawal,
        api_resources.Channel.OBJECT_NAME: api_resources.Channel,
        api_resources.Charge.OBJECT_NAME: api_resources.Charge,
        api_resources.Coupon.OBJECT_NAME: api_resources.Coupon,
        api_resources.CouponTemplate.OBJECT_NAME: api_resources.CouponTemplate,
        api_resources.Customs.OBJECT_NAME: api_resources.Customs,
        api_resources.Event.OBJECT_NAME: api_resources.Event,
        api_resources.Identification.OBJECT_NAME: api_resources.Identification,
        api_resources.Order.OBJECT_NAME: api_resources.Order,
        api_resources.Recharge.OBJECT_NAME: api_resources.Recharge,
        api_resources.RedEnvelope.OBJECT_NAME: api_resources.RedEnvelope,
        api_resources.Refund.OBJECT_NAME: api_resources.Refund,
        api_resources.Royalty.OBJECT_NAME: api_resources.Royalty,
        api_resources.RoyaltySettlement.OBJECT_NAME:
            api_resources.RoyaltySettlement,
        api_resources.RoyaltyTemplate.OBJECT_NAME:
            api_resources.RoyaltyTemplate,
        api_resources.RoyaltyTransaction.OBJECT_NAME:
            api_resources.RoyaltyTransaction,
        api_resources.SettleAccount.OBJECT_NAME: api_resources.SettleAccount,
        api_resources.SubApp.OBJECT_NAME: api_resources.SubApp,
        api_resources.Transfer.OBJECT_NAME: api_resources.Transfer,
        api_resources.User.OBJECT_NAME: api_resources.User,
        api_resources.Withdrawal.OBJECT_NAME: api_resources.Withdrawal,
    }


def convert_to_pingpp_object(resp, api_key=None):
    global OBJECT_CLASSES

    if len(OBJECT_CLASSES) == 0:
        load_object_classes()
    types = OBJECT_CLASSES.copy()

    # If we get a PingppResponse, we'll want to return a
    # PingppObject with the last_response field filled out with
    # the raw API response information
    pingpp_response = None

    if isinstance(resp, pingpp.pingpp_response.PingppResponse):
        pingpp_response = resp
        resp = pingpp_response.data

    if isinstance(resp, list):
        return [convert_to_pingpp_object(i, api_key) for i in resp]
    elif isinstance(resp, dict) and \
            not isinstance(resp, pingpp.pingpp_object.PingppObject):
        resp = resp.copy()
        klass_name = resp.get('object')
        if isinstance(klass_name, six.string_types):
            klass = types.get(klass_name, pingpp.pingpp_object.PingppObject)
        else:
            klass = pingpp.pingpp_object.PingppObject

        return klass.construct_from(resp, api_key,
                                    last_response=pingpp_response)
    else:
        return resp


def convert_array_to_dict(arr):
    if isinstance(arr, list):
        d = {}
        for i, value in enumerate(arr):
            d[str(i)] = value
        return d
    else:
        return arr


def ca_bundle_path(ca_bundle):
    if ca_bundle and os.path.exists(os.path.realpath(ca_bundle)):
        return os.path.realpath(ca_bundle)
    else:
        return os.path.join(
            os.path.dirname(__file__), 'data/ca-certificates.crt')
