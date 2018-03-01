import pandas as pd

df=pd.read_excel('stock_data.xlsx',"Sheet1")

print(df)


def convert_people_cell(cell):
    if cell == "n.a.":
        return 'Sam Walton'
    return cell


def convert_price_cell(cell):
    if cell == "n.a.":
        return 50
    return cell


df = pd.read_excel("stock_data.xlsx", "Sheet1", converters={
    'people': convert_people_cell,
    'price': convert_price_cell
})
print("\nreading with converters/replacing values \n")
print(df)


#Write two dataframes to two separate sheets in excel

print("\ntwo dataframes in two separate sheets of excel\n")


df_stocks = pd.DataFrame({
    'tickers': ['GOOGL', 'WMT', 'MSFT'],
    'price': [845, 65, 64 ],
    'pe': [30.37, 14.26, 30.97],
    'eps': [27.82, 4.61, 2.12]
})

df_weather =  pd.DataFrame({
    'day': ['1/1/2017','1/2/2017','1/3/2017'],
    'temperature': [32,35,28],
    'event': ['Rain', 'Sunny', 'Snow']
})


with pd.ExcelWriter('stocks_weather.xlsx') as writer:
    df_stocks.to_excel(writer, sheet_name="stocks")
    df_weather.to_excel(writer, sheet_name="weather")






