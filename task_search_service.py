class TaskSearchService:
    def __init__(self, tasks):
        self.tasks = tasks

    def search_tasks(self, query):
        return [task for task in self.tasks if query.lower() in task["title"].lower()]

# Datos de ejemplo
def create_tasks(num_tasks):
    return [{"title": f"Tarea {i}", "completed": False} for i in range(1, num_tasks + 1)]

if __name__ == "__main__":
    tasks = create_tasks(1000)
    search_service = TaskSearchService(tasks)
    
    # Ejemplo de búsqueda
    result = search_service.search_tasks("Tarea 100")
    print(f"Resultados de búsqueda: {len(result)} tarea(s) encontrada(s).")