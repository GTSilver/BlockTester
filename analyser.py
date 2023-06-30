import pandas as pd
from loader import *


def create_report(cfg: Config, dataframe: pd.DataFrame):
    dataframe = dataframe.copy()
    dataframe.columns = [x[:5] for x in get_filelist(cfg)]
    print(dataframe)
    # dgr = awd.copy()
    # dgr['sum'] = awd.apply(sum, axis = 1)
    # L = lambda row: sum(1 for x in row if x > 0)
    # dgr['count'] = awd.apply(L, axis = 1)
    # dgr = dgr.sort_values(['count', 'sum'], ascending = False)
    # print('\n', dgr.head(20))
    #
    # dgr.to_csv('awd.csv', sep = '\t')
