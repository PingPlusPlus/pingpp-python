from __future__ import absolute_import, division, print_function

from pingpp.api_resources.abstract import CreateableAppBasedAPIResource
from pingpp.api_resources.abstract import ListableAppBasedAPIResource


class BatchWithdrawal(CreateableAppBasedAPIResource,
                      ListableAppBasedAPIResource):
    OBJECT_NAME = 'batch_withdrawal'

    @classmethod
    def class_name(cls):
        return 'batch_withdrawal'
