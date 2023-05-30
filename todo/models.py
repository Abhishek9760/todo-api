from django.db import models

class Task(models.Model):
    OPEN = 'OPEN'
    WORKING = 'WORKING'
    DONE = 'DONE'
    OVERDUE = 'OVERDUE'

    STATUS_CHOICES = [
        (OPEN, 'Open'),
        (WORKING, 'Working'),
        (DONE, 'Done'),
        (OVERDUE, 'Overdue'),
    ]

    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    due_date = models.DateField(null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    status = models.CharField(
        max_length=7,
        choices=STATUS_CHOICES,
        default=OPEN,
    )

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
