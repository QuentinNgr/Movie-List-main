Ce programme permet d'afficher une interface graphique pour la gestion d'une liste films. Il permet de simplifier le suivi des films regardés, à regarder, possédés ou autre sans avoir recours à un tableur de type excel.
Il permet également de faire appel à la base de données IMDb afin de récupérer immédiatement les inforamtions des différents films ajoutés à l'application.
Les informations sont stockées dans "CleanNoH.txt" et "DATALOCAL.txt". Le premier ne stocke que les informations primaires (nom, année de sortie, durée, note IMDb, status). Le second stocke également les informations sur les acteurs, le réalisateruu, le résumé et autres.

Ce programme a été écrit en Python 3.9 à l'aide de l'IDE Pycharm version 2020.3.3 sur une machine Windows 10.
Il fait appel aux packages suivants :
-IMDbPY https://imdbpy.github.io/ version 2020.09.25 : permet de faire appel à la base de données IMDb
-tkinter https://docs.python.org/fr/3/library/tkinter.html version 8.6 : permet d'afficher une fenêtre graphique
-textblob https://textblob.readthedocs.io/en/dev/install.html version 0.16.0 : permet de traduire un texte (utilisé pour traduire le résumé d'un film en > fr)
-urllib.request module https://docs.python.org/3/library/urllib.request.html : permet de vérifier la connection internet à l'ouverture du programme

ATTENTION : Vous devez créer les fichiers textes "CleanNoH.txt" et "DATALOCAL.txt" vous même (ne rejoutez aucune information à l'intérieur, laissez les vides).

La fenêtre graphique est pour l'instant composée de 7 zones :
___________________________
|                 |       |
|        1        |   2   |
|                 |_______|
|                 |   3   |
|_________________|_______|
|___________4___|____5____|
|                         |
|           6             |
|_________________________|
|___________7_____________|

Zone 1 : Un tableau de 5 colonnes affichant les données contenues dans "CleanNoH.txt"
 Les colonnes "titre" ,"année", "durée" sont explicites. La note est récupérée depuis IMDb. 
 Le status représente l'état du film que vous ajoutez. Il est représenté par un nombre car cela simplifie grandement l'affichage et la compréhension si vous savez ce que représente le nombre. 
  Par exemple, vous pouvez déclarer que les films ayant le status "0" sont ceux que vous n'avez pas encore vu, ceux ayant le status "1" sont ceux ayant déjà été vus.

Zone 2 : Une zone de recherche dans le tableau. 
 Vous pouvez ainsi rechercher un film répondant à certaines caractéristiques dans votre liste locale.
 Si vous souhaitez filtrer l'affichage avec plusieurs critères, utilisez le bouton FILTER du bas.

Zone 3 : Les boutons Modifier et Supprimer.
 Pour utiliser le premier, vous devez d'abord sélectionner un film du tableau (zone 1). Vous pouvez ensuite modifier les informations principales dans la zone 4 et les autres dans la zone 6.
  Vous pouvez ensuite cliquer sur le bouton modifier.
 Pour le second, il suffit de sélectionner le film que vous souhaitez supprimer de votre liste. Cette action est irréversible, si vous avez appuyé par erreur, vous devrez rajouter un film.

Zone 4 : Permet d'ajouter un film dans CleanNoH.txt, le fichier primaire.

Zone 5 : Permet de faire une recherche dans la base de donnée IMDb, les résultats seront affichés dans la zone 6. Une connexion internet est nécessaire.

Zone 6 : Les informations complètes du film sélectionnée localement dans la zone 1 ou du film recherché dans la zone 5.
 Dans le cas d'une recherche internet, plusieurs résultats seront proposés. vous pouvez naviguer de l'un à l'autre avec les flèches <- -> en haut à droite.
 Si vous voulez ajouter un film de cette manière, recherchez son nom dans le champ IMDb. Une fois le film trouvé, cliquez sur "INSERT" puis sur "ADD".

Zone 7 : La version du programme et vérification de la connection internet (si vous souhaitez utiliser la recherche IMDb).

Bugs:
Des problèmes d'affichage sont possibles sur de petits écrans à la résolution plus faible, ainsi que sur certaines machines utilisant Linux.
La traduction automatique a des lacunes, textblob n'étant pas infaillible surtout sur des expression portant à confusion.
L'utilisateur doit créer les fichiers "CleanNoH.txt" et "DATALOCAL.txt", même vides.
L'utilisateur doit installer lui même les packages nécessaires.

Fonctionalités à améliorer :
-Filtre : par genre, acteur, réalisateur
-Modifier : doit être plus ergonomique
-Ajouter : doit être plus ergonomique
-Apparence : un code couleur autre que blanc/gris, une meilleure police d'affichage

Fonctionalités à ajouter :
-obtenir l'affiche d'un film
-pouvoir noter un film
-implémenter un algorithme de recommendation, local et/ou via internet, selon les films préférés.
-pouvoir ajouter d'autres médias (séries...)

