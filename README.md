# Autor:
Lidia Alcantara Valverde

# Proyecto1
Primer proyecto del master data science & IA

# FUTUROS DE MATERIAS EN LA BOLSA 


### 0- Formulación de preguntas

- Es posible predecir la tendencia del precio a futuro?
- Hay correlacion entre las materias?

### 1- Extraccion de datos 

Este proyecto tratara sobre algunos de los precios de las materias en la bolsa, concretamente 10 materias, que son las siguientes: 

1. Oro: Es el metal precioso más valorado mundialmente. Se extrae a través de actividades de minería en todos los continentes a excepción de la Antártica y tiene aplicaciones que van desde la industria joyera hasta la electrónica. También es un activo financiero universalmente aceptado y uno de los más cotizados globalmente.

    El oro tomó mayor relevancia en las diferentes sociedades antiguas como medio de pago. Actualmente, funciona como una herramienta de respaldo para bancos centrales de países de todo el mundo y como un bien de inversión y almacenamiento de riqueza que permite recibir beneficios con sus cambios de precio. El precio del oro fluctúa según políticas monetarias, fenómenos naturales y condiciones geopolíticas. Por lo general, el oro tiende a aumentar de valor en situaciones que representen un riesgo geopolítico o económico como situaciones políticas complejas, desastres naturales o guerras civiles. https://es.investing.com/commodities/gold-historical-data

2. Platino: es un metal precioso de color blanco plateado con capacidades dúctiles y maleables. Se utiliza en joyas, catalizadores para la industria automotriz y laboratorios químicos.

    Debido a que la industria automotriz tiene una fuerte demanda por este metal, los precios del platino se ven influenciados por las cifras de ventas y fabricación de automóviles. De igual forma, dado que los principales yacimientos se encuentran en Sudáfrica y Rusia, las cifras de producción de estos países pueden afectar los precios.
    https://es.investing.com/commodities/platinum-historical-data

3. Plata: es un metal precioso utilizado por sus propiedades conductivas y estéticas. Esta materia prima se emplea en circuitos eléctricos, joyería, artículos decorativos y como depósito de valor. Junto con el oro, la plata fue utilizada ampliamente como moneda en el siglo viii a.C. Algunos de los principales productores de plata son México, Perú y China. https://es.investing.com/commodities/silver-historical-data

4. Oil: El crudo de petróleo (PETRÓLEO) es una materia prima natural que se utiliza para una variedad de funciones y productos cruciales y populares, entre los que se incluye la gasolina, el diésel, la calefacción y la generación de electricidad. 

    Como la mayoría de recursos no renovables, el precio del crudo de petróleo está muy influido por la oferta y la demanda. A su vez, la oferta y la demanda de esta materia prima se ve influida por una amplia gama de elementos geológicos, legales, tecnológicos y políticos. https://es.investing.com/commodities/crude-oil-historical-data?utm_source=google&utm_medium=cpc&utm_campaign=19619206691&utm_content=646207805913&utm_term=dsa-1944158660633_&GL_Ad_ID=646207805913&GL_Campaign_ID=19619206691&ISP=1&npl=1&af_adset_id=143446769417&ppu=9801673&gad_source=1&gclid=CjwKCAjw-qi_BhBxEiwAkxvbkBwu46q1rQTdOZMvbj0QnjCP7F_L7cuEL6LXRaXdBwnOznJUev3kcRoC_BcQAvD_BwE

5. Plomo: El plomo es un metal pesado, de baja temperatura de fusión, de color gris-azulado que ocurre naturalmente en la corteza terrestre. Sin embargo, raramente se encuentra en la naturaleza en la forma de metal. Generalmente se encuentra combinado con otros dos o más elementos formando compuestos de plomo. https://es.investing.com/commodities/lead-historical-data

6. Paladio: un metal raro, se emplea en diversas industrias, principalmente, pero no de forma exclusiva, en productos electrónicos. Por su bajo punto de fusión y ausencia de reacción al oxígeno, el paladio es relativamente fácil de manipular además de resistente, razón por la cual se utiliza en la fabricación de muchos ordenadores portátiles y smartphones a nivel global.
 
    El paladio se considera un mineral no tóxico, por eso se emplea en productos que requieren un contacto directo con el cuerpo humano. Por ejemplo, a menudo se combina con el oro para crear joyería de oro blanco y también se usa en empastes dentales. 
 
    El mineral de paladio se produce de manera natural y es muy raro, por lo que la mayoría de las industrias reciclan este metal. Rusia es el primer productor mundial, y una empresa rusa, Norilsk Nickel, es responsable del 39 % del suministro mundial. Otros grandes países productores son Canadá, Sudáfrica, Estados Unidos y Zimbabue. 
 
    La gráfica del paladio puede verse afectada por problemas de oferta y demanda; no obstante, como a veces se considera un activo de tipo «refugio seguro», como el oro y la plata, también podría verse afectado por la volatilidad en el mercado de valores. https://es.investing.com/commodities/palladium-historical-data

7. Gas natural: es una materia prima objeto de comercio con muchas aplicaciones comerciales e industriales. Al ser un combustible fósil por definición, pasa a través de procesos para filtrar y eliminar otras sustancias antes de convertirse en económicamente viable. El gas natural también se considera el combustible fósil de quema más limpia, lo que fomenta la adaptación tecnológica para garantizar mejores métodos para su captación y distribución. https://es.investing.com/commodities/natural-gas-historical-data

8. Cobre: es un metal muy utilizado por sus muchas aplicaciones, como su capacidad para conducir el calor y la electricidad. Se trata de un metal nativo, lo cual significa que se encuentra en la naturaleza en su forma metálica directamente utilizable, lo que ha contribuido a su pronto descubrimiento y consumo. El atractivo aspecto del cobre lo hace apropiado para un uso decorativo y artístico. Este metal se extrae de minas subterráneas que pueden encontrase en Australia, Canadá, China, Chile, México y otros países. https://es.investing.com/commodities/copper-historical-data?utm_source=google&utm_medium=cpc&utm_campaign=19619206691&utm_content=646207805913&utm_term=dsa-1944158660633_&GL_Ad_ID=646207805913&GL_Campaign_ID=19619206691&ISP=1&npl=1&af_adset_id=143446769417&ppu=9801673&gad_source=1&gclid=CjwKCAjw-qi_BhBxEiwAkxvbkK-gg45j1OeaLuHlxWGtOtqIfu7CPDBE0jb7nPAYYygn3DLMsd6aKBoC0p4QAvD_BwE

9. Café arábica: es un producto básico que se consume en todo el mundo en forma de granos de café de esta variedad de la planta. Los granos de café arábica son procesados para la preparación de una bebida elaborada. El café arábica crece en regiones subtropicales y tropicales, ya sea en altitudes altas o bajas. Para su producción, es necesario cosechar, lavar y secar los granos de la planta de café arábica. Luego, se remueve la cascara y son tostados, para despues de eso comercializarlos como granos enteros o molidos en polvo más fino.

    Además de la preparación de café líquido, el grano de la planta puede usarse para la producción de cerveza o como aromatizante. Además, también es un ingrediente común en bebidas calientes, bebidas frías y platos dulces. A pesar de su uso extendido, el café arábica no es considerado un producto de primera necesidad. Es la variedad de café que predomina en el mercado, especialmente en comparación al café Robusta, que está mucho menos extendido.
 
    El precio del café arábica varía según los índices de renta discrecional de los consumidores, además de aspectos adicionales como la política mundial, las condiciones climáticas, la logística y el transporte del grano. https://es.investing.com/commodities/us-coffee-c-historical-data

10. Cacao: es una de las materias primas más utilizadas en el mundo. Se trata del pilar de la industria chocolatera mundial y también se emplea en muchos otros productos de industrias como las de alimentos y bebidas, cosmética y farmacia.

    África es la fuente principal de cultivo de cacao, pues Costa de Marfil es el mayor productor mundial, seguida de Ghana. Nigeria y Camerún también se encuentran entre los cinco mayores productores del mundo. El único país no africano entre los cinco primeros es Indonesia. 

    La gráfica del cacao podría verse influida por diversos factores, como la oferta y la demanda, las tendencias globales en la alimentación y la nutrición, las condiciones climáticas, las disputas políticas, y más. https://es.investing.com/commodities/us-cocoa-historical-data?utm_source=google&utm_medium=cpc&utm_campaign=19619206691&utm_content=646207805919&utm_term=dsa-1944158660633_&GL_Ad_ID=646207805919&GL_Campaign_ID=19619206691&ISP=1&npl=1&af_adset_id=143446769417&ppu=9801673&gad_source=1&gclid=CjwKCAjw-qi_BhBxEiwAkxvbkA5YtG26raopXscCVu6PEyf-woMa78uyU1eJLXZdHrq7FGJ2gGkaCxoC58AQAvD_BwE


### 2- Obtencion del dataset

He cargado los 10 csv. En algunos casos no se han podido descargar todas las filas necesarias asi que se ha tenido que hacer en 2 dataframe que posteriormente he juntado con la funcion concat de la libreria de pandas. Para hacer este apartado he creado un directorio con las rutas donde se encuentran, es decir, la carpeta data, seguidamente he echo una funcion con un for para que recorra el directorio y los junte todos con la funcion concat.

A continuacion con la funcion merge he ido juntando todos los dataframes del directorio hasta convertirlo en uno, cada columna lleva el nombre de dicha columna y el nombre de la materia a la que corresponde. El primer dataframe lo coge solo y despues va añadiendo con la opcion 'outer' para hacer un full join.

### 3- Transformación

#### Convertir la base de datos para poder trabajar con ella 

- convertir la variable fecha en tipo data, he creado una funcion llamada convertir_fecha para poder hacerlo y ordenar el indice por la fecha.

- quitar el caracter de % de la variable % variacion, he usado la funcion replace.


#### Limpieza de nulos: 

- He borrado las columnas de vol. ya que representaban la volatilidad, que ya va representada por el % de volatilidad pero era una variable que venia nulos asi que me quedo con la variable del %. 

- Funcion Quitar_domingos es una funcion para quitar todos los datos correspondientes a los dias que sean domingo ya que la bolsa esta cerrada los fines de semana y si tenemos datos es porque son premercado o de otra bolsa.

- quitar datos casi vacios, he creado esa funcion para quitar las filas en las que solo haya valores en 3 materias o menos ya que si hay tan pocos datos es porque ha tenido que estar cerrada la bolsa o ha sido festivo y considero que ese dato no me interesa.

- No tenemos el valor de los primeros años de las materias de Plomo, Paladio y Platino. He creado una funcion para que rellene los precios anteriores a la primera fecha con los valores de la primera fecha que tenemos 

- el resto de valores NA he echo lo mismo que en el punto anterior, poner los datos del dia anterior.

### 4- Importación

He creado una carpeta llamada importación con las bases de datos de cada materia limpios y con una columna extra con el nombre de dicha materia para en un futuro en el dashboard de power bi poder cargarlo con la opcion de carpeta y que se junten todos los datasets en formato 'long' ya que en las visualizaciones de powerbi me interesa ese formato

### 4- Visualizaciones 

Para hacer inferencia he creado una tabla de estadisticas de la variable del valor último llamada estadisticas. 

He realizado varias graficas temporales para verlas mejor he separado primero con todas las materias, luego con las materias que tienen los precios mas bajos ya que si no no se pueden ver. Estos son la plata, petroleo, gas natural y cobre. 
    - Viendo estos graficos podemos ver que el oro sigue una tendencia alcista continua y la plata tambien. 
    - El cacao ha tenido una fuerte subida desde el 2024.
    - El resto de metales son mas o menos estables salvo el paladio que subio mucho y ya ha recuperado el valor del precio estable que tenia.
    - Podemos ver que el gas natural sigue las subidas del petroleo
    - El petroleo tiene muy en cuenta las crisis economicas que ha habido como en 2008 y en 2020 en el covid. Baja mucho el precio en muy poco tiempo.

He realizado graficos de boxplot para las materias menos el cacao para ver como se distribuian, podemos ver que los valores mas dispersos y por lo tanto los que tienen mas outliers son los valores del café y del paladio.

### 5- Inferencia

He creado la correlacion de las materias junto con un grafico heatmap ( gráfico de calor). En el podemos ver que las siguientes correlaciones son las mas elevadas:
    - oro: 88% con la plata y 83% con el cobre 
    - petroleo: 79% con el cobre 
    - plata: 87% con el cobre y 83% con el café 
    - café: a demas de la plata, 79% con el cobre

### 6- Contraste de hipotesis

He creado varias hipotesis para ver si se comportan de la misma manera 2 materias concretas, para ello he creado una funcion en la cual puedes escribir por el imput que te pide la terminal que introduzcas el nombre de las 2 materias y lo calcula respecto al % de varianza.

    - Las materias de ejemplo que he usado son el oro y el plomo, podemos ver que no podemos aceptar la hipotesis alternativa, asi que podemos decir que la varianza es diferente.

### 7- Modelo de prediccion

He creado un modelo de prediccion ARIMA para el Platino, cogiendo los datos desde el 01-01-2009 hasta el 01-01-2025 y que tenga en cuenta los 5 dias anteriores y los 5 dias posteriores y que prediga los 365 dias restantes y con un intervalo de confianza del 90%.

He encapsulado el codigo en una funcion y se puede usar el mismo modelo para el resto de materias o cambiar al gusto.


### 8- conclusiones dashboard powerbi

    - Como hemos dicho, con los graficos podemos ver la distribucion en el tiempo, lo mas destacable son las subidas del 2024 del cacao y que el oro sigue una tendencia alcista a lo largo del tiempo y tiene muy poca correccion.

    - Podemos ver que hay correlacion entre las variables del oro y la plata, eso puede ser util ya que en diferentes brokers cobran comision y hay diferenciales de apertura y se puede invertir en la variable que este mas correlacionada y que tenga menos diferencial y comisiones.

    - Por otro lado tenemos una tabla en la que muestra cuantos dias lleva cerrando en positivo o negativo, eso puede ser un indicador de que si lleva varios dias igual puede haber una correccion y cambio de tendencia y puede ser momento para cerrar la posicion con ganancias y esperar a que pase dicha correccion.

    

