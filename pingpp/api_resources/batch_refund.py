from __future__ import absolute_import, division, print_function

from pingpp.api_resources.abstract import CreateableAPIResource
from pingpp.api_resources.abstract import ListableAPIResource


class BatchRefund(CreateableAPIResource, ListableAPIResource):
    OBJECT_NAME = 'batch_refund'

    @classmethod
    def class_name(cls):
        return 'batch_refund'
