# DSA210_Emir_Ceylan_project

Does Sunshine Bring Happiness? A Global Analysis of Climate and Well-Being

# Overview

There's a universal cultural link between sunshine and happiness and rain with sadness or melancholy. We see this idea even in kid books with smiling suns and crying rainy clouds. I decided put that understanding to test.
This projects investigates that idea by analyzing the avarage number of sunny days and avarage yearly temperatures correlation to the Hapiness Index score of countries.By combining meteorological and social data, we aim to uncover whether sunlight, climate, and happiness are truly connected or if economic and social factors dominate.

## Research Question

**Primary Research Question:**
> Does average annual temperature correlate with national happiness scores, and if so, to what extent can this relationship be explained by climate alone versus socioeconomic factors?

**Sub-Questions:**

1. **Correlation Analysis**: Is there a statistically significant correlation between average temperature and happiness scores across countries?

2. **Confounding Factors**: How much of the temperature-happiness relationship can be attributed to correlated socioeconomic factors (GDP per capita, social support, freedom, corruption)?

3. **Optimal Climate Zones**: Do countries with moderate temperatures (e.g., 10-20°C) show higher happiness scores compared to extreme climates (very cold or very hot)?

4. **Regional Patterns**: Are there regional differences in how climate affects happiness? For example, do Nordic countries maintain high happiness despite cold climates?

5. **Causality vs. Correlation**: Can we identify mechanisms through which climate might influence happiness (e.g., through economic productivity, social behavior, health outcomes)?

**Hypotheses:**

- **H1 (Null)**: There is no significant relationship between average temperature and national happiness scores.
- **H2 (Alternative)**: There is a negative correlation between extreme temperatures (both hot and cold) and happiness, with moderate climates showing peak happiness.
- **H3 (Confounding)**: Any observed temperature-happiness correlation is primarily mediated by GDP and social support rather than climate itself.

**Initial Finding** (from data cleaning):
- Preliminary analysis shows a **moderate negative correlation (r = -0.37)** between temperature and happiness
- Colder countries (Finland, Iceland, Norway) rank among the happiest
- This suggests the relationship may be more complex than "sunshine equals happiness"

## Motivation

Understanding how sunlight and temperature affect mental well-being can help shape **healthier urban environments**.  
If sunshine truly contributes to happiness, urban planners and architects could prioritize natural light exposure when designing cities, offices, and living spaces.

## Data Sources

   ### World Happiness Report (2023–2024)

   - Contains Happiness Index, GDP per capita, social support, freedom, corruption, and generosity by country.
   - Source: https://worldhappiness.report

   ### Average Annual Sunshine & Temperature Data

   - From NOAA, Meteostat, or Our World in Data Climate Dataset
   - Example dataset: https://datahub.io/core/global-temp or https://meteostat.net

   ### (Optional) Population Density or Latitude Data

    - To explore whether latitude or urbanization affects happiness.

## Methods and Analysis Plan

### Data Cleaning
- Normalize country names across datasets. 
- Handle missing values for temperature/sunshine.

###Exploratory Data Analysis (EDA)
- Summary statistics (mean, variance). 
- Correlation heatmap (happiness vs. temperature, GDP, sunshine). Scatter plots and boxplots per region.

### Statistical Analysis
- Compute Pearson correlation between happiness and sunshine/temperature.- Conduct regression analysis:

    - Model 1: Happiness ~ Temperature
    - Model 2: Happiness ~ Temperature + GDP + Freedom (to see indirect effects).

### Visualization

- World choropleth map showing happiness vs. average sunlight.
- Scatter plots with regression lines.

### Machine Learning 
- Train a regression model to predict happiness score based on climate and socio-economic features.

## Expected Findings

- A positive correlation between happiness and moderate sunlight (too cold or too hot may lower scores).

- Wealthier or socially free countries may show higher happiness even with less sunshine, revealing hidden confounders.

- Visualization may show that mid-latitude countries (e.g., Spain, Italy, Australia) score higher than extremes (e.g., Norway or India).

## Tools
- Python (Pandas, NumPy, Seaborn, Plotly, Scikit-learn)
- Jupyter Notebook for analysis
- GitHub for code versioning
- (Optional) APIs: Meteostat API, Open-Meteo API