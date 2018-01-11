from __future__ import absolute_import, division, print_function

from pingpp import api_requestor, util
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

    def __init__(self, id=None, api_key=None, **params):
        super(CouponTemplate, self).__init__(id, api_key, **params)
        self.create_coupons = self.__create_coupons
        self.retrieve_coupons = self.__retrieve_coupons

    @classmethod
    def __operate_coupons(cls, api_key=None, app=None, coupon_tmpl=None,
                          method='get', **params):
        _instance = cls(coupon_tmpl, api_key, **params)
        url = _instance.__coupon_url(app)
        requestor = api_requestor.APIRequestor(api_key)
        response, api_key = requestor.request(method, url, params)
        return util.convert_to_pingpp_object(response, api_key)

    @classmethod
    def create_coupons(cls, api_key=None, app=None, coupon_tmpl=None,
                       **params):
        response = cls.__operate_coupons(api_key, app, coupon_tmpl,
                                         method='post', **params)
        return util.convert_to_pingpp_object(response, api_key)

    @classmethod
    def retrieve_coupons(cls, api_key=None, app=None, coupon_tmpl=None,
                         **params):
        response = cls.__operate_coupons(api_key, app, coupon_tmpl,
                                         method='get', **params)
        return util.convert_to_pingpp_object(response, api_key)

    def __create_coupons(self, app=None, **params):
        url = self.__return_req_url(app)
        self.refresh_from(self.request('post', url, params))
        return self

    def __retrieve_coupons(self, app=None):
        url = self.__return_req_url(app)
        self.refresh_from(self.request('get', url))
        return self

    def __coupon_url(self, app=None):
        return self.instance_url(app) + "/coupons"
