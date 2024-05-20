import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.model_selection import GridSearchCV
from utils import *
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report

df = pd.read_csv('cardio_train.csv', sep=';')

df.drop_duplicates(inplace=True)

df.dropna(inplace=True)

df['bmi'] = df['weight'] / (df['height']/100)**2
df['age'] = df['age'] / 365

feature_cols = ['age', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'bmi']
X = df[feature_cols] # Caractéristiques
y = df.cardio # Variable cible

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

logreg = LogisticRegression()
logreg.fit(X_train_scaled, y_train)

y_pred = logreg.predict(X_test_scaled)
print(y_pred)

logreg2 = LogisticRegression(max_iter=10000)
param_grid = {
    'C': [0.001, 0.01, 0.1, 1, 10, 100],
    'penalty': ['l1', 'l2'],
    'solver': ['liblinear', 'saga']
}

grid_search = GridSearchCV(logreg2, param_grid, cv=5, scoring='accuracy', verbose=1)

grid_search.fit(X_train_scaled, y_train)

print("Meilleurs paramètres ", grid_search.best_params_)

y_pred = grid_search.predict(X_test_scaled)


# raaport de classification
report = classification_report(y_test, y_pred)
print(report)

cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
print("Matrice de confusion: ", cnf_matrix)
