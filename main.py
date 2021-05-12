from fastapi import FastAPI, Request
import json

app = FastAPI()

DATOS = {
    "1":"Python",
    "2":"Java",
    "3":"PHP",
    "4":"JavaScript",
    "5":"C++"
}

def parse_json(data):
    sin_codificar = json.dumps(data)
    return json.loads(sin_codificar)

@app.get("/")
def raiz():
    sin_codificar = json.dumps(DATOS)
    return json.loads(sin_codificar)

@app.post("/agregar")
async def agregar(request:Request):
    nuevos_datos = {}
    formdata = await request.form()
    i = 1
    for id in DATOS:
        nuevos_datos[id] = DATOS[id]
        i += 1
    
    nuevos_datos[str(i)] = formdata["nuevolenguaje"]
    return parse_json(nuevos_datos)
