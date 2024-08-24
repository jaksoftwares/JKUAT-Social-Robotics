from django.apps import AppConfig


class ProjectsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'projects'

from django import template

register = template.Library()

@register.filter
def custom_linebreaks(text):
    # Insert <br> after every 100 characters
    return '<br>'.join(text[i:i+100] for i in range(0, len(text), 100))