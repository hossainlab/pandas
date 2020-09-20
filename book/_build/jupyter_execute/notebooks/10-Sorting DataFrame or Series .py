# Sorting DataFrame or Series 

# import pandas 
import pandas as pd 

**Note**: None of the sorting methods below affect the underlying data. (In other words, the sorting is temporary).


# read a dataset of top-rated IMDb movies into a DataFrame
movies = pd.read_csv('http://bit.ly/imdbratings')
movies.head()

# sort the 'title' Series in ascending order (returns a Series)
movies.title.sort_values().head()

# sort in descending order instead
movies.title.sort_values(ascending=False).head()

# sort the entire DataFrame by the 'title' Series (returns a DataFrame)
movies.sort_values('title', ascending=False).head()

# sort the entire DataFrame by the 'duration' Series (returns a DataFrame)
movies.sort_values('duration', ascending=False).head()

# sort by two columns: first sort_by duration and then content_rating
movies.sort_values(['duration', 'content_rating'], ascending=False).head()

# None of the sorting methods below affect the underlying data. (In other words, the sorting is temporary). 
movies.head() 