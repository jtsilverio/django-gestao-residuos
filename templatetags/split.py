from django import template

register = template.Library()


@register.filter
def split(value, key):
    """
    Returns the value turned into a list where each item is an unicode object.
    """
    return value.split(key)
