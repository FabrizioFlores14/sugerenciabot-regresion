# SugerenciaBot Regresión 📈

Este microservicio expone un endpoint `/evaluar` que recibe registros diarios de productos en formato JSON y retorna sugerencias personalizadas de reposición mediante un modelo de regresión lineal múltiple con interacción.

## 📊 Modelo aplicado

Se entrena un modelo por producto utilizando la siguiente fórmula: cantidad_ventas ~ riesgo + stock + umbral + riesgo:stock


El término de interacción `riesgo:stock` permite capturar relaciones complejas entre las variables, generando recomendaciones más inteligentes.

## 🚀 Funcionamiento

1. **Input**: Lista de registros diarios desde N8N (vía HTTP POST).
2. **Procesamiento**: Entrenamiento automático por producto.
3. **Output**: Mensajes explicativos por producto como sugerencias para reposición.

## 📬 Formato de respuesta

```json
{
  "sugerenciasp": [
    "🔍 Producto: A\n- Nivel de riesgo: ...\n📌 Recomendación: ...",
    "🔍 Producto: B\n- Nivel de riesgo: ...\n⚠️ Alerta: ..."
  ]
}

Estas sugerencias se integran en un correo semanal automatizado vía N8N.
