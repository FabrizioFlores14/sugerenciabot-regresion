from fastapi import FastAPI, Request
from pydantic import BaseModel
from model import entrenar_y_predecir

app = FastAPI()

class DatosEntrada(BaseModel):
    registros: list[dict]  # Lista de diccionarios con los datos diarios

@app.post("/evaluar")
async def evaluar(data: DatosEntrada):
    try:
        sugerencias = entrenar_y_predecir(data.registros)
        return {"sugerenciasp": sugerencias}
    except Exception as e:
        return {"error": str(e)}
