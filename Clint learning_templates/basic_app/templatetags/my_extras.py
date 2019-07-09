from django import template

register = template.Library()

def cut(value,arg):
    return value.replace(arg,'')

def upper(value):
    return value.upper()

register.filter('cut',cut)
register.filter('upper',upper)
