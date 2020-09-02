from .models import TodoItem


class TodoController:
    def __init__(self):
        self.total = TodoItem.objects.all().count()
        self.complete = TodoItem.objects.filter(status=True).count()
        self.incomplete = TodoItem.objects.filter(status=False).count()
        self.todos = TodoItem.objects.values()  # .values() gives as dictionary

    @staticmethod
    def add(title: str, description: str):
        todo = TodoItem(
            title=title,
            description=description
        )
        todo.save()

    @staticmethod
    def remove(id: int):
        TodoItem.objects.filter(id=id).delete()


