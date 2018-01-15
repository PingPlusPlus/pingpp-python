from __future__ import absolute_import, division, print_function

from pingpp import util
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
    def update(cls, id, api_key=None, app=None, **params):
        return cls.modify(id, api_key=api_key, app=app, **params)

    @classmethod
    def modify(cls, sid, api_key=None, app=None, **params):
        url = "%s/%s" % (cls.class_url(app), util.utf8(sid))
        return cls._modify(url, api_key=api_key, **params)
