import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Load the cleaned dataset
df = pd.read_csv('/home/steodhiambo/WORK -ANALYSIS/cleaned_dashboard_data.csv')

print("=== STEP 3: HYPOTHESIS TESTING ===")

print("\nDataset loaded with shape:", df.shape)
print("\nWork type distribution:")
print(df['work_type_standardized'].value_counts())

# Test Hypothesis 1: Remote work increases productivity compared to in-office work
print("\n" + "="*60)
print("HYPOTHESIS 1: Remote work increases productivity compared to in-office work")
print("="*60)

# Compare productivity between remote and in-office
remote_prod = df[df['work_type_standardized'] == 'Remote']['productivity_score']
in_office_prod = df[df['work_type_standardized'] == 'In-Office']['productivity_score']

print(f"Remote productivity mean: {remote_prod.mean():.2f}")
print(f"In-Office productivity mean: {in_office_prod.mean():.2f}")
print(f"Difference (Remote - In-Office): {remote_prod.mean() - in_office_prod.mean():.2f}")

# Perform t-test
t_stat, p_val = stats.ttest_ind(remote_prod.dropna(), in_office_prod.dropna())
print(f"T-test p-value: {p_val:.4f}")
if p_val < 0.05:
    print("Result: SIGNIFICANT difference in productivity between remote and in-office work")
    if remote_prod.mean() > in_office_prod.mean():
        print("Supports H1: Remote work has higher productivity")
    else:
        print("Does NOT support H1: In-office work has higher productivity")
else:
    print("Result: NO significant difference in productivity between remote and in-office work")
    print("Cannot confirm or reject H1")

# Test Hypothesis 2: Remote work decreases employee morale due to reduced collaboration
print("\n" + "="*60)
print("HYPOTHESIS 2: Remote work decreases employee morale due to reduced collaboration")
print("="*60)

# Compare morale between remote and in-office
remote_morale = df[df['work_type_standardized'] == 'Remote']['morale_score']
in_office_morale = df[df['work_type_standardized'] == 'In-Office']['morale_score']

print(f"Remote morale mean: {remote_morale.mean():.2f}")
print(f"In-Office morale mean: {in_office_morale.mean():.2f}")
print(f"Difference (Remote - In-Office): {remote_morale.mean() - in_office_morale.mean():.2f}")

# Perform t-test
t_stat, p_val = stats.ttest_ind(remote_morale.dropna(), in_office_morale.dropna())
print(f"T-test p-value: {p_val:.4f}")
if p_val < 0.05:
    print("Result: SIGNIFICANT difference in morale between remote and in-office work")
    if remote_morale.mean() < in_office_morale.mean():
        print("Supports H2: Remote work has lower morale")
    else:
        print("Does NOT support H2: Remote work has higher morale")
else:
    print("Result: NO significant difference in morale between remote and in-office work")
    print("Cannot confirm or reject H2")

# Test Hypothesis 3: Hybrid work models provide optimal balance between productivity and morale
print("\n" + "="*60)
print("HYPOTHESIS 3: Hybrid work models provide optimal balance between productivity and morale")
print("="*60)

hybrid_prod = df[df['work_type_standardized'] == 'Hybrid']['productivity_score']
hybrid_morale = df[df['work_type_standardized'] == 'Hybrid']['morale_score']

print("Productivity by work type:")
print(f"  Remote: {remote_prod.mean():.2f}")
print(f"  Hybrid: {hybrid_prod.mean():.2f}")
print(f"  In-Office: {in_office_prod.mean():.2f}")

print("Morale by work type:")
print(f"  Remote: {remote_morale.mean():.2f}")
print(f"  Hybrid: {hybrid_morale.mean():.2f}")
print(f"  In-Office: {in_office_morale.mean():.2f}")

# Check if hybrid is between remote and in-office for both metrics
hybrid_prod_between = (hybrid_prod.mean() > in_office_prod.mean()) and (hybrid_prod.mean() < remote_prod.mean()) or \
                      (hybrid_prod.mean() < in_office_prod.mean()) and (hybrid_prod.mean() > remote_prod.mean())

hybrid_morale_between = (hybrid_morale.mean() > in_office_morale.mean()) and (hybrid_morale.mean() < remote_morale.mean()) or \
                        (hybrid_morale.mean() < in_office_morale.mean()) and (hybrid_morale.mean() > remote_morale.mean())

print(f"Hybrid productivity is between remote and in-office: {hybrid_prod_between}")
print(f"Hybrid morale is between remote and in-office: {hybrid_morale_between}")

if hybrid_prod_between and hybrid_morale_between:
    print("Supports H3: Hybrid work provides a balance between remote and in-office")
else:
    print("Does NOT support H3: Hybrid work does not provide an optimal balance")

# Test Hypothesis 4: Collaboration effectiveness is highest in in-office settings
print("\n" + "="*60)
print("HYPOTHESIS 4: Collaboration effectiveness is highest in in-office settings")
print("="*60)

# Since morale_score includes collaboration, we'll use that as a proxy for collaboration effectiveness
print("Collaboration/morale by work type:")
print(f"  In-Office: {in_office_morale.mean():.2f}")
print(f"  Hybrid: {hybrid_morale.mean():.2f}")
print(f"  Remote: {remote_morale.mean():.2f}")

if in_office_morale.mean() > hybrid_morale.mean() and in_office_morale.mean() > remote_morale.mean():
    print("Supports H4: In-office has highest collaboration/morale")
else:
    print("Does NOT support H4: In-office does not have highest collaboration/morale")

# Additional analysis: Correlation between productivity and morale
print("\n" + "="*60)
print("ADDITIONAL ANALYSIS: Morale-Productivity Correlation")
print("="*60)

# Calculate correlation between productivity and morale
correlation = df[['productivity_score', 'morale_score']].corr()
print("Overall correlation between productivity and morale:")
print(correlation)

# Calculate correlation by work type
for work_type in df['work_type_standardized'].unique():
    subset = df[df['work_type_standardized'] == work_type][['productivity_score', 'morale_score']].dropna()
    if len(subset) > 2:  # Need at least 3 points for correlation
        corr_val = subset['productivity_score'].corr(subset['morale_score'])
        print(f"Correlation in {work_type}: {corr_val:.3f}")

# Summary table of means by work type
print("\n" + "="*60)
print("SUMMARY TABLE: Means by Work Type")
print("="*60)
summary_table = df.groupby('work_type_standardized')[['productivity_score', 'morale_score']].mean()
summary_table['count'] = df.groupby('work_type_standardized').size()
print(summary_table)

print("\n" + "="*60)
print("HYPOTHESIS TESTING SUMMARY")
print("="*60)
print("H1 (Remote increases productivity):", "SUPPORTED" if remote_prod.mean() > in_office_prod.mean() else "NOT SUPPORTED")
print("H2 (Remote decreases morale):", "SUPPORTED" if remote_morale.mean() < in_office_morale.mean() else "NOT SUPPORTED")
print("H3 (Hybrid provides optimal balance):", "SUPPORTED" if hybrid_prod_between and hybrid_morale_between else "NOT SUPPORTED")
print("H4 (In-office has highest collaboration):", "SUPPORTED" if in_office_morale.mean() > hybrid_morale.mean() and in_office_morale.mean() > remote_morale.mean() else "NOT SUPPORTED")

print("\n=== STEP 3 COMPLETE ===")
print("Hypothesis testing completed with statistical analysis.")