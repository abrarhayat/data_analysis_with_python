import pandas as pd
import numpy as np


# A file created for make testing pandas very convenient


def create_df(location, header=None):
    if header is None:
        df = pd.read_csv(location, header=None)
        return df
    else:
        df = pd.read_csv(location)
        df.columns = header
        return df


def print_4_heads(df, text):
    print('\n' + text)
    print(df.head(4))


def replace_cols_with_nan(df, col_names):
    df.dropna(subset=col_names, axis=0, how='any', inplace=True)
    for col_name in col_names:
        df[col_name] = df[col_name].replace('?', np.nan)
    return df


def replace_cols_with_mean(df, col_names):
    for col_name in col_names:
        try:
            mean = df[col_name].astype('float').mean(axis=0)
            df[col_name] = df[col_name].replace(np.nan, mean)
        except (TypeError, ValueError):
            print(col_name, "cannot be converted to float")
    return df


def change_col_types(df, col_names, target_type):
    return df[col_names].astype(target_type)


def get_clean_data_frame(csv_file_dir, columns_to_clean):
    df = create_df(csv_file_dir, columns_to_clean)
    df = replace_cols_with_nan(df, columns_to_clean)
    df = replace_cols_with_mean(df, columns_to_clean)
    df.dropna(subset=columns_to_clean, axis=0, inplace=True)
    return df