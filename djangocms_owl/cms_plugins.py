from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import OwlCarousel


class OwlCarouselPlugin(CMSPluginBase):
    name = _('Owl Carousel')
    model = OwlCarousel
    allow_children = True
    render_template = 'djangocms_owl/owl_carousel.html'
    fieldsets = (
        (None, {
            'fields': (
                'items',
                'auto_height',
            )
        }),
        (_('Navigation'), {
            'fields': (
                'pagination',
                'pagination_numbers',
                'navigation',

            ),
        }),
        (_('AutoPlay'), {
            'fields': (
                'autoplay',
                'stop_on_hover',
            ),
        }),
    )


plugin_pool.register_plugin(OwlCarouselPlugin)
