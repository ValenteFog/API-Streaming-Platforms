from fastapi import FastAPI
import pandas as pd


app = FastAPI()


@app.get('/')
async def home():
    return {'''Juan Valentín Fogliatti <br>
Soy Henry - Data Science 05 - Proyecto Individual 01 <br>

Repositorio: https://github.com/ValenteFog/PI01_DATA05<br>
Video Explicativo:<br>

Haga consultas sobre películas y series de las plataformas de streaming<br>
AMAZON PRIME - DISNEY+ - HULU - NETFLIX<br>

MODO DE USO:<br>

Para consultar una plataforma utilice esta denominación: amazon, disney, hulu ó netflix.<br>
Para consultar la duración de una película o serie utilice: min ó season, respectivamente.<br>
Para consultar un año utilice valores numéricos enteros.<br>
Para consultar por género utilice su denominación en inglés. Hay +100 disponibles.<br>

* Para conocer la máxima duración según tipo de film (película/serie), por plataforma y por año: <br>
Utilice /get_max_duration/año/plataforma/(min o season)<br>
Ejemplo: /get_max_duration/2018/hulu/min ó /get_max_duration/2015/netflix/season<br>

* Para conocer la cantidad de películas y series (por separado) por plataforma: <br>
Utilice /get_count_plataform/plataforma<br>
Ejemplo: /get_count_plataform/disney ó get_count_plataform/amazon<br>

* Para conocer la cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo: <br>
Utilice /get_listedin/genero<br>
Ejemplo: /get_listedin/comedy ó get_listedin/action<br>

* Para conocer el actor que más se repite según plataforma y año: <br>
Utilice /get_actor/plataforma/año<br>
Ejemplo: /get_actor/netflix/2018<br>
'''}


@app.get('/get_max_duration/{anio}/{plataforma}/{duracion}')
async def get_max_duration(anio: int, plataforma: str, duracion: str):
    plataforma = plataforma.lower().strip()
    duracion = duracion.lower().strip()
    db = pd.read_csv(
        r'https://raw.githubusercontent.com/ValenteFog/PI01_DATA05/master/Datasets/plataforma_db.csv')
    query_1 = db[(db['plataforma'] == plataforma) & (
        db['release_year'] == anio) & (db['duration_type'] == duracion)]
    out = query_1.sort_values(
        'duration_len', ascending=False, ignore_index=True)
    return (f'La producción "{out.title[0]}", con {out.duration_len[0]} {duracion}, fue la de mayor duración en la plataforma {plataforma}')


@app.get('/get_count_plataform/{plataforma}')
async def get_count_plataform(plataforma: str):
    plataforma = plataforma.lower().strip()
    db = pd.read_csv(
        r'https://raw.githubusercontent.com/ValenteFog/PI01_DATA05/master/Datasets/plataforma_db.csv')
    query_2 = db[db['plataforma'] == plataforma]
    cant = query_2['type'].value_counts()
    return (f'En la plataforma {plataforma} hay un total de {cant[0]} películas y de {cant[1]} series')


@app.get('/get_listedin/{genero}')
async def get_listedin(genero: str):
    genero = genero.lower().strip()
    db = pd.read_csv(
        r'https://raw.githubusercontent.com/ValenteFog/PI01_DATA05/master/Datasets/plataforma_db.csv')
    query_3 = db[db['listed_in'].str.contains(genero, case=False)]
    query_3 = query_3.groupby(['plataforma'])[
        'plataforma'].count().sort_values(ascending=False)
    query_3 = query_3.to_dict()

    return (f'El genero "{genero}" se repite {list(query_3.values())[0]} veces para la plataforma {list(query_3)[0]}')


@app.get('/get_actor/{plataforma}/{anio}')
async def get_actor(plataforma: str, anio: int):
    plataforma = plataforma.lower().strip()
    db = pd.read_csv(
        r'https://raw.githubusercontent.com/ValenteFog/PI01_DATA05/master/Datasets/plataforma_db.csv')
    db.drop(db[db['cast'] == 'sin datos'].index, inplace=True)
    query_4 = db.query(
        f'plataforma == "{plataforma}" & release_year == {anio}')
    cant = query_4['cast'].str.get_dummies(sep=', ').sum()
    cant = cant.sort_values(ascending=False).to_dict()

    return (f'El actor "{list(cant)[0]}" se repite {list(cant.values())[0]} veces para la plataforma {plataforma} en el año {anio}')
