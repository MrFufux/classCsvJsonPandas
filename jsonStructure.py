import json
from collections import Counter
import matplotlib.pyplot as plt 
# pc udem
# file_path = r'C:/Users/b12s306/Desktop/dataJSON/todos.json'
# mi pc
file_path = r'D:\pythonProjects\dataJsonCsvPandasClass\data\todos.json'


# R identificador del archivo json
with open(file_path, 'r') as json_file:
    data = json.load(json_file)

    print(data[0])
    print('The userid is: ', data[0]['userId'])
    print('The id is: ', data[0]['id'])
    print('The title is: ', data[0]['title'])
    print('The status is: ', data[0]['completed'])


    completed_task = [task for task in data if task ['completed']]
    for task in completed_task[:5]:
        print(task)

    print('----------------------------------------------------------------------')

    incomplete_task = [task for task in data if not task ['completed']]
    for task in incomplete_task[:5]:
        print(task)

    print('----------------------------------------------------------------------')

    totalOfData = len(data)

    print(f' the total lenght of elements are : {totalOfData}')

    print('----------------------------------------------------------------------')

    print(data[0].keys())

    print('----------------------------------------------------------------------')
    
    for item in data[:100]:
        print(item)
    
    print('----------------------------------------------------------------------')

    for item in data[:-5]:
        print(item)
    
print('----------------------------------------------------------------------')

# metodo sorted

sorted_task = sorted(data, key = lambda x: x['title'])
for task in sorted_task[:5]:
    print(f'the title is: {task["title"]}')

print('----------------------------------------------------------------------')

# counter method conteo
# cuantas tareas se han completado y cuales no

# variable tareas completadas
completed_count = sum(task["completed"] for task in data)
# variable tareas no completadas
incompleted_count = len(data) - completed_count

print(completed_count)
print(incompleted_count)


print('----------------------------------------------------------------------')
'''
# creando JSON de objetos incompletos
incomplete_path = 'incompleteStatus.json'
with open(incomplete_path, 'w') as json_file:
    # .dumb function
    json.dump(incomplete_task, json_file, indent = 5)

    print(f'The new archive is created in {incomplete_path}')

'''
# importamos Counters de la libreria collections

user_count_task = Counter(task["userId"] for task in data)

for user_id, count in user_count_task.items():
    print(f'The count is: {count} and the userIds is: {user_id}')

print('----------------------------------------------------------------------')

# graficamos con la libreria matplotlib
# guardar este objeto tipo lista

user_ids = list(user_count_task.keys())
task_counts = list(user_count_task.values())

# graficamos un grafico de barras simple
# (x, y, color)
plt.bar(user_ids, task_counts, color='#134ab7')
plt.title('Task per User')
plt.xlabel('User Ids')
plt.ylabel('Amount of Task')
# plt.show()


# search with a keyword
keyword = "et"
matching_task = [task for task in data if keyword.lower() in task["title"].lower()]

for task in matching_task[:10]:
    print(f"id: {task['id']}, title: '{task['title']}")

print('----------------------------------------------------------------------')


