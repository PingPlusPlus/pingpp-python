from __future__ import absolute_import, division, print_function

from pingpp import api_requestor, util
from pingpp.six.moves.urllib.parse import quote_plus
from pingpp.api_resources.abstract.user_based_api_resource import (
    UserBasedAPIResource)


class DeletableUserBasedAPIResource(UserBasedAPIResource):

    def delete(self, app=None, user=None, **params):
        self.refresh_from(self.request('delete',
                                       self.instance_url(app, user),
                                       params))
        return self

    @classmethod
    def _delete(cls, sid, api_key=None, app=None, user=None, **params):
        url = "%s/%s" % (cls.class_url(app, user), quote_plus(util.utf8(sid)))
        requestor = api_requestor.APIRequestor(api_key)
        response, api_key = requestor.request('delete', url, params)
        return util.convert_to_pingpp_object(response, api_key)
