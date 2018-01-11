from __future__ import absolute_import, division, print_function

from pingpp import util
from pingpp.six.moves.urllib.parse import quote_plus
from pingpp.api_resources.abstract import APIResource
from pingpp.api_resources import Charge


class Refund(APIResource):
    OBJECT_NAME = 'refund'

    def instance_url(self):
        self.id = util.utf8(self.id)
        self.charge = util.utf8(self.charge)
        base = Charge.class_url()
        cust_extn = quote_plus(self.charge)
        extn = quote_plus(self.id)
        return "%s/%s/refunds/%s" % (base, cust_extn, extn)

    @classmethod
    def retrieve(cls, id, api_key=None, **params):
        raise NotImplementedError(
            "Can't retrieve a refund without a charge ID. "
            "Use charge.refunds.retrieve('refund_id') instead.")
