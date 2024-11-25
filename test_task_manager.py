from task_manager import TaskManager

def test_task_management_uat():
    task_manager = TaskManager()
    
    # Agregar tarea
    task = task_manager.add_task("Tarea de ejemplo")
    assert task["title"] == "Tarea de ejemplo"
    assert task["completed"] == False
    
    # Completar tarea
    task = task_manager.complete_task(task)
    assert task["completed"] == True
    
    # Editar tarea
    task = task_manager.edit_task(task, "Tarea editada")
    assert task["title"] == "Tarea editada"
    
    # Verificar que la tarea está en la lista de tareas
    tasks = task_manager.get_tasks()
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Tarea editada"
    
    # Eliminar tarea
    deleted_task = task_manager.delete_task(task)
    assert deleted_task["title"] == "Tarea editada"
    assert len(task_manager.get_tasks()) == 0

# Si deseas ejecutar las pruebas directamente
if __name__ == "__main__":
    test_task_management_uat()
    print("Todas las pruebas han pasado.")