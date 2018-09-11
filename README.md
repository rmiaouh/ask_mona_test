# _TEST ASK-MONA_

Pour reproduire ce test il faudra utiliser les deux fichiers nommés respectivement "test_ask_mona_etape1.py" & "test_ask_mona_etape2.py".
_______________________________________________________________________________________________________________________________

# 1ère étape : "test_ask_mona_etape1.py"
Ce fichier a pour but de "scrapper" les fichiers qui viennent de l'api github.

--> Avant de lancer ce programme depuis un IDE python 3 vous devrez compléter quelques informations necessaires.

1) Veuillez créer 3 dossiers, (nommez les comme vous voulez, dans mon cas le 1er dossier se nomme : fJson | le 2eme : fCsv | le 3eme : fOut)
2) Complétez dans le programme "test_ask_mona_etape1.py" les 3 variables "path_dossier" par les chemins d'accès de vos dossiers respectifs.

- path_dossierJSON = "/your/path/here/fJson"
- path_dossierCSV = "/your/path/here/fCsv"
- path_dossierOUT = "/your/path/here/fOut"

3) Renseignez votre user-name github ainsi que votre token dans les variables _username_ et _token_. 
Pour savoir comment obtenir un token, connectez vous sur votre compte github, puis : https://github.com/settings/tokens.
Attention un token est visible une fois pendant une courte periode.

username = 'your_user_name_GITHUB_here'
token = 'your_token_number_here'


