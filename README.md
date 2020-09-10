# job_project

## 1 ère étape Scrapper le site Indeed

** Trois méthodes de scrapping ont été utilisés**

### 1. Beautiful Soup : cette méthode consiste à 

### 2. Selenium   
  #### a. 1ère méthode : utiliser la liste complète des éléments repérés 
          1. Prendre la liste de tous nos éléments (intitulé, entreprise, location) grâce à la méthode "browser.find_elements_by..." au pluriel  
          2. Une fois que tous les éléments d'une page ont été pris, **convertir les éléments en format texte** puis **ajouter à nos listes**  
          3. Changer de page  
          4. Réitérez phase 1, phase 2, phase 3 tant qu'il y a des pages restantes  
          
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

## 2 ème étape le pre-processing

  ### Notre scrapping

#### Le Lieu
        
Le Lieu de l'offre s'affiche de cette manière (l'arrondissement est optionnel)  
```"- Ville arrondissement (75)"```  
Exemples : 
```" - Paris 5 (75)" ```  
``` "Boulogne-Billancourt (92)"```

**Pré-processing** : Diviser le **Lieu** en  deux colonnes **Ville** et **Département**   
Difficultés : Le Regex pour obtenir les villes sachant que certaines villes ont des accents, des traits d'union...

#### Le Résumé

Pour chacune de nos annonces, en fonction des mots présent dans le titre de l'offre, nous récupérons les mots parmi une liste que nous avons défini  
Exemple de liste :
```best_words  = ['data', 'alternance', 'stage']```

Nous rajoutons la colonne **Resume** qui permet à partir de mot clefs de trouver l'offre la plus proche de nos envies.

Par simplification, nous avons fait cela sur le titre de l'offre.

*A partir de l'offre, nous pourrions scrapper l'annonce complète et passer le même algo pour trouver les mots clefs dnas l'annonce complète et pas seulement le titre de l'offre*

  