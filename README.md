# job_project

## 1 ère étape Scrapper le site Indeed

** Trois méthodes de scrapping ont été utilisés**

### 1. Beautiful Soup : cette méthode consiste à 

### 2. Selenium   
  #### a. 1ère méthode : utiliser la liste complète des éléments repérés 
          1. Prendre la liste de tous nos éléments (intitulé, entreprise, location) grâce à la méthode "browser.find_elements_by..." au pluriel  
          2. Une fois que tous les éléments d'une page ont été pris, **convertir les éléments en format texte** puis **ajouter à nos listes**  
          3. Changer de page  
          3. Réitérez phase 1, phase 2, phase 3 tant qu'il y a des pages restantes  
          
  **AVANTAGES**  
  Permet d'avoir un résultat rapide en faisant directement des listes par pages sans passer par les annonces  
  **INCONVÉNIENTS**  
  Ne permet d'avoir **seulement** contenu dans la "preview" de l'annonce
  
  #### b. 2ème méthdoe : cliquer sur l'anonce
          1.   
          2.   
          3.   
          
  **AVANTAGES**  
    - Meilleure personnalisation : permet d'avoir plus d'informations si besoin  
  **INCONVÉNIENTS**  
    - Plus longue  
    - Plus difficile à mettre en place
  