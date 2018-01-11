from __future__ import absolute_import, division, print_function

from pingpp.api_resources.abstract import ListableAppBasedAPIResource


class BalanceTransaction(ListableAppBasedAPIResource):
    OBJECT_NAME = 'balance_transaction'

    @classmethod
    def class_name(cls):
        return 'balance_transaction'
