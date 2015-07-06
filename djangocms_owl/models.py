# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _

from cms.models import CMSPlugin

from .conf import settings


class OwlCarousel(CMSPlugin):
    pagination = models.BooleanField(
        default=False,
        help_text=_('Show pagination. (dot dot dot)'), )
    pagination_numbers = models.BooleanField(
        default=False,
        help_text=_('Show numbers inside pagination buttons'), )
    navigation = models.BooleanField(
        default=False,
        help_text=_('Display "next" and "prev" buttons.'), )

    autoplay = models.BooleanField(
        default=False,
        help_text=_('Slides cycle automatically every 5 seconds'))
    stop_on_hover = models.BooleanField(
        default=False,
        help_text=_('Stop autoplay on mouse hover'), )

    items = models.PositiveSmallIntegerField(
        default=1,
        help_text=_('maximum amount of items displayed at a time'), )

    auto_height = models.BooleanField(
        default=False,
        help_text=_('Add height to owl-wrapper-outer so you can use different heights on slides.'), )

    style = models.CharField(
        _('style'),
        max_length=255,
        choices=settings.DJANGOCMS_OWL_STYLES,
        default=settings.DJANGOCMS_OWL_STYLES[0][0],
        help_text=_('CSS class'), )
    template = models.CharField(
        _('template'),
        max_length=255,
        choices=settings.DJANGOCMS_OWL_TEMPLATES,
        default=settings.DJANGOCMS_OWL_TEMPLATES[0][0], )

    def get_style(self):
        if self.style and self.style != settings.DJANGOCMS_OWL_DEFAULT:
            return self.style
        return ''
