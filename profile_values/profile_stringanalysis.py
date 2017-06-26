"""Analyse dataframe of strings"""

import pandas as pd
import py_valuenormalization as vn


def analyse_strings(data_frame):
    """
        Removes duplicates in a DataFrame of strings
        and forms clusters of the strings.
        Args:
            data_frame (pandas DataFrame): Input pandas DataFrame
        Returns:
            dict_string_analysis (dict)
    """
    dict_string_analysis = {}
    df_no_duplicates = remove_duplicates(data_frame)
    dict_string_analysis['unique_values'] = df_no_duplicates
    dict_string_analysis['cluster_values'] = cluster_strings(df_no_duplicates)
    return dict_string_analysis


def remove_duplicates(data_frame):
    """
        Removes duplicates in a DataFrame of strings.
        Args:
            data_frame (pandas DataFrame): Input pandas DataFrame
        Returns:
            new_df(pandas DataFrame)
    """
    new_df = data_frame.drop_duplicates()
    return new_df


def cluster_strings(data_frame):
    """
        Forms clusters of the strings.
        Args:
            data_frame (pandas DataFrame): Input pandas DataFrame
        Returns:
            clusters (dict)
        """
    col_title = data_frame.columns.get_values()[0]
    values = data_frame[col_title].values.tolist()
    hac = vn.HierarchicalClustering(values)
    clusters = hac.cluster(sim_measure='3gram Jaccard',
                           linkage='single', thr=0.7)
    return clusters
