# https://stackoverflow.com/questions/3927018/django-how-to-check-if-field-widget-is-checkbox-in-the-template
# https://docs.djangoproject.com/en/4.2/howto/custom-template-tags/
from django import template

register = template.Library()


@register.simple_tag
def page_parser(field_name, value, urlencode=None):
    url = f"?{field_name}={value}"

    if urlencode:
        query_list = urlencode.split("&")
        filtered_query_list = filter(
            lambda p: p.split("=")[0] != field_name, query_list
        )
        query_for_other_fields = "&".join(filtered_query_list)

        url = f"{url}&{query_for_other_fields}"

    return url
