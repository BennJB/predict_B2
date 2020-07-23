import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from xgboost.sklearn import XGBClassifier
 
def modeling_RF():
    estimator = None
    try:
        df1 = pd.read_csv('last_total.csv', encoding = 'cp949')
        
        df_dummy = pd.get_dummies(df1)
        train, test = train_test_split(df_dummy, test_size = 0.2, random_state=1234)
        train_x = train.drop('target_bool', axis=1)
        train_y = train['target_bool']
        test_x = test.drop('target_bool', axis=1)
        test_y = test['target_bool']

        xgb = XGBClassifier(random_state=1234, learning_rate= 0.6000000000000001, max_depth= 9, n_estimators= 200)
        xgb.fit(train_x,train_y)
        abc = xgb.score(train_x,train_y)

    except Exception as e:
        print(e)
    finally:
        pass
    
    return abc