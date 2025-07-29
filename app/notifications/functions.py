from .models import *
from collections import defaultdict
from django.apps import apps


class BulkCreateManager(object):
    """
    This helper class keeps track of ORM objects to be created for multiple
    model classes, and automatically creates those objects with `bulk_create`
    when the number of objects accumulated for a given model class exceeds
    `chunk_size`.
    Upon completion of the loop that's `add()`ing objects, the developer must
    call `done()` to ensure the final set of objects is created for all models.
    """

    def __init__(self, chunk_size=100):
        self._create_queues = defaultdict(list)
        self.chunk_size = chunk_size

    def _commit(self, model_class):
        model_key = model_class._meta.label
        model_class.objects.bulk_create(self._create_queues[model_key])
        self._create_queues[model_key] = []

    def add(self, obj):
        """
        Add an object to the queue to be created, and call bulk_create if we
        have enough objs.
        """
        model_class = type(obj)
        model_key = model_class._meta.label
        self._create_queues[model_key].append(obj)
        if len(self._create_queues[model_key]) >= self.chunk_size:
            self._commit(model_class)

    def done(self):
        """
        Always call this upon completion to make sure the final partial chunk
        is saved.
        """
        for model_name, objs in self._create_queues.items():
            if len(objs) > 0:
                self._commit(apps.get_model(model_name))

def shouldSendMsg(cont, id, res, val):
    msg = LastSentMsg.objects.filter(content_type = cont, object_id = id, reason = res, value = val).first()
    if msg is None:
        return True
    else:
        return False

def sendMsg(cont, id, res, val, msghead_en, msghead_ar, msg_en, msg_ar, icon, style, users):
    msg = LastSentMsg.objects.filter(content_type = cont, object_id = id, reason = res).first()
    if msg is None:
         msg = LastSentMsg.objects.create(content_type = cont, object_id = id, reason = res, value = val)
         msg.save()
    else:
        msg.value = val
        msg.save()

    bulk_mgr = BulkCreateManager(chunk_size=20)
    for user in users:
        bulk_mgr.add(Msg(user=user, messagehead_en = msghead_en, messagehead_ar = msghead_ar, message_en=msg_en, message_ar=msg_ar, iconClass = icon, styleClass = style))