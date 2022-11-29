import pandas as pd

# Deposits

# Convert timestamp to year and month
deposits = pd.read_csv('Datos/depositsFrom(preVideo).csv')
deposits.drop('date', inplace=True, axis=1)
rows = len(deposits)
topDepositors = pd.DataFrame()

for i in range(rows):
    topDepositors = pd.concat([topDepositors,deposits.iloc[i].nlargest(10).to_frame().T])

topDepositors = topDepositors.fillna(0).astype('int64')
date = ['2019-12-01','2020-01-01','2020-02-01','2020-03-01','2020-04-01','2020-05-01','2020-06-01','2020-07-01','2020-08-01','2020-09-01'
,'2020-10-01','2020-11-01','2020-12-01','2021-01-01','2021-02-01','2021-03-01','2021-04-01','2021-05-01','2021-06-01','2021-07-01'
,'2021-08-01','2021-09-01','2021-10-01','2021-11-01','2021-12-01','2022-01-01','2022-02-01','2022-03-01','2022-04-01','2022-05-01'
,'2022-06-01','2022-07-01','2022-08-01','2022-09-01','2022-10-01','2022-11-01']
topDepositors.insert(0,'date',date)

topDepositors.to_csv('Datos/depositsFromTop(video).csv', index=False)
#print (topDepositors)


# Withdrawals

# Convert timestamp to year and month
deposits = pd.read_csv('Datos/withdrawalsFrom(preVideo).csv')
deposits.drop('date', inplace=True, axis=1)
rows = len(deposits)
topDepositors = pd.DataFrame()

for i in range(rows):
    topDepositors = pd.concat([topDepositors,deposits.iloc[i].nlargest(10).to_frame().T])

topDepositors = topDepositors.fillna(0).astype('int64')
date = ['2019-12-01','2020-01-01','2020-02-01','2020-03-01','2020-04-01','2020-05-01','2020-06-01','2020-07-01','2020-08-01','2020-09-01'
,'2020-10-01','2020-11-01','2020-12-01','2021-01-01','2021-02-01','2021-03-01','2021-04-01','2021-05-01','2021-06-01','2021-07-01'
,'2021-08-01','2021-09-01','2021-10-01','2021-11-01','2021-12-01','2022-01-01','2022-02-01','2022-03-01','2022-04-01','2022-05-01'
,'2022-06-01','2022-07-01','2022-08-01','2022-09-01','2022-10-01','2022-11-01']
topDepositors.insert(0,'date',date)

topDepositors.to_csv('Datos/withdrawalsFromTop(video).csv', index=False)
#print (topDepositors)