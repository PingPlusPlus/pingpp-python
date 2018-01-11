from __future__ import absolute_import, division, print_function

from pingpp.api_resources.abstract import ListableAPIResource


class RoyaltyTransaction(ListableAPIResource):
    OBJECT_NAME = 'royalty_transaction'

    @classmethod
    def class_name(cls):
        return 'royalty_transaction'
