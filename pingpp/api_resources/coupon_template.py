from __future__ import absolute_import, division, print_function

from pingpp import api_requestor, util
from pingpp.six.moves.urllib.parse import quote_plus

from pingpp.api_resources.abstract import CreateableAppBasedAPIResource
from pingpp.api_resources.abstract import ListableAppBasedAPIResource
from pingpp.api_resources.abstract import UpdateableAppBasedAPIResource


class CouponTemplate(CreateableAppBasedAPIResource,
                     ListableAppBasedAPIResource,
                     UpdateableAppBasedAPIResource):
    OBJECT_NAME = 'coupon_template'

    @classmethod
    def class_name(cls):
        return 'coupon_template'

    @classmethod
    def update(cls, sid, api_key=None, app=None, **params):
        return cls.modify(sid, api_key=api_key, app=None, **params)

    @classmethod
    def delete(cls, id, app=None, api_key=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        url = "%s/%s" % (cls.class_url(app),
                         quote_plus(util.utf8(id)))
        response, api_key = requestor.request('delete', url, params)
        return util.convert_to_pingpp_object(response, api_key)

    @classmethod
    def create_coupons(cls, id, api_key=None, app=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        url = "%s/%s/coupons" % (cls.class_url(app),
                                 quote_plus(util.utf8(id)))
        response, api_key = requestor.request('post', url, params)
        return util.convert_to_pingpp_object(response, api_key)

    @classmethod
    def list_coupons(cls, id, api_key=None, app=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        url = "%s/%s/coupons" % (cls.class_url(app),
                                 quote_plus(util.utf8(id)))
        response, api_key = requestor.request('get', url, params)
        return util.convert_to_pingpp_object(response, api_key)
