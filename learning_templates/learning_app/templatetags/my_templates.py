from django import template

register = template.Library()

@register.filter(name='cut')

def cut(value,arg):
    """
    THIS CUTS OUT ALL VALUES OF "arg" FROM STRINGS!
    """
    return value.replace(arg,'')

# register.filter('cut':cut)
