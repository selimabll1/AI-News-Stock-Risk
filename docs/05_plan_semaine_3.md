# Livrable 3 — Semaine 3 : inventaire et collecte

## Résultat attendu

Une liste vérifiée des sources, puis une première base brute **datée**, avec un manifeste et un journal des acquisitions. À ce stade, il ne s'agit **pas** de fabriquer des résultats prédictifs.

## Ordre de travail proposé

1. Finaliser les définitions et points ouverts dans `docs/03_decisions_ouvertes.md`.
2. Pour chaque source, noter fournisseur, URL, droits d'usage, unités, fréquence, dates, paramètres de requête.
3. Télécharger et archiver séparément les deux indicateurs Google Trends (News / Web).
4. Identifier et obtenir les cours des 26 actions IA et des actions conventionnelles ; préciser les risques de biais de survivance.
5. Obtenir VIX, inflation et Treasury bills ; vérifier leurs transformations.
6. Dresser le bilan des données disponibles / absentes ; ne pas masquer les lacunes.
7. Ensuite seulement, écrire les scripts de nettoyage et de construction des variables pour la semaine 4.

## Critères d'acceptation

- Source de chaque fichier traçable (URL et date, si applicable).
- Paramètres Google Trends et fréquence mensuelle documentés.
- Aucune donnée future dans les informations utilisées pour prédire le passé.
- Données réelles conservées en local et non envoyées à GitHub sans vérification de licence.
- Modifications validées par pull request.
