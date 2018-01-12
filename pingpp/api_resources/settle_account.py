from __future__ import absolute_import, division, print_function

from pingpp import api_requestor, util
from pingpp.six.moves.urllib.parse import quote_plus

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
    def delete(cls, user, id, app=None, api_key=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        url = "%s/%s" % (cls.class_url(app, user),
                         quote_plus(util.utf8(id)))
        response, api_key = requestor.request('delete', url, params)
        return util.convert_to_pingpp_object(response, api_key)

    @classmethod
    def update(cls, user, id, api_key=None, app=None, **params):
        return cls.modify(id, api_key=api_key, app=app, user=user, **params)
