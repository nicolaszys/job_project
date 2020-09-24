import numpy as np
import pandas as pd
import re

df = pd.read_csv("../result_csv/scrap_indeed_fourteen_days.csv")

# Convert all values in lower cases
df = df.applymap(lambda s:s.lower() if type(s) == str else s)

# Supress rows where nan value
df.dropna(axis=0, inplace=True)

# Difficultés pour extract les noms de villes :
    # les accents
    # les villes avec un ou plusieurs "-"
    # les villes qui commence avec la déterminant (ex: la garenne-colombes)

# Extract le nom de la ville de la column "Lieu"
df['Ville'] = df['Lieu'].str.extract("([a-zA-Z*(é|è|à|ù)]+[\sa-zA-Z*(é|è|à|ù)+]+[a-zA-Z*(é|è|à|ù)+\-+[a-zA-Z*(é|è|à|ù+)\-]+[a-zA-Z*(é|è|à|ù)]+|[a-zA-Z]+\-+[a-zA-Z]+|[a-zA-Z]+)",expand=True)

# Extract le département (difficulté) :
    # paris 8e (16) --> prendre le 75 et non le 16
df['Departement'] = df['Lieu'].str.extract('(\S\d{2,5})',expand=True)

# Supprimer les parenthèses
df['Departement'] = df['Departement'].str.extract('(\w{2})',expand=True)    

# Supprimer la column lieu
df.drop(['Lieu'], axis=1, inplace=True)

df.dropna(axis=0, inplace=True)
df.reset_index(inplace=True)
df.drop(['index'], axis=1, inplace=True)

# Trouver les mots importants 
resume = []
for offre in df['Offre']:
    resume.append(offre.split(" "))

df['Resume'] = resume

best_word = ['alternance','stage','apprentissage','internship','data','analyst','scientist','développeur','chargé(e)s','stage/alternance']
for i in range(0,len(df['Resume'])):
    ref = []
    for el in df['Resume'][i]:
        print(el)
        if el in best_word:
            ref.append(el)
    if ref == []:
        ref = ['Mauvaise Anonce']
    df['Resume'][i] = ref 