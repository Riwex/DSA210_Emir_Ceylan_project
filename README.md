# DSA210_Emir_Ceylan_project

Does Sunshine Bring Happiness? A Global Analysis of Climate and Well-Being

# Overview

There is a universal link between sun/sunny days with happiness and rain with sadness/melancohly. We can even see it in kid books with smiling big suns and crying rainy clouds. I decided put that understanding to test. 
This projects investigates that idea by analyzing the avarage number of sunny days and avarage yearly temperatures correlation to the Hapiness Index score of countries.By combining meteorological and social data, we aim to uncover whether sunlight, climate, and happiness are truly connected or if economic and social factors dominate.

# Data Sources

    World Happiness Report (2023–2024)

Contains Happiness Index, GDP per capita, social support, freedom, corruption, and generosity by country.
Source: https://worldhappiness.report

    Average Annual Sunshine & Temperature Data

From NOAA, Meteostat, or Our World in Data Climate Dataset
Example dataset: https://datahub.io/core/global-temp or https://meteostat.net

    (Optional) Population Density or Latitude Data

To explore whether latitude or urbanization affects happiness.

# Methods and Analysis Plan

Data Cleaning
Normalize country names across datasets. Handle missing values for temperature/sunshine.

Exploratory Data Analysis (EDA)
Summary statistics (mean, variance). Correlation heatmap (happiness vs. temperature, GDP, sunshine). Scatter plots and boxplots per region.

Statistical Analysis
Compute Pearson correlation between happiness and sunshine/temperature.Conduct regression analysis:

Model 1: Happiness ~ Temperature
Model 2: Happiness ~ Temperature + GDP + Freedom (to see indirect effects).

Visualization

World choropleth map showing happiness vs. average sunlight.
Scatter plots with regression lines.

Machine Learning 
Train a regression model to predict happiness score based on climate and socio-economic features.

# Expected Findings

A positive correlation between happiness and moderate sunlight (too cold or too hot may lower scores).

Wealthier or socially free countries may show higher happiness even with less sunshine, revealing hidden confounders.

Visualization may show that mid-latitude countries (e.g., Spain, Italy, Australia) score higher than extremes (e.g., Norway or India).

# Tools
Python (Pandas, NumPy, Seaborn, Plotly, Scikit-learn)
Jupyter Notebook for analysis
GitHub for code versioning
(Optional) APIs: Meteostat API, Open-Meteo API