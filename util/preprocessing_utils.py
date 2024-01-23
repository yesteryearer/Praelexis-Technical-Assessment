import pandas as pd

def standardize_column(df: pd.DataFrame, column_name: str):
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in DataFrame")

    mean = df[column_name].mean()
    std_dev = df[column_name].std()
    df[column_name] = (df[column_name] - mean) / std_dev

    return df

def standardize_all_columns(df: pd.DataFrame):
    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            mean = df[column].mean()
            std_dev = df[column].std()

            if std_dev != 0:
                df[column] = (df[column] - mean) / std_dev
            else:
                df[column] = df[column] - mean
        else:
            print(f"Skipping non-numeric column: {column}")

    return df
