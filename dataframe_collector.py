import pandas as pd


def dataframe_concat(column_names: [str], dataframe_list: [pd.DataFrame]) -> pd.DataFrame:
    result = dataframe_list[0][column_names]
    for i in range(1, len(dataframe_list) - 1):
        result = pd.concat([result, dataframe_list[i][column_names]])
    result = result.reset_index(drop = True)
    return result.fillna(0)
