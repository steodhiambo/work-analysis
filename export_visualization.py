import pandas as pd

# Load the cleaned dataset from previous step
df = pd.read_csv('/home/steodhiambo/WORK -ANALYSIS/cleaned_dashboard_data.csv')

print("=== STEP 4: EXPORT FOR VISUALIZATION ===")
print(f"Dataset shape: {df.shape}")

# Verify the data has all necessary columns for visualization
required_columns = ['Response ID', 'work_type_standardized', 'productivity_score', 'morale_score', 'year']
print(f"Required columns present: {all(col in df.columns for col in required_columns)}")

print("\nDataset preview:")
print(df.head())

print("\nDataset info:")
print(df.info())

print("\nWork type distribution:")
print(df['work_type_standardized'].value_counts())

print("\nProductivity score statistics:")
print(df['productivity_score'].describe())

print("\nMorale score statistics:")
print(df['morale_score'].describe())

# Export the final dataset for visualization
df.to_csv('/home/steodhiambo/WORK -ANALYSIS/final_dashboard_data.csv', index=False)

print(f"\nFinal dataset exported as 'final_dashboard_data.csv' with shape {df.shape}")
print("File is ready for visualization in PromptBI.")

print("\n=== STEP 4 COMPLETE ===")
print("Dataset exported successfully for dashboard creation.")