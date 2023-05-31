from datetime import datetime
from django.db import models
from django.core.exceptions import ValidationError


def validate_due_date(value):
    # validating due date
    now = datetime.today().date()
    if(value < now):
        raise ValidationError("Due date must come after today's date")


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
    due_date = models.DateField(null=True, blank=True, validators=[validate_due_date])
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

    def set_tags(self, tags):
        # setting the tags to the task object instance

        tag_obj_list = []
        for tag in tags:
            # Filtering the tags
            tag_obj = Tag.objects.filter(name__iexact=tag['name'].lower()).first()

            # If tags are not found then create new tags
            if not tag_obj:
                tag_obj = Tag.objects.create(name=tag['name'].lower())
                tag_obj.save()
            tag_obj_list.append(tag_obj)
        
        # finally set all the tags to the instance
        self.tags.set(tag_obj_list)



class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
