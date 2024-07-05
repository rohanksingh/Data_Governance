import great_expectations as ge 
import pandas as pd


df= pd.read_csv('mtcars.csv')
df= ge.from_pandas(df)

df.expect_column_values_to_not_be_null('mpg')
df.expect_column_values_to_be_unique('Model')

validation_result= df.validate()

print(validation_result)