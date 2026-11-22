# Rapport Google Trends — expériences et critiques méthodologiques

Projet Math Finance — note de recherche méthodologique (sans date de rédaction sur la couverture).

## Contenu de l’archive LaTeX

- `Rapport_Google_Trends_Experiences_2026.tex` : source éditable du rapport.
- `fig_*.pdf` : quatre figures vectorielles intégrées au rapport.
- `table_annexe.tex` : annexe des 312 observations mensuelles retenues.

Aucun nouveau CSV consolidé n'est nécessaire : le dépôt `AI_News_Risk` possède déjà
`data/processed/ai_trends_monthly.csv`, créé par `scripts/03_prepare_google_trends.py`.
Les exports bruts demeurent dans `data/raw/google_trends/`.

## Emplacement conseillé dans le dépôt

- PDF final : `deliverables/semaine_03/Rapport_Google_Trends_Experiences_2026.pdf`
- Sources LaTeX + figures + annexe : `reports/google_trends/latex/`

## Compiler sous LaTeX

Installer une distribution contenant `xelatex`, les bibliothèques LaTeX usuelles et
les polices libres Noto Serif et Noto Sans. Dans le dossier `latex` :

```powershell
xelatex -interaction=nonstopmode Rapport_Google_Trends_Experiences_2026.tex
xelatex -interaction=nonstopmode Rapport_Google_Trends_Experiences_2026.tex
```

Les quatre figures `fig_*.pdf` et `table_annexe.tex` doivent rester dans le même
répertoire que le `.tex`.

## Décision méthodologique

Deux séries principales : terme `Artificial Intelligence`, monde entier,
toutes catégories, janvier 2012 à décembre 2024, Web Search et News Search.
Les autres tests sont documentés mais ne remplacent pas ces deux séries.
