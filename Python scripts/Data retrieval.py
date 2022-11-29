from re import T
import requests
import json
import pandas as pd
from IPython.display import display
import time

# Script para traer todos los datos del subgrafo, sin duplicados y organizados de mas a menos reciente.

# Variables que guardara el timestamp actual y que luego se remplazara por el ultimo traido en cada bloque de 1000
currentTimeStampDeposits = int(time.time())
currentTimeStampWithdrawals = int(time.time())
# Dataframes vacios sobre los cuales se añadiran los registros 
df_deposits = pd.DataFrame()
df_withdrawals = pd.DataFrame()
done = False
# URL para la peticion a theGraph
url = 'https://api.studio.thegraph.com/query/33393/proyectodegrado/0.24'

# Loop en donde se accede a los datos en el subgrafo en grupos de 1000
while True:

  # Querry para traer todos los datos de los deposits y withdrawals, organizados de mas a menos recientes donde su timestamp es igual o menor al ultimo registrado
  query = """query ($timeStampDeposits: Int, $timeStampWithdrawals: Int){
      deposits(
        first: 1000
        orderBy: timestamp
        orderDirection: desc
        where: {timestamp_lte: $timeStampDeposits}
      ) {
        id
        from
        to
        value
        gasLimit
        gasPrice
        timestamp
        input
      }
      withdrawals(
        first: 1000
        orderBy: timestamp
        orderDirection: desc
        where: {timestamp_lte: $timeStampWithdrawals}
      ) {
        id
        from
        to
        value
        gasLimit
        gasPrice
        timestamp
        input
      }
    }"""

  # Se asignan las variables de los timestamps al querry
  variables = {'timeStampDeposits': currentTimeStampDeposits, 'timeStampWithdrawals' : currentTimeStampWithdrawals}

  # Se realiza la peticion al thegraph
  r = requests.post(url, json={'query': query, 'variables': variables})

  # Se imprime el codigo de respuesta de la peticion para verificar su funcionamiento durante la ejecucion
  print("Codigo de respuesta de la peticion: " + str(r.status_code))
  # De ser encesario se puede imprimir lo que devuelve la peticion para analizar errores que se puedan dar
  #print(r.text)

  # Se carga la informacion
  json_data = json.loads(r.text)

  # Si la ultima peticion habia tenido 5 o menos registros se terminara la ejecion en este punto, pues podria quedar en un loop si los 5 tienen el mismo timestamp
  if done:
    break

  if(len(json_data['data']['deposits']) <= 5 and len(json_data['data']['withdrawals']) <= 5 )  :
    done = True

  # Si la peticion no tienen registros, no se procedera 
  if(len(json_data['data']['deposits']) == 0 and len(json_data['data']['withdrawals']) == 0 )  :
    break
  
  # Se guardaran los datos en dataframes, de concatenaran a los datos anteriores, se eliminaran los duplicados y los ids se acomodarn a la concatenacion
  df_data_deposits = json_data['data']['deposits']
  df_data_withdrawals = json_data['data']['withdrawals']
  df_depositsTemp = pd.DataFrame(df_data_deposits)
  df_withdrawalsTemp = pd.DataFrame(df_data_withdrawals)
  df_deposits = pd.concat([df_deposits,df_depositsTemp], ignore_index=True).drop_duplicates().reset_index(drop=True)
  df_withdrawals = pd.concat([df_withdrawals,df_withdrawalsTemp], ignore_index=True).drop_duplicates().reset_index(drop=True)

  # Se actualizan los timeStamps con los ultimos traidos en el  querry
  currentTimeStampDeposits = int(df_deposits.iloc[-1].get("timestamp"))
  currentTimeStampWithdrawals = int(df_withdrawals.iloc[-1].get("timestamp"))

# Al finalizar el ciclo, se almacenaran los datos en .csv
print("Guardando datos en csv")
df_deposits.to_csv('deposits.csv')
df_withdrawals.to_csv('withdrawals.csv')
print("Datos guardados")
