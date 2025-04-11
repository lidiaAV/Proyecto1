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