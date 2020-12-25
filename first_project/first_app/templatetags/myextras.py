from django import template

register = template.Library()

@register.filter(name='cut')
def potong(value,arg):
    return value.replace(arg,'')


@register.filter
def upper(value):

    return value.upper()

