from .models import TodoItem


class TodoController:
    def __init__(self):
        self.total = TodoItem.objects.all().count()
        self.complete = TodoItem.objects.filter(status=True).count()
        self.incomplete = TodoItem.objects.filter(status=False).count()
        self.todos = TodoItem.objects.values()  # .values() gives as dictionary

