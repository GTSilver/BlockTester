import pandas as pd
from loader import Config


def select_result_column(column_name: str, cfg: Config, dataframe_list: [pd.DataFrame]) -> [pd.DataFrame]:
    columns_list = dataframe_list.columns.to_list()
    separate_index = columns_list.index(cfg.last_column_separator_name) + 1
    columns = columns_list[:separate_index]

    for i in range
    if column_name in columns:
        return data[column_name]
    else:
        raise NameError("Name not exist in result columns")


def get_setting_columns(cfg: Config, data: pd.DataFrame) -> [str]:
    columns_list = data.columns.to_list()
    separate_index = columns_list.index(cfg.last_column_separator_name) + 1
    return columns_list[separate_index:]

