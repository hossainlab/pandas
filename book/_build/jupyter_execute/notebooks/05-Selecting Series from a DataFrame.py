# Selecting Series from DataFrame 

## Single Series

# conventional way to import pandas
import pandas as pd

# read a dataset of UFO reports into DataFrame 
ufo = pd.read_table('http://bit.ly/uforeports', sep=',')

# read a csv is equivalent to read_table, except it assumes a comma separator 
ufo = pd.read_csv('http://bit.ly/uforeports')

# examine first 5 rows 
ufo.head()

# select 'City' Series using bracket notation
ufo['City']

type(ufo['City'])

# select 'City' Series using dot(.) notation
ufo.City

__Note__
- Bracket notation will always work, whereas dot notation has **limitations**
- Dot notation doesn't work if there are **spaces** in the Series name
- Dot notation doesn't work if the Series has the same name as a **DataFrame method or attribute** (like 'head' or 'shape')
- Dot notation can't be used to define the name of a **new Series** (see below)

# create a new 'Location' Series (must use bracket notation to define the Series name)
ufo['Location'] = ufo.City + ', ' + ufo.State
ufo.head()

## Multiple Series

# select multiple series from dataframe 
ufo[['City', 'State', 'Time']]