# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 16:03:05 2024

@author: Viv Hughes
"""

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

july23 = pd.read_csv(r'C:\Users\Viv Hughes\OneDrive - University of Virginia\Desktop\solar data\bolingGreen_july_data_23.csv')

plt.ion()
# columns are series
dni = july23.loc[:, 'dni']
cloud = july23.loc[:, 'cloud_opacity']
temp = july23. loc[:, 'air_temp']

# getting dni avg for each hour from 8am to 6pm
dniavg = [july23.loc[2:32, 'dni'].mean(),
           july23.loc[33:63, 'dni'].mean(),
           july23.loc[64:94, 'dni'].mean(),
           july23.loc[95:125, 'dni'].mean(),
           july23.loc[126:156, 'dni'].mean(),
           july23.loc[157:187, 'dni'].mean(),
           july23.loc[188:218, 'dni'].mean(),
           july23.loc[219:249, 'dni'].mean(),
           july23.loc[250:280, 'dni'].mean(),
           july23.loc[281:311, 'dni'].mean(),
           july23.loc[312:342, 'dni'].mean()
           ]

# getting hourly cloud opactiy avg
cloudavg = [july23.loc[2:32, 'cloud_opacity'].mean(),
           july23.loc[33:63, 'cloud_opacity'].mean(),
           july23.loc[64:94, 'cloud_opacity'].mean(),
           july23.loc[95:125, 'cloud_opacity'].mean(),
           july23.loc[126:156, 'cloud_opacity'].mean(),
           july23.loc[157:187, 'cloud_opacity'].mean(),
           july23.loc[188:218, 'cloud_opacity'].mean(),
           july23.loc[219:249, 'cloud_opacity'].mean(),
           july23.loc[250:280, 'cloud_opacity'].mean(),
           july23.loc[281:311, 'cloud_opacity'].mean(),
           july23.loc[312:342, 'cloud_opacity'].mean()
           ]

# getting hourly air temp avg
tempavg = [july23.loc[2:32, 'air_temp'].mean(),
           july23.loc[33:63, 'air_temp'].mean(),
           july23.loc[64:94, 'air_temp'].mean(),
           july23.loc[95:125, 'air_temp'].mean(),
           july23.loc[126:156, 'air_temp'].mean(),
           july23.loc[157:187, 'air_temp'].mean(),
           july23.loc[188:218, 'air_temp'].mean(),
           july23.loc[219:249, 'air_temp'].mean(),
           july23.loc[250:280, 'air_temp'].mean(),
           july23.loc[281:311, 'air_temp'].mean(),
           july23.loc[312:342, 'air_temp'].mean()
           ]

# basic dni avg vs hour plot
plt.plot([8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], dniavg, c='r', label = 'DNI Avg Per Hour')
plt.xlabel("Hour, In Military Time")
plt.ylabel("DNI")
plt.title('Avg DNI per Hour for All Boling Green 2023 Data')
plt.show()
# basic air temp avg vs hour plot
plt.plot([8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], tempavg, c='r', label = 'Air Temp Avg Per Hour')
plt.xlabel("Hour, In Military Time")
plt.ylabel("Air Temp (C)")
plt.title('Avg Air Temp per Hour for All Boling Green 2023 Data')
plt.show()
# how cloud opacity affects dni plot

plt.scatter(cloud, dni, color='r')
plt.xlabel('Cloud Opacity')
plt.ylabel('DNI')
plt.title('DNI due to Cloud Opacity')
plt.show()