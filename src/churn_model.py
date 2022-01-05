import pandas as pd

from sklearn.ensemble import RandomForestClassifier

import pickle

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
df_churn = pd.read_csv('telco_churn.csv')

df_churn = df_churn[['gender', 'PaymentMethod', 'MonthlyCharges', 'tenure', 'Churn']].copy()

df = df_churn.copy()

df.fillna(0, inplace=True)

print(df.head())
