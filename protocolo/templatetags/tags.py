from django import template
register = template.Library()

@register.filter
def convert(value):
    return value.encode('iso-8859-1').decode('iso-8859-1') if value else value

@register.simple_tag
def minimum(val1, val2):
    return min(val1,val2)

@register.simple_tag
def count(list):
    return len(list)

@register.simple_tag
def subtraction(val1, val2):
    return val1-val2

@register.simple_tag
def abvd_evaluation(val):
    if val == 0:
        return "Nulo"
    elif val <= 7:
        return "Ligeiro"
    elif val <= 14:
        return "Moderado"
    elif val <= 19:
        return "Severo"
    elif val <= 24:
        return "Muito Severo"

@register.simple_tag
def aivd_evaluation(val, sex):
    if sex == 'Masculino':
        if val == 0:
            return "Total"
        elif val <= 1:
            return "Grave"
        elif val <= 3:
            return "Moderada"
        elif val <= 4:
            return "Ligeira"
        else:
            return "Independente"
    elif sex == 'Feminino':
        if val <= 1:
            return "Total"
        elif val <= 3:
            return "Grave"
        elif val <= 5:
            return "Moderada"
        elif val <= 7:
            return "Ligeira"
        else:
            return "Independente"
