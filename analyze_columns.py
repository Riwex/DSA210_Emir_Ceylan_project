import pandas as pd
import numpy as np

# Load one happiness file to analyze
df = pd.read_excel('data/Happiness Scores Country/data (1).xlsx')

print("=" * 80)
print("COLUMN ANALYSIS - Happiness Data")
print("=" * 80)

# Show first 5 countries with all their values
print("\nFirst 5 countries - ALL columns:")
for idx in range(5):
    print(f"\n{idx+1}. {df['MuiChip-label'].iloc[idx]} (Rank: {df['MuiDataGrid-cell'].iloc[idx]})")
    for i, col in enumerate(df.columns):
        if i >= 4:  # Skip rank, flags, links, country name
            print(f"   Col {i}: {col} = {df[col].iloc[idx]}")

# Check data types and statistics
print("\n" + "=" * 80)
print("COLUMN STATISTICS")
print("=" * 80)

for i, col in enumerate(df.columns):
    if i >= 4:  # Numeric columns
        try:
            # Try to convert to numeric
            numeric_data = pd.to_numeric(df[col], errors='coerce')
            print(f"\nColumn {i}: {col}")
            print(f"  Type: {df[col].dtype}")
            print(f"  Min: {numeric_data.min()}")
            print(f"  Max: {numeric_data.max()}")
            print(f"  Mean: {numeric_data.mean():.2f}")
            print(f"  Non-null count: {numeric_data.notna().sum()}/{len(df)}")
        except:
            print(f"\nColumn {i}: {col} - Cannot convert to numeric")

# World Happiness Report typically has these columns:
# - Happiness Score (Ladder score)
# - GDP per capita (Explained by: Log GDP per capita)
# - Social support (Explained by: Social support)
# - Healthy life expectancy (Explained by: Healthy life expectancy)
# - Freedom to make life choices (Explained by: Freedom to make life choices)
# - Generosity (Explained by: Generosity)
# - Perceptions of corruption (Explained by: Perceptions of corruption)
# - Dystopia + residual

print("\n" + "=" * 80)
print("SUGGESTED COLUMN MAPPING (based on World Happiness Report format)")
print("=" * 80)
suggested_mapping = {
    'MuiDataGrid-cell': 'Rank',
    'flag_icon src': 'Flag_URL',
    'MuiChip-label href': 'Country_URL',
    'MuiChip-label': 'Country',
    'MuiDataGrid-cell 2': 'Happiness_Score',
    'MuiDataGrid-cell 3': 'Happiness_Score_Change',  # Based on negative values seen
    'MuiDataGrid-cell 4': 'Unknown_4',
    'MuiDataGrid-cell 5': 'Unknown_5',
    'MuiDataGrid-cell 6': 'Unknown_6',
    'MuiDataGrid-cell 7': 'Unknown_7',
    'MuiDataGrid-cell 8': 'Unknown_8',
    'MuiDataGrid-cell 9': 'Unknown_9',
    'MuiDataGrid-cell 10': 'Unknown_10',
    'MuiDataGrid-cell 11': 'Unknown_11',
    'MuiDataGrid-cell 12': 'Unknown_12',
    'MuiDataGrid-cell 13': 'Unknown_13',
    'MuiDataGrid-cell 14': 'Unknown_14',
    'MuiDataGrid-cell 15': 'Unknown_15',
}

for old_name, new_name in suggested_mapping.items():
    print(f"{old_name:30s} -> {new_name}")
