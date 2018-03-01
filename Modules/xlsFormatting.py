import xlsxwriter
import random


workbook=xlsxwriter.Workbook('xlsFormat.xlsx')
worksheet_analysis=workbook.add_worksheet('analysis')


def fill_columns(columns=[],startCell=0,endCell=0,worksheet=None):
    for column in columns:
        worksheet_analysis.write_column(column+str(startCell)+":"+column+str(endCell),random.sample(range(10),(endCell-startCell+1)))
    workbook.close()


def apply_format(columns=[],startCell=0,endCell=0,worksheet=None,format=None):
    for column in columns:
        worksheet_analysis.conditional_format(
            column + str(startCell) + ":" + column + str(endCell),
            {
                "type": "cell",
                "criteria": "<=5",
                "value": 5,
                "format": format
            }
        )

    workbook.close()






Success_cell=workbook.add_format(
    {
        "bg_color" : "#00ff00",
        "border" : 1
    }
)

fill_columns(
    columns=["A","B","C","D"],
    startCell=1,
    endCell=10,
    worksheet=worksheet_analysis

)
apply_format(
columns=["A","B","C","D"],
    startCell=1,
    endCell=10,
    worksheet=worksheet_analysis,
    format= Success_cell
)