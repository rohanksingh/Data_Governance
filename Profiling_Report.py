import pandas as pd 
from ydata_profiling import ProfileReport

df= pd.read_csv('mtcars.csv')
profile=ProfileReport(df, title='Data Profiling Report')
profile.to_file('data_profiling_report.html')