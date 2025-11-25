import pandas as pd

print('Checking all happiness files structure...\n')
for i in range(1, 12):
    filename = f'data/Happiness Scores Country/data ({i}).xlsx'
    df = pd.read_excel(filename)
    print(f'data ({i}).xlsx: Shape {df.shape}, First country: {df["MuiChip-label"].iloc[0]}, Last country: {df["MuiChip-label"].iloc[-1]}')
