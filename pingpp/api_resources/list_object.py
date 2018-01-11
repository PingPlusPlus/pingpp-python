from __future__ import absolute_import, division, print_function

import warnings

from pingpp import util
from pingpp.pingpp_object import PingppObject

from pingpp.six.moves.urllib.parse import quote_plus


class ListObject(PingppObject):
    OBJECT_NAME = 'list'

    def all(self, **params):
        warnings.warn("The `all` method is deprecated and will"
                      "be removed in future versions. Please use the "
                      "`list` method instead",
                      DeprecationWarning)
        return self.list(**params)

    def list(self, **params):
        return self.request('get', self['url'], params)

    def create(self, **params):
        return self.request('post', self['url'], params)

    def retrieve(self, id, **params):
        base = self.get('url')
        id = util.utf8(id)
        extn = quote_plus(id)
        url = "%s/%s" % (base, extn)

        return self.request('get', url, params)

    def __iter__(self):
        return getattr(self, 'data', []).__iter__()

    def __len__(self):
        return getattr(self, 'data', []).__len__()
