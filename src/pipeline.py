# pipeline_binaria.py

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer

def criar_pipeline_binaria(colunas_binarias):
    """
    Cria uma pipeline simples para transformar colunas binárias em 0 e 1.
    
    Parâmetros:
        colunas_binarias (list): Lista com os nomes das colunas binárias.

    Retorna:
        ColumnTransformer: Um objeto que transforma as colunas binárias.
    """
    pipeline = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),  # Preenche valores ausentes com o valor mais comum
        ('ordinal', OrdinalEncoder())  # Converte os valores em 0 e 1
    ])

    transformador = ColumnTransformer(transformers=[
        ('binarias', pipeline, colunas_binarias)
    ], remainder='drop')  # Só mantém as colunas binárias por enquanto

    return transformador
