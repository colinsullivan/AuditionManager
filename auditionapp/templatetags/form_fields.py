from django import template

register = template.Library()

@register.inclusion_tag('partials/actor_form_field.html')
def actor_form_field(formField):
  return {
    'formField': formField
  }