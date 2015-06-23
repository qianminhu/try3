from django.db import models
from django.contrib.auth.models import User


class CurrentTask(models.Model):

    task = models.CharField(max_length=255)
    ONCE = 'One Time'
    WEEKLY = 'Weekly'
    MONTHLY = 'Monthly'
    FREQUENCY_CHOICES = ((ONCE, 'One Time'), (WEEKLY, 'Weekly'), (MONTHLY, 'Monthly'))
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES, default=ONCE)
    description = models.CharField(max_length=600)

    def __unicode__(self):
        return self.task

class TaskType(models.Model):
    type = models.ForeignKey(CurrentTask)
    person_in_charge = models.ForeignKey(User)
    date_due = models.DateTimeField('date due')
