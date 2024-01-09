# Linear Regression Algorithm Sample

# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df=pd.read_csv("diabetes.csv")


print(df.shape)

df.info()

print(df.head())

print(df.isnull().sum())

df['BloodPressure']=df['BloodPressure'].replace(0, df['BloodPressure'].mean())
df['Pregnancies']=df['Pregnancies'].replace(0, df['Pregnancies'].mean())
df['Glucose']=df['Glucose'].replace(0, df['Glucose'].mean())
df['SkinThickness']=df['SkinThickness'].replace(0, df['SkinThickness'].mean())
df['Insulin']=df['Insulin'].replace(0, df['Insulin'].mean())
df['BMI']=df['BMI'].replace(0, df['BMI'].mean())

print(df.isnull().sum())

print(df.describe())

#Exploratory Data Analysis (EDA)

