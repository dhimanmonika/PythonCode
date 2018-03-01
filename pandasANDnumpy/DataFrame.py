import pandas as pd

df=pd.read_csv('weather_data.csv')

print(df)

# to get rows and cols
print("rows and columns  :", df.shape)

#to get top 2 rows of file
print("top 2 rows of file :",df.head(2))


#to get last 2 rows of file
print("last 2 rows of file :",df.tail(2))


#to get columns of file
print("columns :",df.columns)

#to get conditional output
print("day when temperature was max :",df['day'][df['temperature'] == df['temperature'].max()])

#to chnage index
df.set_index('day', inplace=True)
print(df)


#to reset index
df.reset_index(inplace=True)

