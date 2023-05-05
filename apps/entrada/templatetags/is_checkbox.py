# https://stackoverflow.com/questions/3927018/django-how-to-check-if-field-widget-is-checkbox-in-the-template
# https://docs.djangoproject.com/en/4.2/howto/custom-template-tags/
from django import template
from django.forms import CheckboxInput, CheckboxSelectMultiple

register = template.Library()

@register.filter(name='is_checkbox')
def is_checkbox(field):
    return (isinstance(field.field.widget, CheckboxInput) or isinstance(field.field.widget, CheckboxSelectMultiple))