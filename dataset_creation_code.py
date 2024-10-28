import pandas as pd
import numpy as np
import random

# Define countries and regions for diversity
countries = [
    "United States", "Canada", "Brazil", "Germany", "United Kingdom", "France", "Australia", "India", 
    "China", "Japan", "South Africa", "Russia", "Mexico", "Italy", "Spain", "South Korea", "Argentina", "Nigeria"
]
regions = {
    "North America": ["United States", "Canada", "Mexico"],
    "South America": ["Brazil", "Argentina"],
    "Europe": ["Germany", "United Kingdom", "France", "Italy", "Spain", "Russia"],
    "Asia": ["China", "Japan", "India", "South Korea"],
    "Africa": ["South Africa", "Nigeria"],
    "Oceania": ["Australia"]
}

# Set the year range and create an empty DataFrame
years = range(2015, 2024)
data = []

# Generate data
for year in years:
    for country in countries:
        region = next((reg for reg, ctrs in regions.items() if country in ctrs), "Unknown")
        happiness_score = round(random.uniform(3, 8), 2)  # Random happiness score between 3 and 8
        gdp_per_capita = round(random.uniform(1000, 60000), 2)  # Random GDP per capita
        life_expectancy = round(random.uniform(50, 85), 2)  # Random life expectancy

        # Append to data list
        data.append([year, country, region, happiness_score, gdp_per_capita, life_expectancy])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    "Year", "Country", "Region", "Happiness Score", "GDP per capita", "Healthy life expectancy"
])

# Save to CSV
df.to_csv("dummy_world_happiness_report.csv", index=False)
print("Dataset created successfully!")
