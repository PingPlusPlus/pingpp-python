from __future__ import absolute_import, division, print_function

from pingpp import api_requestor, util

from pingpp.api_resources.abstract import CreateableAPIResource
from pingpp.api_resources.abstract import ListableAPIResource
from pingpp.api_resources.abstract import UpdateableAPIResource


class Royalty(CreateableAPIResource,
              ListableAPIResource,
              UpdateableAPIResource):
    OBJECT_NAME = 'royalty'

    @classmethod
    def class_name(cls):
        return 'royaltie'

    @classmethod
    def update(cls, api_key=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        url = cls.class_url()
        response, api_key = requestor.request('put', url, params)
        return util.convert_to_pingpp_object(response, api_key)
