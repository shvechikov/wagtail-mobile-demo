from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.utils import camelcase_to_underscore


class MobileMixin:
    def get_template(self, request, *args, **kwargs):
        if request.is_ajax() and self.ajax_template:
            return self.ajax_template

        cls = self.__class__
        template = "%s/%s/%s.html" % (
            cls._meta.app_label,
            request.flavour,
            camelcase_to_underscore(cls.__name__),
        )
        return template


class HomePage(MobileMixin, Page):
    pass
