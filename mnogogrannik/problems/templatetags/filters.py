from django import template
from django.utils.safestring import mark_safe
from django.template.defaultfilters import stringfilter
import markdownx.utils
from markdownx.settings import MARKDOWNX_MARKDOWNIFY_FUNCTION

register = template.Library()


@register.filter
@stringfilter
def markdownify(text):
    markdown_x = getattr(markdownx.utils, MARKDOWNX_MARKDOWNIFY_FUNCTION.split('.')[-1])
    return mark_safe(markdown_x(text))