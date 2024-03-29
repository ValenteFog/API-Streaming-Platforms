from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import pandas as pd


app = FastAPI()


@app.get("/", response_class=PlainTextResponse)
async def main():
    return '''
Repository: https://github.com/ValenteFog/PI01_DATA05
Video Presentation: https://youtu.be/j5qsUhYff_0

Make queries about movies and series from the streaming platforms
AMAZON PRIME - DISNEY+ - HULU - NETFLIX

USAGE:

To query a platform, use the following names: amazon, disney, hulu or netflix.
To query the duration of a movie or series, use: min or season, respectively.
To query a year, use integer values.
To query by genre, use its English name. There are +100 available.

* To know the maximum duration according to the type of film (movie/series), by platform and by year:
Use /get_max_duration/year/platform/(min or season)
Example: /get_max_duration/2018/hulu/min or /get_max_duration/2015/netflix/season

* To know the number of movies and series (separately) per platform:
Use /get_count_plataform/platform
Example: /get_count_plataform/disney or get_count_plataform/amazon

* To know the number of times a genre and platform repeat with the highest frequency:
Use /get_listedin/genre
Example: /get_listedin/comedy or /get_listedin/action

* To know the actor who appears most frequently according to platform and year:
Use /get_actor/platform/year
Example: /get_actor/netflix/2018
'''


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
    return (f'La producción {out.title[0]}, con {out.duration_len[0]} {duracion}, fue la de mayor duración en la plataforma {plataforma}')


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

    return (f'El genero {genero} se repite {list(query_3.values())[0]} veces para la plataforma {list(query_3)[0]}')


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

    return (f'El actor {list(cant)[0]} se repite {list(cant.values())[0]} veces para la plataforma {plataforma} en el año {anio}')
