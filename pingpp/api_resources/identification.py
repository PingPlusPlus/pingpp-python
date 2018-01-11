from __future__ import absolute_import, division, print_function

from pingpp.api_resources.abstract import CreateableAPIResource


class Identification(CreateableAPIResource):
    OBJECT_NAME = 'identification'

    @classmethod
    def class_name(cls):
        return 'identification'

    @classmethod
    def class_url(cls):
        cls_name = cls.class_name()
        return "/v1/%s" % (cls_name,)

    def instance_url(self):
        return self.class_url()
