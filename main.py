from printer import *
from dataframes_collector import *
from analyser import *

cfg = Config('config.json')
dataframe_list = load_dataframe_list(cfg)
result_dataframe = dataframes_list_concatinate_vertical([cfg.target_column_parameter], dataframe_list)

column_list = dataframe_list[0].columns.to_list()
setting_columns = column_list[column_list.index(cfg.last_column_separator_name) + 1:]
setting_dataframe = dataframes_list_concatinate_vertical(setting_columns, dataframe_list)

print_features_important(setting_dataframe, result_dataframe, setting_columns)

main_dataframe = dataframes_list_concatinate_horizontal(cfg.target_column_parameter, dataframe_list)
main_dataframe.columns = [x[:5] for x in get_filelist(cfg)]

create_report(main_dataframe).to_csv('output.csv', sep='\t')
