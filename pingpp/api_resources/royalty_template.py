from __future__ import absolute_import, division, print_function

from pingpp.api_resources.abstract import CreateableAPIResource
from pingpp.api_resources.abstract import ListableAPIResource
from pingpp.api_resources.abstract import UpdateableAPIResource
from pingpp.api_resources.abstract import DeletableAPIResource


class RoyaltyTemplate(CreateableAPIResource,
                      ListableAPIResource,
                      UpdateableAPIResource,
                      DeletableAPIResource):
    OBJECT_NAME = 'royalty_template'

    @classmethod
    def class_name(cls):
        return 'royalty_template'

    @classmethod
    def delete(cls, id, api_key=None, **params):
        return cls._delete(id, api_key=api_key, **params)

    @classmethod
    def update(cls, id, api_key=None, **params):
        return cls.modify(id, api_key=api_key, **params)
