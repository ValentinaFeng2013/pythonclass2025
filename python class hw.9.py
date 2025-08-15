import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import LabelEncoder
penguins = sns.load_dataset("penguins")
penguins = penguins.dropna().reset_index(drop=True)
from sklearn.preprocessing import LabelEncoder
categorical_cols = ['island', 'sex', 'species']
for col in categorical_cols:
    le = LabelEncoder()
    penguins[col] = le.fit_transform(penguins[col])
penguins_X = penguins.drop('species', axis=1)
penguins_y = penguins['species']
X_train, X_test, y_train, y_test = train_test_split(penguins_X, penguins_y, test_size=0.2, random_state=42)
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
rf_acc = accuracy_score(y_test, y_pred_rf)
print(f"Random Forest Accuracy: {rf_acc}")
dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train)
y_pred_dt = dt.predict(X_test)
dt_acc = accuracy_score(y_test, y_pred_dt)
print(f"Decision Tree Accuracy: {dt_acc}")