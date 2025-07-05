from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List
from app.model import entrenar_y_predecir

app = FastAPI(
    title="SugerenciaBot - Recomendador por Regresión",
    description="API para generar sugerenciasp semanales usando regresión lineal múltiple con interacción.",
    version="1.0.0"
)

# Modelo de entrada para cada registro
class RegistroInventario(BaseModel):
    Producto: str
    Fecha: str
    Stock: int
    Riesgo: float
    veces_vendido: int
    cantidad_vendida: int

@app.post("/sugerenciasp")
async def generar_sugerenciasp(data: List[RegistroInventario]):
    try:
        lista_dicts = [item.dict() for item in data]
        resultado = entrenar_y_predecir(lista_dicts)
        return JSONResponse(content=resultado)
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
