import pandas as pd
import pickle

print("Loading datasets...")

basics = pd.read_csv(
    "title.basics.tsv",
    sep="\t",
    usecols=["tconst","titleType","primaryTitle","genres"],
    nrows=200000,
    low_memory=False
)

ratings = pd.read_csv(
    "title.ratings.tsv",
    sep="\t",
    usecols=["tconst","averageRating","numVotes"]
)

data = basics.merge(ratings,on="tconst")

data = data[data["titleType"]=="movie"]

data["genres"] = data["genres"].fillna("Unknown")
data = data[data["genres"]!="\\N"]

data = data.head(50000)

pickle.dump(data,open("movies.pkl","wb"))

print("movies.pkl created successfully")