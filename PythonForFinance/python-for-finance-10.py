
# target creating function for machine learning label

import numpy as np
import pandas as pd 
import pickle

def process_data_for_labels(ticker):
    hm_days = 7
    df = pd.read_csv('sp500_joined_closes.csv', index_col=0)
    tickers = df.columns.values.tolist()
    df.fillna(0, inplace=True)

    for i in range(1, hm_days+1):
        # np.log(df/df.shift(1)).dropna()
        df['{}_{}d'.format(ticker,i)] = (df[ticker].shift(-i) - df[ticker])/df[ticker]

    df.fillna(0, inplace=True)

    print(df) 
    
    return tickers, df


def buy_sell_hold(*args):
    cols = [c for c in args]
    requirement = 0.02
    for col in cols:
        if col > requirement:
            return 1
        if col < -requirement:
            return -1
    return 0


if __name__ == "__main__":
    buy_sell_hold('a', 'b', 1)