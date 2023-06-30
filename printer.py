import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


def print_features_important(setting_dataframe: pd.DataFrame, result_dataframe: pd.DataFrame, setting_columns: [str]):
    model = LinearRegression()
    model.fit(setting_dataframe, result_dataframe)
    coef = model.coef_[0]
    features = list(zip(np.round(abs(coef) / sum(abs(coef)) * 100, 2), setting_columns))
    features.sort(reverse=True)
    print('Top features important:')
    for k, v in features:
        print('\t', k, v, sep='\t')
    print()