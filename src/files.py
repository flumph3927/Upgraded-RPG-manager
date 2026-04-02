#saving and getting back from files with dataframes
import pandas, character

#create function that takes dataframe and saves it to csv
def save(frme,path):
    frme.to_json(path)

#create function that loads dataframe from csv and returns dictionary of characters
def load(path):
    stuff=pandas.read_json(path)
    out={}
    for (i,v) in stuff.items():
        out[i]=character.Character([i]+list(v))
    return out