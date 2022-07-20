from django import template
register = template.Library()

@register.filter
def convert(value):
    return value.encode('iso-8859-1').decode('iso-8859-1') if value else value