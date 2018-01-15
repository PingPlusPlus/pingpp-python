from __future__ import absolute_import, division, print_function

from pingpp import error, util, six
from pingpp.six.moves.urllib.parse import quote_plus
from pingpp.api_resources.abstract.app_based_api_resource import (
    AppBasedAPIResource)


class UserBasedAPIResource(AppBasedAPIResource):

    @classmethod
    def retrieve(cls, user, id, api_key=None, app=None, **params):
        instance = cls(id, api_key, **params)
        instance.refresh(app, user)
        return instance

    def refresh(self, app=None, user=None):
        self.refresh_from(self.request('get', self.instance_url(app, user)))
        return self

    @classmethod
    def class_name(cls):
        if cls == UserBasedAPIResource:
            raise NotImplementedError(
                'UserBasedAPIResource is an abstract class.  You should '
                'perform actions on its subclasses (e.g. Charge, Customer)')
        return super(UserBasedAPIResource, cls).class_name()

    @classmethod
    def class_url(cls, app=None, user=None):
        cls_name = cls.class_name()
        if not app:
            from pingpp import app_id
            app = app_id
        return "/v1/apps/%s/users/%s/%ss" % (app, user, cls_name)

    def instance_url(self, app=None, user=None):
        id = self.get('id')
        if not isinstance(id, six.string_types):
            raise error.InvalidRequestError(
                'Could not determine which URL to request: %s instance '
                'has invalid ID: %r, %s. ID should be of type `str` (or'
                ' `unicode`)' % (type(self).__name__, id, type(id)), 'id')

        id = util.utf8(id)
        base = self.class_url(app, user)
        extn = quote_plus(id)
        return "%s/%s" % (base, extn)
