# Removing Columns

# import pandas 
import pandas as pd 

# read a dataset of UFO reports into a DataFrame
ufo = pd.read_csv('http://bit.ly/uforeports')
ufo.head()

## Remove Single Columns 

# remove single columns(axis=1 refers to columns, axis=0 refers to row)
ufo.drop('City', axis=1, inplace=True)
ufo.head()

## Remove Multiple Columns

# remove multiple columns 
ufo.drop(['Colors Reported', 'Time'], axis=1, inplace=True)
ufo.head()

# read a dataset of top-rated IMDb movies into a DataFrame
movies = pd.read_csv('http://bit.ly/imdbratings')
movies.head()

# remove single column(axis=1 refers to colums)
movies.drop('genre', axis=1, inplace=True)
movies.head()

# remove multiple columns from DataFrame 
movies.drop(['actors_list', 'content_rating', 'duration'], axis=1, inplace=True)
movies.head()