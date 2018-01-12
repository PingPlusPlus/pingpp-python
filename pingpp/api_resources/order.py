from __future__ import absolute_import, division, print_function

import warnings
from pingpp import api_requestor, util
from pingpp.six.moves.urllib.parse import quote_plus

from pingpp.api_resources.abstract import CreateableAPIResource
from pingpp.api_resources.abstract import ListableAPIResource
from pingpp.api_resources.abstract import UpdateableAPIResource


class Order(CreateableAPIResource,
            ListableAPIResource,
            UpdateableAPIResource):
    OBJECT_NAME = 'order'

    @classmethod
    def pay(cls, id, api_key=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        url = "%s/%s/pay" % (cls.class_url(),
                             quote_plus(util.utf8(id)))
        response, api_key = requestor.request('post', url, params)

        return util.convert_to_pingpp_object(response, api_key)

    @classmethod
    def cancel(cls, id, api_key=None, **params):
        params['status'] = 'canceled'
        return cls.modify(id, api_key, **params)

    @classmethod
    def list_charges(cls, id, api_key=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        url = "%s/%s/charges" % (cls.class_url(),
                                 quote_plus(util.utf8(id)))
        response, api_key = requestor.request('get', url, params)
        return util.convert_to_pingpp_object(response, api_key)

    @classmethod
    def retrieve_charge(cls, id, charge_id, api_key=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        url = "%s/%s/charges/%s" % (cls.class_url(),
                                    quote_plus(util.utf8(id)),
                                    quote_plus(util.utf8(charge_id)))
        response, api_key = requestor.request('get', url, params)
        return util.convert_to_pingpp_object(response, api_key)

    @classmethod
    def refund(cls, id, api_key=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        url = "%s/%s/order_refunds" % (cls.class_url(),
                                       quote_plus(util.utf8(id)))
        response, api_key = requestor.request('post', url, params)
        return util.convert_to_pingpp_object(response, api_key)

    @classmethod
    def list_refunds(cls, id, api_key=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        url = "%s/%s/order_refunds" % (cls.class_url(),
                                       quote_plus(util.utf8(id)))
        response, api_key = requestor.request('get', url, params)
        return util.convert_to_pingpp_object(response, api_key)

    @classmethod
    def retrieve_refund(cls, id, refund_id, api_key=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        url = "%s/%s/order_refunds/%s" % (cls.class_url(),
                                          quote_plus(util.utf8(id)),
                                          quote_plus(util.utf8(refund_id)))
        response, api_key = requestor.request('get', url, params)
        return util.convert_to_pingpp_object(response, api_key)

    @classmethod
    def refund_list(cls, id, **params):
        warnings.warn("The `refund_list` method is deprecated and will"
                      "be removed in future versions. Please use the "
                      "`list_refunds` method instead",
                      DeprecationWarning)
        return cls.list_refunds(id, **params)

    @classmethod
    def refund_retrieve(cls, id, **params):
        warnings.warn("The `refund_retrieve` method is deprecated and will"
                      "be removed in future versions. Please use the "
                      "`retrieve_refund` method instead",
                      DeprecationWarning)
        return cls.retrieve_refund(id, **params)

    @classmethod
    def charge_list(cls, id, **params):
        warnings.warn("The `charge_list` method is deprecated and will"
                      "be removed in future versions. Please use the "
                      "`list_charges` method instead",
                      DeprecationWarning)
        return cls.list_charges(id, **params)

    @classmethod
    def charge_retrieve(cls, id, charge_id, **params):
        warnings.warn("The `charge_retrieve` method is deprecated and will"
                      "be removed in future versions. Please use the "
                      "`retrieve_charge` method instead",
                      DeprecationWarning)
        return cls.retrieve_charge(id, charge_id, **params)
