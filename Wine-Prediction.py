import numpy as np
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('winequality-red.csv')
data
data.info()


# Graph of 'fixed acidity', 'volatile acidity', 'citric acid','residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol' with quality
sb.set_style("whitegrid")
fig = plt.figure(figsize=[10, 10])

colms = ['fixed acidity', 'volatile acidity', 'citric acid',
         'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']
i = 1
for col in colms:
    plt.subplot(4, 3, i)
    plt.subplots_adjust(wspace=0.5)
    sb.barplot(data=data, x='quality', y=col)
    i += 1
plt.show()

# Graph telling out of 0 to 1599, how many enteries are of high, medium and low quality
data_aux = data.copy()
data_aux['quality'].replace([3, 4], ['low', 'low'], inplace=True)
data_aux['quality'].replace([5, 6], ['Med', 'Med'], inplace=True)
data_aux['quality'].replace([7, 8], ['High', 'High'], inplace=True)
sb.countplot(data_aux['quality'])
plt.title("High,Medium and Low Quality Prediction")
plt.show()
