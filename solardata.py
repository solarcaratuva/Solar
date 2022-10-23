# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 13:05:00 2022

@author: Viv Hughes
"""

import pandas as pd
import matplotlib as plt

july = pd.read_csv(r'C:\Users\Viv Hughes\Downloads\solar_july_2020_data.csv')

# columns are series
dni = july.loc[:, 'DNI']
#clearsky.dni
#cloudtype

# gets the averages for each hour from 8 am to 6 pm
dniavg = [july.loc[0:32, 'DNI'].mean(),
           july.loc[33:63, 'DNI'].mean(),
           july.loc[64:94, 'DNI'].mean(),
           july.loc[95:125, 'DNI'].mean(),
           july.loc[126:156, 'DNI'].mean(),
           july.loc[157:187, 'DNI'].mean(),
           july.loc[188:218, 'DNI'].mean(),
           july.loc[219:249, 'DNI'].mean(),
           july.loc[250:280, 'DNI'].mean(),
           july.loc[281:311, 'DNI'].mean(),
           july.loc[312:342, 'DNI'].mean()
           ]
           
#dni.avg.plot()
dni.plot(kind = 'scatter', x = 'Hour', y = 'DNI')
plt.show()