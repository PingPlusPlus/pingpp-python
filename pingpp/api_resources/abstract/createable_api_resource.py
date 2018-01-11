from __future__ import absolute_import, division, print_function

from pingpp.api_resources.abstract.api_resource import APIResource
from pingpp import api_requestor, util


class CreateableAPIResource(APIResource):

    @classmethod
    def create(cls, api_key=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        url = cls.class_url()
        response, api_key = requestor.request('post', url, params)

        return util.convert_to_pingpp_object(response, api_key)
