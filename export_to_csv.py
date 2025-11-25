import pandas as pd
import os

# Export happiness data
print("Exporting happiness data...")
happiness_df = pd.read_excel('data/Happiness Scores Country/data (1).xlsx')
happiness_df.to_csv('data/happiness_sample.csv', index=False)
print(f"  Happiness: {happiness_df.shape} -> data/happiness_sample.csv")

# Export temperature data
print("\nExporting temperature data...")
temp_df = pd.read_excel('data/Temperature by Country/en.xlsx')
temp_df.to_csv('data/temperature_en.csv', index=False)
print(f"  Temperature (en): {temp_df.shape} -> data/temperature_en.csv")

te_df = pd.read_excel('data/Temperature by Country/tradingeconomics.xlsx')
te_df.to_csv('data/temperature_tradingeconomics.csv', index=False)
print(f"  Temperature (tradingeconomics): {te_df.shape} -> data/temperature_tradingeconomics.csv")

we_df = pd.read_excel('data/Temperature by Country/worldeconomics.xlsx')
we_df.to_csv('data/temperature_worldeconomics.csv', index=False)
print(f"  Temperature (worldeconomics): {we_df.shape} -> data/temperature_worldeconomics.csv")

print("\nExport complete!")
