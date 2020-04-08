'''
 Data set  is obtained From kaggle

'''

# data Analysis library
import pandas as pd

import numpy as np

# graphical visualization libraries
import seaborn as sns
import plotly.express as px
import matplotlib
matplotlib.use('Agg')


df = pd.read_csv('./creditcard.csv')

fraud_data = df.loc[df['Class'] == 1 ]

normal_data = df.loc[ df['Class'] == 0 ]

def Time_vs_Amount__Class_as_heu():
    # relation graph
    fig = sns.relplot(x='Amount', y = 'Time', hue = 'Class', data = df, color = 'r')
    fig.savefig('./v1.eps', format = 'eps')


def class_vs_Amount():
    # relation graph
    fig = sns.relplot(x='Amount', y = 'Class', data = df, color = 'r')
    fig.savefig('./v2.eps', format = 'eps')


def time_vs_amount__class_as_heu():
    # category graph
    fig = sns.catplot(x='Amount', y = 'Time', hue = 'Class', data = df, color = 'r')
    fig.savefig('./v3.eps', format = 'eps')


#print(fraud_data.tail())
fig = px.scatter(data_frame = fraud_data, x = 'Time', y = 'Amount', render_mode=  'markers+lines', title = 'Fraud Data Visulaization')
#fig = px.scatter(data_frame = normal_data, x = 'Time', y = 'Amount')
fig.show()

