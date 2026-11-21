# AI News & Stock Market Risk — Reproduction Study

**Auteurs : Aziz Gharbi et Selima Bellil**  
**Année universitaire : 2026–2027**  
**Projet : Intelligence artificielle, primes de risque et volatilité boursière**

## Objectif

Reproduire, dans la mesure des données accessibles, la méthodologie empirique de :

> Salisu, A. A., & Badmus, S. (2026). *Can AI News Improve the Out-of-Sample Forecasts of Risk Premia and Volatility in the U.S. Stock Market?* Quality & Quantity. https://doi.org/10.1007/s11135-026-02816-9

Deux variables à expliquer : **primes de risque** et **volatilité des rendements**. Le périmètre de l'article est mensuel, **2012–2024**, pour **503 entreprises du S&P 500**, dont **26 classées « AI-related »** par les auteurs. Ces effectifs décrivent **l'étude originale** et ne préjugent pas de la disponibilité de notre base reconstituée.

## État du projet

| Livrable | Période | Statut |
| --- | --- | --- |
| 1 — Fiche de lecture | Semaine 1 | Rédigé, voir `deliverables/semaine_01/` |
| 2 — Synthèse bibliographique | Semaine 2 | Rédigé, voir `deliverables/semaine_02/` |
| 3 — Sources, données, préparation et traçabilité | Semaines 3–4 | Infrastructure créée ; données **non collectées** |
| Estimation et prévisions | Semaines 5–7 | À venir |
| Rapport scientifique final et soutenance | Semaine 8 | À venir |

## Démarrage sur Windows / PowerShell

```powershell
# À exécuter à la racine du dépôt après l'avoir cloné
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python scripts/00_check_environment.py
python scripts/01_inventory_sources.py
python -m pytest -q
```

Si `py -3.11` n'est pas disponible, utiliser une version Python >=3.11 installée sur le poste (`py -3.12` ou `py -3.13`, par exemple). Ne pas publier `.venv/`, des clés API ou des données sous licence.

## Arborescence

- `config/` — période, sources, paramètres documentés.
- `data/raw/` — téléchargements originaux **non modifiés** (ignorés par Git).
- `data/interim/` — alignements et transformations intermédiaires (ignorés par Git).
- `data/processed/` — jeux de données finaux reproductibles (ignorés par Git).
- `docs/` — protocole, dictionnaire, décisions et planning.
- `src/ai_risk_replication/` — fonctions Python réutilisables.
- `scripts/` — contrôles et futures étapes de collecte / estimation.
- `notebooks/` — exploration, jamais la seule source des calculs.
- `reports/` — figures et tableaux générés (ignorés par Git par défaut).
- `deliverables/` — livrables LaTeX/PDF validés.
- `tests/` — contrôles de cohérence du code.

## Démarche scientifique

1. Relever les **sources et définitions exactes** de l'article. Les informations manquantes sont signalées, pas inventées.
2. Documenter les dates de collecte et les paramètres Google Trends (terme, localisation, type de recherche, fenêtre, téléchargement).
3. Vérifier les transformations financières (cours ajustés, rendement, taux sans risque, construction de la volatilité, compositions des portefeuilles).
4. Reproduire les modèles de l'article (WN/FQGLS) avant de proposer des méthodes alternatives.
5. Comparer les prévisions sur des périodes non utilisées pour estimer les modèles ; empêcher les fuites d'information.
6. Distinguer clairement **résultats de l'article**, **reproduction**, **adaptation** et **extension**.

**Extension NLP/agent** : idée de recherche future, **non implémentée** et séparée de la réplication de référence.

## Collaboration Git

Nous travaillons par petites branches (`feat/data-sources`, `feat/google-trends`, `feat/market-data`, etc.) et pull requests. Pas de CI/CD complexe à ce stade. Les données acquises avec licence restrictive ne sont pas publiées dans le dépôt.

Voir `docs/04_workflow_git.md` pour les commandes et `docs/05_plan_semaine_3.md` pour les prochaines tâches.
