from __future__ import absolute_import, division, print_function

from pingpp import api_requestor, util

from pingpp.api_resources.abstract import CreateableAPIResource


class CardInfo(CreateableAPIResource):
    OBJECT_NAME = 'card_info'

    @classmethod
    def class_name(cls):
        return 'card_info'

    @classmethod
    def class_url(cls):
        cls_name = cls.class_name()
        return "/v1/%s" % (cls_name,)

    @classmethod
    def query(cls, api_key=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        url = cls.class_url()
        response, api_key = requestor.request('post', url, params)
        return util.convert_to_pingpp_object(response, api_key)
