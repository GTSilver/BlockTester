import numpy as np

from loader import *


def create_report(dataframe: pd.DataFrame, top_size: int):
    df_analyse = dataframe.copy()
    df_analyse['sum values'] = dataframe.apply(sum, axis=1)
    df_analyse['zero & low count'] = dataframe.apply(lambda x: (x <= 0).sum(), axis=1)
    df_analyse['low zero count'] = dataframe.apply(lambda x: (x < 0).sum(), axis=1)
    df_analyse = df_analyse.sort_values(['sum values'], ascending = False)

    result_dict = {#'all df': dataframe.stack(),
                   'sum values': df_analyse['sum values'],
                   'zero & low count': df_analyse['zero & low count'],
                   'low zero count:': df_analyse['low zero count'],
                   'low zero is 0 sum': df_analyse[df_analyse['low zero count'] == 0]['sum values']}

    print(len(result_dict['low zero is 0 sum']))

    for i in range(len(result_dict)):
        key = list(result_dict.keys())[i]
        result_dict[key] = get_round_stats(result_dict[key], 2, top_size)

    result_df = pd.DataFrame(result_dict)

    return result_df.T


def get_round_stats(series: pd.Series, digits: int, top_size: int) -> pd.Series:
    series = series[:top_size]
    result = pd.Series({'quantile 0.25': series.quantile(0.25),
                        'mean': series.mean(),
                        'quantile 0.75': series.quantile(0.75),
                        'moda': np.mean(series.mode()),
                        'std': series.std()})

    for i in range(len(result.values)):
        result.iloc[i] = round(result.iloc[i], digits)

    return result
