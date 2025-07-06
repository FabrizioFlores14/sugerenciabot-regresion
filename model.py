import pandas as pd
import statsmodels.formula.api as smf
from utils import generar_mensaje

def entrenar_y_predecir(data: list[dict]) -> list[dict]:
    df = pd.DataFrame(data)

    if df.empty or len(df["producto"].unique()) < 1:
        return [{"producto": "Ninguno", "sugerencia": "No hay suficientes datos para entrenar"}]

    resultados = []

    for producto, grupo in df.groupby("producto"):
        if grupo["cantidad_ventas"].sum() == 0:
            resultados.append({
                "producto": producto,
                "sugerencia": "No se registran ventas históricas. No se puede generar una predicción confiable."
            })
            continue

        try:
            modelo = smf.ols("cantidad_ventas ~ riesgo + stock + umbral + riesgo:stock", data=grupo).fit()
            predicciones = modelo.predict(grupo)
            promedio_pred = predicciones.mean()

            riesgo = grupo["riesgo"].iloc[-1]
            stock = grupo["stock"].iloc[-1]
            umbral = grupo["umbral"].iloc[-1]

            mensaje = generar_mensaje(producto, riesgo, stock, umbral, promedio_pred)
            resultados.append({"producto": producto, "sugerencia": mensaje})

        except Exception as e:
            resultados.append({
                "producto": producto,
                "sugerencia": f"No se pudo entrenar el modelo: {str(e)}"
            })

    return resultados

