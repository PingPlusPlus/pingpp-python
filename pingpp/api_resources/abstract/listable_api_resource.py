from __future__ import absolute_import, division, print_function

import warnings

from pingpp import api_requestor, util
from pingpp.api_resources.abstract.api_resource import APIResource


class ListableAPIResource(APIResource):

    @classmethod
    def all(cls, *args, **params):
        warnings.warn("The `all` class method is deprecated and will"
                      "be removed in future versions. Please use the "
                      "`list` class method instead",
                      DeprecationWarning)
        return cls.list(*args, **params)

    @classmethod
    def auto_paging_iter(cls, *args, **params):
        return cls.list(*args, **params).auto_paging_iter()

    @classmethod
    def list(cls, api_key=None, **params):
        requestor = api_requestor.APIRequestor(api_key,
                                               api_base=cls.api_base())
        url = cls.class_url()
        response, api_key = requestor.request('get', url, params)
        pingpp_object = util.convert_to_pingpp_object(response, api_key)
        pingpp_object._retrieve_params = params
        return pingpp_object
