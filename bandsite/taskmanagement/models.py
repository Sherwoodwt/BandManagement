from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator

from bandmanagement.models import Band, Member

# Create your models here.

class DateModel(models.Model):
    '''Abstract model that has created_at and updated_at auto_now functionality
    without using auto_now'''

    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        '''overrides models.save to set created/updated_at'''
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(DateModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True

class Task(DateModel):
    '''Model of a task'''
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    assignee = models.ForeignKey(Member, blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    finished = models.BooleanField(default=False)
    difficulty = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5),])
    due_date = models.DateTimeField()

    def __str__(self):
        return self.title
