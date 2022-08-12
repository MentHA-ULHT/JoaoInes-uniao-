from django import template
register = template.Library()

@register.filter
def convert(value):
    return value.encode('iso-8859-1').decode('iso-8859-1') if value else value

@register.simple_tag
def minimum(val1, val2):
    return min(val1,val2)