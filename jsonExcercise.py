# Excercise: Estructurar e imprimir ordenadamente

# listar todas las tareas completadas
# contar cuantas tareas tiene asignadas cada user
# buscar tareas por palabra clave en el titulo
# salir del programa

import json
from collections import Counter

# Cargar el archivo JSON
# mi pc
file_path = r'D:\pythonProjects\dataJsonCsvPandasClass\data\todos.json'

# udem pc
# file_path = r'C:/Users/b12s306/Desktop/dataJSON/todos.json'


# Leer el archivo JSON y cargar los datos.
def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Listar todas las tareas completadas.
def list_completed_tasks(data):
    completed_tasks = [task for task in data if task["completed"]]
    print("\nTareas completadas:")
    for task in completed_tasks[:10]:  # Mostrar las primeras 10
        print(f"ID: {task['id']}, Título: {task['title']}")
    print(f"Total de tareas completadas: {len(completed_tasks)}\n")

# Contar cuántas tareas tiene asignadas cada usuario.
def count_tasks_by_user(data):
    user_task_count = Counter(task["userId"] for task in data)
    print("\nCantidad de tareas por usuario:")
    for user_id, count in user_task_count.items():
        print(f"Usuario {user_id}: {count} tareas")

# Buscar tareas por palabra clave en el título.
def search_tasks_by_keyword(data):
    keyword = input("\nIngrese una palabra clave para buscar: ")
    matching_tasks = [task for task in data if keyword.lower() in task["title"].lower()]
    print(f"\nTareas que contienen '{keyword}':")
    for task in matching_tasks[:10]:  # Mostrar las primeras 10
        print(f"ID: {task['id']}, Título: {task['title']}")
    print(f"\nTotal de tareas encontradas: {len(matching_tasks)}\n")

def main():
    data = load_data(file_path)
    while True:
        print('-------------------------------------\nWelcome to this menu\n')
        print('1. List all completed tasks')
        print('2. Count tasks by user')
        print('3. Search tasks by keyword')
        print('4. Exit\n--------------------------------------')
        
        choice = input('Please type the operation that you want: ')
        
        if choice == '1':
            list_completed_tasks(data)
        elif choice == '2':
            count_tasks_by_user(data)
        elif choice == '3':
            search_tasks_by_keyword(data)
        elif choice == '4':
            print('\nExiting the program...\n')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == "__main__":
    main()