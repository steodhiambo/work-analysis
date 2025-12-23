import pandas as pd

# Load the datasets with different encoding
df_2020 = pd.read_csv('/home/steodhiambo/WORK -ANALYSIS/2020_rws.csv', encoding='latin-1')
df_2021 = pd.read_csv('/home/steodhiambo/WORK -ANALYSIS/2021_rws.csv', encoding='latin-1')

print("=== STEP 1: DATA UNDERSTANDING ===")
print("\n2020 Dataset Shape:", df_2020.shape)
print("2021 Dataset Shape:", df_2021.shape)

print("\n=== KEY COLUMNS FOR ANALYSIS ===")
print("\n2020 Dataset - Important Columns:")
# Work type columns
print("- Work type: 'Thinking about your current job, how much of your time did you spend remote working last year?'")
print("- Preferred work type: 'How much of your time would you have preferred to work remotely last year?'")
print("- Post-pandemic preference: 'Imagine that COVID-19 is cured or eradicated. Going forward, how much of your time would you prefer to work remotely?'")

# Productivity columns
print("- Productivity: 'Please compare your productivity when you work remotely to when you work at your employers workplace. Roughly how productive are you, each hour, when you work remotely?'")

# Morale/collaboration columns
print("- Collaboration: 'I could easily collaborate with colleagues when working remotely'")
print("- Remote work recommendation: 'I would recommend remote working to others'")

print("\n2021 Dataset - Important Columns:")
# Work type columns
print("- Work type: 'Thinking about your current job, how much of your work time did you spend working remotely this year?'")
print("- Preferred work type: 'How much of your work time would you have preferred to work remotely so far this year?'")
print("- Post-pandemic preference: 'Imagine that COVID-19 is cured or eradicated. Going forward, how much of your work time would you prefer to work remotely?'")

# Productivity columns
print("- Productivity: 'Please compare your productivity when you work remotely to when you work at your employers workplace. Roughly how productive are you, each hour, when you work remotely?'")
print("- Manager productivity: 'Now think about the productivity of the employees you manage. Roughly how productive are the employees you manage, each hour, when they work remotely?'")

# Morale/collaboration columns
print("- Collaboration: 'I could easily collaborate with colleagues when working remotely'")
print("- Remote work policy sentiment: 'How do you feel about your employers remote working policy?'")

print("\n=== SAMPLE DATA ===")
print("\n2020 Sample:")
print(df_2020[['Response ID', 'Thinking about your current job, how much of your time did you spend remote working last year?', 
              'Please compare your productivity when you work remotely to when you work at your employers workplace. Roughly how productive are you, each hour, when you work remotely?',
              'Thinking about remote working last year, how strongly do you agree or disagree with the following statements? - I could easily collaborate with colleagues when working remotely']].head(2))

print("\n2021 Sample:")
print(df_2021[['Response ID', 'Thinking about your current job, how much of your work time did you spend working remotely this year?',
              'Please compare your productivity when you work remotely to when you work at your employers workplace. Roughly how productive are you, each hour, when you work remotely?',
              'Thinking about remote working in the last 6 months, how strongly do you agree or disagree with the following statements? - I could easily collaborate with colleagues when working remotely']].head(2))

print("\n=== COLUMN COUNT COMPARISON ===")
print(f"2020 has {len(df_2020.columns)} columns")
print(f"2021 has {len(df_2021.columns)} columns")
print(f"Unique columns in 2020: {set(df_2020.columns) - set(df_2021.columns)}")
print(f"Unique columns in 2021: {set(df_2021.columns) - set(df_2020.columns)}")