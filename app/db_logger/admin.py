from __future__ import unicode_literals
import logging

from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from unfold.admin import ModelAdmin

from django.conf import settings
from .models import StatusLog

DJANGO_DB_LOGGER_ADMIN_LIST_PER_PAGE = getattr(settings, 'DJANGO_DB_LOGGER_ADMIN_LIST_PER_PAGE', 10)



@admin.register(StatusLog)
class LoggingAdmin( ModelAdmin):
    list_display = ('colored_msg', 'traceback', 'create_datetime_format')
    list_display_links = ('colored_msg',)
    list_filter = ('level',)
    list_per_page = DJANGO_DB_LOGGER_ADMIN_LIST_PER_PAGE

    def colored_msg(self, instance):
        if instance.level in [logging.NOTSET, logging.INFO]:
            color = 'blue'
        elif instance.level == logging.DEBUG:
            color = 'green'
        elif instance.level == logging.WARNING:
            color = 'orange'
        else:
            color = 'red'
        return format_html('<span style="color: {color};">{msg}</span>', color=color, msg=instance.msg)

    colored_msg.short_description = 'Message'

    def traceback(self, instance):
        return format_html('<pre><code>{content}</code></pre>', content=instance.trace if instance.trace else '')

    def create_datetime_format(self, instance):
        return timezone.localtime(instance.create_datetime).strftime('%Y-%m-%d %X')

    create_datetime_format.short_description = 'Created at'





