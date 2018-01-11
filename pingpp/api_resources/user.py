from __future__ import absolute_import, division, print_function

from pingpp.api_resources.abstract import CreateableAppBasedAPIResource
from pingpp.api_resources.abstract import ListableAppBasedAPIResource
from pingpp.api_resources.abstract import UpdateableAppBasedAPIResource
from pingpp.api_resources.abstract import DeletableAppBasedAPIResource


class User(CreateableAppBasedAPIResource,
           ListableAppBasedAPIResource,
           UpdateableAppBasedAPIResource,
           DeletableAppBasedAPIResource):
    OBJECT_NAME = 'user'

    @classmethod
    def update(cls, api_key=None, app=None, user=None, **params):
        return cls.modify(user, api_key=api_key, app=app, **params)
