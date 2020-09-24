import streamlit as st
import plotly.express as px
import pandas as pd

def load_data(dataset):
    data = pd.read_csv(dataset)

    # Departement par ordre alphabetique
    departement = data['Departement'].unique()
    dep = sorted(departement)

    # Ville par ordre alphabetique
    cities = data['Ville'].unique()
    city = sorted(cities)

    # Entreprise par ordre alphabetique
    companies = data['Entreprise'].unique()
    company = sorted(companies)

    # Mots favoris
    key_words = ['alternance','stage','apprentissage','internship','data','analyst','scientist','développeur','chargé(e)s','stage/alternance']
    key_word = sorted(key_words)

    st.title("Trouvez l'annonce qui vous correspond !")
    st.subheader("Avec Indeed")

    st.sidebar.title("Choisissez vos paramètres")
    dep_choice = st.sidebar.multiselect("Vos départements",dep)
    city_choice = st.sidebar.multiselect("Vos villes",city)
    company_choice = st.sidebar.multiselect("Vos entreprises",company)
    key_choice = st.sidebar.multiselect("Vos envies",key_word)

    st.subheader("Votre résultat de recherche par département")
    st.write(data.loc[data['Departement'].isin(dep_choice)])

    st.subheader("Votre résultat de recherche par ville")
    st.write(data.loc[data['Ville'].isin(city_choice)])

    st.subheader("Votre résultat de recherche par entreprise")
    st.write(data.loc[data['Entreprise'].isin(company_choice)])    

    # st.subheader("Votre résultat de recherche par mots-clef")
    # st.write(data.loc[data['Resume'].isin(word_choice)])

    st.subheader("Votre résultat avec vos recherches combinés")
    # if data.loc[data['Departement'].isin(dep_choice)]:
    #     st.write(data)
    data[(data['Departement'].isin(dep_choice))|
        (data['Entreprise'].isin(company_choice))|
        (data['Ville'].isin(city_choice))]

    return dataset

load_data("../mongo_db_connexion/scrap_post_pre_process.csv")

