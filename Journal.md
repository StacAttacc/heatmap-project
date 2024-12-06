# projet1-aguila-valitiana
9/11/2023
  -création du github
  -téléchargement des données
  -planification du prototype
  -filter les données dont on a besoin
  -lire les données GTFS

9/13/2023
  -recherche sur les données GTFS
  -playlist trouvé sur youtube sur le fonctionnement des données GTFS (par ArcGIS ESRI)
    <
      [https://www.youtube.com/watch?v=AEC37x04tcw&list=PLGZUzt4E4O2KQz9IxGKrEyKB8rA0UVx1W]
      Les vidéos dan cette playlist explique bien c'est quoi des données GTFS,
        comment elles sont utilisées,
        nous montre une application où on peut utiliser ces données GTFS pour dessiner des cartes
          [https://github.com/Esri/public-transit-tools] (leur github),
        nous montre toutes les fonctionnalités de leur application qui traite des données GTFS.
      Leur vidéos sont un peu veux, donc n'est pas à jour sur l'état actuel de peur application,
        mais sont quand même une bonne ressource selon nous.
      On a décidé de prendre quelque chose d'autre pour faire le prototype.
      
      {7/10, il serait utile si on travaillait plus profondément sur une application concernant les transports pubiques de Montréal}
    >
  -setup pour le projet
    <
      On utilise Python avec Pandas et Folium
      On a constaté qu'utiliser Heatmap.js aurait été utile,
        mais cependant on n'a presentment pas réussi à le faire marcher correctement.
    >

9/18/2023
  -liens informatives pour le prototype
    <
      [https://makeshiftinsights.com/blog/heatmaps-leaflet-heatmap-js/]
      Utilise Leaflet et Heatmap.js
        [https://www.patrick-wied.at/static/heatmapjs/]
      C'est un peu compliqueé d'utiliser Python avec JavaScript.
      Cependant, dès qu'on a plus de savoir sur comment l'utiliser,
        je pense qu'il sera très facile de faire des Heatmaps avec.
      On n'a pas encore réussi à le faire marcher,
        cependant, on va réessayer, les résultats seront ici sous-peu.

      {
        8/10, on utiliserait ceci si on aurait besoin de faire un site web contenant le heatmap et
        non juste on prototype avec Python
      }
    >,
    <
      [https://github.com/pa7/heatmap.js/tree/master/examples/googlemaps-heatmap]
      Lien github pour utiliser Googlemaps et Heatmap ensemble
        [https://www.patrick-wied.at/static/heatmapjs/example-heatmap-googlemaps.html] (exemple de Heatmap avec Googlemaps),
      Mêmes problèmes qu'avant, on ne sait pas vraiment comment l'utiliser et
        il ne répond pas vraiment aux besoins du prototype.

      {7/10, une autre option pour le site web}
    >,
    <
      [https://github.com/luka1199/geo-heatmap]
      Une Catre Géothermique qui utilise python.
      Ça a l'air très utile et il utilise Folium.
      Il est trop complexe pour ce qu'on veut faire comme prototype et
        on ne pense pas avoir le temps de vraiment l'essayer, alors on va passer à autre chose.
      Cependant, il est un candidat excellent pour la version non-prototype si on en faisait une.

      {
        10/10, très bonne ressource si on fairait vraiment cette application,
        en plus d'avoir d'autres fonctions utiles si déciderait d'ajouter des choses en extra
      }
    >,
    <
      [https://github.com/Bondify/gtfs_functions]
      Lien github vers GTFS_functions.
      Très utile pour notre projet pour l'analyse de données GTFS.
      On peut directement utiliser les données GTFS avec.
      On peut filtrer les données avec, donc on peut optimiser notre application.
      Vu le nombre de données qu'on doit travailler avec et a puissance de nos ordinateurs,
        c'est le bienvenu.

      {
        10/10, il a la majorité des choses dont on a besoin.
        Il est facile à utiliser.
        Il est bon pour faire une représentation visuelle des données (sans la Heatmap)
      }
    >,
    <
      [https://towardsdatascience.com/python-for-gtfs-segment-frequencies-in-a-map-4dc3bc1e26ff]
      Tutoriel pour comment utiliser GTFS_functions pour calculer la fréquence de passage des bus.
      Il semble calculer la fréquence par route et non par zone.

      {8/10, intéressant, mais pas exactement ce qu'on a besoin pour notre prototype.}
    >,
    <
      [https://wellsr.com/python/plotting-geographical-heatmaps-with-python-folium-module/]
      Comment utiliser folium avec pour les cartes thermiques, très utile.
      On utilise ceci pour notre prototype.

      {10/10, il est exactement ce qu'on avait besoin comme tutoriel pour notre prototype}
    >,

  -réussi à générer une carte avec folium et pandas, pas encore réussi la heatmap

9/27/2023
  -réussi à faire la heatmap
    <
      On a réussi à faire la heatmap avec Folium HeatMap et GTFS_Functions.
      Ce n'est pas exactement ce qui est demandé.
        Au lieu d'avoir des zones séparés en carré sur ue petite portion de la carte,
        on a pris en compte toute l'île et mis les points d'intérêts sur les arrêts de bus.
      Cependant, ça marche assez pour être utile.
    >
  -netoyer et améliorer le journal
