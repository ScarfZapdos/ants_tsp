# Voyageur de Commerce et Fourmis
## Algorithmes de Recherche


Ce projet a pour but de résoudre le problème du voyageur de commerce sur les plus grandes villes de France à l'aide de "fourmis". Ces fourmis sont en fait des agents multiples.

## Architecture du projet
* Dans le dossier principal, retrouvez tout le code utile :
	+ **`fourmis.py`** contient le code des classes pour les fourmis et le graphe. C'est là que le SMA agit.
	+ `test_params.py` contient le code qui permet de produire les fichiers texte de `results`
	+ `plot_best_path.py` permet de tracer `map.png`
	+ **`map.png`** est une carte du meilleur trajet trouvé par les fourmis. Elle a été tracée grâce à matplotlib et cartopy
	+ `exploit*.py` permet de tracer les courbes de `plots`
	+ **`visualize.py`** permet de visualiser le déroulement de l'algorithme principal avec pygame

* Dans **`plots`**, retrouvez des graphiques qui décrivent l'évolution du nombre d'itérations moyen pour obtenir le meilleur chemin selon les paramètres. Grâce à ces graphiques, on a les meilleures valeurs présumées de chaque paramètre.

* Dans `results`, retrouvez les résultats sous forme de texte des tests qui ont permis de tracer les graphiques de `plots`.


![Map of the best path](https://github.com/ScarfZapdos/ants_tsp/blob/main/map.png)
