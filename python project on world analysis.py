#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
population_data = pd.read_csv('world_population.csv')

# Display the first few rows of the dataset
print(population_data.head())
# Check for missing values
print(population_data.isnull().sum())

# Fill or drop missing values as appropriate
population_data = population_data.fillna(0)

# Convert year columns to numeric
years = population_data.columns[4:]
population_data[years] = population_data[years].apply(pd.to_numeric, errors='coerce')

# Display the first few rows of the cleaned dataset
print(population_data.head())
# Calculate the global population growth
global_population = population_data.groupby('Year').sum()

# Plot the global population growth
plt.figure(figsize=(12, 6))
sns.lineplot(data=global_population, x='Year', y='Population')
plt.title('Global Population Growth Over Time')
plt.xlabel('Year')
plt.ylabel('Population')
plt.show()
# Assuming there's an 'area' column in the dataset
# Calculate population density
population_data['Density'] = population_data['Population'] / population_data['Area']

# Plot population density for a specific country (e.g., India)
india_data = population_data[population_data['Country'] == 'India']

plt.figure(figsize=(12, 6))
sns.lineplot(data=india_data, x='Year', y='Density')
plt.title('Population Density of India Over Time')
plt.xlabel('Year')
plt.ylabel('Population Density')
plt.show()
# Plot population growth for the top 5 most populous countries
top_countries = population_data.groupby('Country')['Population'].max().nlargest(5).index
top_countries_data = population_data[population_data['Country'].isin(top_countries)]

plt.figure(figsize=(12, 6))
sns.lineplot(data=top_countries_data, x='Year', y='Population', hue='Country')
plt.title('Population Growth of Top 5 Most Populous Countries Over Time')
plt.xlabel('Year')
plt.ylabel('Population')
plt.legend(title='Country')
plt.show()

