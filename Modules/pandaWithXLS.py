import pandas as pd
import xlsxwriter

df=pd.read_excel('xlsFormat.xlsx')
#print(df)
writer=pd.ExcelWriter('data.xlsx',engine='xlsxwriter')

df.to_excel(writer)
writer.save()