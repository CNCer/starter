from django.db import models

class DiffMixin:
    loaded = False
    dbObject = None
    deltas = {}

    def load (self, force=False):
        if not self.is_new:
            if self.loaded == False or force:
                try:
                    self.dbObject = self.__class__.objects.get(pk=self.pk)
                    self.loaded = True
                except self.__class__.DoesNotExist:
                    self.dbObject = None
                    self.loaded = True

    def build_deltas(self, force=False):
        if not self.loaded or force:
            self.load(force)
        if self.dbObject is None:
            self.deltas = {}
            return
        for field in self._meta.fields:
            if field.name == 'id':
                continue
            elif getattr(self, field.name) != getattr(self.dbObject, field.name):
                self.deltas[field.name] = {
                    'old': getattr(self.dbObject, field.name),
                    'new': getattr(self, field.name),
                }

    def has_field_changed(self, field_name, force=False):
        if not self.loaded or force:
            self.build_deltas(force)
        return field_name in self.deltas
    
    def unload(self):
        self.loaded = False
        self.dbObject = None
        self.deltas = {}

    @property
    def is_new(self)->bool:
        return self._state.adding
