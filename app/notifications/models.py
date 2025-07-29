from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType

# Create your models here.

class NotificationReason(models.TextChoices):
    STOCK_LEVEL_CHANGE = "ST", ("Stock")

class NotificationValue(models.TextChoices):
    STOCK_LEVEL_UP = "SLU", ("Stock level up")
    STOCK_LEVEL_DOWN = "SLD", ("Stock level down")


class Msg(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, blank=False)
    iconClass = models.CharField(max_length = 50, blank=False)
    styleClass = models.CharField(max_length = 50, blank=False)
    messagehead = models.CharField(max_length = 200)
    message = models.CharField(max_length = 200)
    seen = models.BooleanField(null=False, blank=False, default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

class LastSentMsg(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveBigIntegerField()
    reason = models.CharField(
        max_length=5,
        choices=NotificationReason,
        null=False,
        blank=False,
    )
    value = models.CharField(
        max_length=5,
        choices=NotificationValue,
        null=False,
        blank=False,
    )

