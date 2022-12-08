from fastapi import FastAPI
import pandas as pd


app = FastAPI()


@app.get('/')
async def home():
    return {'Bienvenidos a ustedes'}


@app.get('/get_max_duration/{anio}/{plataforma}/{duracion}')
async def get_max_duration(anio: int, plataforma: str, duracion: str):
    plataforma = plataforma.lower().strip()
    duracion = duracion.lower().strip()
    db = pd.read_csv(r'./Datasets/plataforma_db.csv')
    query_1 = db[(db['plataforma'] == plataforma) & (
        db['release_year'] == anio) & (db['duration_type'] == duracion)]
    out = query_1.sort_values(
        'duration_len', ascending=False, ignore_index=True)
    return (f'La producción "{out.title[0]}", con {out.duration_len[0]} {duracion}, fue la de mayor duración en la plataforma {plataforma}')


@app.get('/get_count_plataform/{plataforma}')
async def get_count_plataform(plataforma: str):
    plataforma = plataforma.lower().strip()
    db = pd.read_csv(r'./Datasets/plataforma_db.csv')
    query_2 = db[db['plataforma'] == plataforma]
    cant = query_2['type'].value_counts()
    return (f'En la plataforma {plataforma} hay un total de {cant[0]} películas y de {cant[1]} series')


@app.get('/get_listedin/{genero}')
async def get_listedin(genero: str):
    genero = genero.lower().strip()
    db = pd.read_csv(r'./Datasets/plataforma_db.csv')
    query_3 = db[db['listed_in'].str.contains(genero, case=False)]
    query_3 = query_3.groupby(['plataforma'])[
        'plataforma'].count().sort_values(ascending=False)
    query_3 = query_3.to_dict()

    return (f'El genero "{genero}" se repite {list(query_3.values())[0]} veces para la plataforma {list(query_3)[0]}')


@app.get('/get_actor/{plataforma}/{anio}')
async def get_actor(plataforma: str, anio: int):
    plataforma = plataforma.lower().strip()
    db = pd.read_csv(r'./Datasets/plataforma_db.csv')
    db.drop(db[db['cast'] == 'sin datos'].index, inplace=True)
    query_4 = db.query(
        f'plataforma == "{plataforma}" & release_year == {anio}')
    cant = query_4['cast'].str.get_dummies(sep=', ').sum()
    cant = cant.sort_values(ascending=False).to_dict()

    return (f'El actor "{list(cant)[0]}" se repite {list(cant.values())[0]} veces para la plataforma {plataforma} en el año {anio}')
