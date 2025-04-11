import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, norm


# Configurar pandas para mostrar todas las columnas
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Cargar los datos de los archivos CSV
#funcion para importar los datos 


def importar_datos(rutas):
    dfs = {}
    for key, ruta in rutas.items():
        dfs[key]= pd.concat([pd.read_csv(r, decimal=',', thousands='.') for r in ruta], axis=0)
        dfs[key].reset_index(drop=True, inplace=True)
    return dfs

#juntamos los dataframes en uno solo uniendolos por la fecha 
def unir_dataframes(df):
    for i in df:
        if i == list(df.keys())[0]:
            #si es el primer dataframe lo guardamos en df_unido
            df_unido= pd.DataFrame(df[i])
            materia_anterior = i
        else:
            df_unido=df_unido.merge(df[i], on='Fecha', how='outer')
            #renombramos las columnas para que no se repitan
            #_x es el primer dataframe y _y el segundo dataframe
            df_unido.columns = df_unido.columns.str.replace('_x','_'+materia_anterior).str.replace('_y','_'+i)
            materia_anterior = i
    return df_unido

#descargar datos limpios separandolos cada uno por materias 
def guardar_datos(df):
    nombre_materias=['oro','platino','plata','petroleo','plomo','cacao','cafe','paladio','gas_natural','cobre']
    # Crear un DataFrame vacío para almacenar los datos de cada materia prima
    df_materias = pd.DataFrame()
    # Iterar sobre cada materia prima y guardar los datos en un archivo CSV separado
    for nombre in nombre_materias:
        # Filtrar el DataFrame para obtener solo los datos de la materia prima actual
        df_materia = df.filter(like=nombre)
        # Crear una nueva columna 'Fecha' con la fecha correspondiente
        df_materia['Fecha'] = df['Fecha']
        # Reordenar las columnas para que 'Fecha' esté al principio
        df_materia = df_materia[['Fecha'] + [col for col in df_materia.columns if col != 'Fecha']]
        #añadir una columna con el nombre de la materia prima
        df_materia['Materia'] = nombre

        # Guardar el DataFrame en un archivo CSV
        df_materia.to_csv(f'importacion/dataset_{nombre}.csv', index=False)
        # Agregar los datos de la materia prima al DataFrame de materias
