# Protocole de reproduction — version initiale

## Hypothèse générale

L'attention liée à l'intelligence artificielle, mesurée par les indicateurs Google Trends, pourrait prédire les primes de risque et la volatilité des actions américaines, avec des effets différents selon leur exposition à l'IA.

## Article de référence

- Salisu & Badmus (2026), DOI : 10.1007/s11135-026-02816-9.
- Échantillon publié : 2012M1–2024M12 ; 503 sociétés S&P 500 ; 26 sociétés AI-related.
- Explicatives : indicateurs AI News Search / AI Web Search, une proxy ETF, inflation et VIX.
- Cibles : prime de risque des rendements et volatilité de ces rendements.

## Équations publiées (notation adaptée)

Prime de risque :

```text
RP_t = a0 + a1 RP_(t-1) + a2 AInews_(t-1) + a3 Delta(AInews_t) + d Control_t + u_t
```

Volatilité :

```text
VOL_t = b0 + b1 VOL_(t-1) + b2 AInews_(t-1) + b3 Delta(AInews_t) + s Control_t + e_t
```

Les auteurs recourent à la démarche Westerlund–Narayan (FQGLS). La description de l'article ne constitue pas à elle seule du code d'estimation reproductible ; les pondérations, résidus, fenêtre de formation et séquence de prévision doivent être documentés avant toute implémentation.

## Questions bloquantes

1. Construisent-ils des indices équipondérés ou pondérés, et à quelle étape calculent-ils les rendements ?
2. Quelle formule précise pour `RetVol` (écart-type mobile, volatilité conditionnelle, etc.) ?
3. Quel instrument et quelle conversion mensuelle pour le taux sans risque ?
4. Quelle série exacte et unité pour l'inflation ?
5. Quels paramètres de téléchargement et ré-échantillonnage Google Trends ?
6. Comment reconstruire **sans fuite de données** le terme contemporain `Delta(AInews_t)` pour une vraie prévision ?
7. Quelle fenêtre d'estimation et quel schéma rolling/expanding ont été utilisés ?

L'article indique des horizons de trois, six et douze mois et compare les performances à une moyenne historique ainsi qu'à une marche aléatoire, via RMSE relatif et test Clark–West. Il ne faut pas en déduire une procédure pratique non décrite.

## Niveaux de preuve dans nos livrables

- **Publié** : chiffre ou estimation reproduit textuellement de l'article, attribué aux auteurs.
- **Reproduit** : calcul obtenu à partir de données et du script traçables.
- **Adapté** : spécification modifiée pour indisponibilité de données, explicitement signalée.
- **Extension** : nouvelle hypothèse ou nouvelle source, séparée de l'étude originale.

L'extension NLP/agent est **hors périmètre du livrable 3**, pour éviter de mélanger réplication et contribution nouvelle.
