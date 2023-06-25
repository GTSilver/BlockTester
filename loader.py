import json
import pandas


class Config:
    filename_separator = ''

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


Config('config.json')
