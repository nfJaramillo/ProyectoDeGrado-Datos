import pandas as pd
import numpy as np

# Withdrawals

# Convert timestamp to year and month
withdrawals = pd.read_csv('Datos/withdrawals.csv')
withdrawals['date'] =  pd.to_datetime(withdrawals['timestamp'],unit='s') 
withdrawals['month'] = withdrawals['date'].dt.month
withdrawals['year'] = withdrawals['date'].dt.year
withdrawals['date'] = withdrawals['year'].astype(str) + '-' + withdrawals['month'].astype(str)
withdrawals['date'] = pd.to_datetime(withdrawals['date'])

# Set value

withdrawals['input'] = withdrawals['input'].str.replace('000000000000000000000000', '-' )
withdrawals['input'] = withdrawals['input'].str.split('-').str[1]
withdrawals['value'] = np.where((withdrawals.input == '910cbd523d972eb0a6f4cae4618ad62622b39dbf') , 10, 
np.where((withdrawals.input == 'a160cdab225685da1d56aa342ad8841c3b53f291')  , 100, 
np.where((withdrawals.input == '') & (withdrawals.to == '0x910cbd523d972eb0a6f4cae4618ad62622b39dbf') , 10, 
np.where((withdrawals.input == '') & (withdrawals.to == '0xa160cdab225685da1d56aa342ad8841c3b53f291') , 100, 0))))
withdrawals['toFinal'] = withdrawals['input']
withdrawals['toFinal'] = np.where((withdrawals.toFinal == '') , withdrawals.to, '0x'+ withdrawals.toFinal)
withdrawals.to_csv('Datos/withdrawalsTest.csv')

# Group by to 
gbtw = withdrawals.groupby(['date','to'])['value'].sum().reset_index(name='value')
gbtw = gbtw.pivot_table('value', ['date'],'to')
gbtw = gbtw.fillna(0).astype('int64')
gbtw = gbtw.cumsum() 
gbtw.sort_values(by='date')
gbtw.to_csv('Datos/withdrawalsToRouters(video).csv')

# Group by to final
gbtw = withdrawals.groupby(['date','toFinal'])['value'].sum().reset_index(name='value')
gbtw = gbtw.pivot_table('value', ['date'],'toFinal')
gbtw = gbtw.fillna(0).astype('int64')
gbtw = gbtw.cumsum() 
gbtw.sort_values(by='date')
gbtw.to_csv('Datos/withdrawalsToFinal(video).csv')

# Group by to NOT ACCUMULATIVE
gbtwna = withdrawals.groupby(['date','to'])['value'].sum().reset_index(name='value')
gbtwna = gbtwna.pivot_table('value', ['date'],'to')
gbtwna = gbtwna.fillna(0).astype('int64')
gbtwna.sort_values(by='date')
gbtwna.to_csv('Datos/withdrawalsToNotAcc(video).csv')

# Group by to final NOT ACCUMULATIVE
gbtwna = withdrawals.groupby(['date','toFinal'])['value'].sum().reset_index(name='value')
gbtwna = gbtwna.pivot_table('value', ['date'],'toFinal')
gbtwna = gbtwna.fillna(0).astype('int64')
gbtwna.sort_values('date')
gbtwna.to_csv('Datos/withdrawalsToFinalNotAcc(video).csv')


# Group by from 
gbfw = withdrawals.groupby(['date','from'])['value'].sum().reset_index(name='value')
gbfw = gbfw.pivot_table('value', ['date'],'from')
gbfw = gbfw.fillna(0).astype('int64')
gbfw = gbfw.cumsum() 
gbfw.sort_values(by='date')
gbfw.to_csv('Datos/withdrawalsFrom(preVideo).csv')

# Deposits

# Convert timestamp to year and month
deposits = pd.read_csv('Datos/deposits.csv')
deposits['date'] =  pd.to_datetime(deposits['timestamp'],unit='s') 
deposits['month'] = deposits['date'].dt.month
deposits['year'] = deposits['date'].dt.year
deposits['date'] = deposits['year'].astype(str) + '-' + deposits['month'].astype(str)
deposits['date'] = pd.to_datetime(deposits['date'])

# Set value
deposits['value'] = deposits['value'].astype('float') / 1000000000000000000
deposits['value'] = deposits['value'].astype('int') 

# Set final destination
deposits['toFinal'] =deposits['input'].str.replace('000000000000000000000000', '-' )
deposits['toFinal'] = '0x' + deposits['toFinal'].str.split('-').str[1].str[:40]
deposits['toFinal'] = np.where(deposits.toFinal.isnull()  , deposits.to, deposits.toFinal)
# Work in progres...

# Group by to 
gbtd = deposits.groupby(['date','to'])['value'].sum().reset_index(name='value')
gbtd = gbtd.pivot_table('value', ['date'],'to')
gbtd = gbtd.fillna(0).astype('int64')
gbtd = gbtd.cumsum() 
gbtd.sort_values(by='date')
gbtd.to_csv('Datos/depositsToRouters(video).csv')

# Group by final
gbtd = deposits.groupby(['date','toFinal'])['value'].sum().reset_index(name='value')
gbtd = gbtd.pivot_table('value', ['date'],'toFinal')
gbtd = gbtd.fillna(0).astype('int64')
gbtd = gbtd.cumsum() 
gbtd.sort_values(by='date')
gbtd.to_csv('Datos/depositsToFinal(video).csv')


# Group by to (Not acumulative)
gbtdna = deposits.groupby(['date','to'])['value'].sum().reset_index(name='value')
gbtdna = gbtdna.pivot_table('value', ['date'],'to')
gbtdna = gbtdna.fillna(0).astype('int64')
gbtdna.sort_values('date')
gbtdna.to_csv('Datos/depositsToNotAcc(video).csv')

# Group by final (Not acumulative)
gbtdna = deposits.groupby(['date','toFinal'])['value'].sum().reset_index(name='value')
gbtdna = gbtdna.pivot_table('value', ['date'],'toFinal')
gbtdna = gbtdna.fillna(0).astype('int64') 
gbtdna.sort_values('date')
gbtdna.to_csv('Datos/depositsToFinalNotAcc(video).csv')




# Group by from 
gbfd = deposits.groupby(['date','from'])['value'].sum().reset_index(name='value')
gbfd = gbfd.pivot_table('value', ['date'],'from')
gbfd = gbfd.fillna(0).astype('int64')
gbfd = gbfd.cumsum() 
gbfd.sort_values(by='date')
gbfd.to_csv('Datos/depositsFrom(preVideo).csv')
