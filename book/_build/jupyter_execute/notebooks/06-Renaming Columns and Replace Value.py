## Renaming Columns

import pandas as pd 

# read a dataset of UFO reports into a DataFrame
ufo = pd.read_csv('http://bit.ly/uforeports')

# examine the first 5 rows 
ufo.head()

# examine the column names 
ufo.columns

# rename two of the columns by useing `rename` method
ufo.rename(columns={'Colors Reported': 'Colors_Reported', 'Shape Reported': 'Shape_Reported'}, inplace=True)

ufo.head()

# replace all of the column names by overwritting the 'colums' attribute 
ufo_cols = ['city', 'colors reported', 'shape reported', 'state', 'time']
ufo.columns = ufo_cols
# see modified columns 
ufo.columns

# replace the column names during the file reading process by using the 'names' parameter
ufo = pd.read_csv('http://bit.ly/uforeports', names=ufo_cols)

# examine the 5 rows 
ufo.head()

# replace all spaces with underscores in the column names by using the 'str.replace' method
ufo.columns = ufo.columns.str.replace(' ', '_')
ufo.columns

# let's look at DataFrame
ufo.head()

# Replace

# read another dataset 
fm = pd.read_csv("../data/framingham.csv")

# examine  first few rows 
fm.head() 

# first rename `male` to `sex` 
fm.rename(columns={"male": "sex"}, inplace=True)

# Now take a look at dataset 
fm.head() 

## Replace Value for Better Understanding of Dataset
__sex__
* 1 = Male 
* 0 = Female 

__diabetes__
* 1 = Yes 
* 0 = No 

# replace sex column value
fm['sex'].replace({1: "male", 0: "female"}, inplace=True)

# replace diabetes column value 
fm['diabetes'].replace({1: "yes", 0: "no"}, inplace=True)

# Examine dataset
fm.head() 