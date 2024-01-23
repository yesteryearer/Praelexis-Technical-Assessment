import pandas as pd

def analyse_columns(df: pd.DataFrame):
    column_analysis = []

    for column in df.columns:
        data_type = df[column].dtype
        total_missing = df[column].isnull().sum()
        missing_ratio = total_missing / len(df) * 100
        unique_values = df[column].nunique()

        column_info = {
            'Column': column,
            'Data Type': data_type,
            'Missing Values': total_missing,
            'Missing Ratio (%)': f'{missing_ratio:.2f}%',
            'Unique Values': unique_values
        }
        column_analysis.append(column_info)

    return pd.DataFrame(column_analysis)