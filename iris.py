#Roisin Anglim 29-04-18 
#Iris dataset GMIT project 

#Import dependencies:
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as pt


#This gives headings to the datas columns
heading=["sepal-length","sepal-width","petal-length","petal-width","Species"]
#Using panda this reads in the data as csv and assigns headings
Data = pd.read_csv('data/iris.csv',names=heading) 

# Check for missing data and remove rows if missing data
EmptyIdx = pd.isnull(Data)
if np.sum(np.sum(EmptyIdx)) > 0 :
  Data =  Data.dropna()

# Seperate data into subcatagories

#Setosa = Data.loc[Data['class'] == 'Iris-setosa']
#Versicolor = Data.loc[Data['class'] == 'Iris-versicolor']
#Virginica = Data.loc[Data['class'] == 'Iris-virginica']
#Classnames = ['Iris-setosa','Iris-versicolor','Iris-virginica']

# Generate discriptive statistics for each class

MeanValues = Data.groupby(['Species']).mean()
StdValues = Data.groupby(['Species']).std()



# Explore data using box plots overlayed with actual datapoints
ax = sns.swarmplot(x="Species", y="petal-length", data=Data)
ax = sns.boxplot(x="Species", y="petal-length", data=Data, whis=np.inf)

pt.show()
ax = sns.swarmplot(x="Species", y="petal-width", data=Data)
ax = sns.boxplot(x="Species", y="petal-width", data=Data, whis=np.inf)
pt.show()
ax = sns.swarmplot(x="Species", y="sepal-width", data=Data)
ax = sns.boxplot(x="Species", y="sepal-width", data=Data, whis=np.inf)
pt.show()
ax = sns.swarmplot(x="Species", y="sepal-length", data=Data)
ax = sns.boxplot(x="Species", y="sepal-length", data=Data, whis=np.inf)

pt.show()
