import os
import pandas as pd

# Ruta a la carpeta que contiene los archivos CSV
csv_folder = r'C:\Users\usuario\csv_input'
# Creamos un dataframe donde alojar la informacion de todos los csv
df_main = pd.DataFrame()

for file in os.listdir(csv_folder):
    if file.endswith(".csv"):
        file_path = os.path.join(csv_folder, file)
        with open(file_path, 'r', encoding='latin1') as archivo:
            df = pd.read_csv(archivo, header=None)
        df = df[1:] #Elimino la fila que no me interesaba
        df_t = df.T # Quiero transponer el df
        df_t.columns = df_t.iloc[0] # los nombres de las columnas del DataFrame como los valores de la primera fila
        df_t = df_t.drop(0) # Elimino la primera fila
        df_main = pd.concat([df_main, df_t]) #agregamos las filas de df_t al final de df_main
# pd.concat() es una función de pandas que se utiliza para concatenar DataFrames a lo largo de un eje específico (por defecto, el eje 0, es decir, las filas).

# Guarda el DataFrame principal en un archivo CSV:
df_main.to_csv(r'C:\Users\usuario\csv_output\main_csv.csv', index=False, encoding='latin1')

# Si queremos leer el csv unificado creado 'main_csv':
with open(r'C:\Users\usuario\csv_output\main_csv.csv', 'r', encoding='latin1') as archivo:
    df = pd.read_csv(archivo)

# Si queremos convertir el csv unificado a excel:
df.to_excel('main_csv.xlsx',index=False)