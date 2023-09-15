from django import template

register = template.Library()

@register.filter(name='render_stars')
def render_stars(value):
    return '⭐' * value
