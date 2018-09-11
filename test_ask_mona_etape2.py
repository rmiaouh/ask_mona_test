#@RM
#Dans cette 2ème étape nous entrainerons notre modèle, nous afficherons le résultat en % et nous vérifierons que celui-ci répond bien à nos demandes

import numpy as np
import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.multiclass import OneVsOneClassifier
from sklearn import linear_model
from sklearn.metrics import precision_score,recall_score

#On vient lire notre fichier nettoyé .csv
#IMPORTANT : Veuillez modifier votre chemin d'accès en fonction de votre dossier OUT
path_dossierOUT = "/your/path/here/fOut"

df = pd.read_csv(path_dossierOUT + "/out_cleaned.csv", sep=',', names=['color','default','id','name','node_id','url','IssueNumber'])

#Décommenter si besoin pour :
#Affiche le premières datas du dataset
#print(df.head())

#Compte le nombre de datas du dataset
#print(len(df))

df_x=df["name"]
df_y=df["id"]

#On vectorise nos données
cv=CountVectorizer()

#On délimite à 20% le pourcentage utilisé pour nos données d'entrainement
x_train, x_test, y_train, y_test = train_test_split(df_x,df_y,test_size=0.2,random_state=4)

#On entraine nos données
x_traincv = cv.fit_transform(x_train)
a=x_traincv.toarray()
#On choisit notre modèle, ici un classificateur multi-classes linéaire
mnb=linear_model.SGDClassifier()
y_train=y_train.astype('int')
mnb.fit(x_traincv,y_train)
#On entraine nos prédictions
x_testcv=cv.transform(x_test)
pred=mnb.predict(x_testcv)
predToArray=np.array(y_test)
#On affiche les résultats du modèle
count=0
for i in range(len(pred)):
    if pred[i]==predToArray[i]:
        count=count+1
a=count
b=len(pred)
resultat = "%.2f" % ((a/b)*100)
print ("################################################")
print ("Résultat du modèle : {}  %".format(resultat))


######################################
#Verification des résultats du modele#
######################################

#Pour vérifier le résultat du modèle nous allons tester notre modèle avec l'issue[7] .
nb_verif = 7
verifpred = mnb.predict(x_testcv[nb_verif])
verif = x_test.iloc[nb_verif]

#Si verifpred = verif alors la classification a fonctionnée
print ("Verification de la prédiction (id du label) : {}".format(verifpred))
print ("Verification du modèle (nom du label) : {}".format(verif))
print ("################################################")

#@RM