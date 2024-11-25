class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = {"title": title, "completed": False}
        self.tasks.append(task)
        return task

    def edit_task(self, task, new_title):
        task["title"] = new_title
        return task

    def delete_task(self, task):
        self.tasks.remove(task)
        return task

    def complete_task(self, task):
        task["completed"] = True
        return task

    def get_tasks(self):
        return self.tasks