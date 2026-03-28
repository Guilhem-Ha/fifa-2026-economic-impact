# 📊 Plan du Projet : Prédiction Retombées Économiques - Coupe du Monde 2026 USA

## 📋 Vue d'ensemble

**Objectif Principal**: Prédire précisément l'impact économique de la Coupe du Monde 2026 aux États-Unis en utilisant des données historiques, des indicateurs régionaux et des modèles prédictifs.

**Horizon Temporel**: 28 mars 2026

## ❓ Questions Clés à Répondre

1. **Impact Économique Total**: Quel sera le revenu économique brut estimé ?
2. **Distribution Géographique**: Quelles villes/régions profiteront le plus ?
3. **Emploi**: Combien d'emplois temporaires et permanents créés ?
4. **Tourisme**: Quel revenu touristique prévisible (nuitées hôtel, restauration, loisirs) ?
5. **Comparaison Historique**: Comment se compare avec les Coupes précédentes (1998-2022) ?

---

## 📊 PHASE 1 : COLLECTE DE DONNÉES (Week 1-2)

### 1.1 Données Historiques des Coupes du Monde (1998-2022)
**Sources**: FIFA, Rapports gouvernementaux, Bases de données publiques
- [ ] Revenus bruts par tournoi
- [ ] Fréquentation totale et moyenne
- [ ] Nombre d'emplois créés
- [ ] Impact sur le PIB du pays hôte
- [ ] Dépenses touristiques internationales
- [ ] Durée moyenne du tournoi
- [ ] Nombre de matches joués

**Fichier de sortie**: `data/raw/historical_world_cup_economics.csv`

### 1.2 Capacités des Stades USA 2026
**Sources**: Fédérations de football américaines, Données officielles FIFA
- [ ] Liste complète des 12 stades (confirmed: MetLife, Arrowhead, AT&T, SoFi, Allegiant, etc.)
- [ ] Capacité maximale de chaque stade
- [ ] Localisation (ville, état)
- [ ] Infractions /infrastructure disponibles
- [ ] Routes d'accès et transport public

**Fichier de sortie**: `data/raw/usa_2026_stadiums.csv`

### 1.3 Données Démographiques des Villes Hôtes
**Sources**: US Census Bureau, databases municipales
- [ ] Population par ville
- [ ] Densité urbaine
- [ ] Revenu moyen par habitant
- [ ] Taux d'emploi local
- [ ] Nombre d'hôtels et capacité d'accueil
- [ ] Attractions touristiques principales
- [ ] Accessibilité aéroportuaire

**Fichier de sortie**: `data/raw/usa_host_cities_demographics.csv`

### 1.4 Données Touristiques USA (Baseline Actuellement)
**Sources**: U.S. Travel Association, Tourism Boards, Airbnb, Bureau of Economic Analysis
- [ ] Flux touristique annuel moyen par région
- [ ] Dépenses touristiques moyennes (hôtel, nourriture, attractions)
- [ ] Pics saisonniers d'in tourisme
- [ ] Durée moyenne de séjour
- [ ] Taux d'occupation hôtels

**Fichier de sortie**: `data/raw/usa_tourism_baseline.csv`

### 1.5 Données Économiques USA par Région
**Sources**: Bureau of Economic Analysis (BEA), Federal Reserve
- [ ] PIB par État et Métropole
- [ ] Secteur hébergement/restauration/loisirs
- [ ] Multiplicateurs économiques régionaux
- [ ] Salaire moyen secteur touristique

**Fichier de sortie**: `data/raw/usa_regional_economic_data.csv`

### 1.6 Historique des Revenus de Billetterie
**Sources**: FIFA, Études académiques
- [ ] Prix moyen des billets (passé vs 2026 prévisions)
- [ ] Distribution des prix (phases de groupe vs finales)
- [ ] Taux d'occupation moyen
- [ ] Patterns de ventes historiques

**Fichier de sortie**: `data/raw/ticket_revenue_history.csv`

### 1.7 Données d'Inflation & Croissance Économique
**Sources**: BLS (Bureau of Labor Statistics), FED, IMF
- [ ] Taux d'inflation historique (1998-2026)
- [ ] Croissance du PIB US (1998-2026)
- [ ] Taux de change USD
- [ ] Prévisions économiques 2026

**Fichier de sortie**: `data/raw/inflation_growth_data.csv`

---

## 🔧 PHASE 2 : NETTOYAGE & FUSION DE DONNÉES (Week 3)

### 2.1 Data Cleaning
- [ ] Traiter les valeurs manquantes
- [ ] Détecter et gérer les outliers
- [ ] Normaliser les monnaies (inflation adjustment)
- [ ] Valider la cohérence des données
- [ ] Documenter toutes les transformations

### 2.2 Feature Engineering
- [ ] Calcul des multiplicateurs économiques par région
- [ ] Ratio revenus/population
- [ ] Indice de développement touristique par ville
- [ ] Estimation de la capacité d'accueil totale
- [ ] Facteurs géographiques (climat, saisonnalité)

### 2.3 Data Integration
- [ ] Fusion des datasets multi-sources
- [ ] Création d'une base de données maître (`processed/`)
- [ ] Documentation des jointures et transformations

**Fichier de sortie**: `data/processed/integrated_dataset.csv`

---

## 📈 PHASE 3 : ANALYSE EXPLORATOIRE (Week 4)

### 3.1 EDA & Visualisations
- [ ] Distribution des revenus historiques
- [ ] Corrélations entre variables clés
- [ ] Analyse par niveau de développement économique du pays hôte
- [ ] Trends temporelles
- [ ] Analyse régionale USA (potentiel par ville)

### 3.2 Comparative Analysis
- [ ] Benchmarking: USA 2026 vs pays hôtes précédents
- [ ] Facteurs favorables/défavorables pour USA
- [ ] Impact des capacités stade sur revenus
- [ ] Patterns des attentes touristiques

**Notebook de sortie**: `notebooks/02_eda_comparative_analysis.ipynb`

---

## 🤖 PHASE 4 : MODÉLISATION PRÉDICTIVE (Week 5)

### 4.1 Modèles de Régression Multivariée
**Variables d'entrée**:
- Capacité totale des stades
- Population des villes hôtes
- PIB régional
- Infrastructure touristique existante
- Multiplicateurs économiques historiques
- Facteurs macro-économiques (inflation, croissance)

**Modèles à tester**:
1. **Linear Regression**: Baseline simple
2. **Ridge/Lasso Regression**: Régularisation
3. **Random Forest**: Relations non-linéaires
4. **XGBoost/LightGBM**: Optimisation avancée
5. **Ensemble Methods**: Moyenne pondérée

### 4.2 Validation & Evaluation
- [ ] Train/test split (80/20)
- [ ] Cross-validation (k-fold, n=5)
- [ ] Métriques: R², RMSE, MAE
- [ ] Analyse de sensibilité
- [ ] Tests de résidu

### 4.3 Prédictions Finales
**Outputs**:
- [ ] Revenu économique total estimé
- [ ] Répartition par région/ville
- [ ] Estimation d'emplois créés
- [ ] Revenus touristiques stratifiés
- [ ] Intervalles de confiance (95%)
- [ ] Scénarios sensibilité (optimiste/pessimiste)

**Notebook de sortie**: `notebooks/03_predictive_models.ipynb`

---

## 📊 PHASE 5 : VISUALIZATION & STORYTELLING (Week 6)

### 5.1 Visualisations Convaincantes
- [ ] Dashboard interactif (Plotly/Dash)
- [ ] Cartes géographiques USA avec impact par région
- [ ] Graphiques comparatifs historiques
- [ ] Sankey diagram d'allocation des revenus
- [ ] Evolution temporelle des impacts (jour par jour du tournoi)

### 5.2 Rapport Final
- [ ] Executive summary (1 page)
- [ ] Méthodologie détaillée
- [ ] Résultats principaux
- [ ] Recommandations pour les stakeholders
- [ ] Limitations et risques

**Fichier de sortie**: `reports/IMPACT_ECONOMIQUE_COUPE_MONDE_2026.pdf`

---

## 📁 Architecture des Fichiers

```
fifa-2026-economic-impact/
├── data/
│   ├── raw/                           # Données brutes
│   │   ├── historical_world_cup_economics.csv
│   │   ├── usa_2026_stadiums.csv
│   │   ├── usa_host_cities_demographics.csv
│   │   ├── usa_tourism_baseline.csv
│   │   ├── usa_regional_economic_data.csv
│   │   ├── ticket_revenue_history.csv
│   │   └── inflation_growth_data.csv
│   └── processed/                     # Données traitées
│       ├── historical_world_cup_data.csv
│       └── integrated_dataset.csv
│
├── src/
│   ├── 01_data_collection_eda.py      # EDA partie 1
│   ├── 02_data_cleaning.py            # Nettoyage & fusion
│   ├── 03_feature_engineering.py      # Feature creation
│   └── utils.py                       # Fonctions utilitaires
│
├── notebooks/
│   ├── 01_data_exploration.ipynb      # Exploration initiale
│   ├── 02_eda_comparative.ipynb       # EDA comparative
│   └── 03_predictive_models.ipynb     # Modélisation & résultats
│
├── reports/
│   └── IMPACT_ECONOMIQUE_COUPE_MONDE_2026.pdf
│
├── PROJECT_PLAN.md                    # Ce fichier
└── requirements.txt                   # Dépendances
```

---

## 🎯 Compétences Démontrées

✅ **Collecte de données multi-sources** - Web scraping, API, bases publiques
✅ **Nettoyage et fusion de datasets** - Harmonisation, validation, transformation
✅ **Analyse comparative** - Historique vs prédictions, benchmarking
✅ **Régression multivariée** - Ensemble methods, validation robuste
✅ **Visualisations convaincantes** - Dashboards interactifs, mappages géographiques
✅ **Storytelling data** - Narratif clair, recommandations actionables

---

## 📅 Timeline Estimée
- **Week 1-2**: Collecte complète de données
- **Week 3**: Nettoyage et fusion
- **Week 4**: EDA et analyse comparative
- **Week 5**: Modélisation et prédictions
- **Week 6**: Visualisations et rapport final

**État**: En cours → Initié 28 mars 2026
