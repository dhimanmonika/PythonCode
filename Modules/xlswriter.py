import xlsxwriter
import random


workbook=xlsxwriter.Workbook('xlsSample.xlsx')
worksheet_data=workbook.add_worksheet('data')
worksheet_analysis=workbook.add_worksheet('analysis')


def fill_columns(columns=[],startCell=0,endCell=0,worksheet=None):
    for column in columns:
        worksheet_analysis.write_column(column+str(startCell)+":"+column+str(endCell),random.sample(range(10),(endCell-startCell+1)))
    workbook.close()

fill_columns(
    columns=["A","B","C","D"],
    startCell=1,
    endCell=10,
    worksheet=worksheet_analysis

)
