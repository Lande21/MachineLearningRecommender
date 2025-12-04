#Author: RU, Jan 27, 2025
#CIS 641
#Referencing Chap 19, building a content-based recommendation system
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

recipes = pd.read_csv("Food_Recipe.csv")

print(recipes.columns)

#Adding the total time it takes including preparation and cooking time for a recipe
recipes['total_time (in mins)'] = recipes['prep_time (in mins)'] + recipes['cook_time (in mins)']
print(recipes.columns)

#Data analysis and stats for our dataset
print("Basic Statistics:")
print(recipes[['prep_time (in mins)', 'cook_time (in mins)', 'total_time (in mins)']].describe())

#Checking for missing values
print("\nMissing Values:")
#print(recipes.isnull().sum())

recipes_cleaned = recipes.dropna(subset=['cuisine','course', 'diet'])
missing_percentage = (recipes_cleaned.isnull().sum() / len(recipes)) * 100
print(missing_percentage)
#deleted top 3 columns with higher number of null values

#Getting the top 15 cuisines by count
top_15_cuisines = recipes_cleaned['cuisine'].value_counts().nlargest(15)

#Plotting the top 15 cuisines
plt.figure(figsize=(10, 6))
sns.countplot(
    data=recipes_cleaned[recipes_cleaned['cuisine'].isin(top_15_cuisines.index)],  #filtering data to include only top 15 cuisines
    y='cuisine',
    order=top_15_cuisines.index,  
    palette='Set2'
)
plt.title('Top 15 Cuisines by Number of Recipes')
plt.xlabel('Number of Recipes')
plt.ylabel('Cuisine')
plt.show()

#Diet Distribution
plt.figure(figsize=(10, 6))
sns.countplot(data=recipes_cleaned, y='diet', order=recipes_cleaned['diet'].value_counts().index, palette='Set1')
plt.title('Distribution of Diets')
plt.xlabel('Number of Recipes')
plt.ylabel('Diet')
plt.show()

#Making content-based filtering recommendation system
#Will get user input on time, and dietary preferences.

user_time = int(input("How much time do you have? (in minutes): "))
user_diet = input("What is your dietary preference? (like: vegetarian, vegan, gluten-free, none): ").strip().lower()

#Filtering recipes based on time and dietary preferences 
filtered_recipes = recipes_cleaned[recipes_cleaned['total_time (in mins)'] <= user_time]
if user_diet != "none":
    filtered_recipes = filtered_recipes[filtered_recipes['diet'].str.lower() == user_diet]

#Displaying recommended recipes to our user
if not filtered_recipes.empty:
    print(f"\nFound {len(filtered_recipes)} recipes matching your preferences:")
    print(filtered_recipes[['name', 'cuisine', 'diet', 'total_time (in mins)']])
else:
    print("No recipes found matching your preferences.")

