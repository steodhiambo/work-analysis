import pandas as pd

# Load the datasets with correct encoding
df_2020 = pd.read_csv('/home/steodhiambo/WORK -ANALYSIS/2020_rws.csv', encoding='latin-1')
df_2021 = pd.read_csv('/home/steodhiambo/WORK -ANALYSIS/2021_rws.csv', encoding='latin-1')

print("=== STEP 1: DATA UNDERSTANDING ===")
print("\n2020 Dataset Shape:", df_2020.shape)
print("2021 Dataset Shape:", df_2021.shape)

print("\n=== KEY COLUMNS IDENTIFIED FOR ANALYSIS ===")

# 2020 Key Columns
print("\n2020 Dataset - Important Columns:")
work_type_2020 = 'Thinking about your current job, how much of your time did you spend remote working last year?'
print(f"- Work type: '{work_type_2020}'")
pref_work_type_2020 = 'How much of your time would you have preferred to work remotely last year?'
print(f"- Preferred work type: '{pref_work_type_2020}'")
post_covid_pref_2020 = 'Imagine that COVID-19 is cured or eradicated. Going forward, how much of your time would you prefer to work remotely?'
print(f"- Post-pandemic preference: '{post_covid_pref_2020}'")

productivity_2020 = 'This question is about your productivity. Productivity means what you produce for each hour that you work. It includes the amount of work you achieve each hour, and the quality of your work each hour.  \nPlease compare your productivity when you work remotely to when you work at your employer\x92s workplace.  \nRoughly how productive are you, each hour, when you work remotely?'
print(f"- Productivity: '{productivity_2020}'")

collaboration_2020 = 'Thinking about remote working last year, how strongly do you agree or disagree with the following statements? - I could easily collaborate with colleagues when working remotely'
print(f"- Collaboration: '{collaboration_2020}'")

recommend_2020 = 'Thinking about remote working last year, how strongly do you agree or disagree with the following statements? - I would recommend remote working to others'
print(f"- Remote work recommendation: '{recommend_2020}'")

print(f"\nSample values for 2020 work type ({work_type_2020}):")
print(df_2020[work_type_2020].value_counts().head())

print(f"\nSample values for 2020 productivity ({productivity_2020}):")
print(df_2020[productivity_2020].value_counts().head())

print(f"\nSample values for 2020 collaboration ({collaboration_2020}):")
print(df_2020[collaboration_2020].value_counts().head())

# 2021 Key Columns
print("\n\n2021 Dataset - Important Columns:")
work_type_2021 = 'Thinking about your current job, how much of your work time have you spent working remotely this year?  If you work a 5 day week, each day of remote working equals 20% of your time.  '
print(f"- Work type: '{work_type_2021}'")
pref_work_type_2021 = 'How much of your work time would you have preferred to work remotely so far this year?  If you work a 5 day week, each day of remote working equals 20% of your time.  '
print(f"- Preferred work type: '{pref_work_type_2021}'")
post_covid_pref_2021 = 'Imagine that COVID-19 is cured or eradicated.   Going forward, how much of your work time would you prefer to work remotely?  If you work a 5 day week, each day of remote working equals 20% of your time.  '
print(f"- Post-pandemic preference: '{post_covid_pref_2021}'")

productivity_2021 = 'This question is about your productivity. Productivity means what you produce for each hour that you work. It includes the amount of work you achieve each hour, and the quality of your work each hour.    Please compare your productivity when you work remotely to when you work at your employer\x92s workplace.    Roughly how productive are you, each hour, when you work remotely?  '
print(f"- Productivity: '{productivity_2021}'")

manager_productivity_2021 = 'Now think about the productivity of the employees you manage.   Roughly how productive are the employees you manage, each hour, when they work remotely?  '
print(f"- Manager productivity: '{manager_productivity_2021}'")

collaboration_2021 = 'Thinking about remote working in the last 6 months, how strongly do you agree or disagree with the following statements?   Please select a single response per row   - I could easily collaborate with colleagues when working remotely'
print(f"- Collaboration: '{collaboration_2021}'")

policy_sentiment_2021 = 'How do you feel about your employer\x92s remote working policy?  '
print(f"- Remote work policy sentiment: '{policy_sentiment_2021}'")

print(f"\nSample values for 2021 work type ({work_type_2021}):")
print(df_2021[work_type_2021].value_counts().head())

print(f"\nSample values for 2021 productivity ({productivity_2021}):")
print(df_2021[productivity_2021].value_counts().head())

print(f"\nSample values for 2021 collaboration ({collaboration_2021}):")
print(df_2021[collaboration_2021].value_counts().head())

print("\n=== SUMMARY ===")
print("We have identified key columns in both datasets that will allow us to analyze:")
print("1. Work type patterns (remote, hybrid, in-office)")
print("2. Productivity comparisons between remote and in-office work")
print("3. Employee morale and collaboration effectiveness")
print("4. Preferences for future work arrangements")
print("5. Managerial perspectives on remote work (2021 only)")