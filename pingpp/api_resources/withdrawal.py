from __future__ import absolute_import, division, print_function

from pingpp.api_resources.abstract import CreateableAppBasedAPIResource
from pingpp.api_resources.abstract import ListableAppBasedAPIResource
from pingpp.api_resources.abstract import UpdateableAppBasedAPIResource


class Withdrawal(CreateableAppBasedAPIResource,
                 ListableAppBasedAPIResource,
                 UpdateableAppBasedAPIResource):
    OBJECT_NAME = 'withdrawal'
