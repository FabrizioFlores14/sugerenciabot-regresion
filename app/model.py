import pandas as pd
import statsmodels.formula.api as smf
from app.utils import calcular_score_reposicion

def entrenar_y_predecir(lista_registros):
    df = pd.DataFrame(lista_registros)

    # Asegurar tipos correctos
    df['Stock'] = pd.to_numeric(df['Stock'], errors='coerce')
    df['Riesgo'] = pd.to_numeric(df['Riesgo'], errors='coerce')
    df['veces_vendido'] = pd.to_numeric(df['veces_vendido'], errors='coerce')
    df['cantidad_vendida'] = pd.to_numeric(df['cantidad_vendida'], errors='coerce')

    # Entrenamiento del modelo con interacción
    formula = 'cantidad_vendida ~ Riesgo + Stock + veces_vendido + Riesgo:Stock'
    modelo = smf.ols(formula=formula, data=df).fit()

    # Predicción sobre los mismos datos
    df['prediccion'] = modelo.predict(df)

    # Agrupar por producto para generar sugerencias semanales
    resumen = df.groupby('Producto').agg({
        'Stock': 'last',
        'Riesgo': 'mean',
        'veces_vendido': 'sum',
        'cantidad_vendida': 'sum',
        'prediccion': 'mean'
    }).reset_index()

    # Calcular el score de reposición y clasificar
    resumen['score_reposicion'] = resumen.apply(calcular_score_reposicion, axis=1)

    resumen['recomendado'] = resumen['score_reposicion'] >= 0.5

    # Preparar salida
    sugerenciasp = []
    for _, row in resumen.iterrows():
        sugerenciasp.append({
            "producto": row["Producto"],
            "score_reposicion": round(row["score_reposicion"], 2),
            "stock_actual": int(row["Stock"]),
            "riesgo_promedio": round(row["Riesgo"], 2),
            "recomendado": bool(row["recomendado"]),
            "razon": generar_razon(row)
        })

    return sugerenciasp

def generar_razon(row):
    if row["recomendado"]:
        return "Predicción alta de demanda con combinación crítica de riesgo y stock."
    else:
        return "Predicción baja de venta. No se recomienda reposición inmediata."
