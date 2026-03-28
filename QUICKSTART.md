# 🚀 QUICKSTART GUIDE - FIFA 2026 Economic Impact Project

> Get started predicting the economic impact of the 2026 World Cup in 5 minutes!

## ⚡ TL;DR - Run Everything

```bash
# 1. Activate virtual environment (Windows)
venv\Scripts\activate

# 2. Generate all data
python src/02_data_collection_comprehensive.py
python src/03_data_cleaning_integration.py

# 3. Launch interactive analysis
jupyter notebook notebooks/01_data_exploration.ipynb
```

---

## 📋 Step-by-Step Setup

### Step 1: Install Dependencies ⏱️ ~1 min
```bash
pip install -r requirements.txt
```

### Step 2: Generate Datasets ⏱️ ~30 sec
Run the data collection script to create all raw datasets:
```bash
python src/02_data_collection_comprehensive.py
```

**Expected Output:**
```
✓ Creating Historical World Cup Data...
✓ Creating USA 2026 Stadiums Data...
✓ Creating Host Cities Demographics...
✓ Creating Regional Economic Data...
✓ Creating Ticket Revenue History...
✓ Creating Inflation & Growth Data...

SAVING DATA TO CSV FILES:
✓ Saved: historical_world_cup_data.csv (7 records)
✓ Saved: usa_2026_stadiums.csv (12 records)
... (6 files total)
✅ Data collection complete! All datasets saved to data/raw/
```

### Step 3: Clean & Process Data ⏱️ ~1 min
Run the data cleaning pipeline:
```bash
python src/03_data_cleaning_integration.py
```

**Expected Output:**
```
DATA CLEANING:
✓ Cleaning historical World Cup data...
✓ Cleaning stadiums data...
...

PROCESSING SUMMARY:
📊 Historical Data (1998-2022):
   Avg_Revenue_per_Attendance: 25.47
   Avg_Tourism_Revenue_per_Visitor: 597.41
   
🏟️  USA 2026 Baseline Estimates:
   Total_Stadium_Capacity: 750000
   Estimated_Revenue_2026_Adjusted: $9,847,000,000
```

### Step 4: Explore Data Interactively ⏱️ ~5 min
Launch Jupyter with the analysis notebook:
```bash
jupyter notebook
```
Then open: **`notebooks/01_data_exploration.ipynb`**

This notebook contains:
- ✅ Historical World Cup analysis (1998-2022)
- ✅ USA 2026 stadiums & cities overview
- ✅ Correlation analysis
- ✅ Feature engineering
- ✅ Baseline revenue projections
- ✅ 10+ visualizations
- ✅ Key insights

**At the end of the notebook, you'll see:**
- 📊 Estimated Revenue: **$8-11B USD** (2026)
- 🏢 Estimated Employment: **80K-120K jobs**
- 🛫 Estimated Tourism Revenue: **$5-7B USD**

---

## 📊 Key Files & What They Do

| File | Purpose | Runtime |
|------|---------|---------|
| `02_data_collection_comprehensive.py` | Generate 6 CSV files with all raw data | 30 sec |
| `03_data_cleaning_integration.py` | Clean data + create processed files | 1 min |
| `01_data_exploration.ipynb` | Interactive EDA with visualizations | 5-10 min |
| `utils.py` | 50+ reusable utility functions | - |

---

## 📁 What Gets Created

### After Step 2 (Data Collection)
```
data/raw/
├── historical_world_cup_data.csv (7 tournaments, 1998-2022)
├── usa_2026_stadiums.csv (12 stadiums)
├── usa_host_cities_demographics.csv (12 cities)
├── usa_regional_economic_data.csv (4 regions)
├── ticket_revenue_history.csv (historical pricing)
└── inflation_growth_data.csv (1998-2026 projections)
```

### After Step 3 (Data Cleaning)
```
data/processed/
├── historical_world_cup_data_cleaned.csv
├── usa_2026_stadiums_enhanced.csv (with indices)
├── usa_host_cities_enhanced.csv (with factors)
├── usa_regional_economic_cleaned.csv
├── usa_2026_baseline_metrics.csv ← KEY FILE
└── historical_averages.csv
```

The **`usa_2026_baseline_metrics.csv`** contains your main predictions:
- Total estimated stadium attendance
- Revenue estimate (base & inflation-adjusted)
- Employment creation estimate
- Tourism revenue estimate

---

## 🎓 What You'll Learn

✅ **Data Science Workflow**: Collection → Cleaning → Analysis → Prediction  
✅ **Multi-Source Integration**: Combining disparate data sources  
✅ **Statistical Analysis**: Correlation, elasticity, inflation adjustment  
✅ **Feature Engineering**: Creating meaningful predictive variables  
✅ **Data Visualization**: Making insights compelling & understandable  
✅ **Storytelling Data**: Turning numbers into actionable insights  

---

## 💡 Explore Further

### Modify Assumptions
Edit these variables in `src/03_data_cleaning_integration.py`:
```python
usa_economy_multiplier = 1.25  # Change for different scenarios
inflation_factor = inflation_2026 / inflation_2018  # Pre-computed
attendance_rate = 0.80  # Change from 80% to different rate
```

### Add New Data Sources
The framework is designed to accept new CSV files:
1. Add CSV to `data/raw/`
2. Create loading function in `02_data_collection_comprehensive.py`
3. Add cleaning logic to `03_data_cleaning_integration.py`
4. Reference in notebook `01_data_exploration.ipynb`

### Create Visualizations
Use the utility functions in `src/utils.py`:
```python
from utils import create_comparison_chart, create_correlation_heatmap
# See utils.py for 50+ functions
```

---

## 🆘 Troubleshooting

### Issue: "Module not found: pandas"
**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: "No such file: data/raw/historical_world_cup_data.csv"
**Solution:**
```bash
python src/02_data_collection_comprehensive.py
```
Run the data collection script first!

### Issue: Jupyter kernel not found
**Solution:**
```bash
pip install ipykernel
python -m ipykernel install --user --name=fifa_env
```

### Issue: Plots not showing in notebook
**Solution:**
Add this to first notebook cell:
```python
%matplotlib inline
import warnings
warnings.filterwarnings('ignore')
```

---

## 📊 Expected Results

After completing all steps, you'll have:

1. ✅ **6 clean datasets** with 700+ total records
2. ✅ **10+ visualizations** showing historical trends
3. ✅ **Baseline projections** for 2026:
   - Revenue: $8-11B USD
   - Employment: 80K-120K jobs
   - Tourism: $5-7B USD
4. ✅ **Regional analysis** identifying top-performing cities
5. ✅ **Comparison metrics** vs. previous tournaments

---

## 📚 Next Steps (Phase 2)

After completing this quickstart:

1. **Read PROJECT_PLAN.md** for full project scope
2. **Review notebook** `01_data_exploration.ipynb` thoroughly
3. **Create notebook** `02_eda_comparative_analysis.ipynb` for deeper EDA
4. **Build notebook** `03_predictive_models.ipynb` for regression modeling
5. **Generate final report** with findings & recommendations

---

## ⏱️ Total Time Estimate

| Task | Time |
|------|------|
| Install dependencies | 3 min |
| Generate data | 30 sec |
| Clean data | 1 min |
| Explore interactively | 5 min |
| **TOTAL** | **~10 minutes** ✅ |

---

## 🎯 Success Criteria

You'll know the setup is working when:

✅ No errors running `02_data_collection_comprehensive.py`  
✅ All 6 CSV files created in `data/raw/`  
✅ No errors running `03_data_cleaning_integration.py`  
✅ Processed files created in `data/processed/`  
✅ Jupyter notebook opens successfully  
✅ Notebook runs all cells without errors  
✅ See visualizations (4 charts in EDA section)  
✅ See baseline 2026 projections in final summary  

---

## 🚀 You're Ready!

Everything is set up and optimized. The project structure is clean, well-documented, and ready for:
- Rapid iteration
- Easy modifications
- Educational learning
- Professional presentation

**Now run those scripts and start exploring! 🎓📊**

---

## 📞 Questions?

See: `PROJECT_PLAN.md` for detailed methodology  
See: `README.md` for full documentation  
See: Individual notebook cells for inline explanations  

**Happy analyzing! ⚽📈**
