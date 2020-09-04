from django.db import models


class TodoItem(models.Model):

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=128)
    status = models.BooleanField(default=False)

    def __init__(self, title, description, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = title
        self.description = description

    def __str__(self):
        return self.title
