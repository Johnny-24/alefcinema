from django import template
import mainapp.views as views

register = template.Library()

@register.simple_tag()
def get_categories():
  return views.cats_db