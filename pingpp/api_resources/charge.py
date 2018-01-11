from __future__ import absolute_import, division, print_function

from pingpp import api_requestor, error, util
from pingpp.six.moves.urllib.parse import quote_plus

from pingpp.api_resources.abstract import CreateableAPIResource
from pingpp.api_resources.abstract import ListableAPIResource


class Charge(CreateableAPIResource, ListableAPIResource):
    OBJECT_NAME = 'charge'

    @classmethod
    def refund(cls, id, api_key=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        url = "%s/%s/refunds" % (cls.class_url(),
                                 quote_plus(util.utf8(id)))
        response, api_key = requestor.request('post', url, params)

        return util.convert_to_pingpp_object(response, api_key)

    @classmethod
    def refund_list(cls, id, api_key=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        url = "%s/%s/refunds" % (cls.class_url(),
                                 quote_plus(util.utf8(id)))
        response, api_key = requestor.request('get', url, params)

        return util.convert_to_pingpp_object(response, api_key)

    @classmethod
    def refund_retrieve(cls, id, refund_id, api_key=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        url = "%s/%s/refunds/%s" % (cls.class_url(),
                                    quote_plus(util.utf8(id)),
                                    quote_plus(util.utf8(refund_id)))
        response, api_key = requestor.request('get', url, params)

        return util.convert_to_pingpp_object(response, api_key)

    @classmethod
    def list(cls, *args, **params):
        if params and params['app']['id'] is None:
            raise error.InvalidRequestError(
                'Please pass app[id] as parameter', 'app[id]')
        return super(Charge, cls).list(*args, **params)

    @classmethod
    def reverse(cls, charge_id=None, api_key=None, **params):
        url = cls.class_url() + '/%s/reverse' % quote_plus(
            util.utf8(charge_id))
        requestor = api_requestor.APIRequestor(api_key)
        response, api_key = requestor.request('post', url, params)
        return util.convert_to_pingpp_object(response, api_key)
