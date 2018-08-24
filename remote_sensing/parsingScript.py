import pandas as pd

dates = pd.to_datetime(pd.Series(['20010101', '20010331']), format = '%Y%m%d')
x = dates.dt.strftime('%Y%m%d')
print(x[0])

x = input('What the fuuuuck???')
print(x)
