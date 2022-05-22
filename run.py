# %%

from multiprocessing.pool import Pool
from multiprocessing import freeze_support

import pandas as pd
import numpy as np
import warnings
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore')
np.random.seed(2022)

DEBUG = True


from autogluon.text import TextPredictor

if __name__ == '__main__':
    # %% Load data
    sts_train_data = pd.read_csv('./data/train.csv', index_col='id')
    sts_test_data = pd.read_csv('./data/test.csv', index_col='id')
    # %% Preprocessing
    sts_train_data.drop(columns=['context'], inplace=True)
    sts_test_data.drop(columns=['context'], inplace=True)
    sts_train_data.rename(columns={'anchor': 'sentence1', 'target':'sentence2'}, inplace=True)
    sts_test_data.rename(columns={'anchor': 'sentence1', 'target':'sentence2'}, inplace=True)
    # %% Select a small training data for debugging purpose
    print(sts_train_data.head())
    print(sts_test_data.head())

    total_N = sts_train_data.shape[0]
    print('Total number of training data: {}'.format(total_N))
    print('Min score=', min(sts_train_data['score']), ', Max score=',
            max(sts_train_data['score']))   
    # %%train model        
    # predictor_sts = TextPredictor(label='score', path='./ag_sts')
    predictor_sts = TextPredictor.load('./ag_sts/')

    if DEBUG:
        print('Training model...')
        ste_train_data_small = sts_train_data.sample(2000)
        print('Training data size: {}'.format(ste_train_data_small.shape[0]))
        predictor_sts.fit(ste_train_data_small, time_limit=60 * 60)
    else:
        predictor_sts.fit(sts_train_data, time_limit=60 * 60)
    # %% test model
    test_score = predictor_sts.evaluate(sts_test_data,
                                        metrics=['rmse', 'pearsonr', 'spearmanr'])
    print('RMSE = {:.2f}'.format(test_score['rmse']))
    print('PEARSONR = {:.4f}'.format(test_score['pearsonr']))
    print('SPEARMANR = {:.4f}'.format(test_score['spearmanr']))