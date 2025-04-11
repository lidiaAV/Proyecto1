import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
from scipy.stats import ttest_ind
from scipy.stats import norm
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA

# Generar estadisticas descriptivas
 
def estadisticas_descriptivas(df):
    #coger solo las columnas numericas
    df_numerico = df.select_dtypes(include=[np.number])
    # Calcular estadísticas descriptivas para cada columna numérica
    estadisticas = df_numerico.describe()
    # Calcular la correlación entre las columnas numéricas
    correlacion = df_numerico.corr()
    return estadisticas, correlacion

#grafico serie temporal de los datos
def grafico_temporal_materias(df):
    # Configurar el tamaño de la figura
    plt.figure(figsize=(12, 6))
    #coger las columnas que contengan la palabra 'Último'
    columnas = [col for col in df.columns if 'Último' in col]
    # Graficar cada columna en el DataFrame
    for col in columnas:
        #graficamos el resto de materias primas
        plt.plot(df['Fecha'], df[col], label=col)
    # Configurar el título y las etiquetas de los ejes
    plt.title('Serie Temporal de Materias Primas')
    plt.xlabel('Fecha')
    plt.ylabel('Valor')
    # Mostrar la leyenda sin la palabra 'Último'
    plt.legend([col.replace('Último_', '') for col in columnas], loc='upper left')
    # Mostrar el gráfico
    plt.show()
    #guardar el grafico
    plt.savefig('graficos/grafico_temporal_materias.png', dpi=300, bbox_inches='tight')
    #cerramos el grafico
    plt.close()

#grafico temporal de la correlacion entre el oro y el petroleo
def grafico_temporal_precios_bajos(df):
    #tamano del grafico
    plt.figure(figsize=(14, 7))
    columnas_bajos = []
    #coger las columnas que contengan la palabra 'Ultimo' y pertenezca a plata,petroleo, cafe, gas natural y cobre
    for i in df.columns:
        if 'Último' in i and ('plata' in i or 'petroleo' in i or 'gas_natural' in i or 'cobre' in i):
            columnas_bajos.append(i)
    # Graficar cada columna en el DataFrame
    for columna in columnas_bajos:
        plt.plot(df['Fecha'], df[columna], label=columna)

    plt.title('Serie Temporal de Precios Bajos')
    plt.xlabel('Fecha')
    plt.ylabel('Precio')
    plt.legend([col.replace('Último_', '') for col in columnas_bajos], loc='upper left')
    plt.show()
    #guardar el grafico
    plt.savefig('graficos/grafico_temporal_precios_bajos.png', dpi=300, bbox_inches='tight')
    #cerramos el grafico
    plt.close()

#hacemos un grafico de boxplots juntos de las materias que tienen valores intermedios
def grafico_boxplot_medios(df):
    # Configurar el tamaño de la figura
    plt.figure(figsize=(12, 6))
    #coger las columnas que contengan la palabra 'Ultimo'
    columnas = [col for col in df.columns if 'Último' in col and ('oro' in col or 'platino' in col or 'plomo' in col or 'paladio' in col)]
    # Graficar cada columna en el DataFrame
    sns.boxplot(df[columnas])
    # Configurar el título y las etiquetas de los ejes
    plt.title('Boxplot de Materias Primas')
    #Mostrar las etiquetas de las filas sin la palabra 'Ultimo'
    plt.xlabel('Materias Primas')
    plt.ylabel('Valor')
    # Mostrar la leyenda sin la palabra 'Último'
    plt.legend([col.replace('Último_', '') for col in columnas], loc='upper left')
    # Mostrar el gráfico
    plt.show()
    #guardar el grafico
    plt.savefig('graficos/grafico_boxplot_medios.png', dpi=300, bbox_inches='tight')
    #cerramos el grafico
    plt.close()

def grafico_boxplot_bajos(df):
    # Configurar el tamaño de la figura
    plt.figure(figsize=(12, 6))
    #coger las columnas que contengan la palabra 'Ultimo'
    columnas = [col for col in df.columns if 'Último' in col and ('plata' in col or 'petroleo' in col or 'gas_natural' in col or 'cafe' in col in col or 'cobre' in col)]
    # Graficar cada columna en el DataFrame
    sns.boxplot(data=df[columnas])
    # Configurar el título y las etiquetas de los ejes
    plt.title('Boxplot de Materias Primas Bajas')
    plt.xlabel('Materias Primas')
    plt.ylabel('Valor')
    plt.legend([col.replace('Último_', '') for col in columnas], loc='upper left')
    # Mostrar el gráfico
    plt.show()
    #guardar el grafico
    plt.savefig('graficos/grafico_boxplot_bajos.png', dpi=300, bbox_inches='tight')
    #cerramos el grafico
    plt.close()


def generar_mapa_calor(correlacion, output_path='graficos/grafico_correlacion.png'):
     # Crear el mapa de calor
    plt.figure(figsize=(12, 8))

    # Quitar la palabra 'Último_' de las etiquetas del eje x e y
    correlacion.columns = correlacion.columns.str.replace('Último_', '', regex=False)
    correlacion.index = correlacion.index.str.replace('Último_', '', regex=False)

    sns.heatmap(correlacion, annot=True, cmap='coolwarm', fmt='.2f', linewidths=.5)
    plt.title('Mapa de Calor de Correlación')
    # Configurar las etiquetas del eje x
    plt.xticks(rotation=45, ha='right')
    # Mostrar el gráfico
    plt.show()
    #guardar el grafico
    plt.savefig('graficos/grafico_correlacion.png', dpi=300, bbox_inches='tight')
    #cerramos el grafico
    plt.close()


def realizar_contraste_hipotesis(df):
    materia1 = input("Introduce la primera materia prima para comparar el test de hipotesis (por ejemplo, 'oro'): ").strip()
    materia2 = input("Introduce la segunda materia prima para comparar el test de hipotesis (por ejemplo, 'plomo'): ").strip()
    # Seleccionar las columnas de interés
    var1 = df[f'% var._{materia1}']
    var2 = df[f'% var._{materia2}']

    # Contraste de hipótesis
    # H0: Las dos materias tienen el mismo comportamiento
    # H1: Las dos materias tienen comportamientos diferentes
    stat, p_value = ttest_ind(var1, var2, equal_var=False)

    # Imprimir resultados del contraste
    print(f"Estadístico t: {stat}")
    print(f"Valor p: {p_value}")
    if p_value < 0.05:
        print(f"Rechazamos H0: Los comportamientos de {materia1} y {materia2} son diferentes.")
    else:
        print(f"No podemos rechazar H0: Los comportamientos de {materia1} y {materia2} son iguales.")

    # Calcular medias e intervalos de confianza
    mean_var1 = var1.mean()
    mean_var2 = var2.mean()
    ci_var1 = norm.interval(0.95, loc=mean_var1, scale=var1.std()/len(var1)**0.5)
    ci_var2 = norm.interval(0.95, loc=mean_var2, scale=var2.std()/len(var2)**0.5)

    print(f"Media {materia1}: {mean_var1}, Intervalo de confianza: {ci_var1}")
    print(f"Media {materia2}: {mean_var2}, Intervalo de confianza: {ci_var2}")

    # Gráfico de distribución
    plt.figure(figsize=(12, 6))
    sns.kdeplot(var1, label=f'Varianza {materia1}', fill=True, alpha=0.5)
    sns.kdeplot(var2, label=f'Varianza {materia2}', fill=True, alpha=0.5)

    # Añadir líneas de medias
    plt.axvline(mean_var1, color='blue', linestyle='--', label=f'Media varianza {materia1}: {mean_var1:.2f}')
    plt.axvline(mean_var2, color='orange', linestyle='--', label=f'Media varianza {materia2}: {mean_var2:.2f}')

    # Añadir intervalos de confianza
    plt.axvspan(ci_var1[0], ci_var1[1], color='blue', alpha=0.2, label=f'IC 95% {materia1}')
    plt.axvspan(ci_var2[0], ci_var2[1], color='orange', alpha=0.2, label=f'IC 95% {materia2}')

    # Configurar el gráfico
    plt.title(f'Distribución de varianza {materia1} y {materia2}')
    plt.xlabel('Valor')
    plt.ylabel('Densidad')
    plt.legend()
    plt.show()
    #guardar el grafico
    plt.savefig(f'graficos/grafico_contraste_hipotesis_{materia1}_{materia2}.png', dpi=300, bbox_inches='tight')
    #cerramos el grafico
    plt.close()

def predecir_materia_arima(df, start_date='2009-01-01', pred_start_date='2025-01-01', steps=365, output_path='graficos/prediccion.png'):
    
    # Solicitar la materia prima al usuario
    materia = input("Introduce la materia prima para hacer la prediccion (por ejemplo, 'platino'): ").strip()
    columna = f'Último_{materia}'

    # Verificar si la columna existe en el DataFrame
    if columna not in df.columns:
        print(f"La columna '{columna}' no existe en el DataFrame.")
        return

    # Filtrar los datos para la materia seleccionada
    df_prediccion = df[['Fecha', columna]].copy()
    df_prediccion['Fecha'] = pd.to_datetime(df_prediccion['Fecha'])
    df_prediccion = df_prediccion[df_prediccion['Fecha'] >= start_date]

    # Dividir los datos en entrenamiento
    entrenar = df_prediccion[df_prediccion['Fecha'] < pred_start_date]

    # Crear y ajustar el modelo ARIMA
    model = ARIMA(entrenar[columna], order=(5, 0, 5))  # (p,d,q) valores ajustables, dias anteriores y posteriores
    model_fit = model.fit()

    # Realizar predicciones
    predicciones = model_fit.get_forecast(steps=steps)
    predicciones_mean = predicciones.predicted_mean
    predicciones_conf_int = predicciones.conf_int(alpha=0.10)

    # Ajustar los índices de las fechas de predicción
    predicciones_mean.index = pd.date_range(start=pred_start_date, periods=len(predicciones_mean), freq='D')
    predicciones_conf_int.index = predicciones_mean.index

    # Filtrar el historial reciente
    historial = df_prediccion[df_prediccion['Fecha'] > '2022-01-01']

    # Crear un gráfico de las predicciones
    plt.figure(figsize=(12, 6))
    plt.plot(historial['Fecha'], historial[columna], label='Datos Reales')
    plt.plot(predicciones_mean.index, predicciones_mean, label='Predicciones', color='red')
    plt.fill_between(predicciones_conf_int.index, 
                     predicciones_conf_int.iloc[:, 0], 
                     predicciones_conf_int.iloc[:, 1], 
                     color='pink', alpha=0.3, label='Intervalo de Confianza')
    plt.title(f'Predicción de {columna} con ARIMA')
    plt.xlabel('Fecha')
    plt.ylabel('Valor')
    plt.legend()
    plt.show()
    # Guardar el gráfico
    plt.savefig(f'graficos/prediccion_{materia}.png', dpi=300, bbox_inches='tight')
    #cerramos el grafico
    plt.close()
