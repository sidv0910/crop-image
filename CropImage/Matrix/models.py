from django.db import models

class Instructions(models.Model):
    id = models.AutoField(primary_key=True)
    instruction = models.TextField()
    booklet = models.JSONField(default=list, blank=True)
    order = models.IntegerField()
