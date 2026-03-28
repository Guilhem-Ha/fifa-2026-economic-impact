"""
FIFA 2026 World Cup - Economic Impact Prediction
Phase 1: Data Collection & Exploratory Data Analysis
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

print("=" * 80)
print("FIFA 2026 WORLD CUP - ECONOMIC IMPACT ANALYSIS")
print("=" * 80)

# Historical World Cup Data (1998-2022)
world_cup_data = {
    'Year': [1998, 2002, 2006, 2010, 2014, 2018, 2022],
    'Host_Country': ['France', 'South Korea', 'Germany', 'South Africa', 'Brazil', 'Russia', 'Qatar'],
    'Host_Region': ['Europe', 'Asia', 'Europe', 'Africa', 'South America', 'Europe', 'Asia'],
    'Total_Attendance': [2785100, 2705197, 3359439, 3178856, 3429873, 3031768, 3404252],
    'Average_Attendance': [43517, 42269, 52491, 49669, 53591, 47372, 53191],
    'Revenue_Millions_USD': [600, 1400, 3600, 3600, 15000, 6100, 220],
    'Host_GDP_Billions_USD': [1500, 600, 3700, 370, 1840, 1660, 250],
    'Host_Population_Millions': [60, 48, 82, 50, 203, 146, 3],
    'Developed_Economy': [True, False, True, False, False, True, False]
}

df = pd.DataFrame(world_cup_data)

print("\n1. HISTORICAL WORLD CUP DATA:")
print(df)

# Statistics
print("\n2. DESCRIPTIVE STATISTICS:")
print(df[['Revenue_Millions_USD', 'Total_Attendance']].describe())

# Correlation
print("\n3. CORRELATION ANALYSIS:")
numerical_cols = ['Total_Attendance', 'Revenue_Millions_USD', 'Host_GDP_Billions_USD', 'Host_Population_Millions']
corr = df[numerical_cols].corr()
print(corr)

# Development Status Analysis
developed = df[df['Developed_Economy'] == True]
developing = df[df['Developed_Economy'] == False]

print("\n4. DEVELOPED vs DEVELOPING:")
print(f"Developed - Avg Revenue: ${developed['Revenue_Millions_USD'].mean():.0f}M")
print(f"Developing - Avg Revenue: ${developing['Revenue_Millions_USD'].mean():.0f}M")

# Save
df.to_csv('data/processed/historical_world_cup_data.csv', index=False)
print("\n✓ Data saved!")