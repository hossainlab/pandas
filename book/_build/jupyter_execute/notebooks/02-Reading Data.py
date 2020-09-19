# Reading Data into Pandas

# conventional way to import pandas
import pandas as pd 

## Read CSV

# read data from csv file 
corona = pd.read_csv("../data/covid-19_cleaned_data.csv")

# Examine first few rows 
corona.head() 

## Read Excel Sheet

# read data from excel file 
movies = pd.read_excel("../data/movies.xls")

# examine first few rows 
movies.head() 

## Read Multiple Excel Sheets 

import xlrd 
# Import xlsx file and store each sheet in to a df list
xl_file = pd.ExcelFile("../data/data.xls",)
# Dictionary comprehension
dfs = {sheet_name: xl_file.parse(sheet_name) for sheet_name in xl_file.sheet_names}

# Data from each sheet can be accessed via key
keylist = list(dfs.keys())

# Examine the sheet name 
keylist[1:10]

# Accessing first sheet
dfs[keylist[0]]

## From URL

# read a dataset of Chipotle orders directly from a URL and store the results in a DataFrame 
orders = pd.read_table('http://bit.ly/chiporders')

# examine the first 5 rows 
orders.head()

# examine the last 5 rows 
orders.tail()

# examine the first `n` number of rows
orders.head(10)

# examine the last `n` number of rows
orders.tail(10)

## Modify Dataset

# read a dataset of movie reviewers (modifying the default parameter values for read_table)
users = pd.read_table('http://bit.ly//movieusers')

# examine the first 5 rows 
users.head()

# DataFrame looks ugly. let's modify the default parameter for read_table 
user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_table('http://bit.ly//movieusers', sep='|' , header=None, names=user_cols)

# now take a look at modified dataset
users.head()

## Read Biological Data(.txt)

# read text/csv data into pandas 
chrom = pd.read_csv("../data/Encode_HMM_data.txt", delimiter="\t", header=None)

# Examine first few rows 
chrom.head()

# it's not much better to see. so we have to modify this dataset
cols_name = ['chrom', 'start', 'stop', 'type']
chrom = pd.read_csv("../data/Encode_HMM_data.txt", delimiter="\t", header=None, names=cols_name)

# now examine first few rows 
chrom.head()

## Read Biological Data(.tsv)

pokemon = pd.read_csv("../data/pokemon.tsv", sep="\t")

pokemon.head() 

## Read HTML Data

# Read HTML data from web 
url = 'https://www.fdic.gov/bank/individual/failed/banklist.html'
data = pd.io.html.read_html(url)

# Check type 
type(data)

# access data 
data[0]