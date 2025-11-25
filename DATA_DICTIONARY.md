# Data Dictionary - Happiness & Climate Analysis

## Dataset Overview

**File**: `data/happiness_temperature_clean.csv`
**Records**: 122 countries
**Purpose**: Analyzing the relationship between climate (temperature) and happiness scores

---

## Column Descriptions

### Primary Variables

| Column Name | Type | Range | Description |
|------------|------|-------|-------------|
| `Country` | String | - | Country name |
| `Happiness_Score` | Float | 4.898 - 7.736 | Overall happiness/life satisfaction score (0-10 scale) from World Happiness Report 2024 |
| `Temperature_C` | Float | 1.50 - 29.54 | Average annual temperature in Celsius |

### Temperature Details

| Column Name | Type | Description |
|------------|------|-------------|
| `Temperature_Current` | Float | Current/recent temperature measurement (°C) |
| `Temperature_Average` | Float | Historical average temperature (°C) |
| `Temperature_C` | Float | Mean of Current and Average temperatures |

### Happiness Score Metadata

| Column Name | Type | Description |
|------------|------|-------------|
| `Score_Change` | Float | Change in happiness score from previous year |
| `Rank` | Integer | Global ranking (1 = highest happiness) |

### Happiness Factor Rankings

These columns represent the country's global ranking for specific happiness factors:

| Column Name | Description |
|------------|-------------|
| `Rank_GDP` | Ranking based on GDP per capita |
| `Rank_Social_Support` | Ranking for social support (having someone to count on) |
| `Rank_Life_Expectancy` | Ranking based on healthy life expectancy |
| `Rank_Freedom` | Ranking for freedom to make life choices |
| `Rank_Generosity` | Ranking based on generosity (charitable giving) |
| `Rank_Corruption` | Ranking for perceptions of corruption (lower rank = less corruption) |

**Note**: Lower rank numbers indicate better performance for that factor.

---

## Data Sources

### Happiness Data
- **Source**: World Happiness Report 2024 (data.worldhappiness.report)
- **Files**: 11 Excel files from `data/Happiness Scores Country/`
- **Coverage**: 130 unique countries (122 matched with temperature data)

### Temperature Data
- **Source**: Trading Economics (tradingeconomics.com)
- **File**: `data/Temperature by Country/tradingeconomics.xlsx`
- **Coverage**: 205 countries
- **Time Period**: December 2024 (current) and historical average

---

## Data Quality Notes

### Missing Values
Some countries have incomplete ranking data for happiness factors:
- `Score_Change`: 37 missing values
- Various ranking columns: 15-25 missing values

This is expected as not all countries report all sub-metrics.

### Match Rate
- **Successful matches**: 122 out of 130 countries (93.8%)
- **Unmatched countries** (8): Canada, Côte d'Ivoire, Eswatini, Kosovo, Republic of Korea, Russian Federation, State of Palestine, Türkiye

Unmatched countries are due to naming inconsistencies between data sources.

---

## Usage Recommendations

### For Analysis
1. **Primary correlation**: Use `Happiness_Score` and `Temperature_C`
2. **Control variables**: Include GDP, Social Support, Life Expectancy rankings
3. **Data completeness**: 122 countries provide robust sample size for statistical analysis

### Handling Missing Values
- **For regression**: Use subset with complete factor rankings (recommended)
- **For basic correlation**: Use all 122 records with Happiness_Score and Temperature_C
- **For visualization**: All 122 records are suitable

---

## Example Analysis Questions

1. **Primary**: Is there a correlation between average temperature and happiness score?
2. **Secondary**: How do GDP and social support mediate this relationship?
3. **Regional**: Do temperature effects differ across climate zones?
4. **Extremes**: Are countries with extreme temperatures (very hot/cold) less happy?

---

## Data Cleaning Process

All data was cleaned using `data_cleaning.py`:
1. Consolidated 11 happiness Excel files
2. Renamed columns from web-scraping format to meaningful names
3. Extracted numeric temperatures from various formats
4. Normalized country names for matching
5. Merged datasets on country name
6. Exported clean CSV files

For full details, see [data_cleaning.py](data_cleaning.py)

---

## Citation

If using this dataset, please cite:
- **World Happiness Report 2024**: Helliwell, J. F., Layard, R., Sachs, J. D., et al. (2024)
- **Temperature Data**: Trading Economics (https://tradingeconomics.com)

---

**Last Updated**: November 25, 2024
**Prepared for**: DSA210 Project - Emir Ceylan
