# Remote Work Productivity & Morale Analysis

A comprehensive data analysis project examining the impact of remote work arrangements on employee productivity and morale using survey data from 2020-2021.

## 📊 Project Overview

This project analyzes over 3,000 survey responses to understand how different work arrangements (remote, hybrid, in-office) affect employee productivity and morale. The analysis provides data-driven insights and policy recommendations for post-pandemic work arrangements.

### Key Findings
- **Remote workers report 77% higher productivity** compared to in-office workers
- **Remote work enhances employee morale** contrary to common assumptions
- **Hybrid models offer balanced benefits** between productivity and collaboration
- **Strong positive correlation** between employee morale and productivity

## 🗂️ Project Structure

```
WORK-ANALYSIS/
├── data/
│   ├── 2020_rws.csv                    # 2020 Remote Work Survey data
│   ├── 2021_rws.csv                    # 2021 Remote Work Survey data
│   ├── cleaned_dashboard_data.csv      # Processed data for analysis
│   └── final_dashboard_data.csv        # Final dataset for visualization
├── scripts/
│   ├── data_understanding.py           # Initial data exploration
│   ├── data_understanding_final.py     # Comprehensive data analysis
│   ├── data_cleaning_feature_engineering.py  # Data preprocessing
│   ├── hypothesis_testing.py           # Statistical analysis
│   └── export_visualization.py         # Data export for dashboards
├── documentation/
│   ├── dashboard_creation_instructions.txt  # Dashboard setup guide
│   ├── insight_synthesis.txt           # Key findings summary
│   ├── policy_recommendation.txt       # Evidence-based policy recommendations
│   └── final_review.txt               # Complete project validation
└── README.md                          # This file
```

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- pandas
- numpy
- scipy
- matplotlib/seaborn (for visualizations)

### Installation
1. Clone the repository:
```bash
git clone git@github.com:steodhiambo/work-analysis.git
cd work-analysis
```

2. Install required packages:
```bash
pip install pandas numpy scipy matplotlib seaborn
```

### Running the Analysis
Execute the scripts in order:

1. **Data Understanding**:
```bash
python data_understanding.py
python data_understanding_final.py
```

2. **Data Cleaning & Feature Engineering**:
```bash
python data_cleaning_feature_engineering.py
```

3. **Statistical Analysis**:
```bash
python hypothesis_testing.py
```

4. **Export for Visualization**:
```bash
python export_visualization.py
```

## 📈 Analysis Methodology

### 1. Data Understanding
- Loaded and examined 2020 and 2021 remote work survey datasets
- Identified key variables for work type, productivity, and morale
- Analyzed data quality and completeness

### 2. Data Cleaning & Feature Engineering
- Standardized work types into three categories: In-Office, Hybrid, Remote
- Created productivity scores on a consistent scale (-40 to +50)
- Engineered morale scores from collaboration and recommendation metrics
- Handled missing values and duplicates

### 3. Hypothesis Testing
Four main hypotheses were tested using statistical methods:

- **H1**: Remote work increases productivity ✅ **SUPPORTED** (p < 0.001)
- **H2**: Remote work decreases morale ❌ **NOT SUPPORTED** (remote has higher morale)
- **H3**: Hybrid work provides optimal balance ✅ **SUPPORTED**
- **H4**: In-office has highest collaboration ❌ **NOT SUPPORTED** (remote has highest morale)

### 4. Statistical Results
- **Sample Size**: 3,019 total responses (1,507 from 2020, 1,512 from 2021)
- **Work Type Distribution**: 
  - In-Office: 1,379 (45.7%)
  - Hybrid: 987 (32.7%)
  - Remote: 653 (21.6%)
- **Statistical Significance**: All major findings significant at p < 0.001

## 📊 Key Insights

### 1. Remote Work Productivity Advantage
- Remote productivity score: **21.11**
- In-office productivity score: **11.91**
- **77% improvement** for remote workers

### 2. Enhanced Employee Morale
- Remote morale score: **4.24/5**
- In-office morale score: **3.58/5**
- **18% higher morale** for remote workers

### 3. Hybrid Model Balance
- Hybrid productivity: **19.18** (balanced between remote and in-office)
- Hybrid morale: **3.83** (good satisfaction level)

### 4. Morale-Productivity Correlation
- Overall correlation: **r = 0.245**
- Consistent positive relationship across all work types

### 5. Year-over-Year Improvement
- 2020 average productivity: **14.18**
- 2021 average productivity: **18.41**
- **30% improvement** from 2020 to 2021

## 🏢 Policy Recommendations

Based on the analysis, we recommend a **Flexible Hybrid Model**:

### Primary Recommendation
- **3-2 Model**: 3 days remote, 2 days in office
- **4-1 Model**: 4 days remote, 1 day in office (for suitable roles)
- **Full Remote**: Available for roles not requiring in-person collaboration

### Implementation Benefits
- **Productivity**: Maintain high productivity levels (19.18 for hybrid)
- **Morale**: Preserve employee satisfaction (3.83 for hybrid)
- **Flexibility**: Attract and retain talent
- **Cost Savings**: Reduce office space requirements

### Success Metrics
- Maintain productivity scores above 16.30 baseline
- Maintain morale scores above 3.82 baseline
- Monitor employee satisfaction and retention rates

## 📋 Dashboard Components

The analysis includes instructions for creating an interactive dashboard with:

- **KPI Cards**: Total responses, average productivity, average morale
- **Productivity Charts**: By work type and year-over-year trends
- **Morale Analysis**: Satisfaction levels across work arrangements
- **Correlation Plots**: Relationship between morale and productivity
- **Trend Analysis**: Changes from 2020 to 2021

## 🔍 Data Quality & Validation

- **Completeness**: 100% response rate for key variables
- **Consistency**: Standardized scales across years
- **Statistical Power**: Large sample sizes ensure reliable results
- **Validation**: Cross-checked findings across multiple metrics

## 📚 Files Description

### Data Files
- `2020_rws.csv`: Original 2020 survey data (1,507 responses, 73 columns)
- `2021_rws.csv`: Original 2021 survey data (1,512 responses, 109 columns)
- `cleaned_dashboard_data.csv`: Processed data with standardized variables
- `final_dashboard_data.csv`: Final dataset optimized for visualization

### Analysis Scripts
- `data_understanding.py`: Initial data exploration and column identification
- `data_understanding_final.py`: Comprehensive data profiling
- `data_cleaning_feature_engineering.py`: Data preprocessing and feature creation
- `hypothesis_testing.py`: Statistical analysis and hypothesis testing
- `export_visualization.py`: Data preparation for dashboard creation

### Documentation
- `dashboard_creation_instructions.txt`: Step-by-step dashboard setup
- `insight_synthesis.txt`: Summary of key findings
- `policy_recommendation.txt`: Evidence-based policy recommendations
- `final_review.txt`: Complete project validation and quality assurance

## 🤝 Contributing

This project was completed as a collaborative analysis with defined team roles:
- **Data Analyst**: Data loading and initial exploration
- **QA/Hypothesis Lead**: Data validation and statistical testing
- **Dashboard Architect**: Visualization design and implementation
- **Policy Lead**: Translation of findings into actionable recommendations

## 📄 License

This project is available for educational and research purposes. Please cite appropriately if using the methodology or findings.

## 📞 Contact

For questions about the analysis methodology or findings, please refer to the documentation files or create an issue in this repository.

---

**Project Completion**: All 8 analysis steps completed with statistical validation and actionable insights for organizational decision-making.