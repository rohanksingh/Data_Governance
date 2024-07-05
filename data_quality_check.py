# data loading and inspection 
import pandas as pd

df = pd.read_csv('mtcars.csv')

print(df.head())

# Basic data checks 
# check for null values 

null_counts= df.isnull().sum()
print("Null Value Counts:")
print(null_counts)

# Check for data Types

data_types= df.dtypes

print("Data types:")
print(data_types)

# Data distribution and summary statistics 

# Generate summary statistics and check data distribution to identify outliers and anomalies

# Summary statistics 

summary_stats=df.describe
print("Summary statistics")
print(summary_stats)


# Data Consistency Checks 

# validate data consistency and uniqueness:

# check for duplicates:

duplicates_rows= df[df.duplicated()]
print("Duplicate rows:")
print(duplicates_rows)

# Check for unique Values:

unique_values= df['hp'].unique()

print("Unique values:")
print(unique_values)

# Custom data quality Rules

# Implement custom data quality rules based on specific requirements

# Example Rule: Check Range of Values

min_value = df['mpg'].min()
max_value= df['mpg'].max()
if min_value <0 or max_value > 100:
    print("Warning Values out of expected range")

# Data quality report generation
# Using pandas-profiling:

from pandas_profiling import ProfileReport

# Generate data profiling report 

profile= ProfileReport(df, title='Data Quality Report')
profile.to_file("data_quality_report.html")

# Automating Data quality checks 






