from __future__ import absolute_import, division, print_function

from pingpp import api_requestor, util
from pingpp.six.moves.urllib.parse import quote_plus
from pingpp.api_resources.abstract.app_based_api_resource import (
    AppBasedAPIResource)


class DeletableAppBasedAPIResource(AppBasedAPIResource):

    def delete(self, app=None, **params):
        self.refresh_from(self.request('delete',
                                       self.instance_url(app),
                                       params))
        return self

    @classmethod
    def _delete(cls, sid, api_key=None, app=None, **params):
        url = "%s/%s" % (cls.class_url(app), quote_plus(util.utf8(sid)))
        requestor = api_requestor.APIRequestor(api_key)
        response, api_key = requestor.request('delete', url, params)
        return util.convert_to_pingpp_object(response, api_key)
