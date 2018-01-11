from __future__ import absolute_import, division, print_function

from pingpp import api_requestor, util
from pingpp.six.moves.urllib.parse import quote_plus

from pingpp.api_resources.abstract import CreateableAppBasedAPIResource
from pingpp.api_resources.abstract import ListableAppBasedAPIResource


class Recharge(CreateableAppBasedAPIResource, ListableAppBasedAPIResource):
    OBJECT_NAME = 'recharge'

    @classmethod
    def refund(cls, id, api_key=None, app=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        url = "%s/%s/refunds" % (cls.class_url(app),
                                 quote_plus(util.utf8(id)))
        response, api_key = requestor.request('post', url, params)
        return util.convert_to_pingpp_object(response, api_key)

    @classmethod
    def refund_list(cls, id, api_key=None, app=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        url = "%s/%s/refunds" % (cls.class_url(app),
                                 quote_plus(util.utf8(id)))
        response, api_key = requestor.request('get', url, params)
        return util.convert_to_pingpp_object(response, api_key)

    @classmethod
    def refund_retrieve(cls, id, refund_id, api_key=None, app=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        url = "%s/%s/refunds/%s" % (cls.class_url(app),
                                    quote_plus(util.utf8(id)),
                                    quote_plus(util.utf8(refund_id)))
        response, api_key = requestor.request('get', url, params)
        return util.convert_to_pingpp_object(response, api_key)
