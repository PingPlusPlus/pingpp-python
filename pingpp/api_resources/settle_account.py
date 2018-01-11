from __future__ import absolute_import, division, print_function

from pingpp import api_requestor, util

from pingpp.api_resources.abstract import CreateableUserBasedAPIResource
from pingpp.api_resources.abstract import ListableUserBasedAPIResource
from pingpp.api_resources.abstract import DeletableUserBasedAPIResource


class SettleAccount(CreateableUserBasedAPIResource,
                    ListableUserBasedAPIResource,
                    DeletableUserBasedAPIResource):
    OBJECT_NAME = 'settle_account'

    @classmethod
    def class_name(cls):
        return 'settle_account'

    @classmethod
    def delete(cls, id=None, app=None, api_key=None, user=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        instance = cls(id, api_key)
        url = instance.instance_url(app, user)
        response, api_key = requestor.request('delete', url, params)
        return util.convert_to_pingpp_object(response, api_key)

    @classmethod
    def update(cls, id=None, api_key=None, app=None, user=None, **params):
        return cls.modify(id, api_key=api_key, app=app, user=user, **params)
