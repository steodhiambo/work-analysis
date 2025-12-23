import pandas as pd
import numpy as np

# Load the datasets
df_2020 = pd.read_csv('/home/steodhiambo/WORK -ANALYSIS/2020_rws.csv', encoding='latin-1')
df_2021 = pd.read_csv('/home/steodhiambo/WORK -ANALYSIS/2021_rws.csv', encoding='latin-1')

print("=== STEP 2: DATA CLEANING & FEATURE ENGINEERING ===")

# Display initial info about missing values
print("\nMissing values in 2020 dataset:")
print(df_2020.isnull().sum().head(10))  # Show first 10 columns

print("\nMissing values in 2021 dataset:")
print(df_2021.isnull().sum().head(10))  # Show first 10 columns

# Create copies for cleaning
df_2020_clean = df_2020.copy()
df_2021_clean = df_2021.copy()

# Define the key columns we identified in Step 1
work_type_2020 = 'Thinking about your current job, how much of your time did you spend remote working last year?'
productivity_2020 = 'This question is about your productivity. Productivity means what you produce for each hour that you work. It includes the amount of work you achieve each hour, and the quality of your work each hour.  \nPlease compare your productivity when you work remotely to when you work at your employer\x92s workplace.  \nRoughly how productive are you, each hour, when you work remotely?'
collaboration_2020 = 'Thinking about remote working last year, how strongly do you agree or disagree with the following statements? - I could easily collaborate with colleagues when working remotely'

work_type_2021 = 'Thinking about your current job, how much of your work time have you spent working remotely this year?  If you work a 5 day week, each day of remote working equals 20% of your time.  '
productivity_2021 = 'This question is about your productivity. Productivity means what you produce for each hour that you work. It includes the amount of work you achieve each hour, and the quality of your work each hour.    Please compare your productivity when you work remotely to when you work at your employer\x92s workplace.    Roughly how productive are you, each hour, when you work remotely?  '
collaboration_2021 = 'Thinking about remote working in the last 6 months, how strongly do you agree or disagree with the following statements?   Please select a single response per row   - I could easily collaborate with colleagues when working remotely'

# Standardize work type categories
def standardize_work_type(value):
    """Convert work type responses to standardized categories"""
    if pd.isna(value):
        return 'Unknown'
    
    value_str = str(value).lower()
    
    if 'never' in value_str or 'rarely' in value_str or 'less than 10%' in value_str:
        return 'In-Office'
    elif 'half' in value_str or '50%' in value_str:
        return 'Hybrid'
    elif 'all' in value_str or '100%' in value_str:
        return 'Remote'
    elif '%' in value_str:
        # Extract percentage to determine category
        try:
            # Find the percentage number in the string
            import re
            percent_match = re.search(r'(\d+)%', value_str)
            if percent_match:
                percent = int(percent_match.group(1))
                if percent < 25:
                    return 'In-Office'
                elif percent <= 75:
                    return 'Hybrid'
                else:
                    return 'Remote'
            else:
                return 'Unknown'
        except:
            return 'Unknown'
    else:
        return 'Unknown'

# Apply standardization to work type columns
df_2020_clean['work_type_standardized'] = df_2020_clean[work_type_2020].apply(standardize_work_type)
df_2021_clean['work_type_standardized'] = df_2021_clean[work_type_2021].apply(standardize_work_type)

print(f"\nStandardized work types in 2020: {df_2020_clean['work_type_standardized'].value_counts()}")
print(f"Standardized work types in 2021: {df_2021_clean['work_type_standardized'].value_counts()}")

# Create productivity scores
def standardize_productivity_score(value):
    """Convert productivity responses to numerical scores (higher is better productivity)"""
    if pd.isna(value):
        return np.nan
    
    value_str = str(value).lower()
    
    # Map responses to numerical values
    productivity_mapping = {
        'my productivity is about same when i work remotely': 0,
        'im 10% more productive when working remotely': 10,
        'im 20% more productive when working remotely': 20,
        'im 30% more productive when working remotely': 30,
        'im 40% more productive when working remotely': 40,
        'im 50% more productive when working remotely (or more)': 50,
        'im 10% less productive when working remotely': -10,
        'im 20% less productive when working remotely': -20,
        'im 30% less productive when working remotely': -30,
        'im 40% less productive when working remotely': -40,
        'im 50% less productive when working remotely (or more)': -50
    }
    
    # Clean the value string to match our mapping
    cleaned_value = value_str.replace('\n', '').strip()
    
    return productivity_mapping.get(cleaned_value, np.nan)

# Apply productivity scoring
df_2020_clean['productivity_score'] = df_2020_clean[productivity_2020].apply(standardize_productivity_score)
df_2021_clean['productivity_score'] = df_2021_clean[productivity_2021].apply(standardize_productivity_score)

print(f"\nProductivity scores in 2020: {df_2020_clean['productivity_score'].describe()}")
print(f"Productivity scores in 2021: {df_2021_clean['productivity_score'].describe()}")

# Create morale scores based on collaboration and recommendation
def standardize_morale_score(collab_response, recommend_response=None):
    """Convert collaboration and recommendation responses to morale scores"""
    if pd.isna(collab_response):
        return np.nan
    
    # Map collaboration responses to scores (higher is better morale/collaboration)
    collab_mapping = {
        'strongly disagree': 1,
        'somewhat disagree': 2,
        'neither agree nor disagree': 3,
        'somewhat agree': 4,
        'strongly agree': 5
    }
    
    collab_str = str(collab_response).lower().strip()
    collab_score = collab_mapping.get(collab_str, np.nan)
    
    # If we have a recommendation response, we can add it to the morale score
    if not pd.isna(recommend_response):
        recommend_mapping = {
            'strongly disagree': 1,
            'somewhat disagree': 2,
            'neither agree nor disagree': 3,
            'somewhat agree': 4,
            'strongly agree': 5
        }
        
        recommend_str = str(recommend_response).lower().strip()
        recommend_score = recommend_mapping.get(recommend_str, np.nan)
        
        # Average the scores if both are available
        if not pd.isna(collab_score) and not pd.isna(recommend_score):
            return (collab_score + recommend_score) / 2
        elif not pd.isna(collab_score):
            return collab_score
        elif not pd.isna(recommend_score):
            return recommend_score
        else:
            return np.nan
    else:
        return collab_score

# Apply morale scoring
# For 2020, we have both collaboration and recommendation
recommend_2020 = 'Thinking about remote working last year, how strongly do you agree or disagree with the following statements? - I would recommend remote working to others'
df_2020_clean['morale_score'] = df_2020_clean.apply(
    lambda row: standardize_morale_score(
        row[collaboration_2020], 
        row[recommend_2020]
    ), axis=1
)

# For 2021, we only have collaboration
df_2021_clean['morale_score'] = df_2021_clean[collaboration_2021].apply(standardize_morale_score)

print(f"\nMorale scores in 2020: {df_2020_clean['morale_score'].describe()}")
print(f"Morale scores in 2021: {df_2021_clean['morale_score'].describe()}")

# Combine the datasets with a year identifier
df_2020_clean['year'] = 2020
df_2021_clean['year'] = 2021

# Select only the columns we need for analysis
columns_needed = [
    'Response ID', 
    'work_type_standardized', 
    'productivity_score', 
    'morale_score', 
    'year'
]

df_combined = pd.concat([
    df_2020_clean[columns_needed],
    df_2021_clean[columns_needed]
], ignore_index=True)

print(f"\nCombined dataset shape: {df_combined.shape}")
print(f"Combined dataset missing values: {df_combined.isnull().sum()}")
print(f"\nWork types in combined dataset: {df_combined['work_type_standardized'].value_counts()}")
print(f"\nSummary of productivity scores by work type:")
print(df_combined.groupby('work_type_standardized')['productivity_score'].describe())
print(f"\nSummary of morale scores by work type:")
print(df_combined.groupby('work_type_standardized')['morale_score'].describe())

# Export the cleaned dataset
df_combined.to_csv('/home/steodhiambo/WORK -ANALYSIS/cleaned_dashboard_data.csv', index=False)

print("\n=== STEP 2 COMPLETE ===")
print("Cleaned dataset exported as 'cleaned_dashboard_data.csv'")
print("Dataset includes standardized work types, productivity scores, and morale scores for analysis.")