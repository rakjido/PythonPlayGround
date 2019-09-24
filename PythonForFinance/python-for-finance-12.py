
# machine learning

from collections import Counter
import numpy as np
import pandas as pd 
import pickle

from sklearn import svm, model_selection, neighbors
from sklearn.ensemble import VotingClassifier, RandomForestClassifier


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
    requirement = 0.028
    for col in cols:
        if col > requirement:
            return 1
        if col < - requirement:
            return -1
    return 0

def extract_featuresets(ticker):
    tickers, df = process_data_for_labels(ticker)

    df['{}_target'.format(ticker)] = list (map( buy_sell_hold,
                                                df['{}_1d'.format(ticker)],
                                                df['{}_2d'.format(ticker)],
                                                df['{}_3d'.format(ticker)],
                                                df['{}_4d'.format(ticker)],
                                                df['{}_5d'.format(ticker)],
                                                df['{}_6d'.format(ticker)],
                                                df['{}_7d'.format(ticker)],
                                                ))

    vals = df['{}_target'.format(ticker)].values.tolist()
    str_vals = [str(i) for i in vals]
    print('Data spread: ', Counter(str_vals))

    df.fillna(0, inplace=True)
    df = df.replace([np.inf, -np.inf], np.nan)
    df.dropna(inplace=True)

    df_vals = df[[ticker for ticker in tickers]].pct_change()
    df_vals = df_vals.replace([np.inf, -np.inf], 0)
    df_vals.fillna(0, inplace=True)

    x = df_vals.values
    y = df['{}_target'.format(ticker)].values

    return x, y, df

def do_ml(ticker):
    x, y, df = extract_featuresets(ticker)

    x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.25)


    # clf = neighbors.KNeighborsClassifier()
    clf = VotingClassifier([('lsvc', svm.LinearSVC()),
                            ('knn', neighbors.KNeighborsClassifier()),
                            ('rfor', RandomForestClassifier())])

    clf.fit(x_train, y_train)
    confidence = clf.score(x_test, y_test)
    print('Accuracy', confidence)

    predictions = clf.predict(x_test)
    print('Prediction spread: ', Counter(predictions))

if __name__ == "__main__":
    do_ml('BAC')