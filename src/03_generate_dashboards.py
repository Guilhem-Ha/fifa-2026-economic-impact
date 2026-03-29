import os
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# Setup directories
os.makedirs('data/processed', exist_ok=True)

print("="*80)
print("📊 Phase 4: Visualizations & Dashboards - Generation")
print("="*80)

# Load data
historical_wc = pd.read_csv('data/raw/historical_world_cup_data.csv')
cities = pd.read_csv('data/raw/usa_host_cities_demographics.csv')
stadiums = pd.read_csv('data/raw/usa_2026_stadiums.csv')

# Merge cities and stadiums for comprehensive info
merged_cities = cities.merge(stadiums, on='City', how='inner')

# Add mock calculated impact data (from Phase 3 base case)
total_base_revenue = 7621.0
total_jobs = 2286346

# Distribute based on Metropolitan GDP and Capacity
merged_cities['Impact_Weight'] = np.log(merged_cities['Metropolitan_GDP_Billions_USD']) * merged_cities['Capacity']
merged_cities['Weight_Normalized'] = merged_cities['Impact_Weight'] / merged_cities['Impact_Weight'].sum()

merged_cities['Estimated_Revenue_Millions'] = merged_cities['Weight_Normalized'] * total_base_revenue
merged_cities['Estimated_Jobs'] = merged_cities['Weight_Normalized'] * total_jobs

# 1. Timeline (Interactive)
historical_sorted = historical_wc.sort_values('Year')
fig_time = make_subplots(
    rows=2, cols=1,
    subplot_titles=('World Cup Revenue Over Time', 'Total Attendance Over Time'),
    vertical_spacing=0.12
)

fig_time.add_trace(go.Scatter(x=historical_sorted['Year'], y=historical_sorted['Revenue_Millions_USD'],
                   mode='lines+markers', name='Historical Revenue', line=dict(color='#1f77b4', width=3)), row=1, col=1)
fig_time.add_trace(go.Scatter(x=[2026], y=[total_base_revenue], mode='markers', name='2026 Projection',
                   marker=dict(size=12, color='#ff7f0e', symbol='star')), row=1, col=1)

fig_time.add_trace(go.Scatter(x=historical_sorted['Year'], y=historical_sorted['Total_Attendance'],
                   mode='lines+markers', name='Historical Attendance', line=dict(color='#2ca02c', width=3)), row=2, col=1)
fig_time.add_trace(go.Scatter(x=[2026], y=[670269], mode='markers', name='2026 Projection',
                   marker=dict(size=12, color='#ff7f0e', symbol='star')), row=2, col=1)

fig_time.update_layout(title='Historical & Projected World Cup Metrics', height=700, template='plotly_white')
fig_time.write_html('data/processed/01_historical_timeline.html')
print("✅ Dashboard 1 saved: 01_historical_timeline.html")

# 2. Top Cities Comparison
top_cities = merged_cities.nlargest(10, 'Estimated_Revenue_Millions')
fig_top = go.Figure()
fig_top.add_trace(go.Bar(x=top_cities['City'], y=top_cities['Estimated_Revenue_Millions'], 
                         name='Revenue ($M)', marker_color='#1f77b4', yaxis='y1'))
fig_top.add_trace(go.Bar(x=top_cities['City'], y=top_cities['Estimated_Jobs']/1000, 
                         name='Jobs (k)', marker_color='#2ca02c', yaxis='y2'))

fig_top.update_layout(
    title='Top 10 Host Cities: Projected Economic Impact',
    yaxis=dict(title='Revenue (Million USD)', side='left'),
    yaxis2=dict(title='Jobs Created (Thousands)', overlaying='y', side='right'),
    height=500, template='plotly_white', barmode='group'
)
fig_top.write_html('data/processed/02_top_cities_comparison.html')
print("✅ Dashboard 2 saved: 02_top_cities_comparison.html")

# 3. Scenario Analysis
scenarios_df = pd.DataFrame({
    'Scenario': ['Pessimistic', 'Conservative', 'Base Case', 'Optimistic', 'Very Optimistic'],
    'Revenue_M': [7240, 7621, 7621, 8002, 8231],
    'Attendance': [586485, 628377, 670269, 712161, 754052],
    'Visitors_M': [32.0, 38.4, 48.0, 57.6, 64.0]
})

fig_scen = make_subplots(rows=1, cols=3, subplot_titles=('Revenue', 'Attendance', 'Visitors'))
colors = ['#d62728', '#ff7f0e', '#1f77b4', '#2ca02c', '#9467bd']

fig_scen.add_trace(go.Bar(x=scenarios_df['Scenario'], y=scenarios_df['Revenue_M'], marker_color=colors), row=1, col=1)
fig_scen.add_trace(go.Bar(x=scenarios_df['Scenario'], y=scenarios_df['Attendance'], marker_color=colors), row=1, col=2)
fig_scen.add_trace(go.Bar(x=scenarios_df['Scenario'], y=scenarios_df['Visitors_M'], marker_color=colors), row=1, col=3)

fig_scen.update_layout(title='Scenario Analysis Overview', height=500, template='plotly_white', showlegend=False)
fig_scen.write_html('data/processed/03_scenario_analysis.html')
print("✅ Dashboard 3 saved: 03_scenario_analysis.html")

# 4. Economic Efficiency Bubble Chart
fig_eff = px.scatter(
    merged_cities,
    x='Estimated_Revenue_Millions',
    y='Estimated_Jobs',
    size='Capacity',
    color='Metropolitan_GDP_Billions_USD',
    hover_name='City',
    title='Economic Efficiency by City (Bubble size = Stadium Capacity)',
    labels={'Estimated_Revenue_Millions': 'Proj. Revenue ($M)', 'Estimated_Jobs': 'Proj. Jobs'},
    template='plotly_white'
)
fig_eff.write_html('data/processed/04_economic_efficiency.html')
print("✅ Dashboard 4 saved: 04_economic_efficiency.html")

# Data Export
export_data = merged_cities[['City', 'Region', 'State_Country', 'Capacity', 'Estimated_Revenue_Millions', 'Estimated_Jobs']].copy()
export_data = export_data.sort_values('Estimated_Revenue_Millions', ascending=False)
export_data['Revenue_Rank'] = range(1, len(export_data) + 1)
export_data['Revenue_per_Seat'] = (export_data['Estimated_Revenue_Millions'] * 1_000_000 / export_data['Capacity']).round(2)

export_data.to_csv('data/processed/regional_impact_summary.csv', index=False)
try:
    export_data.to_excel('data/processed/regional_impact_summary.xlsx', index=False)
    print("✅ Export Excel saved: regional_impact_summary.xlsx")
except Exception as e:
    print("⚠️  Warning: Excel export failed (openpyxl might be missing). CSV generated successfully.")

# Create index.html
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>USA 2026 Economic Impact Dashboards</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Verdana, sans-serif; background: #f0f2f5; padding: 2rem; }
        .container { max-width: 1000px; margin: 0 auto; }
        h1 { color: #1a365d; text-align: center; }
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 30px; }
        .card { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); text-align: center; }
        a { display: inline-block; background: #004481; color: white; padding: 10px 20px; text-decoration: none; border-radius: 4px; margin-top: 15px; }
        a:hover { background: #002d56; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🏆 USA 2026 FIFA World Cup - Impact Dashboards</h1>
        <div class="grid">
            <div class="card">
                <h3>📈 Historical Timeline</h3>
                <p>Evolution of WC revenues and attendance</p>
                <a href="01_historical_timeline.html" target="_blank">View Dashboard</a>
            </div>
            <div class="card">
                <h3>🏙️ Top Cities Comparison</h3>
                <p>Projected revenue & jobs for host cities</p>
                <a href="02_top_cities_comparison.html" target="_blank">View Dashboard</a>
            </div>
            <div class="card">
                <h3>📊 Scenario Analysis</h3>
                <p>Financial projections across 5 scenarios</p>
                <a href="03_scenario_analysis.html" target="_blank">View Dashboard</a>
            </div>
            <div class="card">
                <h3>🎯 Economic Efficiency</h3>
                <p>Efficiency of revenue generation vs capacity</p>
                <a href="04_economic_efficiency.html" target="_blank">View Dashboard</a>
            </div>
        </div>
    </div>
</body>
</html>
"""
with open("data/processed/index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("✅ Index generated: index.html")
print("="*80)
print("🎯 PHASE 4 COMPLETELY EXECUTED!")
print("="*80)
