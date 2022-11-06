# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 13:05:00 2022

@author: Viv Hughes
"""

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

july = pd.read_csv(r'C:\Users\Viv Hughes\Downloads\solar_july_2020_data.csv')

# columns are series
dni = july.loc[:, 'DNI']
clearskydni = july.loc[:, 'Clearsky DNI']
# cloudtype

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

clearskyavg = [july.loc[0:32, 'Clearsky DNI'].mean(),
           july.loc[33:63, 'Clearsky DNI'].mean(),
           july.loc[64:94, 'Clearsky DNI'].mean(),
           july.loc[95:125, 'Clearsky DNI'].mean(),
           july.loc[126:156, 'Clearsky DNI'].mean(),
           july.loc[157:187, 'Clearsky DNI'].mean(),
           july.loc[188:218, 'Clearsky DNI'].mean(),
           july.loc[219:249, 'Clearsky DNI'].mean(),
           july.loc[250:280, 'Clearsky DNI'].mean(),
           july.loc[281:311, 'Clearsky DNI'].mean(),
           july.loc[312:342, 'Clearsky DNI'].mean()
           ]
           
# dni.avg.plot()
# plt.plot(kind = 'scatter', x = 'Hour', y = 'DNI')
# plt.show()

# basic DNI vs. hourly plot
"""
plt.plot([8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], dniavg, c='r', label = 'DNI Avg Per Hour')
plt.xlabel("Hour, In Military Time")
plt.ylabel("DNI")
plt.show()
"""

# my attempt at plotting both DNI and Clearsky DNI on one plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot([8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], dniavg, c='r', label = 'DNI Avg Per Hour')
ax.plot([8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], clearskyavg, c='g', label = 'Clearsky DNI Avg Per Hour')
ax.set_xlabel('Hour in Military Time')
ax.set_ylabel('DNI')
plt.legend()
plt.show()