import os
import json
import pandas as pd


class Config:
    last_column_separator_name = ''
    input_directory_path = ''
    target_column_parameter = ''

    def __init__(self, config_path: str):
        def read_json_attr(config_path_: str) -> {}:
            with open(config_path_, 'r') as f:
                return json.load(f)

        def read_class_attr() -> {}:
            attr = {}
            for k, v in self.__class__.__dict__.items():
                if "__" in k:
                    continue
                attr[k] = v
            return attr

        def fill_class(json_attr_: {}, class_attr_: {}):
            for k in class_attr_.keys():
                setattr(self, str(k), json_attr_[k])

        json_attr = read_json_attr(config_path)
        class_attr = read_class_attr()
        fill_class(json_attr, class_attr)


def load_dataframe_list(cfg: Config) -> [pd.DataFrame]:
    path = cfg.input_directory_path
    csv_list = []
    files = get_filelist(cfg)
    for f in files:
        dataframe = pd.read_csv(path + "\\" + f, sep=';').\
                     set_index("Pass").\
                     sort_index().\
                     fillna(0)
        csv_list.append(dataframe)
    return csv_list


def get_filelist(cfg: Config) -> [str]:
    for root, dirs, files in os.walk(cfg.input_directory_path):
        ...
    return files
