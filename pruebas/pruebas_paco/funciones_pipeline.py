# PIPELINE

def pipeline(*steps):
    def wrapper(inputs):
        for step in steps:
            inputs = step(inputs)
        return inputs
    return wrapper

# Contar nulos originales

def step2(df):
    lista_cols = []
    cols_base = ['Country Name','Country Code','year', 'count_null', 'crisis_target']
    for col in df.columns:
        if col not in cols_base:
            lista_cols.append(col)
    return lista_cols

def cols_nulos(df,lista_cols):
    df = df.copy()
    df["count_null"] = df[lista_cols].isna().sum(axis=1)
    df["some_null"]  = (df["count_null"] > 0).astype(int)
    return df


def cols_nulos_wrapper(df):
    lista_cols = step2(df)
    return cols_nulos(df,lista_cols)


# Filtrado de países con >50% de nulos

def step1(df):
    lista_paises = df['Country Name'].drop_duplicates().to_list()
    return lista_paises

def step2(df):
    lista_cols = []
    cols_base = ['Country Name','Country Code','year', 'count_null', 'crisis_pred']
    for col in df.columns:
        if col not in cols_base:
            lista_cols.append(col)
    return lista_cols

def contador_nulos(df, lista_paises, lista_cols,valor):
    df = df.copy()
    rows = []
    for pais in lista_paises:
        for col in lista_cols:
            porc_nulos_col = round(df.loc[df['Country Name'] == pais,col].isna().mean(),2)
            if porc_nulos_col > valor:
                rows.append((pais,col,porc_nulos_col))

    
                        
    return pd.DataFrame(rows,columns=['country','indicator','media_null'])

def contador_nulos_wrapper(df,valor=0.70):
    lista_paises = step1(df)
    lista_cols = step2(df)
    df_null = contador_nulos(df, lista_paises, lista_cols,valor)
    paises_null = df_null['country'].drop_duplicates().to_list()
    return df_null,paises_null



# Relleno de nulos:

def step1(df):
    lista_paises = df['Country Name'].drop_duplicates().to_list()
    return lista_paises

def step2(df):
    lista_cols = []
    cols_base = ['Country Name','Country Code','year', 'count_null', 'crisis_pred']
    for col in df.columns:
        if col not in cols_base:
            lista_cols.append(col)
    return lista_cols



def relleno_nulos_media_pais(df,lista_paises,lista_cols, how = 'mean'):
    import numpy as np
    from pandas.api.types import is_numeric_dtype
    df = df.copy()
    if how == 'mean':   
        for pais in lista_paises:
            for col in lista_cols:
                if is_numeric_dtype(df[col]):
                    media_col_x_pais = round(df.loc[(df['Country Name'] == pais),col].mean(),6)
                    if np.isnan(media_col_x_pais):
                        media_col_x_pais = round(df[col].median(),6)
                    filtro = df['Country Name'] == pais
                    df.loc[filtro, col] = df.loc[filtro, col].fillna(media_col_x_pais)
                else:
                    continue
        print(df.isna().mean())
        return df
    elif how == 'median':
        for pais in lista_paises:
            for col in lista_cols:
                if is_numeric_dtype(df[col]):
                    media_col_x_pais = round(df.loc[(df['Country Name'] == pais),col].median(),6)
                    if np.isnan(media_col_x_pais):
                        media_col_x_pais = round(df[col].median(),6)
                    filtro = df['Country Name'] == pais
                    df.loc[filtro, col] = df.loc[filtro, col].fillna(media_col_x_pais)
                else:
                    continue
        print(df.isna().mean())
        return df
    
def relleno_nulos_wrapper(df,how = 'mean'):
    lista_paises = step1(df)
    lista_cols = step2(df)
    return relleno_nulos_media_pais(df,lista_paises,lista_cols, how)

# Seleccion de features con correlacion > 70%

def step2(df):
    lista_cols = []
    cols_base = ['Country Name','Country Code','year', 'count_null', 'some_null','crisis_pred']
    for col in df.columns:
        if col not in cols_base:
            lista_cols.append(col)
    return lista_cols


def features_corr(df,lista_cols,criterio_col = 0.7):
    import numpy as np
    excluidas = []
    corr_numeric = df[lista_cols].corr(numeric_only = True)
    
    for col in lista_cols:
        print(f"Comprobando colinealidad de {col}")
        if col not in excluidas:
            for col_2, valor_corr in corr_numeric[col].items():
                print(f"\tComprobando {col} con {col_2}")
                if col != col_2 and col_2 in lista_cols:
                    if np.abs(valor_corr) >= criterio_col:
                        print(f"\t\t--> {col} correla con {col_2} al {valor_corr:0.4f}, EXCLUIMOS {col_2} <--")
                        excluidas.append(col_2)
                    else:
                        print(f"\t\t{col} correla con {col_2} al {valor_corr:0.4f}, mantenemos {col_2}")
                elif col == col_2:
                    print("\t\tSon la misma variable, no comprobamos")
    
        elif col in excluidas:
            print(f"\tLa columna {col} ya ha sido excluida")
    
    excluidas = list(set(excluidas))
    return excluidas


def features_corr_wrapper(df):
    lista_cols = step2(df)
    return features_corr(df,lista_cols,criterio_col = 0.7)

# CLASES
import pandas as pd
import re
from sklearn.base import BaseEstimator, TransformerMixin

class CrisisDataExtractor(BaseEstimator, TransformerMixin):
    #Extrae años de crisis desde columnas tipo texto y genera un dataset en formato largo 
    def __init__(self, countries_filter=None):
        # Lista de países a filtrar (ej. top_68).
        self.countries_filter = countries_filter
        self.crisis_cols = {
            "banking_start": "Systemic Banking Crisis (starting date)",
            "currency": "Currency Crisis",
            "sovereign_debt": "Sovereign Debt Crisis (year)",
            "debt_restruct": "Sovereign Debt Restructuring (year)"
        }

    def fit(self, X, y=None):
        return self

    def _extract_years(self, value):
        # Extrae años .
        if pd.isna(value):
            return []
        return [int(y) for y in re.findall(r"\d{4}", str(value))]

    def transform(self, X):
        X = X.copy()
        # Filtrar países si se especifica
        if self.countries_filter is not None:
            X = X[X["Country"].isin(self.countries_filter)]
        rows = []
        # Iterar filas
        for _, row in X.iterrows():
            country = row["Country"]
            # Iterar tipos de crisis
            for crisis_key, crisis_col in self.crisis_cols.items():
                years = self._extract_years(row.get(crisis_col))
                for year in years:
                    rows.append({
                        "Country": country,
                        "year": year,
                        "crisis_type": crisis_key,
                        "crisis_dummy": 1
                    })
        crisis_long = pd.DataFrame(rows)
        return crisis_long
    
class CrisisPivotTransformer(BaseEstimator, TransformerMixin):
    # Transforma un df long en wide
    def __init__(self, index_cols=None):
        self.index_cols = index_cols or ["Country", "year"]

    def fit(self, X, y=None):
        # No aprende parámetros
        return self

    def transform(self, X):

        df = X.copy()
        # Validación básica de columnas esperadas
        required_cols = set(self.index_cols + ["crisis_type"])
        missing_cols = required_cols - set(df.columns)

        if missing_cols:
            raise ValueError(
                f"Faltan columnas requeridas para el pivot: {missing_cols}"
            )
        # Si no existe crisis_dummy, lo creamos
        if "crisis_dummy" not in df.columns:
            df["crisis_dummy"] = 1
        # Pivot LONG → WIDE
        events_wide = (
            df.pivot_table(
                index=self.index_cols,
                columns="crisis_type",
                values="crisis_dummy",
                aggfunc="max",
                fill_value=0
            )
            .reset_index()
        )
        # Limpiar metadato del nombre de columnas
        events_wide.columns.name = None
        # Asegurar tipo entero (evita floats 0.0/1.0)
        crisis_cols = [
            col for col in events_wide.columns
            if col not in self.index_cols
        ]

        events_wide[crisis_cols] = events_wide[crisis_cols].astype(int)

        return events_wide
    
class CrisisMerger(BaseEstimator, TransformerMixin):
    def __init__(self, df_macro):
        self.df_macro = df_macro.copy()

    def fit(self, X, y=None):
        return self

    def transform(self, X):

        df_events = X.copy()
        # Validaciones básicas
        required_cols = {"Country", "year"}
        missing_cols = required_cols - set(df_events.columns)

        if missing_cols:
            raise ValueError(f"Faltan columnas requeridas: {missing_cols}")
        # Crear etiqueta ANY_CRISIS
        crisis_cols = [c for c in df_events.columns if c not in ["Country", "year"]]

        df_events["any_crisis"] = (df_events[crisis_cols].sum(axis=1).gt(0).astype(int))

        # Aplicar SHIFT temporal (T-1)
        df_events["year_pred"] = df_events["year"] - 1

        # Preparar tabla de etiquetas
        labels = (
            df_events[["Country", "year_pred", "any_crisis"]]
            .rename(columns={
                "Country": "Country Name",
                "year_pred": "year"
            })
            .drop_duplicates()
        )

        # Merge con macro
        final_df = self.df_macro.merge(labels,on=["Country Name", "year"],how="left")

        # Construir target final
        final_df["crisis_target"] = (final_df["any_crisis"].fillna(0).astype(int))

        final_df = final_df.drop(columns=["any_crisis"])

        # Orden final limpio
        final_df = final_df.sort_values(["Country Name", "year"]).reset_index(drop=True)

        return final_df