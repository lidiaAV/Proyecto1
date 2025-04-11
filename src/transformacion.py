import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def convertir_fecha(df):
    # Convertir la columna 'Fecha' a tipo datetime
    # Preprocesar las fechas para añadir separadores si faltan
    df['Fecha'] = df['Fecha'].astype(str)  # Asegurarse de que la columna 'Fecha' es de tipo string
    df['Fecha'] = df['Fecha'].str.zfill(8)  # Asegurarse de que todas las fechas tengan al menos 8 caracteres
    df['Fecha'] = df['Fecha'].str.replace(r'(\d{2})(\d{2})(\d{4})', r'\1/\2/\3', regex=True)

    # Convertir la columna 'Fecha' a tipo datetime
    df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d/%m/%Y', errors='coerce')
    #ordenamos el dataframe por la fecha
    df = df.sort_values(by='Fecha')
    #reseteamos el indice
    df = df.reset_index(drop=True)
    #hacer una columna con el dia de la semana
    df['Dia_semana'] = df['Fecha'].dt.day_name()
    return df

def convertir_var_float(df):
    #si la columna contiene 'var' la convertimos a float
    #sustituimos el % por nada y el , por .
    #convertimos a float
    df.loc[:, df.columns.str.contains('var')] = df.loc[:, df.columns.str.contains('var')].replace('%', '', regex=True).replace(',', '.', regex=True).astype(float)
    return df

def limpiar_datos(df):
    #borramos la columna vol de todas las materias primas ya que no es relevante para el analisis ya que el porcentaje indica lo mismo y esta mas completo.
    df_limpio= df.drop(columns=['Vol._oro','Vol._platino','Vol._plata','Vol._petroleo','Vol._plomo','Vol._cacao','Vol._cafe','Vol._paladio','Vol._gas_natural','Vol._cobre'], axis='columns')
    return df_limpio

def quitar_domingos(df):
    # Convertir la columna 'Dia_semana' a tipo string
    df['Dia_semana'] = df['Dia_semana'].astype(str)
    # Filtrar los datos para eliminar los domingos
    df_sin_domingos = df[df['Dia_semana'] != 'Sunday']
    return df_sin_domingos

#quitar filas casi vacias, cogemos los datos cuando solo hay datos de 3 materias primas y el resto son nan
def quitar_datos_casi_vacios(df):
    # Crear una copia del DataFrame para evitar modificar el original
    df_vacios = df.copy()
    # Contar el número de valores no nulos en cada fila
    conteo_no_nulos = df_vacios.notnull().sum(axis=1)
    # Filtrar las filas donde el conteo de valores no nulos es menor que 15 ya que hay 5 columnas por cada materia y si hay menos datos de 15 ha de ser festivo o un dato que no nos interese ya que no tiene valores suficientes.
    df_vacios = df_vacios[conteo_no_nulos > 20]
    #reestablecer el indice
    df_vacios=df_vacios.reset_index(drop=True)
    return df_vacios

#rellenar los nas de antes de salir al mercado del paladio, platino y plomo 
def rellenar_datos_cortos(df):
    # Crear una copia del DataFrame para evitar modificar el original
    df_rellenado = df.copy()
    # Definir las columnas a rellenar que contengan paladio, platino y plomo
    columnas_a_rellenar = [col for col in df.columns if 'paladio' in col or 'platino' in col or 'plomo' in col]
    # Iterar sobre las columnas a rellenar
    for col in columnas_a_rellenar:
        #buscar el primer valor no nulo
        primer_valor_no_nulo = df_rellenado[col].first_valid_index()
        # Rellenar los valores NaN antes de ese valor con el primer valor no nulo encontrado
        if primer_valor_no_nulo is not None:
            valor_a_rellenar = df_rellenado[col].loc[primer_valor_no_nulo]
            df_rellenado.loc[:primer_valor_no_nulo, col] = df_rellenado.loc[:primer_valor_no_nulo, col].fillna(valor_a_rellenar)
    return df_rellenado

#rellenar los nas con el valor anterior de la misma columna
def rellenar_datos(df):
    # Crear una copia del DataFrame para evitar modificar el original
    df_rellenado = df.copy()
    # Rellenar los valores NaN con el valor anterior de la misma columna
    df_rellenado.fillna(method='ffill', inplace=True)
    return df_rellenado

#hacemos un grafico de boxplots juntos de las materias que tienen valores bajos

def grafico_boxplot_bajos(df):
    # Configurar el tamaño de la figura
    plt.figure(figsize=(12, 6))
    #coger las columnas que contengan la palabra 'Ultimo'
    columnas = [col for col in df.columns if 'Último' in col and ('plata' in col or 'petroleo' in col or 'gas_natural' in col or 'cafe' in col in col or 'cobre' in col)]
    # Graficar cada columna en el DataFrame
    sns.boxplot(data=df[columnas])
    # Configurar el título y las etiquetas de los ejes
    plt.title('Boxplot de Materias Primas')
    plt.xlabel('Materias Primas')
    plt.ylabel('Valor')
    plt.legend([col.replace('Último_', '') for col in columnas], loc='upper left')

    # Mostrar el gráfico
    plt.show()
    #guardar el grafico
    plt.savefig('graficos/grafico_boxplot_bajos.png', dpi=300, bbox_inches='tight')

