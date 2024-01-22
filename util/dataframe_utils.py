import pandas as pd

def analyse_columns(dataframe: pd.DataFrame):
    column_analysis = []

    for column in dataframe.columns:
        data_type = dataframe[column].dtype
        total_missing = dataframe[column].isnull().sum()
        missing_ratio = total_missing / len(dataframe) * 100
        unique_values = dataframe[column].nunique()

        column_info = {
            'Column': column,
            'Data Type': data_type,
            'Missing Values': total_missing,
            'Missing Ratio (%)': f'{missing_ratio:.2f}%',
            'Unique Values': unique_values
        }
        column_analysis.append(column_info)

    return pd.DataFrame(column_analysis)