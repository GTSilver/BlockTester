from loader import *
from selector import *
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression

cfg = Config('config.json')
dataframe_list = load_dataframe_list(cfg)
setting_columns_list = get_setting_columns(cfg, data)
result_column_list = select_result_column("Result", cfg, data)





# data_for_pca = data[0].copy()
# for i in range(1, len(data) - 1):
#     data_for_pca = pd.concat([data_for_pca, data[i]])
# data_for_pca = data_for_pca.reset_index(drop=True)
#
# X = data_for_pca.copy()
# del X["Result"]
# del X["Custom"]
#
# pca = PCA()
#
# y = data_for_pca["Result"]
#
# model = LinearRegression()
# model.fit(X, y)
#
# importance = model.coef_
#
# pca.fit(X)
#
# print(X.columns)
