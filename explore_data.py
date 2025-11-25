import pandas as pd

print("=" * 60)
print("HAPPINESS DATA")
print("=" * 60)
happiness_df = pd.read_excel('data/Happiness Scores Country/data (1).xlsx')
print(f"\nShape: {happiness_df.shape}")
print(f"\nColumns: {list(happiness_df.columns)}")
print("\nFirst row values:")
for i, col in enumerate(happiness_df.columns):
    print(f"  {i}. {col}: {happiness_df[col].iloc[0]}")

print("\n\nSecond row values:")
for i, col in enumerate(happiness_df.columns):
    print(f"  {i}. {col}: {happiness_df[col].iloc[1]}")

print("\n" + "=" * 60)
print("TEMPERATURE DATA (en.xlsx)")
print("=" * 60)
temp_df = pd.read_excel('data/Temperature by Country/en.xlsx')
print(f"\nShape: {temp_df.shape}")
print(f"\nColumns: {list(temp_df.columns)}")
print("\nFirst row values:")
for i, col in enumerate(temp_df.columns):
    print(f"  {i}. {col}: {temp_df[col].iloc[0]}")

print("\n\nSecond row values:")
for i, col in enumerate(temp_df.columns):
    print(f"  {i}. {col}: {temp_df[col].iloc[1]}")

print("\n" + "=" * 60)
print("OTHER TEMPERATURE FILES")
print("=" * 60)
print("\nTradingeconomics.xlsx:")
te_df = pd.read_excel('data/Temperature by Country/tradingeconomics.xlsx')
print(f"Shape: {te_df.shape}")
print(f"Columns: {list(te_df.columns)}")

print("\nWorldeconomics.xlsx:")
we_df = pd.read_excel('data/Temperature by Country/worldeconomics.xlsx')
print(f"Shape: {we_df.shape}")
print(f"Columns: {list(we_df.columns)}")
