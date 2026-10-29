"""Limpieza. clean_all() llama a las funciones pequenas en orden."""


def clean_column_names(df):
    """Nombres de columna en minusculas y con guion bajo."""
    # TODO
    return df


def handle_nulls(df):
    """Trata los valores nulos y justifica la estrategia."""
    # TODO
    return df


def clean_all(df):
    """Funcion principal: llama a todas las funciones de limpieza en orden."""
    df = clean_column_names(df)
    df = handle_nulls(df)
    return df
