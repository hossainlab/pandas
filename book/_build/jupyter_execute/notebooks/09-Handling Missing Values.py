# Handling Missing Values 

# import pandas 
import pandas as pd 

# read ufo data 
ufo = pd.read_csv("http://bit.ly/uforeports")

# last 5 rows 
ufo.tail() 

# check missing values 
ufo.isnull() 

__Note__
1. True: Missing 
2. False: Not Missing

# using notnull() 
ufo.notnull() 

__Note__
1. axis = 0: Rows 
2. axis = 1: Columns 

# sum of missing values: by default axis = 0
ufo.isnull().sum() 

# Let's create a series 
pd.Series([True, False, True]).sum() 

# filtering using isnull() 
ufo[ufo.City.isnull()]

# Check specific column
ufo.City.isnull().sum() 

## Drop Missing Values 

# shape 
ufo.shape 

# drop missing: drop row contains missing values 
# it is inplace = False 
ufo.dropna(how='any').shape

# how=all 
ufo.dropna(how='all').shape 

# subset: any 
ufo.dropna(subset=['City', 'Shape Reported'], how='any').shape

# subset: all 
ufo.dropna(subset=['City', 'Shape Reported'], how='all').shape

## Filling Missing Values 

# value counts: by default drop = True 
ufo["Shape Reported"].value_counts() 

# value counts: false 
ufo["Shape Reported"].value_counts(dropna=False) 

# fillna() 
ufo["Shape Reported"].fillna(value="VARIOUS", inplace=True)

# now take a look 
ufo["Shape Reported"].value_counts() 