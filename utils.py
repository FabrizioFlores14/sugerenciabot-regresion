def generar_mensaje(producto: str, riesgo: float, stock: float, umbral: float, prediccion: float) -> str:
    mensaje = f"🔍 Producto: {producto}\n"
    mensaje += f"- Nivel de riesgo actual: {riesgo}\n"
    mensaje += f"- Stock disponible: {stock} unidades\n"
    mensaje += f"- Umbral mínimo definido: {umbral} unidades\n"
    mensaje += f"- Predicción de ventas semanales: {round(prediccion, 2)} unidades\n\n"

    if prediccion > umbral and stock < umbral:
        mensaje += f"📌 Recomendación: Se anticipa una **alta demanda**. Se recomienda realizar una reposición inmediata."
    elif prediccion > stock:
        mensaje += f"⚠️ Alerta: La demanda estimada supera el stock actual. Evaluar reposición urgente."
    elif prediccion < 1:
        mensaje += f"✅ Reposición no necesaria: No se anticipan ventas significativas esta semana."
    else:
        mensaje += f"🟡 Observación: El producto presenta una demanda moderada. Monitoréalo de cerca."

    return mensaje

