# Filtering Rows 

# import pandas 
import pandas as pd 

# read movie data 
movies = pd.read_csv("http://bit.ly/imdbratings")

# examine first few rows 
movies.head() 

## Filtering Movies with `for` Loop

booleans = [] 
for length in movies.duration: 
    if length >= 200: 
        booleans.append(True)
    else: 
        booleans.append(False)

# Check length of booleans 
len(booleans)

# Inspect booleans elements 
booleans[0:5]

# create a pandas series 
is_long = pd.Series(booleans)

# Inspect few values 
is_long.head() 

# show dataframe all columns in duration 200 minutes 
movies[is_long]

## Filtering by Condition

# filtering by conditions 
is_long = movies.duration >= 200
is_long.head() 

# show the rows duration >200
movies[is_long]

## Filtering in DataFrame 

# filtering by columns 
movies[movies.duration >= 200]

# select only genre
movies[movies.duration >= 200].genre

# same as above 
movies[movies.duration >= 200]['genre']

# select columns by label 
movies.loc[movies.duration >= 200, 'genre']

## Multiple Filtering Criteria

* True and True == True 
* True and False == False 
* True or True == True 
* True or False == True 
* False or False == False 


True and True

True and False

# multiple criteria 
movies[(movies.duration >= 200) & (movies.genre == 'Drama')]

# multiple criteria 
movies[(movies.duration >= 200) | (movies.genre == 'Drama')]

# multiple or conditions 
movies[(movies.genre == "Crime") | (movies.genre == 'Drama') | (movies.genre == "Action")]

# multiple or using isin() method 
movies.genre.isin(["Drama", "Action", "Crime"])

# pass the series in DataFrame 
movies[movies.genre.isin(["Drama", "Action", "Crime"])]