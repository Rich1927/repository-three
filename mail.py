#Менеджер задач.Задача: Создай класс `Task`, который позволяет управлять задачами (делами). У задачи должны быть
# атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено). Реализуй функцию для добавления задач,
# отметки выполненных задач и вывода списка текущих (не выполненных) задач.
class Task:
    def __init__(self):
        self.tasks = []

    def add_task(self, deadline, description):
        self.tasks.append({'deadline': deadline, 'description': description, 'status': 'не выполнено'})

    def complete_task(self, description):
        for task in self.tasks:
            if task['description'] == description:
                task['status'] = 'выполнено'
                print(f"Задача \"{description}\" выполнена")
                return
        print(f"Задача \"{description}\" не найдена")

    def show_tasks(self):
        print("\nТекущие задачи:")
        for task in self.tasks:
            if task['status'] == 'не выполнено':
                print(f"{task['description']} - {task['deadline']}")


# Использование
manager = Task()
manager.add_task("2025-04-17", "Прочитать книгу")
manager.add_task("2025-05-10", "Пробежать марафон")
manager.add_task("2025-04-25", "Починить квадрокоптер")

manager.show_tasks()
manager.complete_task("Прочитать книгу")
manager.show_tasks()
