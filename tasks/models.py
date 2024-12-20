from django.db import models
from django.shortcuts import reverse


class Task(models.Model):
    task_title = models.CharField(max_length=100)
    due_date = models.DateTimeField()
    description = models.TextField()

    def get_detail_url(self):
        return reverse('tasks:detail', args=[self.pk])

