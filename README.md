# 🌍 **World Crisis Predictor**

En una era marcada por múltiples crisis e incertidumbre, los datos históricos de los países pueden aportar información valiosa para anticipar posibles crisis futuras.

En este proyecto de Machine Learning desarrollamos un modelo capaz de predecir la probabilidad de que un país experimente una crisis en un año determinado, utilizando indicadores económicos, financieros, comerciales, y laborales.

Los datos utilizados provienen principalmente de **indicadores macroeconómicos del Banco Mundial**, combinados con información histórica de crisis financieras obtenida de **Leaven & Valencia (IMF)**.

El objetivo final del modelo es **identificar de forma temprana posibles crisis**, permitiendo mejorar la capacidad de análisis y anticipación ante eventos económicos adversos.

<hr style="height:6px;border:none;color:#333;background-color:#333;">

## 📑 Tabla de Contenidos
---
- [Descripción](#descripción)
- [Características del Proyecto](#-características-del-proyecto)
- [Estructura del repositorio](#-estructura-del-repositorio)
- [Tecnologías utilizadas](#-tecnologías-utilizadas)
- [Instrucciones de reproducción](#-instrucciones-de-reproducción)
- [Principales resultados](#-principales-resultados)
- [Autores](#autores)

## Descripción
El objetivo del proyecto es predecir la probabilidad de que un país entre en crisis económica en un año concreto a partir de indicadores macroeconómicos históricos. Para ello se ha construido un modelo de clasificación supervisada entrenado con datos económicos y financieros de múltiples países. 

Dado que las crisis son eventos poco frecuentes pero con gran impacto, el modelo se ha optimizado priorizando la detección de crisis reales, minimizando los falsos negativos.

## ⚙️ Características del Proyecto

- **Construcción del dataset**:
Se ha creado un dataset a partir de **indicadores macroeconómicos del Banco Mundial (World Bank)** seleccionados por su relevancia para el análisis de crisis económicas.

Las variables incluyen indicadores relacionados con:

- Sistema financiero y liquidez
- Sector externo
- Deuda y sostenibilidad externa
- Crecimiento económico
- Inflación

El **target (variable objetivo)** se ha obtenido a partir de la base de datos de crisis financieras de **Laeven & Valencia (IMF)**.

- **Preprocesamiento e Ingeniería de Características**:
El dataset ha pasado por varias fases de preparación: 
  - Selección y priorización de variables mediante análisis de correlación y visualización 
  - Agrupación conceptual de indicadores económicos
  - Tratamiento de valores nulos
  - Transformación estadística mediante Yeo-Johnson
  - Eliminación de variables poco informativas
  - Exclusión de países con **insuficiente disponibilidad de datos**

- **Modelado y Optimización**
Se entrenaros varios **modelos de clasificación** () ypara predecir la ocurrencia de crisis económicas. Posteriormente se realizó un proceso de oprimización de hiperparámetros para mejorar el rendimiento del modlo. La evaluación se realizó utilizando diferentes métricas, priorizando especialmente el **Recall de la clase positiva (crisis)**. Esto se debe a que en problemas de riesgo financiero es más importante **detectar la mayor cantidad posible de crisis reales**, incluso a costa de aceptar algunos falsos positivos.

- **Implementación**
El modelo final seleccionado fue guardado par uso posterior mediante joblib, permitiendo su reutilización en futuras predicciones o integración en sistemas de análisis.

---
## 📂 Estructura de repositorio
```
src/  
│
├── data_sample/  
│   Muestra del dataset utilizado (máx. 5MB)  
│
├── img/  
│   Gráficos e imágenes generadas durante el proyecto  
│
├── models/  
│   Modelos entrenados guardados en formato joblib o pickle  
│
├── notebooks/  
│   Notebooks utilizados para exploración, desarrollo y experimentación  
│
└── utils/  
    Código auxiliar reutilizable (funciones, clases y scripts)  
```
## 🛠 Tecnologías utilizadas

**Lenguajes:** 
- `python`

**Librerías principales**: `numpy, pandas, scikit-learn, matplotlib, seaborn, (incluir modelos)`

## ▶️ Instrucciones de reproducción

1. Clonar el repositorio

```
git clone <repo_url>
```

2. Instalar dependencias

```
pip install -r requirements.txt
```

3. Ejecutar el notebook principal

```
main.ipynb
```

Este notebook permite reproducir el pipeline completo del proyecto.

## 📊 Principales resultados

El modelo fue evaluado utilizando precisión, recall y F1-score para ambas clases:
- **Clase 0**: No crisis
- **Clase 1**: Crisis económica

Dado que el objetivo principal del proyecto es **detectar el mayor número posible de crisis reales**, se priorizó **maximizar el recall de la clase positiva (crisis)**, incluso si esto implicaba aceptar un mayor número de falsos positivos.

Este comportamiento es esperado y deseable en problemas de predicción de riesgo, donde **no detectar una crisis (falso negativo) es mucho más costoso que generar una falsa alarma**.

El modelo final prioriza por tanto:

✔ Alta sensibilidad a crisis económicas  
✔ Capacidad de alerta temprana  
⚠ A costa de generar más predicciones de crisis que luego no ocurren

Este enfoque es habitual en **modelos de alerta temprana financiera o económica**, donde el objetivo principal es **no pasar por alto eventos críticos**.

## Autores

Francisco de las Cuevas (LinkedIn | GitHub)  
Sandra García Moreno (LinkedIn | GitHub)  
Sergi de la Cruz Núñez (LinkedIn | GitHub)  
