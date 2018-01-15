from __future__ import absolute_import, division, print_function

from pingpp import error, util, six
from pingpp.api_resources.abstract.api_resource import APIResource
from pingpp.six.moves.urllib.parse import quote_plus


class AppBasedAPIResource(APIResource):

    @classmethod
    def retrieve(cls, id, api_key=None, app=None, **params):
        instance = cls(id, api_key, **params)
        instance.refresh(app)
        return instance

    def refresh(self, app=None):
        self.refresh_from(self.request('get', self.instance_url(app)))
        return self

    @classmethod
    def class_name(cls):
        if cls == AppBasedAPIResource:
            raise NotImplementedError(
                'AppBasedAPIResource is an abstract class.  You should '
                'perform actions on its subclasses (e.g. Charge, Customer)')
        return super(AppBasedAPIResource, cls).class_name()

    @classmethod
    def class_url(cls, app=None):
        cls_name = cls.class_name()
        if not app:
            from pingpp import app_id
            app = app_id
        return "/v1/apps/%s/%ss" % (quote_plus(app), cls_name)

    def instance_url(self, app=None):
        id = self.get('id')
        if not isinstance(id, six.string_types):
            raise error.InvalidRequestError(
                'Could not determine which URL to request: %s instance '
                'has invalid ID: %r, %s. ID should be of type `str` (or'
                ' `unicode`)' % (type(self).__name__, id, type(id)), 'id')

        id = util.utf8(id)
        base = self.class_url(app)
        extn = id if self.class_name() == "user" else quote_plus(id)
        return "%s/%s" % (base, extn)
