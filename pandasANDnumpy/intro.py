import pandas as pd
df = pd.read_csv('weather.csv')

print("max temperature :" ,df['Temperature'].max())

print("dates on which it rained :",df['EST'][df['Events']=='Rain'])

df.fillna(0, inplace=True)
print("average windspeed :",df['WindSpeedMPH'].mean())




