"""profile_encoding.py"""

"""This script contains the methods to perform the analysis on the encoding style of the data frame."""

import pandas as pd
import operator
from IPython.display import display, HTML


def encoding_analysis(df_column):
    """
        Checks the encoding style of the strings and returns if there are any strings
        with unusual characters.
        Args:
            dataframe (pandas dataframe): Input pandas dataframe
        Returns:
            dict (dict)
        Examples:
            >>> dict = encoding_analysis(dataframe)
            >>> dict['containsUnusualCharacters']
            True
            >>> dict['stringsWithUnusualCharacters']
            >>> dict['unusualStrings']

    """
    dict = {}
    print('FULL ANALYSIS' + '\n' + '----------------------------------' + '\n')
    contains_unusual_char = info_compatible_encoding(df_column)
    if contains_unusual_char:
        df1, df2 = info_list_unusal_chars(contains_unusual_char, df_column)
        print('The strings that contain the unusual characters are:')
        display(df1)
        print('The strings with the indicated unusual characters are:')
        display(df2)
    # Storing the return values in dictionary
    dict['containsUnusualCharacters'] = contains_unusual_char
    dict['unusualStrings'] = df1
    dict['stringsWithUnusualCharacters'] = df2
    return dict


def info_compatible_encoding(df_column):
    """
        Returns if the given data frame has strings that contain unusual characters.
        Args:
            dataframe (pandas dataframe): Input pandas dataframe
        Returns:
            contains_unusual_char (bool)
        Examples:
            >>> info_compatible_encoding(dataframe)
            True
    """
    col_title = df_column.columns.get_values()[0]
    contains_unusual_char = False
    dataFrame = df_column
    for index, row in dataFrame.iterrows():
        curr_attr = row[col_title]
        try:
            curr_attr.encode('ascii')
        except ValueError as error:
            contains_unusual_char = True
            break
            #             if "\\x" in ascii(curr_attr):
            #                 contains_unusual_char = True
    if contains_unusual_char:
        print('The data frame contains unusual characters')
        results.append('Unusual characters present: Yes\n')
    else:
        print('The data frame does not contain unusual characters')
        results.append('Unusual characters present: No\n')
    return contains_unusual_char


def info_list_unusal_chars(contains_unusual_char, df_column):
    """
        Returns 2 lists of strings with unusual characters and strings along
        with indicated unusual characters.
        Args:
            contains_unusual_char(bool): Input bool
            dataframe (pandas dataframe): Input pandas dataframe
        Returns:
            (df1,df2) (tuple of pandas dataframes)
    """
    dataFrame = df_column
    col_title = df_column.columns.get_values()[0]
    non_ascii_str = []
    non_ascii_char = []
    list_str_chr = []
    columns = ['String', 'Character']
    data_frame_curr = pd.DataFrame(columns=columns)
    if contains_unusual_char:
        for index, row in dataFrame.iterrows():
            non_ascii_char_string = ''
            curr_attr = row[col_title]
            try:
                curr_attr.encode('ascii')
            except:
                for letter in curr_attr:
                    if ord(letter) < 32 or ord(letter) > 126:
                        non_ascii_str += [curr_attr]
                        non_ascii_char += [letter]
                        if non_ascii_char_string == '':
                            non_ascii_char_string = letter
                        else:
                            non_ascii_char_string = non_ascii_char_string + ' , ' + letter
                list_str_chr.append([curr_attr, non_ascii_char_string])
        df1 = print_unusual_str(non_ascii_str)
        df2 = print_mapping_unusual(list_str_chr)
        return (df1, df2)


def print_unusual_str(list):
    """
        Returns a dataframe of strings that contain unusual characters.
        Args:
            list (list): Input list
        Returns:
            unusualStringsDataFrame (pandas dataframe)
    """
    unusualStringsDataFrame = pd.DataFrame(list, columns=['String'])
    return unusualStringsDataFrame


def print_mapping_unusual(list):
    """
        Returns a dataframe with 2 columns of strings and the
        unusual characters in each.
        Args:
            list (list): Input list
        Returns:
            stringsWithUnusualChar (pandas dataframe)
    """
    stringsWithUnusualChar = pd.DataFrame(list, columns=['String', 'Unusual Character'])
    return stringsWithUnusualChar
