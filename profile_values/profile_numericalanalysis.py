"""Analysing numerical values"""

import numpy as np
import pandas as pd
import pandas_profiling as pp


def numerical_analysis(df_column):
    """
    Returns whether the DataFrame is of type numeric, is a
    hybrid of numerical and non-numerical values,profile report
    of the numerical data.
    Args:
        df_column (pandas DataFrame): Input pandas DataFrame
    Returns:
        dict (dict)
    """
    dict_numerical_analysis = {}
    df_column, is_numeric, is_hybrid = find_type(df_column)
    dict_numerical_analysis['is_numeric'] = is_numeric
    dict_numerical_analysis['is_hybrid'] = is_hybrid
    if is_numeric:
        dict_numerical_analysis['analysis_report'] = pp.ProfileReport(df_column)
    return dict_numerical_analysis


def find_type(df_column):
    """
    Returns whether the DataFrame is of type numeric,
    is a hybrid of numerical and non-numerical values.
    Args:
        df_column (pandas DataFrame): Input pandas DataFrame
    Returns:
        DataFrame,bool,bool: Tuple of pandas DataFrame,bool,bool
    """
    # Initialize all needed values
    col_title = df_column.columns.get_values()[0]
    is_numeric = False
    is_hybrid = False
    # Find if the dType is numerical or not
    if df_column[col_title].dtype == np.number:
        is_numeric = True
    elif check_numeric_type_cast(df_column)[1]:
        is_numeric = True
        df_column = check_numeric_type_cast(df_column)[0]
    if not is_numeric:
        is_hybrid = check_hybrid_type(df_column)
    return df_column, is_numeric, is_hybrid


def check_numeric_type_cast(df_column):
    """
    Checks whether the DataFrame values can be typecast
    to type numeric and returns the DataFrame.
    Args:
        df_column (pandas DataFrame): Input pandas DataFrame
    Returns:
        df_column,isNumeric: Tuple of pandas DataFrame,bool
    """
    col_title = df_column.columns.get_values()[0]
    is_numeric = True
    try:
        df_column[col_title] = pd.to_numeric(df_column[col_title],
                                             errors='raise')
    except:
        is_numeric = False
    return df_column, is_numeric


def check_hybrid_type(df_column):
    """
    Returns whether the DataFrame consists of numeric and non-numeric values.
    Args:
        df_column (pandas DataFrame): Input pandas DataFrame
    Returns:
        bool
    """
    col_title = df_column.columns.get_values()[0]
    col_series = pd.to_numeric(df_column[col_title], errors='coerce')
    if len(col_series.dropna()):
        return True
    else:
        return False
