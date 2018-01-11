from __future__ import absolute_import, division, print_function

from pingpp.api_resources.abstract import CreateableAPIResource
from pingpp.api_resources.abstract import ListableAPIResource


class RedEnvelope(CreateableAPIResource, ListableAPIResource):
    OBJECT_NAME = 'red_envelope'

    @classmethod
    def class_name(cls):
        return 'red_envelope'
