import time
import concurrent.futures
from task_search_service import TaskSearchService, create_tasks

def performance_test_search_service(num_searches, query):
    tasks = create_tasks(1000)
    search_service = TaskSearchService(tasks)

    start_time = time.time()
    
    # Realizar búsquedas concurrentes
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(search_service.search_tasks, query) for _ in range(num_searches)]
        results = [future.result() for future in concurrent.futures.as_completed(futures)]
    
    end_time = time.time()
    
    print(f"Tiempo total para {num_searches} búsquedas: {end_time - start_time:.4f} segundos")
    print(f"Total de resultados encontrados: {sum(len(result) for result in results)}")

if __name__ == "__main__":
    performance_test_search_service(1000, "Tarea 100")