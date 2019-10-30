import pandas as pd
import numpy as np

class DataMinification:
    def __init__(self,df):
        self.df=df

    def reduce_mem_usage(self, verbose=True):
        numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
        start_mem = self.df.memory_usage().sum() / 1024 ** 2
        for col in self.df.columns:
            col_type = self.df[col].dtypes
            if col_type in numerics:
                c_min = self.df[col].min()
                c_max = self.df[col].max()
                if str(col_type)[:3] == 'int':
                    if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                        self.df[col] = self.df[col].astype(np.int8)
                    elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                        self.df[col] = self.df[col].astype(np.int16)
                    elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                        self.df[col] = self.df[col].astype(np.int32)
                    elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                        self.df[col] = self.df[col].astype(np.int64)
                else:
                    if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                        self.df[col] = self.df[col].astype(np.float16)
                    elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                        self.df[col] = self.df[col].astype(np.float32)
                    else:
                        self.df[col] = self.df[col].astype(np.float64)
        end_mem = self.df.memory_usage().sum() / 1024 ** 2
        if verbose: print('Mem. usage decreased to {:5.2f} Mb ({:.1f}% reduction)'.format(end_mem, 100 * (
                    start_mem - end_mem) / start_mem))
        return self.df


def main(df):
    d = DataMinification(df)
    d.reduce_mem_usage()

if __name__ == '__main__':
    main()