from __future__ import absolute_import, division, print_function

from pingpp.api_resources.abstract import CreateableAPIResource
from pingpp.api_resources.abstract import ListableAPIResource


class Customs(CreateableAPIResource, ListableAPIResource):
    OBJECT_NAME = 'customs'

    @classmethod
    def class_name(cls):
        return 'custom'
