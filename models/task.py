import peewee
from datetime import datetime
from .base_model import BaseModel

class Task(BaseModel):
    source_url = peewee.TextField()
    status = peewee.TextField(default="waiting")
    started_at = peewee.DateTimeField(null=True)
    finished_at = peewee.DateTimeField(null=True)
    ref_id = peewee.TextField(null=True)

    def set_as_processing(self):
      self.started_at = datetime.now()
      self.status = 'processing'
      self.save()

    def set_as_failed(self):
      self.status = 'failed'
      self.finished_at = datetime.now()
      self.save()

    def set_as_finished(self, ref_id):
      self.status = 'finished'
      self.ref_id = ref_id
      self.finished_at = datetime.now()
      self.save()

