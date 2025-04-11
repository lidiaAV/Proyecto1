import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
from scipy.stats import norm
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA
from scipy.stats import ttest_ind

import src.exploracion as exp
import src.transformacion as trs
import src.visualizacion as viz

if __name__ == "__main__":

    rutas = {
        'oro': ['data/Datos_oro2.csv', 'data/Datos_oro.csv'],
        'platino': ['data/Datos_platino.csv'],
        'plata': ['data/Datos_plata2.csv', 'data/Datos_plata.csv'],
        'petroleo': ['data/Datos_petroleo2.csv', 'data/Datos_petroleo.csv'],
        'plomo': ['data/Datos_plomo.csv'],
        'cacao': ['data/Datos_cacao2.csv', 'data/Datos_cacao.csv'],
        'cafe': ['data/Datos_cafe2.csv', 'data/Datos_cafe.csv'],
        'paladio': ['data/Datos_paladio.csv'],
        'gas_natural': ['data/Datos_gas_natural2.csv', 'data/Datos_gas_natural.csv'],
        'cobre': ['data/Datos_cobre2.csv', 'data/Datos_cobre.csv']
    }


    df_funcion=exp.importar_datos(rutas)
    df= exp.unir_dataframes(df_funcion)
    df=trs.convertir_fecha(df)
    df=trs.convertir_var_float(df)
    df_sin_var= trs.limpiar_datos(df)
    df_sin_domingos= trs.quitar_domingos(df_sin_var)
    df_sin_pocos_datos= trs.quitar_datos_casi_vacios(df_sin_domingos)
    df_sin_pocos_datos.to_csv('data/dataset_recortado.csv', index=False)
    df_rellenado= trs.rellenar_datos_cortos(df_sin_pocos_datos)
    df_limpio= trs.rellenar_datos(df_rellenado)
    exp.guardar_datos(df_limpio)
    df_limpio.to_csv('data/dataset_limpio.csv', index=False)
    #aplicar la funcion generar estadisticas descriptivas a todos los datos que contengan la palabra 'ultimo' 
    df_limpio_ultimo = df_limpio.filter(like='Último')
    estadisticas, correlacion = viz.estadisticas_descriptivas(df_limpio_ultimo)
    print(estadisticas)

    viz.grafico_temporal_materias(df_limpio)
    viz.grafico_temporal_precios_bajos(df_limpio)
    viz.grafico_boxplot_medios(df_limpio)
    viz.grafico_boxplot_bajos(df_limpio)
    viz.generar_mapa_calor(correlacion)
    viz.realizar_contraste_hipotesis(df_limpio) #probado con oro y plomo y con plata y cobre
    viz.predecir_materia_arima(df_limpio) #platino