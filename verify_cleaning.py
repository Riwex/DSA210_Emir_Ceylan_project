"""
Quick verification and summary of cleaned data
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv('data/happiness_temperature_clean.csv')

print("=" * 80)
print("CLEANED DATA VERIFICATION")
print("=" * 80)

print(f"\nDataset shape: {df.shape}")
print(f"Number of countries: {len(df)}")

print("\n" + "=" * 80)
print("BASIC STATISTICS")
print("=" * 80)
print(df[['Happiness_Score', 'Temperature_C', 'Score_Change']].describe())

print("\n" + "=" * 80)
print("TOP 10 HAPPIEST COUNTRIES")
print("=" * 80)
top_10 = df.nlargest(10, 'Happiness_Score')[['Country', 'Happiness_Score', 'Temperature_C', 'Rank']]
print(top_10.to_string(index=False))

print("\n" + "=" * 80)
print("TOP 10 HOTTEST COUNTRIES")
print("=" * 80)
hottest = df.nlargest(10, 'Temperature_C')[['Country', 'Temperature_C', 'Happiness_Score', 'Rank']]
print(hottest.to_string(index=False))

print("\n" + "=" * 80)
print("TOP 10 COLDEST COUNTRIES")
print("=" * 80)
coldest = df.nsmallest(10, 'Temperature_C')[['Country', 'Temperature_C', 'Happiness_Score', 'Rank']]
print(coldest.to_string(index=False))

print("\n" + "=" * 80)
print("INITIAL CORRELATION ANALYSIS")
print("=" * 80)
correlation = df[['Happiness_Score', 'Temperature_C']].corr()
print(correlation)
print(f"\nPearson correlation coefficient: {df['Happiness_Score'].corr(df['Temperature_C']):.4f}")

# Create a simple scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Temperature_C'], df['Happiness_Score'], alpha=0.6, s=50)
plt.xlabel('Average Temperature (°C)', fontsize=12)
plt.ylabel('Happiness Score', fontsize=12)
plt.title('Happiness Score vs Average Temperature\n(122 Countries)', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)

# Add trend line
z = np.polyfit(df['Temperature_C'], df['Happiness_Score'], 1)
p = np.poly1d(z)
plt.plot(df['Temperature_C'], p(df['Temperature_C']), "r--", alpha=0.8, linewidth=2, label=f'Trend line')
plt.legend()

plt.tight_layout()
plt.savefig('data/initial_correlation_plot.png', dpi=150, bbox_inches='tight')
print("\n[OK] Saved initial correlation plot: data/initial_correlation_plot.png")

print("\n" + "=" * 80)
print("DATA CLEANING VERIFICATION COMPLETE!")
print("=" * 80)
print("\nReady for analysis! Use the cleaned dataset:")
print("  - data/happiness_temperature_clean.csv")
print("\nNext step: Open happiness_climate_analysis.ipynb for full analysis")
