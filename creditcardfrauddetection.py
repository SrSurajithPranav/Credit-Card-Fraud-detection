# -*- coding: utf-8 -*-
"""creditcardfrauddetection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dYiQgfYHk53UMyt0WROINGpnGmuLu0dR

*Import necessary libraries*
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""*Mount Google Drive and load the data*"""

# Mount Google Drive if your dataset is stored there
from google.colab import drive
drive.mount('/content/drive')

# Load the credit card fraud dataset from Google Drive
data = pd.read_csv('/content/drive/MyDrive/dataset_folder/creditcard.csv')

"""*Displaying dataset*"""

data.head()

"""*Check dataset information*"""

data.info()

"""*Check for missing values*


"""

missing_values = data.isnull().sum()

"""*Exploring distribution of legitmate and fradulent transcation*

"""

class_distribution = data['Class'].value_counts()

"""*Separate the data for analysis*"""

legitimate_transactions = data[data.Class == 0]
fraudulent_transactions = data[data.Class == 1]

"""
*Display statistical measures for legitimate transactions*
"""

legit_stats = legitimate_transactions.Amount.describe()

"""
*Display statistical measures for fraudulent transactions*"""

fraud_stats = fraudulent_transactions.Amount.describe()

"""
*Create an under-sampled dataset with balanced classes*
"""

fraud_sample = fraudulent_transactions.sample(n=31)
undersampled_data = pd.concat([fraud_sample, legitimate_transactions], axis=0)

"""

*Display the class distribution in the undersampled dataset*"""

undersampled_class_distribution = undersampled_data['Class'].value_counts()

"""
*Split the data into features and target*"""

X = undersampled_data.drop(columns='Class', axis=1)
Y = undersampled_data['Class']

"""*Split the data into training and testing sets*

"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

"""*Initialize and train a logistic regression model with increased max_iter*

"""

print('Training accuracy: ', train_accuracy)
print('Testing accuracy: ', test_accuracy)

