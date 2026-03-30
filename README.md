# 📊 Economic Impact of the 2026 FIFA World Cup - USA

> **Predicting the economic impact of the 2026 FIFA World Cup hosted in the United States using multi-source data collection, advanced analytics, and machine learning.**

## Project Objectives

This project serves as a **comprehensive data science case study** demonstrating:
- **Multi-source data collection** (web scraping, APIs, public databases)
- **Data cleaning & fusion** (harmonizing disparate sources)
- **Exploratory Data Analysis** (EDA with statistical insights)
- **Feature engineering** (creating predictive variables)
- **Predictive modeling** (regression, ensemble methods)
- **Data visualization** (interactive dashboards & storytelling)

The goal is to deliver **data-driven insights** on the expected economic outcomes of hosting the 2026 World Cup in the USA.

---

##  Key Research Questions

| Question | Impact |
|----------|--------|
| **What will the total economic impact be?** | Revenue projections for the entire tournament |
| **Which regions will benefit most?** | Regional breakdown and city-level opportunities |
| **How many jobs will be created?** | Employment generation estimates |
| **What tourism revenue is expected?** | Hospitality, dining, entertainment spending |
| **How does it compare to previous tournaments?** | Benchmarking vs. 1998-2022 World Cups |

---

##  Project Structure

```
fifa-2026-economic-impact/
│
├── 📊 PROJECT_PLAN.md              # Detailed project plan & timeline
├── README.md                        # This file
├── requirements.txt                 # Python dependencies
│
├── 📂 data/
│   ├── raw/                        # Original datasets (CSV files)
│   │   ├── historical_world_cup_data.csv
│   │   ├── usa_2026_stadiums.csv
│   │   ├── usa_host_cities_demographics.csv
│   │   ├── usa_regional_economic_data.csv
│   │   ├── usa_tourism_baseline.csv
│   │   ├── ticket_revenue_history.csv
│   │   └── inflation_growth_data.csv
│   │
│   └── processed/                  # Cleaned & feature-engineered data
│       ├── historical_world_cup_data_cleaned.csv
│       ├── usa_2026_stadiums_enhanced.csv
│       ├── usa_host_cities_enhanced.csv
│       ├── usa_regional_economic_cleaned.csv
│       ├── usa_2026_baseline_metrics.csv
│       └── integrated_dataset.csv
│
├── 📂 src/                         # Source code & utilities
│   ├── 01_data_collection_eda.py           # Initial EDA (provided)
│   ├── 02_data_collection_comprehensive.py # Enhanced data collection
│   ├── 03_data_cleaning_integration.py     # Data cleaning pipeline
│   └── utils.py                            # Utility functions
│
├── 📂 notebooks/                   # Jupyter Notebooks (executable analysis)
│   ├── 01_data_exploration.ipynb           # Exploratory Data Analysis
│   ├── 02_eda_comparative_analysis.ipynb   # Comparative analysis (phase 2)
│   └── 03_predictive_models.ipynb          # Modeling & predictions (phase 3)
│
├── 📂 reports/                     # Final deliverables
│   └── IMPACT_ECONOMIQUE_COUPE_MONDE_2026.pdf (to be generated)
│
└── 📂 venv/                        # Python virtual environment
```

---

##  Getting Started

### Prerequisites
- Python 3.9+
- Git
- Jupyter Notebook or JupyterLab
- ~2 GB disk space

### Installation

1. **Clone the repository** (or navigate to project folder)
```bash
cd fifa-2026-economic-impact
```

2. **Create virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

### Quick Start

#### Option A: Run Python scripts (automated data processing)
```bash
# Generate comprehensive datasets
python src/02_data_collection_comprehensive.py

# Clean and integrate data
python src/03_data_cleaning_integration.py
```

#### Option B: Use Jupyter Notebooks (interactive analysis)
```bash
jupyter notebook
```
Then open your browser and navigate to the notebooks:
- `notebooks/01_data_exploration.ipynb` ← **Start here!**
- `notebooks/02_eda_comparative_analysis.ipynb` (phase 2)
- `notebooks/03_predictive_models.ipynb` (phase 3)

---

##  Data Sources

### 1. **Historical World Cup Data** (1998-2022)
- **Source**: FIFA, World Bank, National statistics offices
- **Variables**: Revenue, attendance, employment, tourism impact
- **Records**: 7 tournaments

### 2. **USA 2026 Host Cities & Stadiums**
- **Source**: FIFA official confirmation, stadium operators
- **Variables**: Capacity, location, accommodation, airport access
- **Records**: 12 stadiums, 12 host cities

### 3. **Demographic Data**
- **Source**: US Census Bureau, city tourism boards
- **Variables**: Population, GDP, income, hotels, visitors
- **Geographic scope**: All 12 World Cup host cities

### 4. **Regional Economic Data**
- **Source**: Bureau of Economic Analysis (BEA), Federal Reserve
- **Variables**: GDP by region, employment, hospitality revenue
- **Regions**: All states/regions hosting World Cup cities

### 5. **Historical Ticket & Revenue Data**
- **Source**: FIFA archives, academic publications
- **Variables**: Average ticket prices, attendance rates, revenue
- **Temporal**: 1998-2022 (adjusted to 2026 USD)

### 6. **Inflation & Growth Factors**
- **Source**: Bureau of Labor Statistics, US Federal Reserve
- **Variables**: CPI, GDP growth, USD exchange rates
- **Years**: 1998-2026 (with 2026 projections)

---

##  Key Metrics & Outputs

### Revenue Predictions
- **Total Economic Impact** (estimated)
- **Revenue Distribution** by source (tickets, tourism, infrastructure)
- **Regional Revenue** breakdown by city

### Employment Impact
- **Total Jobs Created** (temporary & permanent)
- **Sectoral Distribution** (hospitality, transportation, retail)
- **Wages & Income** projections

### Tourism Impact
- **Visitor Projections** (domestic & international)
- **Hotel Occupancy** rates
- **Tourism Revenue** (accommodation, dining, entertainment)
- **Duration of Stay** analysis

### Comparative Analysis
- **vs. Historical Average** (1998-2022)
- **vs. Most Similar Tournaments** (Brazil 2014, Russia 2018)
- **USA Advantages & Disadvantages**

---

##  Methodology Notes

### Assumptions
1. **Attendance**: 80% average stadium capacity (conservative)
2. **Economic Multiplier**: USA economy 1.25x historical average (developed economy)
3. **Inflation Adjustment**: 2018 baseline → 2026 CPI adjustment
4. **Tourism Increment**: 15% additional international visitors above baseline
5. **Employment**: Scaled from historical ratios based on tournament size

### Limitations
- Historical data limited to 7 tournaments (1998-2022)
- Qatar 2022 affected by unique circumstances (COVID, smaller country)
- Regional economic variations not perfectly predictable
- External shocks (economic recession, pandemic) not modeled

### Validation Strategy
- Train/test split (80/20) on historical data
- K-fold cross-validation (k=5)
- Sensitivity analysis for key assumptions
- Comparison with expert estimates

---

##  License & Attribution

This is an **independent analysis project** created for educational & analytical purposes. 

Data sources are publicly available:
- FIFA (official)
- World Bank
- US Census Bureau
- Bureau of Economic Analysis

---


