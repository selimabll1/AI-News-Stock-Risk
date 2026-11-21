# Collaboration Git — Aziz Gharbi & Selima Bellil

## Démarrage sur un dépôt GitHub existant

Cloner l'URL réelle du dépôt dans un dossier choisi :

```powershell
git clone https://github.com/USER/REPOSITORY.git
cd REPOSITORY
```

Copier **le contenu** de l'archive dans ce dossier, sans créer un sous-dossier supplémentaire, puis :

```powershell
git status
git add .
git commit -m "chore: initialize econometric replication structure"
git push -u origin main
```

Remplacer `main` par le nom réel de la branche par défaut (`git branch --show-current`). Si le dépôt contient déjà des fichiers, les comparer avant d'écraser quoi que ce soit.

## Collaboration

```powershell
git checkout -b feat/data-inventory
# Modifier la documentation et les scripts
git add .
git commit -m "docs: inventory data sources"
git push -u origin feat/data-inventory
```

Créer ensuite une pull request GitHub vers la branche principale. Garder chaque PR petite, documentée et révisable. Ne jamais partager des tokens ni des datasets privés.

Branches proposées : `feat/data-inventory`, `feat/google-trends`, `feat/market-data`, `feat/monthly-cleaning`, `feat/eda`.
