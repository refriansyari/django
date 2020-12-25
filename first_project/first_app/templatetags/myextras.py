from django import template

register = template.Library()

@register.filter(name='cut')
def potong(value,arg):
    return value.replace(arg,'')


@register.filter
def upper(value,arg):

    return value.upper(arg,'')

