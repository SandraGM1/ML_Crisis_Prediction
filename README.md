# 🌍 **Predictor de Crisis Mundial**

En una era marcada por múltiples crisis e incertidumbre, los datos históricos de los países pueden aportar información valiosa para anticipar posibles crisis futuras.

En este proyecto de **Machine Learning** desarrollamos un modelo capaz de **predecir la probabilidad de que un país experimente una crisis en un año determinado**, utilizando indicadores económicos, financieros, comerciales, y laborales.

Los datos utilizados provienen principalmente de **indicadores macroeconómicos del Banco Mundial**, combinados con información histórica de crisis financieras obtenida de **Leaven & Valencia (IMF)**, una base de datos que identifica episodios de crisis financieras sistémicas en distintos países y años.

El objetivo final del modelo es **identificar de forma temprana posibles crisis**, permitiendo mejorar la capacidad de análisis y anticipación ante eventos económicos adversos.

<hr style="height:6px;border:none;color:#333;background-color:#333;">

## 📑 Tabla de Contenidos
---
- [Descripción](#descripción)
- [Características del Proyecto](#%EF%B8%8F-características-del-proyecto)
- [Estructura del repositorio](#-estructura-de-repositorio)
- [Tecnologías utilizadas](#-tecnologías-utilizadas)
- [Instrucciones de reproducción](#%EF%B8%8F-instrucciones-de-reproducción)
- [Principales resultados](#-principales-resultados)
- [Autores](#autores)

## Descripción
El objetivo del proyecto es predecir la probabilidad de que un país entre en crisis económica en un año concreto a partir de indicadores macroeconómicos históricos. Para ello se ha construido un modelo de clasificación supervisada entrenado con datos económicos y financieros de múltiples países. 

Dado que las crisis son eventos poco frecuentes pero con gran impacto, el modelo se ha optimizado priorizando la detección de crisis reales, minimizando los falsos negativos.

## ⚙️ Características del Proyecto

- **Construcción del dataset**  
Se ha creado un dataset a partir de **indicadores macroeconómicos del Banco Mundial (World Bank)** seleccionados por su relevancia para el análisis de crisis económicas.

Las variables incluyen indicadores relacionados con:

- Sistema financiero y liquidez
- Sector externo
- Deuda y sostenibilidad externa
- Actividad económica
- Inversión y formación de capital
- Inflación y precios
- Variable objetivo

El **target (variable objetivo)** se ha obtenido a partir de la base de datos de crisis financieras de **Laeven & Valencia (IMF)**.

- **Preprocesamiento e Ingeniería de Características**  
El dataset ha pasado por varias fases de preparación: 
  - Selección y priorización de variables mediante análisis de correlación y visualización 
  - Agrupación conceptual de indicadores económicos
  - Tratamiento de valores nulos
  - Transformación estadística mediante Yeo-Johnson
  - Eliminación de variables poco informativas
  - Exclusión de países con **insuficiente disponibilidad de datos**

- **Modelado y Optimización**  
Varios **modelos de clasificación** fueron entrenados para predecir la ocurrencia de crisis económicas. Posteriormente se realizó un proceso de optimización de hiperparámetros para mejorar el rendimiento del modelo. La evaluación se realizó utilizando diferentes métricas, priorizando especialmente la **Sensibilidad de la clase positiva (crisis)**. Esto se debe a que en problemas de riesgo financiero es más importante **detectar la mayor cantidad posible de crisis reales**, incluso a costa de aceptar algunos falsos positivos.

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

README.md
main.ipynb
presentacion.pdf
```
## 🛠 Tecnologías utilizadas

**Lenguajes:**: `python`

**Librerías principales**: `numpy, pandas, scikit-learn, matplotlib, seaborn, (incluir modelos)`

## ▶️ Instrucciones de reproducción

1. Clonar el repositorio

```
git clone https://github.com/SandraGM1/ML_Crisis_Prediction.git
```

2. Ejecutar el notebook principal

```
main.ipynb
```

Este notebook permite reproducir el pipeline completo del proyecto.

## 📊 Principales resultados

El modelo fue evaluado utilizando precisión, sensibilidad y F1-score para ambas clases:
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

Francisco de las Cuevas ([LinkedIn](https://www.linkedin.com/in/francisco-de-las-cuevas-valencia/) | GitHub)  
Sandra García Moreno (LinkedIn | GitHub)  
Sergi de la Cruz Núñez ([LinkedIn](https://www.linkedin.com/in/sergi-de-la-cruz-905543257/) | [GitHub](https://github.com/sergidelacruz))  

<hr style="height:6px;border:none;color:#333;background-color:#333;">
<hr style="height:6px;border:none;color:#333;background-color:#333;">

# 🌍 World Crisis Predictor

In an era marked by multiple crises and uncertainty, historical country data can provide valuable insights for anticipating potential future crises.

In this **Machine Learning** project, we developed a model capable of **predicting the probability that a country will experience a crisis in a given year**, using economic, financial, trade, and labor indicators.

The data used in this project come primarily from **macroeconomic indicators provided by the World Bank**, combined with historical information on financial crises from **Laeven & Valencia (IMF)**, a database that identifies episodes of **systemic financial crises** across different countries and years.

The ultimate goal of the model is to **identify potential crises early**, improving the capacity for analysis and anticipation of adverse economic events.

<hr style="height:6px;border:none;color:#333;background-color:#333;">

## 📑 Table of Contents
---
- [Description](#description)
- [Project Features](#%EF%B8%8F-project-features)
- [Repository Structure](#-repository-structure)
- [Tech Stack](#-tech-stack)
- [Getting Started](#%EF%B8%8F-getting-started)
- [Results](#-results)
- [Authors](#authors)

## Description

The objective of the project is to predict the probability that a country will enter an economic crisis in a given year based on historical macroeconomic indicators. To achieve this, a supervised classification model was built and trained using economic and financial data from multiple countries.

Since crises are rare events but have a major impact, the model was optimized to prioritize the detection of real crises, minimizing false negatives.

## ⚙️ Project Features

- **Dataset Construction**:
A dataset was created using World Bank macroeconomic indicators, selected for their relevance in analyzing economic crises.

The variables include indicators related to:

- Financial System and Liquidity
- External Sector
- Debt and External Sustainability
- Economical Activity
- Investment and Capital Formation
- Inflation and Prizes
- Target Feature

The **target variable** was obtained from the financial crisis database compiled by **Laeven & Valencia (IMF)**.

- **Preprocessing and Feature Engineering**  
The dataset went through several preparation stages:
  - Variable selection and prioritization through correlation analysis and visualization
  - Conceptual grouping of economic indicators
  - Handling missing values
  - Statistical transformation using Yeo-Johnson
  - Removal of low-information variables
  - Exclusion of countries with insufficient data availability

- **Modeling and Optimization**  
Several **classification models** were trained to predict the occurrence of economic crises. Afterwards, a hyperparameter optimization process was carried out to improve model performance. Evaluation was performed using different metrics, with particular emphasis on the **Recall of the positive class (crisis)**. This is because in financial risk problems it is more important to **detect as many real crises as possible**, even if it means accepting some false positives.

- **Implementation**  
The final selected model was saved for future use using joblib, allowing it to be reused for future predictions or integrated into analytical systems.

---
## 📂 Repository Structure
```
src/  
│
├── data_sample/  
│   Muestra del dataset utilizado (máx. 5MB)  
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

README.md
main.ipynb
presentacion.pdf
```
## 🛠 Tech Stack

**Languages:**: `python`

**Main libraries**: `numpy, pandas, scikit-learn, matplotlib, seaborn, (incluir modelos)`

## ▶️ Getting Started

1. Clone the repository
```
git clone https://github.com/SandraGM1/ML_Crisis_Prediction.git
```
2. Run the main notebook
```
main.ipynb
```
This notebook allows you to reproduce the complete project pipeline.

## 📊 Results

The model was evaluated using precision, recall, and F1-score for both classes:
- Class 0: No crisis
- Class 1: Economic crisis

Since the main goal of the project is to **detect as many real crises as possible**, the model prioritizes **maximizing recall for the positive class (crisis)**, even if this results in a higher number of false positives.

This behavior is expected and desirable in risk prediction problems, where **failing to detect a crisis (false negative) is much more costly than generating a false alarm**.

The final model therefore prioritizes:

✔ High sensitivity to economic crises  
✔ Early warning capability  
⚠ At the cost of generating more crisis predictions that may not actually occur  

This approach is common in **financial or economic early warning models**, where the primary objective is **not to overlook critical events**.

## Authors

Francisco de las Cuevas ([LinkedIn](https://www.linkedin.com/in/francisco-de-las-cuevas-valencia/) | GitHub)  
Sandra García Moreno (LinkedIn | GitHub)  
Sergi de la Cruz Núñez ([LinkedIn](https://www.linkedin.com/in/sergi-de-la-cruz-905543257/) | [GitHub](https://github.com/sergidelacruz))  
