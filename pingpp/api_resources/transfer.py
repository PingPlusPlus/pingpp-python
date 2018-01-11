from __future__ import absolute_import, division, print_function

from pingpp.api_resources.abstract import CreateableAPIResource
from pingpp.api_resources.abstract import ListableAPIResource


class Transfer(CreateableAPIResource, ListableAPIResource):
    OBJECT_NAME = 'transfer'
