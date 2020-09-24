# IMPORT

import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time
import random
import pandas as pd
from datetime import date

# DEMARRAGE DE SELENIUM
browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://www.indeed.fr/')

# ENTREZ LES MOTS CLEFS A RECHERCHER (ex : Alternance data)
input_bar = browser.find_element_by_xpath('//*[@id="text-input-what"]').send_keys('Alternance data')

# Time sleep
time.sleep(random.randrange(0,2))

# ENTREZ LA LOCATION (ex: Paris)
# A revoir

# Time sleep
time.sleep(random.randrange(0,2))

# INPUT LA RECHERCHE
input_recherche = browser.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div/div/form/div[3]/button').click()

# Filter a 24 dernieres heures (1/2)
date = browser.find_element_by_id('filter-dateposted').click()

# Time sleep
time.sleep(random.randrange(0,1))

# Filter a 24 dernieres heures (2/2)
#one_day = browser.find_element_by_partial_link_text('Dernières').click()
three_days = browser.find_element_by_partial_link_text('3 derniers jours').click()
#seven_days = browser.find_element_by_partial_link_text('7 derniers jours').click()
#fourteen_days = browser.find_element_by_partial_link_text('14 derniers jours').click()

# Time sleep
time.sleep(2)

# Si fenêtre du mail apparait, pour fermer cette fenêtre
try:
    browser.find_element_by_css_selector('[aria-label="Close"]').click()
except:
    pass

# Time sleep
time.sleep(random.randrange(0,1))

# VARIABLES
titles = []
companies = []
locations = []
urls = []
i = 0
page = True
browser.execute_script("window.scrollTo(0, 200)")

while page:
    try:
        liste_test = browser.find_elements_by_css_selector("[data-tn-element='jobTitle']")
        for i in range(0,len(liste_test)):
            # Time sleep
            time.sleep(1)
            # job annonce click
            job = liste_test[i].click()
            # Time sleep
            time.sleep(random.randrange(1,2))

            # TITLE
            try:
                title = browser.find_element_by_id('vjs-jobtitle').text
            except:
                title = 'N/A'

            #ENTREPRISE
            try:
                company = browser.find_element_by_css_selector('[rel="nofollow noopener"]').text
            except Exception:
                pass
            try:
                company = browser.find_element_by_id('vjs-cn').text
            except:
                company = 'N/A'

            # LOCATION
            try:
                location = browser.find_element_by_id("vjs-loc").text
            except:
                location = 'N/A'

            # URL
            try: 
                url = browser.current_url
            except:
                url = 'N/A'

            # Time sleep
            time.sleep(random.randrange(0,1))

            # Remplir nos listes
            titles.append(title)
            companies.append(company)
            locations.append(location)
            urls.append(url)

            # Scroll 
            #browser.execute_script("window.scrollTo(0, 800)")
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Incrementation
            i += 1

            # Time sleep
            # time.sleep(1)

        browser.execute_script("window.scrollTo(0, 6000)")
        
        try:
            arrow = browser.find_element_by_css_selector('[aria-label="Suivant"]').click()
            #print(f'page{i}')
        except:
            page = False
        
    except:
        #page = False
        print("c'est fini")
        break

# FERMETURE DU BROWSER
browser.close()

d = {'Entreprise':companies, 'Offre': title, 'Lieu': locations, 'URL':urls}
df = pd.DataFrame(data=d)

# Avoir la date d'aujourd'hui pour renommer le CSV
today = date.today()

df.to_csv(f'../result_csv/scrap_indeed_{today}.csv',index=False)


