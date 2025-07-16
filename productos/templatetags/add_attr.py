from django import template

register = template.Library()


@register.filter(name='add_attr')
def add_attr(field, css):
    attrs = {}
    definition = css.split(':')
    if len(definition) == 2:
        attrs[definition[0]] = definition[1]
    return field.as_widget(attrs=attrs)
