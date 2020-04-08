from sklearn import linear_model
from sklearn.model_selection import train_test_split
import numpy as np

# import for DataFrame
from Visualization import fraud_data, normal_data, df

# import to Handle the Warnings
import warnings
warnings.filterwarnings('ignore')

x = df.iloc[:, :-1]
y = df['Class']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.35)

# classifier with logistic Regression
clf = linear_model.LogisticRegression(C = 1e5)
clf.fit(x_train, y_train)

y_pred = np.array(clf.predict(x_test))

y = np.array(y_test)

# imports
from sklearn.metrics import  confusion_matrix, classification_report, accuracy_score

print(confusion_matrix(y_test, y_pred))

print("Accuracy : ",accuracy_score(y_test, y_pred))
print("\n\n")
print(classification_report(y_test, y_pred))

