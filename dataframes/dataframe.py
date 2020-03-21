import pandas as pd

pd.set_option('display.max_columns', 200)


# for printing all column names
def print_all_df_column_names(dataframe):
    column_names = ''
    for col in dataframe:
        print(col)
        column_names = column_names + "\'" + col + "\'" + ', '
    print('\n')
    print("column_names: ", column_names)


location = "/home/abrar/data_analysis_with_python/dataframes/test_data/fake_job_postings.csv"
# df = pd.read_csv(location, header='none')
df = pd.read_csv(location)

headers = ['job_id', 'title', 'location', 'department', 'salary_range', 'company_profile', 'description',
           'requirements', 'benefits', 'telecommuting', 'has_company_logo', 'has_questions', 'employment_type',
           'required_experience', 'required_education', 'industry', 'function', 'fraudulent']

# set headers
df.header = headers

# show only n rows
print(df.head(5))
print('\n')

# show types of data in each column
print(df.dtypes)
print('\n')

# show stats on df
print(df.describe())
print('\n')

# show stats on all columns even object type ones
print(df.describe(include='all'))
print('\n')
