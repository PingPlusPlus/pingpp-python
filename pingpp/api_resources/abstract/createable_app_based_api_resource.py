from __future__ import absolute_import, division, print_function

from pingpp import api_requestor, util
from pingpp.api_resources.abstract.app_based_api_resource import (
    AppBasedAPIResource)


class CreateableAppBasedAPIResource(AppBasedAPIResource):

    @classmethod
    def create(cls, api_key=None, app=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        url = cls.class_url(app)
        response, api_key = requestor.request('post', url, params)

        return util.convert_to_pingpp_object(response, api_key)
