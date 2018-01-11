from __future__ import absolute_import, division, print_function

from pingpp import api_requestor, util
from pingpp.api_resources.abstract.app_based_api_resource import (
    AppBasedAPIResource)


class ListableAppBasedAPIResource(AppBasedAPIResource):

    @classmethod
    def auto_paging_iter(cls, *args, **params):
        return cls.list(*args, **params).auto_paging_iter()

    @classmethod
    def list(cls, api_key=None, app=None, **params):
        requestor = api_requestor.APIRequestor(api_key,
                                               api_base=cls.api_base())
        url = cls.class_url(app)
        response, api_key = requestor.request('get', url, params)
        pingpp_object = util.convert_to_pingpp_object(response, api_key)
        pingpp_object._retrieve_params = params
        return pingpp_object
