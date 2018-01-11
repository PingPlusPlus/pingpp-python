from __future__ import absolute_import, division, print_function

from pingpp import api_requestor, util
from pingpp.six.moves.urllib.parse import quote_plus
from pingpp.api_resources.abstract.user_based_api_resource import (
    UserBasedAPIResource)


class UpdateableUserBasedAPIResource(UserBasedAPIResource):

    @classmethod
    def _modify(cls, url, api_key=None, app=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        response, api_key = requestor.request('put', url, params)
        return util.convert_to_pingpp_object(response, api_key)

    @classmethod
    def modify(cls, sid, api_key=None, app=None, user=None, **params):
        url = "%s/%s" % (cls.class_url(app, user), quote_plus(util.utf8(sid)))
        return cls._modify(url, api_key=api_key, **params)
