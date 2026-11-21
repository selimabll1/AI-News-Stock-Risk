# Politique des données

- `raw/` : téléchargements originaux non modifiés ; ajouter pour chaque fichier un journal (source, URL, paramètres, date, licence).
- `interim/` : étapes intermédiaires produites par scripts.
- `processed/` : jeux mensuels et portefeuilles prêts à estimer.
- `external/` : autres fichiers acquis sur autorisation.

Ces dossiers sont ignorés par Git pour éviter de publier des données potentiellement soumises à licence, des fichiers volumineux ou des informations sensibles. Le dépôt public conserve les métadonnées, le dictionnaire, les scripts et les méthodes ; pas les observations réelles, tant que leurs droits ne sont pas vérifiés.

**Important :** au 17 novembre 2026, aucun téléchargement ni calcul n'a été effectué par ce dépôt.
