import pandas as pd

xls = pd.ExcelFile('file.xls')
df = xls.parse(sheet_name="Feuille1", index_col=None, na_values=['NA'], comment='')
df.to_csv('fileCsv.csv')
