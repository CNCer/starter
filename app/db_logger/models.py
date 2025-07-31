import logging
from django.db import models
from six import python_2_unicode_compatible


LOG_LEVELS = (
    (logging.NOTSET, 'NotSet'),
    (logging.INFO, 'Info'),
    (logging.WARNING, 'Warning'),
    (logging.DEBUG, 'Debug'),
    (logging.ERROR, 'Error'),
    (logging.FATAL, 'Fatal'),
)


@python_2_unicode_compatible
class StatusLog(models.Model):
    logger_name = models.CharField(max_length=100)
    level = models.PositiveSmallIntegerField(choices=LOG_LEVELS, default=logging.ERROR, db_index=True)
    msg = models.TextField()
    trace = models.TextField(blank=True, null=True)
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    def __str__(self):
        return self.msg

    class Meta:
        ordering = ('-create_datetime',)
        verbose_name_plural = verbose_name = 'Logging'
