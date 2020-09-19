# Methods and Attributes
__Remember__
* Methods ends with **parentheses**, while **attributes** don't
* df.shape: Attribute
* df.info(): Method

# import pandas 
import pandas as pd 

# read a dataset of top-rated IMDb movies into a DataFrame
movies = pd.read_csv('http://bit.ly/imdbratings')

# example method: show the first 5 rows 
movies.head()

# example method: calculate summary statistics
movies.describe()

# example attribute: number of rows and columns 
movies.shape

# example attribute: data type of each column
movies.dtypes

# use an optional parameter to the describe method to summarize only 'object' column
movies.describe(include='object')