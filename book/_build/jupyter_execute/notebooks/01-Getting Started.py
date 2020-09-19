# Getting Started 

# Conventional  way to import pandas 
import pandas as pd 

# Check pandas version
pd.__version__

# Show version of all packages 
pd.show_versions()

## Creating Series

# Create Series 
s1 = pd.Series([3, 6, 9, 12])
s1

# Check type 
type(s1)

# To see values 
s1.values

# To see index/keys 
s1.index

# Creating labeled series 
s2 = pd.Series([200000, 300000, 4000000, 500000], index=['A', 'B', 'C', 'D'])

s2

s2.values

s2.index

# Indexing
s2['A']

# Boolean indexing
s2[s2 > 700000]

## Creating DataFrame 

# Create a DataFrame 
data = {'Country': ['Belgium', 'India', 'Brazil'],
        'Capital': ['Brussels', 'New Delhi', 'Brasília'],
        'Population': [11190846, 1303171035, 207847528]
}

df = pd.DataFrame(data, columns=["Country", "Capital", "Population"])

df

# Check type 
type(df)

# Indexing
df["Country"]

# or 
df.Country

# Boolean indexing 
df["Population"]  > 40000000

df["Country"] == "Belgium"

df["Capital"] == "Brasilia"