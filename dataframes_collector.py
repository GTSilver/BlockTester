import pandas as pd
from loader import get_filelist

def dataframes_list_concatinate_vertical(column_names: [str], dataframe_list: [pd.DataFrame]) -> pd.DataFrame:
    result = dataframe_list[0][column_names]
    for i in range(1, len(dataframe_list) - 1):
        result = pd.concat([result, dataframe_list[i][column_names]])
    result = result.reset_index(drop = True)
    return result.fillna(0)


def dataframes_list_concatinate_horizontal(column_name: str, dataframe_list: [pd.DataFrame]) -> pd.DataFrame:
    result = dataframe_list[0][column_name]
    for i in range(1, len(dataframe_list)):
        result = pd.concat([result, dataframe_list[i][column_name]], axis = 1)
    return result
