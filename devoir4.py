# coding : utf-8

#EXPLICATIONS : Voici le résultat final de mon devoir. Malheureusement, je ne peux vérifier si le tout
#fonctionne, et ce, probablement puisque j'utilise Windows. Une erreur s'affiche en tout temps à partir
#du 888 caractère du CSV (UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 888: 
#character maps to <undefined>). J'ai même tenté de supprimé une ligne du CSV original, mais cela n'a pas été
#concluant.
# 
# J'ai commencé par lié le CSV au script, puis m'assurer d'aller chercher les paires de mots 
# dans les textes qui représentent la quatrième colonne du document -> doc = tal(inter[3]). 
# J'ai ensuite fait la lemmatisation (étape 4) et la recherche des paires de mots (étape 5). Lors de 
# mes premiers tests, j'avais omis d'ajouter une boucle me permettant d'aller cibler les termes "islam" et
# "musulm" (étape 6). Toutefois, à la suite de nos échanges par courriel, j'ai réalisé qu'il me
# manquait cette étape. Il se peut toutefois qu'il y ait une erreur à cet endroit, car, tel qu'expliqué 
# plus haut, je ne peux le tester. J'ai terminé mon travail en faisant ressortir les résutlats. 

import csv, spacy
from collections import Counter

martineau = "martineau.csv"

tal = spacy.load("fr_core_news_md")

f = open(martineau)
interventions = csv.reader(f)
next(interventions)

tousMots = []
bigrams = []


for inter in interventions:
    doc = tal(inter[3])

    #ÉTAPE 1 = avoir les tokens
    tokens = [token.text for token in doc]
    #print(tokens)

    #ÉTAPE 2 = LEMMATISATION (pour enlever les )
    #lemmes = [token.lemma_ for token in doc]

    #ÉTAPE 3 = enlever les mots vides
    #tokens = [token.text for token in doc if token.is_stop == False]

    #ÉTAPE 4 = après vérification, cette étape est censée lemmatiser, enlever les mots vides et la ponctuation
    #Les 2 étapes précédentes ne sont donc pas nécessaires.
    mots = [token.lemma_ for token in doc if token.is_stop == False and token.is_punct == False]

    #ÉTAPE 5 = paires de mots
    for x, y in enumerate(mots[:-1]):
        bigrams = ("{} {}".format(mots[x],mots[x+1]))

        #ÉTAPE 6 = condition pour que l'un de ces deux mots contienne les chaînes de caractères «islam*» ou «musulm*»
        if "islam" in bigrams or "musulm" in bigrams:
            tousMots.append(bigrams)

#ÉTAPE 7 = résultats
freq = Counter(tousMots)
print(freq.most_common(51))
print(len(tousMots))