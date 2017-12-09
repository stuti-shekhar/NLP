# import modules
import pandas as pd

# Import the excel file and call it xls_file
xls_file = pd.ExcelFile('../data/example.xls')
xls_file

<pandas.io.excel.ExcelFile at 0x111912be0>

# View the excel file's sheet names
xls_file.sheet_names

['Sheet1']

# Load the xls file's Sheet1 as a dataframe
df = xls_file.parse('Sheet1')
df
