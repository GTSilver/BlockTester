import pandas as pd
from loader import *


def create_report(dataframe: pd.DataFrame):
    df_analyse = dataframe.copy()
    df_analyse['sum values'] = dataframe.apply(sum, axis=1)
    df_analyse['zero & low count'] = dataframe.apply(lambda x: (x <= 0).sum(), axis=1)
    df_analyse['low zero count'] = dataframe.apply(lambda x: (x < 0).sum(), axis=1)

    result_dict = {'all df': dataframe.stack(),
                   'sum values': df_analyse['sum values'],
                   'zero & low count': df_analyse['zero & low count'],
                   'low zero count:': df_analyse['low zero count'],
                   'low zero is 0 sum': df_analyse[df_analyse['low zero count'] == 0].apply(sum, axis=1)}

    for i in range(len(result_dict)):
        key = list(result_dict.keys())[i]
        result_dict[key] = get_round_stats(result_dict[key], 2)

    result_df = pd.DataFrame(result_dict)

    return result_df.T


def get_round_stats(series: pd.Series, digits: int) -> pd.Series:
    result = pd.Series({'quantile 0.25': series.quantile(0.25),
                        'mean': series.mean(),
                        'quantile 0.75': series.quantile(0.75),
                        'moda': series.mode(),
                        'std': series.std()})

    for i in range(len(result.values)):
        result.iloc[i] = round(result.iloc[i], digits)

    return result

# dataframe.to_csv('awd.csv', sep = '\t')
