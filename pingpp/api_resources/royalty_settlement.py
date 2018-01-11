from __future__ import absolute_import, division, print_function

from pingpp.api_resources.abstract import CreateableAPIResource
from pingpp.api_resources.abstract import ListableAPIResource
from pingpp.api_resources.abstract import UpdateableAPIResource


class RoyaltySettlement(CreateableAPIResource,
                        ListableAPIResource,
                        UpdateableAPIResource):
    OBJECT_NAME = 'royalty_settlement'

    @classmethod
    def class_name(cls):
        return 'royalty_settlement'
