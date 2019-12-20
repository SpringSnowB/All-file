import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy
import sklearn
import missingno
data = pd.read_csv("/home/tarena/data/Border_Crossing_Entry_Data.csv",encoding='utf-8')
print(data.head())
print(data.info())
print(data.describe())