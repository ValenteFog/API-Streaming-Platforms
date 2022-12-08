<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Data Engineering`**</h1>


## ¡Bienvenidos! 
Mi nombre es Juan Valentín Fogliatti. Soy estudiante de Soy Henry, de la cohorte Nº5 de la carrera de Data Science, y actualmente estoy transitando la etapa de Labs. Como el título lo indica, este es el Proyecto Individual Nº1, en el cual desempeñamos el rol de un **Data Engineer**.  

<hr>  

## **Descripción del Proyecto**
Se nos ha facilitado un repositorio que incluse 4 datasets de conocidas plataformas de streaming: Amazon Prime, Disney+, Hulu y Netflix. Dichos datasets se encuentran en archivos de diferentes extensiones, y nuestra labor consiste en ingestarlos, aplicar las transformaciones que consideremos pertinentes, y luego disponibilizar los datos limpios para su consulta a través de una API. Esta API deberá ser construida en un entorno virtual dockerizado. Un plus será levantar esta API en Mogenius.

<br>

## **Objetivos a alcanzar**
Para este proyecto debemos ser capaces de:

1. Ingestar y normalizar los datos.

2. Relacionar el conjunto de datos y transformarlos de forma necesaria para poder realizar consultas. 

3. Crear una API en un entorno Docker.

5. Realizar las consultas solicitadas, expuestas en el siguiente apartado.

6. Realizar un video demostrativo.

7. Realizar un deployment de la API en Mogenius.

<br>

### Las consultas a realizar son:

+ Máxima duración según tipo de film (película/serie), por plataforma y por año:
    El request debe ser: get_max_duration(año, plataforma, [min o season])

+ Cantidad de películas y series (separado) por plataforma
    El request debe ser: get_count_plataform(plataforma)  
  
+ Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo.
    El request debe ser: get_listedin('genero')  
    Como ejemplo de género pueden usar 'comedy', el cuál deberia devolverles un cunt de 2099 para la plataforma de amazon.

+ Actor que más se repite según plataforma y año.
  El request debe ser: get_actor(plataforma, año)

<br>

## **Archivos dentro del Repositorio**
Dentro de este repositorio tenemos una serie de archivos y carpetas que brevemente expondremos.

* El archivo 'PI01_procesos.ipynb' es un notebook de jupyter donde básicamente se despliega todo el proyecto. Consta de una primera parte en donde se hace la ingesta de datos, se exploran esos datos y luego se transforman en función de las necesidades. El output final es un archivo '.csv' que contiene la información procesada y lista para luego ser utilizada por la API. Una segunda parte expone las funciones que se utilizarán para realizar las consultas a la API que creemos.

* El archivo 'Dockerfile' que contiene las instrucciones necesarias para crear una imagen del contenedor desde cero e indica la imágen base que va a utilizar, en nuestro caso FastAPI.

* La carpeta 'Datasets' incluye 5 archivos. Cuatro de ellos son los fuentes de nuestros datos, que nos fueron facilitados para este trabajo. El quinto archivo es el '.csv' resultante del proceso de ETL que realizamos en el notebook, y que será tomado por la API para realizar las consultas.

* La carpeta 'app' contiene el archivo 'main.py', un archivo de Python que contiene todo lo necesario para levantar la API. Allí se instancia FastAPI, se define la homepage para nuestra API, y el código para realizar las consultas (que traemos también del notebook).

<br>

## **Tecnologías utilizadas**
Para realizar todo este proyecto se utilizó:
* Python
* Docker
* Librerías de Python: pandas, FastAPI
* Mogenius
* Github