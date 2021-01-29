import pandas as pd
df1 = pd.read_csv('/home/cuip/Mobility-Simulation/CARTA Ridership Data/RIDERSHIP BY ROUTE AND STOP.XLSX - Temporary_Query_Detail.csv') 
df2 = pd.read_csv('/home/cuip/Mobility-Simulation/CARTA Ridership Data/stops.csv') 

df = df1.merge(df2, on='Latitude')
print(df)
df.to_csv('mergedFile.csv')