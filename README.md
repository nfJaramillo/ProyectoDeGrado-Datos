# ProyectoDeGrado-Datos

Este repositorio contiene 2 carpetas, una llamada Datos con diversos archivos .csv y otra llamada Python scripts con diversos archivos .py. A continuación, se explica cada uno de los archivos y scripts:

## Data retrieval.py
Aquí se extraen los datos con ayuda de GraphQL del subgrafo alojado en https://testnet.thegraph.com/explorer/subgraphs/7PonLjDmPw1tRU8rDxARsk5ziWjmtcPqQFVWzXSdP1mT?view=Overview y se guardan en 2 archivos .csv: deposits.csv y withdrawals.csv.

## Preprocessing data 1.py y Preprocessing data 2.py
Se transforman los datos extraídos en Data retrieval.py con ayuda de Pandas, tomando datos del receptor final del input data, generando agrupaciones por meses de las transacciones, entre otras cosas generando los demás archivos que permiten generar análisis en videos, gráficas y estadísticas.

## Video… .py
Todos estos scripts con ayuda de FFmpeg generan los siguientes videos:

Depósitos vs retiros a Smart Contracts Finales de Tornado Cash: https://youtu.be/hL5DigK8K8o

Top 10 Smart Contracts que depositaron a Tornado Cash (Acumulado): https://youtu.be/dXKwTilpxOs

Depósitos a Smart Contracts Routers de Tornado Cash (Acumulado): https://youtu.be/55Bn_Scrd0o

Depósitos a Smart Contracts Finales de Tornado Cash (Acumulado): https://youtu.be/DPB8eMwYSUA

Top 10 Smart Contracts que retiraron de Tornado Cash (Acumulado): https://youtu.be/8LkM6SCE3XE

Retiros de Smart Contracts Routers de Tornado Cash (Acumulado): https://youtu.be/4HPusxsVMR4

Retiros de Smart Contracts Finales de Tornado Cash (Acumulado): https://youtu.be/byjGh_aD3Ng

Finalmente se puede encontrar una presentación que resume todo el preoceso desde la extracción de los datos hasta las conclusiones en: 
https://www.canva.com/design/DAFTWVLKud4/9tS5EEbm74U-_CSp3XZtrw/view

Todo lo aquí contenido fue realizado como parte del proyecto de grado de Ingeniería de Sistemas y Computación en la Universidad de los Andes realizado por Nicolás Jaramillo y con Darío Ernesto Correal como asesor durante el periodo 2022-20.

