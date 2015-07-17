from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .conf import settings
from .models import OwlCarousel


class OwlCarouselPlugin(CMSPluginBase):
    name = _('Owl Carousel')
    model = OwlCarousel
    allow_children = True
    render_template = 'djangocms_owl/owl_carousel.html'
    child_classes = settings.DJANGOCMS_OWL_CHILD_CLASSES
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
        (_('Style'), {
            'fields': (
                'style',
                'template',
            ),
        }),
    )
    TEMPLATE_PATH = 'djangocms_owl/%s.html'
    render_template = TEMPLATE_PATH % 'default'

    def render(self, context, instance, placeholder):
        if instance.template:
            self.render_template = self.TEMPLATE_PATH % instance.template

        context = super(OwlCarouselPlugin, self).render(context, instance, placeholder)
        context.update({
            'style': instance.get_style(),
        })

        return context


plugin_pool.register_plugin(OwlCarouselPlugin)
