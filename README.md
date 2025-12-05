# Content-Based Recommendation System

## Project Overview
This is a content-based recommendation system that suggests recipes based on user preferences. The system analyzes a dataset of food recipes and recommends dishes that match the user's time availability and dietary preferences.

**Course:** CIS 641  
**Author:** RU  
**Date Created:** January 27, 2025

## Dataset
The project uses the **Food_Recipe.csv** dataset containing recipe information including:
- Recipe name
- Cuisine type
- Course type
- Dietary information
- Preparation time (in minutes)
- Cooking time (in minutes)

## Features

### Data Analysis
- Calculates total recipe time (preparation + cooking)
- Provides descriptive statistics on recipe preparation and cooking times
- Analyzes missing values and cleans the dataset
- Visualizes the top 15 cuisines by number of recipes
- Displays the distribution of dietary options

### Recommendation System
- **User Input:** Accepts time constraints (in minutes) and dietary preferences
- **Filtering:** Matches recipes based on:
  - Total time available (must not exceed user's specified time)
  - Dietary preference (vegetarian, vegan, gluten-free, etc.)
- **Output:** Displays all matching recipes with details on cuisine, diet type, and total time required

## How to Use

1. Ensure `Food_Recipe.csv` is in the same directory as the script
2. Run the script:
   ```bash
   python Contentbasedrecommendationsys.py
   ```
3. When prompted:
   - Enter the maximum time available for cooking (in minutes)
   - Enter your dietary preference (e.g., vegetarian, vegan, gluten-free, or "none" for no preference)
4. View the recommended recipes that match your criteria

## Requirements
- pandas
- numpy
- matplotlib
- seaborn

Install dependencies using:
```bash
pip install pandas numpy matplotlib seaborn
```

## Output
The script provides:
1. Basic statistics on recipe times
2. Visualizations of cuisine and diet distributions
   
   <img width="489" height="280" alt="image" src="https://github.com/Lande21/MachineLearningRecommender/blob/main/Figure_1.png" />
   <img width="489" height="280" alt="image" src="https://github.com/Lande21/MachineLearningRecommender/blob/main/Figure_2.png" />
4. A filtered list of recipes matching user preferences with columns: name, cuisine, diet, and total time
   <img width="489" height="180" alt="image" src="https://github.com/user-attachments/assets/fde27495-2bb7-4a6e-a1ac-79cf265ee95c" />


## Notes
- Missing values in cuisine, course, and diet columns are removed
- The top 3 columns with the highest null value counts are excluded from analysis
- Dietary preference matching is case-insensitive
