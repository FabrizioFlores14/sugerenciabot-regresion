def calcular_score_reposicion(row):
    """
    Calcula el score combinando predicción, riesgo y stock inverso.
    """
    pred = row['prediccion']
    riesgo = row['Riesgo']
    stock = row['Stock']

    # Escala del score: más predicción + más riesgo + menos stock = mayor score
    score = (0.5 * pred) + (0.3 * riesgo) + (0.2 * (1 / (stock + 1)))  # +1 para evitar división por cero
    return min(score, 1.0)  # Limitar a máximo 1.0
