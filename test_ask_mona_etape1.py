#@RM - créé le 10/09/2018

#Dans cette première étape nous allons télécharger les données nécéssaires à la création de notre model de classification.
#Les fichiers du test étant des fichiers .json nous allons télécharger ceux-ci.
#Nous en profiterons aussi pour trier directement les données et nous attarder directement sur la partie "label"
#C'est donc cette partie que nous téléchargerons


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
#                           IMPORTANT !!!!                                #
#                  BIEN LIRE TOUS LES COMMENTAIRES                        #
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#

import requests
import json
import pandas as pd
import os
import csv

#Pour que ce tout fonctionne bien, il faudra compléter plusieurs variables.

#                           IMPORTANT !!!!                                #

#1) Veuillez créer 3 dossiers, (nommez les comme vous voulez, dans mon cas le 1er dossier se nomme : fJson | le 2eme : fCsv | le 3eme : fOut)
#Indiquez les chemins d'accès de vos 3 dossiers. Exemple : path_dossierJSON = "/home/robin/test_ask_mona/fJson" | (sans le dernier Slash "/")
path_dossierJSON = "/your/path/here/fJson"
path_dossierCSV = "/your/path/here/fCsv"
path_dossierOUT = "/your/path/here/fOut"

#renseignez ici votre user-name github ainsi que votre token. 
#pour savoir comment obtenir un token, connectez vous sur votre compte github, puis : https://github.com/settings/tokens.
#attention un token est visible une fois pendant une courte periode.
username = 'your_user_name_GITHUB_here'
token = 'your_token_number_here'

#Enfin, veuillez remplir le numéro de l'issue de départ ainsi que celle de fin. (en sachant que la première issue existante est la 00001 et la dernière est ~ 58050)
#Ces issues seront ensuite téléchargées (dans cet exemple vous pouvez laisser les chiffres ci-dessous)
issueDepart = 55000
issueFin = 58000

#Nous créons une fonction qui permet d'enregistrer notre fichier sur notre ordinateur et cela depuis un lien URL
def toJson(path, fileName, data ):
    fPName = path + fileName + '.json'
    with open (fPName, 'w') as fp:
        json.dump(data,fp)

#Nous paramétrons le nombre d'issues que nous désirons, sachant que l'issue minimum =  00001 | et que l'issue maximum à ce jour ~ 58050.
for i in range(issueDepart,issueFin):

    link = requests.get("https://api.github.com/repos/Microsoft/vscode/issues/%s/labels" %i, auth=(username,token))
    data = link.json()
    
    #Nous indiquons ici le ('lien de notre dossier' , 'Le nom de notre dossier%s' %i, lesDatas que l'on souhaite)
    toJson(path_dossierJSON, '/Step1%s' %i, data)

    df = pd.read_json(path_dossierJSON + "/Step1%s.json" %i)
    df.to_csv(path_dossierCSV +"/Step1%s.csv" %i)


   
    
    #On regarde si le fichier est vide ou non ("<4" correspond à 4 octets) (si il est vide, nous n'en voulons pas)
    if os.path.getsize(path_dossierCSV + "/Step1%s.csv" %i) < 4:
        result = True
    else:
        result = False
        df = pd.read_csv(path_dossierCSV + "/Step1%s.csv" %i)
        #Nous allons ensuite ajouter une colonne où se trouvera le numéro de l'Issue en question
        df['IssueNumber'] = i
        #Commentez la ligne ci-dessous si un bug remonte. Selon la version et le système utilisé, il se peut que la colonne "Unnamed:0" ne soit pas présente.
        del df['Unnamed: 0']
        #On transforme ensuite nos datas en .csv.
        df.to_csv(path_dossierCSV + "/Step1%s.csv" %i)


x = issueDepart + 1



#Nous fabriquons ici le fichier de sortie nommé "out.csv"
fout=open(path_dossierOUT + "/out.csv", "a")

#Nous ouvrons ici un premier fichier csv afin d'avoir les labels et les features de celui-ci
for line in open(path_dossierCSV + "/Step1" + str(issueDepart) + ".csv"):
    fout.write(line)

#Nous allons ensuite 'greffer' au premier fichier .csv les autres fichiers afin de faire fusionner ceux-ci
#Nous selectionnons le nom de fichier en fonction de leur issues (ici nous allons de l'issue 57801 à l'issue 57817)
for num in range(x,issueFin):
    f = open(path_dossierCSV + "/Step1" + str(num) + ".csv")
    #next(f) permet de supprimer l'entête (que l'on nomme aussi 'labels' ou encore header) des autres fichiers. (d'où le fait que l'on sépare le 1er fichier .csv des autres)
    next(f)
    for line in f:
        #On écrit dans le fichier .csv de sortie
        fout.write(line)
    f.close()
fout.close()
#On ferme les fichiers

#Enfin, on vient nettoyer notre fichier des impuretés, car dans certaines issues le terme "validation failed" vient perturber nos données
df = pd.read_csv(path_dossierOUT + "/out.csv")

#Nous supprimerons donc toutes les lignes où se trouve écrit "Validation Failed"
df = df[df.color != "Validation Failed"]
#Enfin, dans mon cas, lors de la mise en forme du Json au Csv, La bibliothèque Pandas vient ajouter une colonne. Cette colonne nous devons la supprimer car elle se sert à rien.
#Commentez la ligne ci-dessous si un bug remonte. Selon la version et le système utilisé, il se peut que la colonne "Unnamed:0" ne soit pas présente.
del df['Unnamed: 0']
#On reformate tout cela et on enlève les "header" (les entêtes)
df.to_csv(path_dossierOUT + "/out_cleaned.csv",header=None) 


#@RM



