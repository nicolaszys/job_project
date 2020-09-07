import requests
from bs4 import BeautifulSoup
import time
import random
import pandas as pd

# CHOIX DES VARIABLES DE L'URL:
    # FROMAGE : date de publication 3 = 3 derniers jours : choix entre 3,7,14


# CREATION DE NOS DICTIONNAIRES DE DONNEES FUTURES
title = []
company = []

# NOMBRE DE PAGE DE 0 à 200 avec un PAS de 10 (fonctionne comme cela dans l'url)
for j in range(0,200,10):
    # HEAD pris dans le navigateur
    head = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
       'accept-encoding': 'gzip, deflate, br',
       'accept-language': 'fr-FR,fr;q=0.9,es-ES;q=0.8,es;q=0.7,en-US;q=0.6,en;q=0.5,la;q=0.4',
       'Cookie': "CTK=1ec2qan6pq2ma800; _ga=GA1.2.1480736921.1593527593; _gcl_au=1.1.866743975.1593527613; JCLK=1; RF=\"TFTzyBUJoNr6YttPP3kyivpZ6-9J49o-Uk3iY6QNQqKE2fh7FyVgtWFBsuN5UtuLz_MWBBiO8Xw=\"; g_state={\"i_l\":0}; optimizelyEndUserId=oeu1594026206066r0.5768540165703828; OptanonAlertBoxClosed=2020-08-03T08:31:59.644Z; _gid=GA1.2.863213106.1599396400; OptanonConsent=isIABGlobal=false&datestamp=Mon+Sep+07+2020+12%3A19%3A25+GMT%2B0200+(Central+European+Summer+Time)&version=6.3.0&consentId=4b932611-d37e-4b98-9ee6-5ffcb5a758aa&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&hosts=&AwaitingReconsent=false&geolocation=%3B",
       'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    
    # Si nb de page = 0 url simple (finalement inutile, url par défaut)
    #if j == 0:
    #    url ='https://www.indeed.fr/jobs?q=Alternance+Data&l=Paris+%2875%29&fromage=14'
    #else:
    url ='https://www.indeed.fr/jobs?q=Alternance+Data&l=Paris+%2875%29&fromage=3&start='+str(j)
        
    # Request BS
    r = requests.get(url,headers=head)
    # print(url)
    # print(r.status_code)
    soup = BeautifulSoup(r.content,'html')
    
    # Time sleep pour être caché
    time.sleep(random.randrange(0,2))
    
    # Récupérer les éléments TITLE (titre de chaque annonce)
    for elem in soup.findAll('a',{'data-tn-element':'jobTitle'}):
        if elem == None:
            title.append("N/A")
        else:
        #print("c'est la page: "+ str(j))
        #print(elem.text.strip())
            title.append(elem.text.strip())
        
    # Récupérer les éléments COMPANY (entreprise de chaque annonce)
    for elem in soup.findAll('span',{'class':'company'}):
        if elem == None:
            company.append("N/A")
        else:
            company.append(elem.text.strip()) 

########
print(len(title))
print(len(company))
########

d = {'Entreprise':company, 'Offre': title,}
df = pd.DataFrame(data=d)
df.to_csv('scrap_indeed.csv',index=False)