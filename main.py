from loader import *
from printer import *
from dataframe_collector import *


cfg = Config('config.json')
dataframe_list = load_dataframe_list(cfg)
result_dataframe = dataframe_concat(['Result'], dataframe_list)

column_list = dataframe_list[0].columns.to_list()
setting_columns = column_list[column_list.index(cfg.last_column_separator_name) + 1:]
setting_dataframe = dataframe_concat(setting_columns, dataframe_list)

print_features_important(setting_dataframe, result_dataframe, setting_columns)
