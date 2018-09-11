![Image of AskMona](https://ibb.co/hUvuS9)

# _TEST ASK-MONA_

Pour reproduire ce test il faudra utiliser les deux fichiers nommés respectivement "test_ask_mona_etape1.py" & "test_ask_mona_etape2.py".
_____________________________________________________________________________________________________________________________


## 1ère étape : "test_ask_mona_etape1.py"

> Ce fichier a pour but de "scrapper" les fichiers qui viennent de l'api github.
> Avant de lancer ce programme depuis un IDE python 3 vous devrez compléter quelques informations necessaires.

1) Veuillez créer 3 dossiers, (nommez les comme vous voulez, dans mon cas le 1er dossier se nomme : fJson | le 2eme : fCsv | > le 3eme : fOut)

2) Complétez dans le programme "test_ask_mona_etape1.py" les 3 variables `path_dossier` par les chemins d'accès de vos dossiers respectifs.

- path_dossierJSON = "/your/path/here/fJson"
- path_dossierCSV = "/your/path/here/fCsv"
- path_dossierOUT = "/your/path/here/fOut"`

3) Renseignez votre user-name github ainsi que votre token dans les variables `username` et `token`. 
Pour savoir comment obtenir un token, connectez vous sur votre compte github, puis : https://github.com/settings/tokens.
Attention un token est visible une fois pendant une courte periode.

- username = 'your_user_name_GITHUB_here'
- token = 'your_token_number_here'

4) Enfin, ce qui va suivre est une option ce qui impliqu que vous n'êtes pas obligé d'y toucher. 
Vous pouvez modifier le numéro de l'issue de départ ainsi que celle de fin. (en sachant que la première issue existante est la 00001 et la dernière est ~ 58050)
#Ces issues seront ensuite téléchargées de l' `issueDepart` à l' `issueFin`

- issueDepart = 55000
- issueFin = 58000

> Si tout s'est bien passé vous allez attendre quelques minutes le temps que tout finisse.
> L'étape 1 aura finalament scrappée les données de l'api github. Ces données sont au format .Json , nous prefererons travailler en .csv , c'est pourquoi une étape de transformation entre .json et .csv est présente. Enfin, les données sont rassemblées en 1 fichier .csv  .

_____________________________________________________________________________________________________________________________

### 2ème étape : "test_ask_mona_etape2.py"

> Ce fichier a pour but de "générer" un modèle de classification depuis le fichier csv généré en fin d'étape 1.
> Avant de lancer ce programme depuis un IDE python 3 vous devrez compléter quelques informations necessaires.

1) Comme pour la première étape, il faudra compléter dans le programme "test_ask_mona_etape2.py" la variable `path_dossier` par le chemin de sortie. Il s'agit du même que celui utilisé dans la première étape (path_dossier_out).

- path_dossierOUT = "/your/path/here/fOut"

> Si tout s'est bien passé vous aurez affichés en bas le résultat du taux de réussite en % de l'entrainement du modèle.
> Le modèle utilisé est un modèle linéaire multi-classes qui est celui qui répond le mieux à ce genre de classification. 
> Plusieurs autres modèles ont été utilisé avec des taux de réussite allant de 90 à 97 %.
> La classification linéaire à l'avantage de ne pas avoir besoin d'un très grand nombre d'échantillons, comme ici nous en utilisons 3000 (moins 20%) ce qui est relativement faible. Ce modèle à aussi l'avantage d'être rapide.

> Dans mon cas mon taux de réussite varie selon les échantillons de données entre 98 et 99%.

> Enfin, vous trouverez à la fin des résultats un test du modèle. Ce test vérifie la véracité du modèle entrainé.

_____________________________________________________________________________________________________________________________

Bonne journée à vous :)

R.MAHOU


