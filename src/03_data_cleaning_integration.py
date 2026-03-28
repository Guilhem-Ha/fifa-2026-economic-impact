"""
FIFA 2026 World Cup - Economic Impact Prediction
Phase 2: Data Cleaning & Integration
"""

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# DATA CLEANING FUNCTIONS
# ============================================================================

def clean_historical_world_cup_data(df):
    """
    Clean and validate historical World Cup data
    """
    print("Cleaning historical World Cup data...")
    
    # Check for missing values
    if df.isnull().sum().sum() > 0:
        print(f"  ⚠️  Found {df.isnull().sum().sum()} missing values - handling...")
        df = df.fillna(df.mean(numeric_only=True))
    
    # Ensure correct data types
    df['Year'] = df['Year'].astype(int)
    df['Total_Attendance'] = df['Total_Attendance'].astype(int)
    df['Revenue_Millions_USD'] = df['Revenue_Millions_USD'].astype(float)
    
    # Validate ranges
    assert df['Revenue_Millions_USD'].min() > 0, "Revenue should be positive"
    assert df['Total_Attendance'].min() > 0, "Attendance should be positive"
    
    # Remove outliers (using IQR method)
    for col in ['Revenue_Millions_USD', 'Total_Attendance']:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        df = df[(df[col] >= Q1 - 1.5*IQR) & (df[col] <= Q3 + 1.5*IQR)]
    
    print(f"  ✓ Cleaned {len(df)} records")
    return df

def clean_stadiums_data(df):
    """
    Clean and validate stadiums data
    """
    print("Cleaning stadiums data...")
    
    # Ensure correct data types
    df['Capacity'] = df['Capacity'].astype(int)
    df['Hotel_Capacity_5000'] = df['Hotel_Capacity_5000'].astype(int)
    
    # Validate capacity ranges
    assert df['Capacity'].min() > 20000, "Stadium capacity should be > 20k"
    assert df['Capacity'].max() < 100000, "Stadium capacity should be < 100k"
    
    # Check for duplicates
    if df.duplicated(subset=['Stadium_Name']).sum() > 0:
        print(f"  ⚠️  Found duplicates - removing...")
        df = df.drop_duplicates(subset=['Stadium_Name'])
    
    print(f"  ✓ Cleaned {len(df)} stadiums")
    return df

def clean_cities_demographics(df):
    """
    Clean cities demographic data
    """
    print("Cleaning cities demographics...")
    
    # Handle missing values
    df = df.fillna(df.mean(numeric_only=True))
    
    # Ensure positive values
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        df[col] = df[col].abs()
    
    # Validate ranges
    assert df['Urban_Population_Millions'].min() > 0
    assert df['Annual_International_Visitors_Millions'].min() >= 0
    
    print(f"  ✓ Cleaned {len(df)} cities")
    return df

def clean_regional_economic_data(df):
    """
    Clean regional economic data
    """
    print("Cleaning regional economic data...")
    
    # Ensure correct data types
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        df[col] = df[col].astype(float)
    
    # Validate unemployment rate (0-10%)
    df['Unemployment_Rate_Percent'] = df['Unemployment_Rate_Percent'].clip(0, 10)
    
    print(f"  ✓ Cleaned {len(df)} regions")
    return df

# ============================================================================
# FEATURE ENGINEERING
# ============================================================================

def create_aggregate_features(stadiums, cities):
    """
    Create aggregate features for prediction
    """
    print("\nCreating aggregate features...")
    
    features = {
        'Total_Stadium_Capacity': [stadiums['Capacity'].sum()],
        'Avg_Stadium_Capacity': [stadiums['Capacity'].mean()],
        'Total_Hotel_Rooms': [stadiums['Hotel_Capacity_5000'].sum() * 5000],
        'Total_Host_Population_Millions': [cities['Urban_Population_Millions'].sum()],
        'Total_Host_GDP_Billions_USD': [cities['Metropolitan_GDP_Billions_USD'].sum()],
        'Avg_Tourism_Potential_Index': [cities['Tourism_Potential_Index'].mean()],
        'Total_Annual_International_Visitors_Millions': [cities['Annual_International_Visitors_Millions'].sum()],
        'Avg_Hotel_Count': [cities['Urban_Population_Millions'].sum()] # Hotels per capita metric
    }
    
    return pd.DataFrame(features)

def create_city_level_factors(cities):
    """
    Create city-level economic factors for regional impact predictions
    """
    print("Creating city-level impact factors...")
    
    cities['Economic_Impact_Factor'] = (
        (cities['Tourism_Potential_Index'] * 0.3) +
        (cities['Economic_Capacity_Index'] * 0.3) +
        (cities['Accommodation_Quality_Index'] * 0.4)
    )
    
    cities['Revenue_Potential_Estimate'] = (
        cities['Economic_Impact_Factor'] * 
        cities['Annual_International_Visitors_Millions'] * 
        0.15  # Incremental revenue from World Cup (15% additional)
    )
    
    return cities

def create_stadium_impact_factors(stadiums):
    """
    Create stadium-level impact estimates
    """
    print("Creating stadium-level impact factors...")
    
    # Normalize capacity to 0-1 scale
    stadiums['Capacity_Normalized'] = (
        (stadiums['Capacity'] - stadiums['Capacity'].min()) /
        (stadiums['Capacity'].max() - stadiums['Capacity'].min())
    )
    
    # Impact factor based on capacity and accommodation
    stadiums['Local_Impact_Factor'] = (
        stadiums['Capacity_Normalized'] * 0.5 +
        (stadiums['Accommodation_Index'] / stadiums['Accommodation_Index'].max()) * 0.5
    )
    
    return stadiums

# ============================================================================
# DATA INTEGRATION
# ============================================================================

def integrate_datasets(historical_wc, stadiums, cities, regional, tickets, inflation):
    """
    Integrate all datasets into a master dataframe
    """
    print("\n" + "="*70)
    print("INTEGRATING DATASETS")
    print("="*70)
    
    # 1. Calculate average metrics from historical data
    historical_avg = {
        'Avg_Revenue_per_Attendance': historical_wc['Revenue_per_Attendee'].mean(),
        'Avg_Revenue_per_GDP_Pct': historical_wc['Revenue_per_GDP_Percent'].mean(),
        'Avg_Visitors_per_Capita': historical_wc['Visitors_per_Capita'].mean(),
        'Avg_Tourism_Revenue_per_Visitor': historical_wc['Tourism_Revenue_per_Visitor'].mean(),
        'Avg_Employment_Created': historical_wc['Employment_Created'].mean(),
        'Avg_Infra_Investment': historical_wc['Infrastructure_Investment_Billions_USD'].mean(),
    }
    
    # 2. Calculate USA 2026 specific metrics
    usa_2026_metrics = create_aggregate_features(stadiums, cities)
    
    # 3. Adjust 2026 predictions based on historical patterns
    # Assumption: USA is developed, high GDP, high tourism baseline
    usa_2026_metrics['Estimated_Visitors_2026'] = usa_2026_metrics['Total_Host_Population_Millions'].iloc[0] * historical_avg['Avg_Visitors_per_Capita']
    
    usa_2026_metrics['Estimated_Revenue_2026_Millions_USD'] = (
        usa_2026_metrics['Estimated_Visitors_2026'].iloc[0] * 
        historical_avg['Avg_Tourism_Revenue_per_Visitor']
    )
    
    usa_2026_metrics['Estimated_Employment_2026'] = (
        usa_2026_metrics['Total_Stadium_Capacity'].iloc[0] / 50000 * 
        historical_avg['Avg_Employment_Created']
    )
    
    # 4. Inflation adjustment (2018 baseline to 2026)
    inflation_2026 = inflation[inflation['Year'] == 2026]['USA_CPI_Index'].values[0]
    inflation_2018 = inflation[inflation['Year'] == 2018]['USA_CPI_Index'].values[0]
    inflation_factor = inflation_2026 / inflation_2018
    
    usa_2026_metrics['Estimated_Revenue_2026_Adjusted'] = (
        usa_2026_metrics['Estimated_Revenue_2026_Millions_USD'] * inflation_factor
    )
    
    print(f"\n✓ Integration complete")
    print(f"  - Inflation adjustment factor: {inflation_factor:.2f}x")
    print(f"  - Base 2026 revenue estimate: ${usa_2026_metrics['Estimated_Revenue_2026_Millions_USD'].iloc[0]:,.0f}M")
    print(f"  - Inflation-adjusted estimate: ${usa_2026_metrics['Estimated_Revenue_2026_Adjusted'].iloc[0]:,.0f}M")
    
    return usa_2026_metrics, historical_avg

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    
    print("\n" + "=" * 90)
    print("FIFA 2026 WORLD CUP - DATA CLEANING & INTEGRATION")
    print("=" * 90)
    
    # Load datasets
    print("\nLoading datasets...")
    historical_wc = pd.read_csv('data/raw/historical_world_cup_data.csv')
    stadiums = pd.read_csv('data/raw/usa_2026_stadiums.csv')
    cities = pd.read_csv('data/raw/usa_host_cities_demographics.csv')
    regional_econ = pd.read_csv('data/raw/usa_regional_economic_data.csv')
    tickets = pd.read_csv('data/raw/ticket_revenue_history.csv')
    inflation = pd.read_csv('data/raw/inflation_growth_data.csv')
    print("✓ All datasets loaded")
    
    # Clean all datasets
    print("\n" + "=" * 90)
    print("DATA CLEANING")
    print("=" * 90)
    
    historical_wc = clean_historical_world_cup_data(historical_wc)
    stadiums = clean_stadiums_data(stadiums)
    cities = clean_cities_demographics(cities)
    regional_econ = clean_regional_economic_data(regional_econ)
    
    # Feature engineering
    print("\n" + "=" * 90)
    print("FEATURE ENGINEERING")
    print("=" * 90)
    
    cities = create_city_level_factors(cities)
    stadiums = create_stadium_impact_factors(stadiums)
    
    # Data integration
    usa_2026_metrics, historical_avg = integrate_datasets(
        historical_wc, stadiums, cities, regional_econ, tickets, inflation
    )
    
    # Save processed datasets
    print("\n" + "=" * 90)
    print("SAVING PROCESSED DATA")
    print("=" * 90)
    
    # Save cleaned and enhanced datasets
    historical_wc.to_csv('data/processed/historical_world_cup_data_cleaned.csv', index=False)
    print("✓ Saved: historical_world_cup_data_cleaned.csv")
    
    stadiums.to_csv('data/processed/usa_2026_stadiums_enhanced.csv', index=False)
    print("✓ Saved: usa_2026_stadiums_enhanced.csv")
    
    cities.to_csv('data/processed/usa_host_cities_enhanced.csv', index=False)
    print("✓ Saved: usa_host_cities_enhanced.csv")
    
    regional_econ.to_csv('data/processed/usa_regional_economic_cleaned.csv', index=False)
    print("✓ Saved: usa_regional_economic_cleaned.csv")
    
    # Save integration results
    usa_2026_metrics.to_csv('data/processed/usa_2026_baseline_metrics.csv', index=False)
    print("✓ Saved: usa_2026_baseline_metrics.csv")
    
    # Save historical averages for reference
    pd.DataFrame([historical_avg]).to_csv('data/processed/historical_averages.csv', index=False)
    print("✓ Saved: historical_averages.csv")
    
    # Display summary
    print("\n" + "=" * 90)
    print("PROCESSING SUMMARY")
    print("=" * 90)
    
    print(f"\n📊 Historical Data (1998-2022):")
    for key, value in historical_avg.items():
        print(f"   {key}: {value:.2f}")
    
    print(f"\n🏟️  USA 2026 Baseline Estimates:")
    for col in usa_2026_metrics.columns:
        if 'Total' in col or '2026' in col:
            print(f"   {col}: {usa_2026_metrics[col].values[0]:,.0f}")
    
    print("\n✅ Data processing complete! Ready for exploratory analysis.")
