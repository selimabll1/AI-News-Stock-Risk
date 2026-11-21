# Dictionnaire préliminaire des variables

| Variable | Rôle | Fréquence | Description / traitement | Vérification |
|---|---|---|---|---|
| `date` | Clé | Mensuelle | Mois calendaire 2012-01 à 2024-12 | Fixé |
| `ai_news_search` | Explicative | Mensuelle | Indice Google Trends pour recherches de nouvelles liées à l'IA | Paramètres exacts à vérifier |
| `ai_web_search` | Explicative | Mensuelle | Indice Google Trends de recherches web sur l'IA | Paramètres exacts à vérifier |
| `ai_etf` | Proxy de robustesse | Mensuelle | ETF technologique mentionné par les auteurs | Instrument et transformation à vérifier |
| `vix` | Contrôle | Mensuelle | Moyenne mensuelle de l'indice VIX journalier | Confirmé dans une note de l'article |
| `inflation_us` | Contrôle | Mensuelle | Indicateur d'inflation US | Source / unité à vérifier |
| `risk_free` | Construction des primes | Mensuelle | Taux des Treasury bills US | Tenor / conversion à vérifier |
| `stock_return` | Intermédiaire | Mensuelle | Rendement des cours | Rendement simple vs logarithmique à vérifier |
| `risk_premium` | Variable dépendante | Mensuelle | Rendement moins taux sans risque | Compatibilité des unités à vérifier |
| `return_volatility` | Variable dépendante | Mensuelle | Volatilité des rendements | Méthode précise non établie |
| `stock_group` | Segmentation | Catégorielle | AI-related / conventional selon l'article | Reconstituer la composition historique |

**Aucune donnée réelle n'est fournie dans le dépôt initial.** Toutes les variables doivent être documentées avec source, unités, dates de disponibilité et convention de calcul avant la première estimation.
