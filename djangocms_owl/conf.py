# -*- coding: utf-8 -*-

from django.conf import settings  # noqa
from django.utils.translation import ugettext_lazy as _

from appconf import AppConf


class OwlConf(AppConf):
    MODULE = _('Generic')

    DEFAULT = 'default'

    CHILD_CLASSES = ()

    STYLES = (
        (DEFAULT, _('Default')),
    )

    TEMPLATES = (
        (DEFAULT, _('Default')),
    )

    INCLUDE_CSS = True

    INCLUDE_JS_OWL = True

    INCLUDE_JS_JQUERY = True

    class Meta:
        prefix = 'djangocms_owl'
