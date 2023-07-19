import numpy as np

from loader import *


def create_report(dataframe: pd.DataFrame, top_size: int):
    df_analyse = dataframe.copy()
    df_analyse['sum values'] = dataframe.apply(sum, axis = 1)
    df_analyse['zero count'] = dataframe.apply(lambda x: (x == 0).sum(), axis = 1)
    df_analyse['up zero count'] = dataframe.apply(lambda x: (x > 0).sum(), axis = 1)
    df_analyse['low zero count'] = dataframe.apply(lambda x: (x < 0).sum(), axis = 1)
    df_analyse = df_analyse.sort_values(['sum values'], ascending = False)

    df_low_zero_null = df_analyse[df_analyse['low zero count'] == 0]

    result_dict = {'sum values all': df_analyse['sum values'],
                   'sum values': df_low_zero_null['sum values'],
                   'zero count': df_low_zero_null['zero count'],
                   'up zero count': df_low_zero_null['up zero count']}

    print(df_low_zero_null.shape[0])

    for i in range(len(result_dict)):
        key = list(result_dict.keys())[i]
        result_dict[key] = get_round_stats(result_dict[key], 2, top_size)

    result_df = pd.DataFrame(result_dict)

    return result_df.T


def get_round_stats(series: pd.Series, digits: int, top_size: int) -> pd.Series:
    series = series[:top_size]
    result = pd.Series({'quant. 0.25': series.quantile(0.25),
                        'mean': series.mean(),
                        'quant. 0.75': series.quantile(0.75),
                        'moda': np.mean(series.mode()),
                        'std': series.std()})

    for i in range(len(result.values)):
        result.iloc[i] = round(result.iloc[i], digits)

    return result
