# Pandas for Data Analysis

## About Pandas

## What is Pandas?
The Pandas library is built on NumPy and provides easy-to-use data structures and data analysis tools for the Python programming language.

## Pandas Series
A **one-dimensional** labeled array a capable of holding any data type

## Pandas DataFrame
A **two-dimensional** labeled data structure with columns of potentially different types

## Advantages of Pandas
- Data representation
- Less writing and more work done
- An extensive set of features
- Efficiently handles large data
- Makes data flexible and customizable
- Made for Python



## Datasets
Filename | Description | Raw File | Original Source | Other
--- | --- | --- | --- | ---
[chipotle.tsv](data/chipotle.tsv) | Online orders from the Chipotle restaurant chain | [bit.ly/chiporders](http://bit.ly/chiporders) | [The Upshot](https://github.com/TheUpshot/chipotle) | [Upshot article](http://www.nytimes.com/interactive/2015/02/17/upshot/what-do-people-actually-order-at-chipotle.html)
[drinks.csv](data/drinks.csv) | Alcohol consumption by country | [bit.ly/drinksbycountry](http://bit.ly/drinksbycountry) | [FiveThirtyEight](https://github.com/fivethirtyeight/data/tree/master/alcohol-consumption) | [FiveThirtyEight article](http://fivethirtyeight.com/datalab/dear-mona-followup-where-do-people-drink-the-most-beer-wine-and-spirits/)
[imdb_1000.csv](data/imdb_1000.csv) | Top rated movies from IMDb | [bit.ly/imdbratings](http://bit.ly/imdbratings) | [IMDb](http://www.imdb.com/search/title?groups=top_1000&sort=user_rating&view=simple) | [Web scraping script](https://github.com/justmarkham/DAT5/blob/master/code/08_web_scraping.py)
[stocks.csv](data/stocks.csv) | Small dataset of stock prices | [bit.ly/smallstocks](http://bit.ly/smallstocks) | [DataCamp](https://www.datacamp.com/courses/manipulating-dataframes-with-pandas?tap_a=5644-dce66f&tap_s=280411-a25fc8) |
[titanic_test.csv](data/titanic_test.csv) | Testing set from Kaggle's Titanic competition | [bit.ly/kaggletest](http://bit.ly/kaggletest) | [Kaggle](https://www.kaggle.com/c/titanic) | [Data dictionary](https://www.kaggle.com/c/titanic/data)
[titanic_train.csv](data/titanic_train.csv) | Training set from Kaggle's Titanic competition | [bit.ly/kaggletrain](http://bit.ly/kaggletrain) | [Kaggle](https://www.kaggle.com/c/titanic) | [Data dictionary](https://www.kaggle.com/c/titanic/data)
[u.user](data/u.user) | Demographic information about MovieLens users | [bit.ly/movieusers](http://bit.ly/movieusers) | [GroupLens](http://grouplens.org/datasets/movielens/100k/) | [Data dictionary](http://files.grouplens.org/datasets/movielens/ml-100k-README.txt)
[ufo.csv](data/ufo.csv) | Reports of UFO sightings from 1930-2000 | [bit.ly/uforeports](http://bit.ly/uforeports) | [National UFO Reporting Center](http://www.nuforc.org/webreports.html) | [Web scraping script](https://github.com/josiahdavis/josiahdavis.github.io/blob/master/supporting%20material/get_ufo_data.py)


## How to create your own Jupyter Book

1. `conda env create -f environment.yml`
2. `conda activate dsn-template`

## Building a Jupyter Book

Run the following command in your terminal: `jb build book/`.
If you would like to work with a clean build, you can empty the build folder by running `jb clean book/`. If the jupyter execution is cached, this command will not delete the cached folder. To remove the build folder, you can run `jb clean --all book/`.

## Publishing this Jupyter Book

Run `ghp-import -n -p -f book/_build/html`
