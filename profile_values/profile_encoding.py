"""Analysing the encoding styles"""

import pandas as pd


def encoding_analysis(df_column):
    """
        Checks the encoding style of the strings and
        Args:
            df_column (pandas DataFrame): Input pandas DataFrame
        Returns:
            dict (dict)
    """
    dict_encoding_analysis = {}
    contains_unusual_char = info_compatible_encoding(df_column)
    if contains_unusual_char:
        df1, df2 = info_list_unusual_chars(contains_unusual_char, df_column)
    # Storing the return values in dictionary
    dict_encoding_analysis['contains_unusual_chars'] = contains_unusual_char
    dict_encoding_analysis['unusual_strings'] = df1
    dict_encoding_analysis['strings_with_unusual_chars'] = df2
    return dict_encoding_analysis


def info_compatible_encoding(df_column):
    """
        Returns if the given data frame has strings that
        contain unusual characters.
        Args:
            df_column (pandas DataFrame): Input pandas DataFrame
        Returns:
            contains_unusual_char (bool)
    """
    col_title = df_column.columns.get_values()[0]
    contains_unusual_char = False
    data_frame = df_column
    for each in data_frame.iterrows():
        curr_attr = each[1][col_title]
        try:
            curr_attr.encode('ascii')
        except ValueError:
            contains_unusual_char = True
            break
            #             if "\\x" in ascii(curr_attr):
            #                 contains_unusual_char = True
    return contains_unusual_char


def info_list_unusual_chars(contains_unusual_char, df_column):
    """
        Returns 2 lists of strings with unusual characters and strings along
        with indicated unusual characters.
        Args:
            contains_unusual_char(bool): Input bool
            df_column (pandas DataFrame): Input pandas DataFrame
        Returns:
            df1,df2 (tuple of pandas DataFrames)
    """
    data_frame = df_column
    col_title = df_column.columns.get_values()[0]
    non_ascii_str = []
    list_str_chr = []
    if contains_unusual_char:
        for each in data_frame.iterrows():
            non_ascii_char_string = ''
            curr_attr = each[1][col_title]
            try:
                curr_attr.encode('ascii')
            except:
                for letter in curr_attr:
                    if ord(letter) < 32 or ord(letter) > 126:
                        non_ascii_str += [curr_attr]
                        if non_ascii_char_string == '':
                            non_ascii_char_string = letter
                        else:
                            non_ascii_char_string = non_ascii_char_string + \
                                                    ' , ' + letter
                list_str_chr.append([curr_attr, non_ascii_char_string])
        df1 = print_unusual_str(non_ascii_str)
        df2 = print_mapping_unusual(list_str_chr)
        return df1, df2


def print_unusual_str(list_unusual_strings):
    """
        Returns a DataFrame of strings that contain unusual characters.
        Args:
            list_unusual_strings (list): Input list
        Returns:
            unusualStringsDataFrame (pandas DataFrame)
    """
    unusual_strings_data_frame = pd.DataFrame(list_unusual_strings,
                                              columns=['String'])
    return unusual_strings_data_frame


def print_mapping_unusual(list_unusual_mapping):
    """
        Returns a DataFrame with 2 columns of strings and the
        unusual characters in each.
        Args:
            list_unusual_mapping (list): Input list
        Returns:
            stringsWithUnusualChar (pandas DataFrame)
    """
    strings_with_unusual_char = pd.DataFrame(list_unusual_mapping,
                        columns=['String', 'Unusual Character'])
    return strings_with_unusual_char
