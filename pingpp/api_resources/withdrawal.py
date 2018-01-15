from __future__ import absolute_import, division, print_function

from pingpp.api_resources.abstract import CreateableAppBasedAPIResource
from pingpp.api_resources.abstract import ListableAppBasedAPIResource
from pingpp.api_resources.abstract import UpdateableAppBasedAPIResource


class Withdrawal(CreateableAppBasedAPIResource,
                 ListableAppBasedAPIResource,
                 UpdateableAppBasedAPIResource):
    OBJECT_NAME = 'withdrawal'

    @classmethod
    def cancel(cls, id, api_key=None, app=None):
        params = {"status": "canceled"}
        return cls.modify(id, api_key=api_key, app=app, **params)

    @classmethod
    def confirm(cls, id, api_key=None, app=None):
        params = {"status": "pending"}
        return cls.modify(id, api_key=api_key, app=app, **params)
