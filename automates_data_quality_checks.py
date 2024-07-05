import pandas as pd
import great_expectations as ge

def automate_data_quality_check(file_path):
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(file_path)
    
    # Convert the Pandas DataFrame to a Great Expectations DataFrame
    ge_df = ge.from_pandas(df)
    
    # Perform data quality checks
    results = {
        "expect_column_values_to_not_be_null": ge_df.expect_column_values_to_not_be_null('cyl'),
        "expect_column_values_to_be_unique": ge_df.expect_column_values_to_be_unique('cyl')
    }
    
    # Save results or trigger alerts based on findings
    validation_results = ge_df.validate()

    if validation_results['success']:
        print("Data validation passed!")
    else:
        print("Data validation failed!")
        for result in validation_results['results']:
            if not result['success']:
                print(f"Expectation {result['expectation_config']['expectation_type']} failed for column {result['expectation_config']['kwargs']['column']}")


# Example usage
automate_data_quality_check('mtcars.csv')
