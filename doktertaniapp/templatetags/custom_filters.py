# Di dalam file custom_filters.py

from django import template

register = template.Library()

@register.filter
def get_by_key(dictionary, key):
    if dictionary is not None and isinstance(dictionary, dict):
        return dictionary.get(key, None)
    return None