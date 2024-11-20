# 11/19/2024
import pandas as pd
import csv

# cargar el archivo csv

#udm pc
# file_path = r'C:/Users/b12s306/Desktop/dataJSON/data/airtravel.CSV']

#mi pc
file_path = r'D:\pythonProjects\dataJsonCsvPandasClass\data\airtravel.CSV'

def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

read_csv(file_path)

print('----------------------------------------------------------------------------')
print('\n-----------------------Guardo Info en archivo csv---------------------------\n')

#udm pc
# file_path = r'C:\Users\b12s306\Desktop\dataJSON\data\prueba.CSV'

#mi pc
file_path = r'D:\pythonProjects\dataJsonCsvPandasClass\data\prueba.CSV'

def write_csv(file_path):
    data =[
        ["Nombre", "Edad", "Pais"],
        ["Wilson", 45, "Inglaterra"],
        ["Andres", 25, "Espana"],
        ["Ana", 35, "Ecuador"],
        ["Pablo", 56, "Bolivia"]
    ]

    # newline es hacer la instruccion
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print(f'El archivo {file_path} ha sido creado exitosamente')

write_csv(file_path)

print('\n----------------------------------------------------------------------------')
print('-------------------------- LIBRERIA Pandas --------------------------------')

'''
Pandas es usado para manipular datos
si quiero que me instale la libreria al correr el codigo
'''
# !pip install pandas
# importamos pandas
# import pandas as pd

#udm pc
# file_path = r'C:\Users\b12s306\Desktop\dataJSON\data\prueba.CSV'

#mi pc
file_path = r'D:\pythonProjects\dataJsonCsvPandasClass\data\prueba.CSV'

# leemos el archivo csv
data = pd.read_csv(file_path)
print(data.head()) # permite ver las primeras 5 filas


print('\n----------------------------------------------------------------------------')
print('-------------------------- ACTIVIDAD Ventas.csv --------------------------------')

#udm pc
# file_path = r'C:\Users\b12s306\Desktop\dataJSON\data\ventas.CSV'

#mi pc
file_path = r'D:\pythonProjects\dataJsonCsvPandasClass\data\ventas.CSV'

# read the csv file
def read_sells_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

read_sells_csv(file_path)

data = pd.read_csv(file_path)

print('\n----------------------------------------------------------------------------\n')
print('Punto 1: Multiplicar cantidad y precio y mostrar en una nueva columna')

data['Total_Sells'] = data['Cantidad'] * data['Precio']
print(data)

print('\n----------------------------------------------------------------------------\n')
print('Punto 2: Mostrar producto con mayor ventas totales')

product_max_ventas = data.groupby('Producto')['Total_Sells'].sum().idxmax()
print(f'El producto con mayor ventas es: {product_max_ventas}')

print('\n----------------------------------------------------------------------------\n')
print('Punto 3: Mostrar producto con menor ventas totales')

product_min_ventas = data.groupby('Producto')['Total_Sells'].sum().idxmin()
print(f'El producto con menor ventas es: {product_min_ventas}')

print('\n----------------------------------------------------------------------------\n')
print('Punto 4: Cambiar el nombre de la columna Total_Sells ')

resume = data.groupby('Producto')['Total_Sells'].sum().reset_index()
resume.rename(columns={'Total_Sells': 'Total_By_Product'}, inplace=True)
print(resume)

print('\n----------------------------------------------------------------------------\n')
print('Punto 5: Calcular porcentaje ')

total_sells = resume['Total_By_Product'].sum()
resume['Sell_Percentage'] = (resume['Total_By_Product'] / total_sells) * 100
print(resume)
