from __future__ import absolute_import, division, print_function

from pingpp.api_resources.abstract import CreateableAPIResource
from pingpp.api_resources.abstract import ListableAPIResource
from pingpp.api_resources.abstract import UpdateableAPIResource


class Agreement(CreateableAPIResource, UpdateableAPIResource, ListableAPIResource):
    OBJECT_NAME = 'agreement'

    @classmethod
    def cancel(cls, id, api_key=None, **params):
        params['status'] = 'canceled'
        return cls.modify(id, api_key, **params)
