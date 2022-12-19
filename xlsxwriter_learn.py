import pandas as pd
import sqlite3
conn = sqlite3.connect('database_conti')

# Create a cursor instance
c = conn.cursor()

query = "SELECT * FROM TABLE_Conti"  # query to collect recors
df = pd.read_sql(query, conn)
# Create a Pandas dataframe from the data.
#df = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45]})

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Dati')

# Get the xlsxwriter objects from the dataframe writer object.
workbook  = writer.book
worksheet = writer.sheets['Dati']

# Get the dimensions of the dataframe.
(max_row, max_col) = df.shape

# Apply a conditional format to the required cell range.
worksheet.conditional_format(1, max_col, max_row, max_col,
                             {'type': '3_color_scale'})

# Close the Pandas Excel writer and output the Excel file.
writer.close()

# Commit changes
conn.commit()

# Close our connection
conn.close()