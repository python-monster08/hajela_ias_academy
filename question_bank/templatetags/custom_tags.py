

from django import template

register = template.Library()

@register.filter
def to_range(value):
    return range(1, int(value) + 1)
