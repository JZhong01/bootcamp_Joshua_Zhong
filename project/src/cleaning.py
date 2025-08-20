from sklearn.preprocessing import MinMaxScaler, StandardScaler
from pandas.api.types import is_numeric_dtype

def fill_missing_median(df):
    return df.fillna(df.median(numeric_only=True))


def drop_missing(df, threshold):
    return df.dropna(thresh=int(df.shape[1] - threshold))


# df_normal = cleaning.normalize_data(df, ['col1','col2'])
# print(df_normal)



def normalize_data(df, columns):
    standardizer = StandardScaler()
    df_normal = df.copy()
    for col in columns:
        if is_numeric_dtype(df_normal[col]):
            reshaped_col = df_normal[col].values.reshape(-1,1)
            df_normal[col] = standardizer.fit_transform(reshaped_col)
        else:
            print('error')
    return df_normal