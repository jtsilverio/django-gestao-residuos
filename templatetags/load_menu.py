from django import template

from core import menus

register = template.Library()


@register.simple_tag(takes_context=True)
def load_menu(context):
    context["sidebar"] = menus.MENU_SIDEBAR
    return ""
