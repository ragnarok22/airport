from django.template import Library

register = Library()


@register.filter(name='length')
def length(number):
    return range(number)
