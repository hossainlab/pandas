# Exploring Dataset

# import pandas
import pandas as pd 

# read a dataset 
df = pd.read_csv("../data/framingham.csv")

## Head 

# head: by default shows first 5 rows 
df.head() 

# head(n); n = 1, 2, 3, 4, ....
df.head(8)

## Tail


# tail: by default shows last 5 rows 
df.tail() 

# tail(n); n=1, 2, 3, 4...
df.tail(8)

## Columns Names 

# Columns 
df.columns

## Observations and Variables(Rows and Columns)

# shape(rows x columns)
df.shape

## Data Types 

# check datatypes 
df.dtypes

## Basic Information about Whole Dataset

# info: it gives an overview of datasets 
df.info() 

## Numerical Summary of a Dataset

# describe: it gives summary statistics or five number summary 
df.describe() 

# for specific column 
df['age'].describe() 

# for multiple columns 
df[['age', 'BMI']].describe() 

## Exploring Series 

# read another dataset 
titanic = pd.read_csv('http://bit.ly/kaggletrain')

# examine first few rows 
titanic.head() 

## Value Counts 

# value_counts()
titanic['Sex'].value_counts() 

# value_counts() in percent
titanic['Sex'].value_counts(normalize=True) 

# returns a series 
type(titanic['Sex'].value_counts(normalize=True))

## Unique() 

# unique() 
titanic['Fare'].unique() 

# return a numpy.ndarray
type(titanic['Fare'].unique())

## Cross Tabulation

# crosstab 
pd.crosstab(titanic['Sex'], titanic['Survived'])

## Describe 

# describe a categorical column 
titanic['Age'].describe() 

## Basic Statistics

# mean()
titanic.Age.mean() 

# max()
titanic.Age.max() 

# min() 
titanic.Age.min() 

# median() 
titanic.Age.median() 

## Visualization

%matplotlib inline 

# barplot
titanic.Sex.value_counts().plot(kind="bar") 

# histogram
titanic.Age.plot(kind="hist")