"""
Data Cleaning Script for Happiness-Climate Analysis
This script consolidates happiness and temperature data from multiple sources.
"""

import pandas as pd
import numpy as np
import re
import warnings
warnings.filterwarnings('ignore')

print("=" * 80)
print("DATA CLEANING PIPELINE - Happiness & Climate Analysis")
print("=" * 80)

# ============================================================================
# PHASE 1: LOAD AND CONSOLIDATE HAPPINESS DATA
# ============================================================================
print("\n[PHASE 1] Loading and consolidating happiness data...")

happiness_dfs = []

for i in range(1, 12):
    filename = f'data/Happiness Scores Country/data ({i}).xlsx'
    df = pd.read_excel(filename)

    # Rename columns to meaningful names
    # Based on World Happiness Report structure
    column_mapping = {
        'MuiDataGrid-cell': 'Rank',
        'flag_icon src': 'Flag_URL',
        'MuiChip-label href': 'Country_URL',
        'MuiChip-label': 'Country',
        'MuiDataGrid-cell 2': 'Happiness_Score',
        'MuiDataGrid-cell 3': 'Score_Change',
        'MuiDataGrid-cell 4': 'Rank_GDP',
        'MuiDataGrid-cell 5': 'Rank_Social_Support',
        'MuiDataGrid-cell 6': 'Rank_Life_Expectancy',
        'MuiDataGrid-cell 7': 'Rank_Freedom',
        'MuiDataGrid-cell 8': 'Rank_Generosity',
        'MuiDataGrid-cell 9': 'Rank_Corruption',
        'MuiDataGrid-cell 10': 'Rank_Positive_Affect',
        'MuiDataGrid-cell 11': 'Rank_Negative_Affect',
        'MuiDataGrid-cell 12': 'Rank_Confidence',
        'MuiDataGrid-cell 13': 'Rank_Democratic_Quality',
        'MuiDataGrid-cell 14': 'Age_Percentile',
        'MuiDataGrid-cell 15': 'Rank_Overall',
    }

    df = df.rename(columns=column_mapping)
    happiness_dfs.append(df)
    print(f"  [OK] Loaded data ({i}).xlsx - {len(df)} countries")

# Concatenate all dataframes
happiness_all = pd.concat(happiness_dfs, ignore_index=True)
print(f"\n  Total rows before deduplication: {len(happiness_all)}")

# Remove duplicates - keep first occurrence
happiness_all = happiness_all.drop_duplicates(subset=['Country'], keep='first')
print(f"  Total unique countries: {len(happiness_all)}")

# ============================================================================
# PHASE 2: CLEAN HAPPINESS DATA
# ============================================================================
print("\n[PHASE 2] Cleaning happiness data...")

# Convert '-' to NaN
happiness_all = happiness_all.replace('-', np.nan)
happiness_all = happiness_all.replace('−', '-')  # Replace unicode minus with regular minus

# Convert numeric columns to proper types
numeric_cols = ['Happiness_Score', 'Score_Change', 'Rank_GDP', 'Rank_Social_Support',
                'Rank_Life_Expectancy', 'Rank_Freedom', 'Rank_Generosity', 'Rank_Corruption',
                'Rank_Positive_Affect', 'Rank_Negative_Affect', 'Rank_Confidence',
                'Rank_Democratic_Quality', 'Age_Percentile', 'Rank_Overall']

for col in numeric_cols:
    if col in happiness_all.columns:
        happiness_all[col] = pd.to_numeric(happiness_all[col], errors='coerce')

# Clean country names
happiness_all['Country_Clean'] = happiness_all['Country'].str.strip()

print(f"  [OK] Converted {len(numeric_cols)} columns to numeric")
print(f"  [OK] Cleaned country names")

# ============================================================================
# PHASE 3: LOAD AND CLEAN TEMPERATURE DATA
# ============================================================================
print("\n[PHASE 3] Loading and cleaning temperature data...")

# Load temperature data from tradingeconomics (most straightforward)
temp_df = pd.read_excel('data/Temperature by Country/tradingeconomics.xlsx')
print(f"  [OK] Loaded tradingeconomics.xlsx - {len(temp_df)} countries")

# Rename columns
temp_df = temp_df.rename(columns={
    'tablescraper-selected-row': 'Country',
    'tablescraper-selected-row 2': 'Temperature_Current',
    'tablescraper-selected-row 3': 'Temperature_Average',
    'd-none': 'Date'
})

# Convert temperatures to numeric
temp_df['Temperature_Current'] = pd.to_numeric(temp_df['Temperature_Current'], errors='coerce')
temp_df['Temperature_Average'] = pd.to_numeric(temp_df['Temperature_Average'], errors='coerce')

# Calculate average temperature
temp_df['Temperature_C'] = temp_df[['Temperature_Current', 'Temperature_Average']].mean(axis=1)

# Clean country names
temp_df['Country_Clean'] = temp_df['Country'].str.strip()

print(f"  [OK] Extracted temperature values")
print(f"  [OK] Average temperature range: {temp_df['Temperature_C'].min():.2f}°C to {temp_df['Temperature_C'].max():.2f}°C")

# ============================================================================
# PHASE 4: COUNTRY NAME NORMALIZATION
# ============================================================================
print("\n[PHASE 4] Normalizing country names for matching...")

# Create mapping for common country name variations
country_name_mapping = {
    # Common variations
    'united states': 'united states of america',
    'usa': 'united states of america',
    'u.s.a.': 'united states of america',
    'uk': 'united kingdom',
    'britain': 'united kingdom',
    'czechia': 'czech republic',
    'south korea': 'korea, south',
    'republic of korea': 'south korea',
    'north korea': 'korea, north',
    'democratic republic of the congo': 'congo (kinshasa)',
    'republic of the congo': 'congo (brazzaville)',
    'lao pdr': 'laos',
    'myanmar': 'burma',
    'palestine': 'palestinian territories',
    'state of palestine': 'palestine',
    'ivory coast': "cote d'ivoire",
    'cape verde': 'cabo verde',
    'east timor': 'timor-leste',
    'viet nam': 'vietnam',
    'turkiye': 'turkey',
    'russian federation': 'russia',
    'republic of moldova': 'moldova',
    'north macedonia': 'macedonia',
    'taiwan province of china': 'taiwan',
    'hong kong sar of china': 'hong kong',
}

def normalize_country_name(name):
    """Normalize country names for better matching"""
    if pd.isna(name):
        return name

    # Convert to lowercase
    normalized = str(name).lower().strip()

    # Remove common suffixes/prefixes
    normalized = normalized.replace(' the', '').replace('the ', '')

    # Apply manual mappings
    if normalized in country_name_mapping:
        normalized = country_name_mapping[normalized]

    return normalized

# Apply normalization
happiness_all['Country_Normalized'] = happiness_all['Country_Clean'].apply(normalize_country_name)
temp_df['Country_Normalized'] = temp_df['Country_Clean'].apply(normalize_country_name)

print(f"  [OK] Applied country name normalization")

# ============================================================================
# PHASE 5: MERGE DATASETS
# ============================================================================
print("\n[PHASE 5] Merging happiness and temperature data...")

# First, try exact match on normalized names
merged = pd.merge(
    happiness_all,
    temp_df[['Country_Normalized', 'Temperature_C', 'Temperature_Current', 'Temperature_Average']],
    on='Country_Normalized',
    how='left'
)

print(f"  [OK] Merged datasets")
print(f"  [OK] Total countries in merged dataset: {len(merged)}")
print(f"  [OK] Countries with temperature data: {merged['Temperature_C'].notna().sum()}")
print(f"  [OK] Countries missing temperature data: {merged['Temperature_C'].isna().sum()}")

# Show which countries are missing temperature data
missing_temp = merged[merged['Temperature_C'].isna()]['Country'].tolist()
if len(missing_temp) > 0:
    print(f"\n  Countries without temperature data ({len(missing_temp)}):")
    for country in sorted(missing_temp)[:20]:  # Show first 20
        print(f"    - {country}")
    if len(missing_temp) > 20:
        print(f"    ... and {len(missing_temp) - 20} more")

# ============================================================================
# PHASE 6: FINAL CLEANUP AND EXPORT
# ============================================================================
print("\n[PHASE 6] Final data quality checks...")

# Select key columns for analysis
final_columns = [
    'Country',
    'Happiness_Score',
    'Score_Change',
    'Temperature_C',
    'Temperature_Current',
    'Temperature_Average',
    'Rank',
    'Rank_GDP',
    'Rank_Social_Support',
    'Rank_Life_Expectancy',
    'Rank_Freedom',
    'Rank_Generosity',
    'Rank_Corruption',
]

final_df = merged[final_columns].copy()

# Remove rows with missing happiness score or temperature
print(f"\n  Before filtering: {len(final_df)} countries")
final_df_complete = final_df.dropna(subset=['Happiness_Score', 'Temperature_C'])
print(f"  After removing incomplete data: {len(final_df_complete)} countries")

# Data quality checks
print(f"\n  Data Quality Summary:")
print(f"    Happiness Score range: {final_df_complete['Happiness_Score'].min():.3f} to {final_df_complete['Happiness_Score'].max():.3f}")
print(f"    Temperature range: {final_df_complete['Temperature_C'].min():.2f}°C to {final_df_complete['Temperature_C'].max():.2f}°C")
print(f"    Missing values per column:")
for col in final_df_complete.columns:
    missing = final_df_complete[col].isna().sum()
    if missing > 0:
        print(f"      {col}: {missing}")

# Export cleaned data
final_df.to_csv('data/happiness_temperature_all.csv', index=False)
print(f"\n  [OK] Exported complete dataset: data/happiness_temperature_all.csv")

final_df_complete.to_csv('data/happiness_temperature_clean.csv', index=False)
print(f"  [OK] Exported clean dataset (no missing values): data/happiness_temperature_clean.csv")

# ============================================================================
# GENERATE DATA SUMMARY REPORT
# ============================================================================
print("\n" + "=" * 80)
print("CLEANING SUMMARY")
print("=" * 80)
print(f"""
Data Sources:
  - Happiness: 11 Excel files from World Happiness Report
  - Temperature: tradingeconomics.xlsx

Final Dataset Statistics:
  - Total countries with happiness data: {len(happiness_all)}
  - Total countries with temperature data: {len(temp_df)}
  - Successfully matched countries: {len(final_df_complete)}
  - Match rate: {len(final_df_complete)/len(happiness_all)*100:.1f}%

Output Files:
  - data/happiness_temperature_all.csv (all countries, some missing data)
  - data/happiness_temperature_clean.csv (only complete records)

Next Steps:
  - Use happiness_temperature_clean.csv for analysis
  - {len(final_df_complete)} countries ready for correlation analysis
""")

print("=" * 80)
print("[OK] DATA CLEANING COMPLETE!")
print("=" * 80)
