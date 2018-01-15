from __future__ import absolute_import, division, print_function

from pingpp import api_requestor, util
from pingpp.six.moves.urllib.parse import quote_plus

from pingpp.api_resources.abstract import CreateableAppBasedAPIResource
from pingpp.api_resources.abstract import ListableAppBasedAPIResource
from pingpp.api_resources.abstract import UpdateableAppBasedAPIResource


class SubApp(CreateableAppBasedAPIResource,
             ListableAppBasedAPIResource,
             UpdateableAppBasedAPIResource):
    OBJECT_NAME = 'sub_app'

    @classmethod
    def class_name(cls):
        return 'sub_app'

    @classmethod
    def update(cls, sid, api_key=None, app=None, **params):
        return cls.modify(sid, api_key=api_key, app=None, **params)

    @classmethod
    def delete(cls, id, api_key=None, app=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        url = "%s/%s" % (cls.class_url(app),
                         quote_plus(util.utf8(id)))
        response, api_key = requestor.request('delete', url, params)
        return util.convert_to_pingpp_object(response, api_key)

    @classmethod
    def create_channel(cls, sub_app, api_key=None, app=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        url = "%s/%s/channels" % (cls.class_url(app),
                                  quote_plus(util.utf8(sub_app)))
        response, api_key = requestor.request('post', url, params)
        return util.convert_to_pingpp_object(response, api_key)

    @classmethod
    def retrieve_channel(cls, sub_app, channel, api_key=None, app=None,
                         **params):
        requestor = api_requestor.APIRequestor(api_key)
        url = "%s/%s/channels/%s" % (cls.class_url(app),
                                     quote_plus(util.utf8(sub_app)),
                                     quote_plus(util.utf8(channel)))
        response, api_key = requestor.request('get', url, params)
        return util.convert_to_pingpp_object(response, api_key)

    @classmethod
    def update_channel(cls, sub_app, channel, api_key=None, app=None,
                       **params):
        requestor = api_requestor.APIRequestor(api_key)
        url = "%s/%s/channels/%s" % (cls.class_url(app),
                                     quote_plus(util.utf8(sub_app)),
                                     quote_plus(util.utf8(channel)))
        response, api_key = requestor.request('put', url, params)
        return util.convert_to_pingpp_object(response, api_key)

    @classmethod
    def delete_channel(cls, sub_app, channel, api_key=None, app=None,
                       **params):
        requestor = api_requestor.APIRequestor(api_key)
        url = "%s/%s/channels/%s" % (cls.class_url(app),
                                     quote_plus(util.utf8(sub_app)),
                                     quote_plus(util.utf8(channel)))
        response, api_key = requestor.request('delete', url, params)
        return util.convert_to_pingpp_object(response, api_key)

    @classmethod
    def create_transfer_channel(cls, sub_app, api_key=None, app=None,
                                **params):
        requestor = api_requestor.APIRequestor(api_key)
        url = "%s/%s/transfer_channels" % (cls.class_url(app),
                                           quote_plus(util.utf8(sub_app)))
        response, api_key = requestor.request('post', url, params)
        return util.convert_to_pingpp_object(response, api_key)

    @classmethod
    def retrieve_transfer_channel(cls, sub_app, channel, api_key=None,
                                  app=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        url = "%s/%s/transfer_channels/%s" % (cls.class_url(app),
                                              quote_plus(util.utf8(sub_app)),
                                              quote_plus(util.utf8(channel)))
        response, api_key = requestor.request('get', url, params)
        return util.convert_to_pingpp_object(response, api_key)

    @classmethod
    def update_transfer_channel(cls, sub_app, channel, api_key=None, app=None,
                                **params):
        requestor = api_requestor.APIRequestor(api_key)
        url = "%s/%s/transfer_channels/%s" % (cls.class_url(app),
                                              quote_plus(util.utf8(sub_app)),
                                              quote_plus(util.utf8(channel)))
        response, api_key = requestor.request('put', url, params)
        return util.convert_to_pingpp_object(response, api_key)

    @classmethod
    def delete_transfer_channel(cls, sub_app, channel, api_key=None, app=None,
                                **params):
        requestor = api_requestor.APIRequestor(api_key)
        url = "%s/%s/transfer_channels/%s" % (cls.class_url(app),
                                              quote_plus(util.utf8(sub_app)),
                                              quote_plus(util.utf8(channel)))
        response, api_key = requestor.request('delete', url, params)
        return util.convert_to_pingpp_object(response, api_key)
