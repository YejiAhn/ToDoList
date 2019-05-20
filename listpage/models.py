from django.db import models
from django.utils import timezone
from datetime import date

Rating_Choices = (
        (1, 'Very Urgent'),
        (2, 'Intermediate'),
        (3, 'Not Urgent')
    )

# Create your models here.
class List(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    due_date = models.DateField(blank=True, null=True)
    degree = models.IntegerField(choices=Rating_Choices, default=1)
    #completed = models.BooleanField(default=False)

    def is_end_date(self):
        return date.today()>self.due_date


    def __str__(self):
        return self.title

    