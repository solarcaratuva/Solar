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
dniavg = [july.loc[2:32, 'DNI'].mean(),
           july.loc[33:63, 'DNI'].mean(),
           july.loc[64:94, 'DNI'].mean(),
           july.loc[95:125, 'DNI'].mean(),
           july.loc[126:156, 'DNI'].mean(),
           july.loc[157:187, 'DNI'].mean(),
           july.loc[188:218, 'DNI'].mean(),
           july.loc[219:249, 'DNI'].mean(),
           july.loc[250:280, 'DNI'].mean(),
           july.loc[281:311, 'DNI'].mean(),
           july.loc[312:342, 'DNI'].mean(), 
           july.loc[343:373, 'DNI'].mean()
           ]

clearskyavg = [july.loc[2:32, 'Clearsky DNI'].mean(),
           july.loc[33:63, 'Clearsky DNI'].mean(),
           july.loc[64:94, 'Clearsky DNI'].mean(),
           july.loc[95:125, 'Clearsky DNI'].mean(),
           july.loc[126:156, 'Clearsky DNI'].mean(),
           july.loc[157:187, 'Clearsky DNI'].mean(),
           july.loc[188:218, 'Clearsky DNI'].mean(),
           july.loc[219:249, 'Clearsky DNI'].mean(),
           july.loc[250:280, 'Clearsky DNI'].mean(),
           july.loc[281:311, 'Clearsky DNI'].mean(),
           july.loc[312:342, 'Clearsky DNI'].mean(), 
           july.loc[343:373, 'Clearsky DNI'].mean()
           ]

# basic DNI vs. hourly plot
"""
plt.plot([7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], dniavg, c='r', label = 'DNI Avg Per Hour')
plt.xlabel("Hour, In Military Time")
plt.ylabel("DNI")
plt.title('All July 2020 Data (regardless of cloud type)')
plt.show()
"""


# my attempt at plotting both DNI and Clearsky DNI on one plot
"""
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot([7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], dniavg, c='r', label = 'DNI Avg Per Hour')
ax.plot([7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], clearskyavg, c='g', label = 'Clearsky DNI Avg Per Hour')
ax.set_xlabel('Hour in Military Time')
ax.set_ylabel('DNI')
plt.legend()
plt.show()
"""


# cloud type plot

# data per cloud type
cloud0 = july.loc[july['Cloud Type'] == 0] # takes in all cloud 0 data only, which is clear sky
cloud1 = july.loc[july['Cloud Type'] == 1] # takes all cloud 1 data: probably clear
cloud2 = july.loc[july['Cloud Type'] == 2] # cloud 2 data: fog
cloud3 = july.loc[july['Cloud Type'] == 3] # cloud 3 data: water
cloud4 = july.loc[july['Cloud Type'] == 4] # cloud 4 data: super-cooled water
cloud5 = july.loc[july['Cloud Type'] == 5] # cloud 5 data: mixed
cloud6 = july.loc[july['Cloud Type'] == 6] # cloud 6 data: opaque ice
cloud7 = july.loc[july['Cloud Type'] == 7] # cloud 7 data: cirrus
cloud8 = july.loc[july['Cloud Type'] == 8] # cloud 8 data: overlapping
cloud9 = july.loc[july['Cloud Type'] == 9] # cloud 9 data: overshooting
cloud10 = july.loc[july['Cloud Type'] == 10] # cloud 10 data: unknown
cloud11 = july.loc[july['Cloud Type'] == 11] # cloud 11 data: dust
cloud12 = july.loc[july['Cloud Type'] == 12] # cloud 12 data: smoke

# takes all data per hour for only cloud 0 and calculate their mean DNI vals
cloud0data = [cloud0.loc[cloud0['Hour'] == 7, 'DNI'].mean(),
                  cloud0.loc[cloud0['Hour'] == 8, 'DNI'].mean(),
                  cloud0.loc[cloud0['Hour'] == 9, 'DNI'].mean(),
                  cloud0.loc[cloud0['Hour'] == 10, 'DNI'].mean(),
                  cloud0.loc[cloud0['Hour'] == 11, 'DNI'].mean(),
                  cloud0.loc[cloud0['Hour'] == 12, 'DNI'].mean(),
                  cloud0.loc[cloud0['Hour'] == 13, 'DNI'].mean(),
                  cloud0.loc[cloud0['Hour'] == 14, 'DNI'].mean(),
                  cloud0.loc[cloud0['Hour'] == 15, 'DNI'].mean(),
                  cloud0.loc[cloud0['Hour'] == 16, 'DNI'].mean(),
                  cloud0.loc[cloud0['Hour'] == 17, 'DNI'].mean(),
                  cloud0.loc[cloud0['Hour'] == 18, 'DNI'].mean()
            ]

# takes all data per hour for only cloud type 1 and calculates their mean DNI vals
cloud1data = [cloud1.loc[cloud0['Hour'] == 7, 'DNI'].mean(),
                  cloud1.loc[cloud1['Hour'] == 8, 'DNI'].mean(),
                  cloud1.loc[cloud1['Hour'] == 9, 'DNI'].mean(),
                  cloud1.loc[cloud1['Hour'] == 10, 'DNI'].mean(),
                  cloud1.loc[cloud1['Hour'] == 11, 'DNI'].mean(),
                  cloud1.loc[cloud1['Hour'] == 12, 'DNI'].mean(),
                  cloud1.loc[cloud1['Hour'] == 13, 'DNI'].mean(),
                  cloud1.loc[cloud1['Hour'] == 14, 'DNI'].mean(),
                  cloud1.loc[cloud1['Hour'] == 15, 'DNI'].mean(),
                  cloud1.loc[cloud1['Hour'] == 16, 'DNI'].mean(),
                  cloud1.loc[cloud1['Hour'] == 17, 'DNI'].mean(),
                  cloud1.loc[cloud1['Hour'] == 18, 'DNI'].mean()
            ]

# cloud 2 DNI: cloud 2 = fog
cloud2data = [cloud2.loc[cloud2['Hour'] == 7, 'DNI'].mean(),
                  cloud2.loc[cloud2['Hour'] == 8, 'DNI'].mean(),
                  cloud2.loc[cloud2['Hour'] == 9, 'DNI'].mean(),
                  cloud2.loc[cloud2['Hour'] == 10, 'DNI'].mean(),
                  cloud2.loc[cloud2['Hour'] == 11, 'DNI'].mean(),
                  cloud2.loc[cloud2['Hour'] == 12, 'DNI'].mean(),
                  cloud2.loc[cloud2['Hour'] == 13, 'DNI'].mean(),
                  cloud2.loc[cloud2['Hour'] == 14, 'DNI'].mean(),
                  cloud2.loc[cloud2['Hour'] == 15, 'DNI'].mean(),
                  cloud2.loc[cloud2['Hour'] == 16, 'DNI'].mean(),
                  cloud2.loc[cloud2['Hour'] == 17, 'DNI'].mean(),
                  cloud2.loc[cloud2['Hour'] == 18, 'DNI'].mean()
            ]

# cloud 3 DNI: cloud 3 = water (which we assume means rain)
cloud3data = [cloud3.loc[cloud3['Hour'] == 7, 'DNI'].mean(),
                  cloud3.loc[cloud3['Hour'] == 8, 'DNI'].mean(),
                  cloud3.loc[cloud3['Hour'] == 9, 'DNI'].mean(),
                  cloud3.loc[cloud3['Hour'] == 10, 'DNI'].mean(),
                  cloud3.loc[cloud3['Hour'] == 11, 'DNI'].mean(),
                  cloud3.loc[cloud3['Hour'] == 12, 'DNI'].mean(),
                  cloud3.loc[cloud3['Hour'] == 13, 'DNI'].mean(),
                  cloud3.loc[cloud3['Hour'] == 14, 'DNI'].mean(),
                  cloud3.loc[cloud3['Hour'] == 15, 'DNI'].mean(),
                  cloud3.loc[cloud3['Hour'] == 16, 'DNI'].mean(),
                  cloud3.loc[cloud3['Hour'] == 17, 'DNI'].mean(),
                  cloud3.loc[cloud3['Hour'] == 18, 'DNI'].mean()
            ]

# cloud 4 DNI: cloud 4 = super-cooled water
cloud4data = [cloud4.loc[cloud4['Hour'] == 7, 'DNI'].mean(),
                  cloud4.loc[cloud4['Hour'] == 8, 'DNI'].mean(),
                  cloud4.loc[cloud4['Hour'] == 9, 'DNI'].mean(),
                  cloud4.loc[cloud4['Hour'] == 10, 'DNI'].mean(),
                  cloud4.loc[cloud4['Hour'] == 11, 'DNI'].mean(),
                  cloud4.loc[cloud4['Hour'] == 12, 'DNI'].mean(),
                  cloud4.loc[cloud4['Hour'] == 13, 'DNI'].mean(),
                  cloud4.loc[cloud4['Hour'] == 14, 'DNI'].mean(),
                  cloud4.loc[cloud4['Hour'] == 15, 'DNI'].mean(),
                  cloud4.loc[cloud4['Hour'] == 16, 'DNI'].mean(),
                  cloud4.loc[cloud4['Hour'] == 17, 'DNI'].mean(),
                  cloud4.loc[cloud4['Hour'] == 18, 'DNI'].mean()
            ]

# cloud 5 DNI: cloud 5 = mix
cloud5data = [cloud5.loc[cloud5['Hour'] == 7, 'DNI'].mean(),
                  cloud5.loc[cloud5['Hour'] == 8, 'DNI'].mean(),
                  cloud5.loc[cloud5['Hour'] == 9, 'DNI'].mean(),
                  cloud5.loc[cloud5['Hour'] == 10, 'DNI'].mean(),
                  cloud5.loc[cloud5['Hour'] == 11, 'DNI'].mean(),
                  cloud5.loc[cloud5['Hour'] == 12, 'DNI'].mean(),
                  cloud5.loc[cloud5['Hour'] == 13, 'DNI'].mean(),
                  cloud5.loc[cloud5['Hour'] == 14, 'DNI'].mean(),
                  cloud5.loc[cloud5['Hour'] == 15, 'DNI'].mean(),
                  cloud5.loc[cloud5['Hour'] == 16, 'DNI'].mean(),
                  cloud5.loc[cloud5['Hour'] == 17, 'DNI'].mean(),
                  cloud5.loc[cloud5['Hour'] == 18, 'DNI'].mean()
            ]

# cloud 6 DNI: cloud 6 = opaque ice
cloud6data = [cloud6.loc[cloud6['Hour'] == 7, 'DNI'].mean(),
                  cloud6.loc[cloud6['Hour'] == 8, 'DNI'].mean(),
                  cloud6.loc[cloud6['Hour'] == 9, 'DNI'].mean(),
                  cloud6.loc[cloud6['Hour'] == 10, 'DNI'].mean(),
                  cloud6.loc[cloud6['Hour'] == 11, 'DNI'].mean(),
                  cloud6.loc[cloud6['Hour'] == 12, 'DNI'].mean(),
                  cloud6.loc[cloud6['Hour'] == 13, 'DNI'].mean(),
                  cloud6.loc[cloud6['Hour'] == 14, 'DNI'].mean(),
                  cloud6.loc[cloud6['Hour'] == 15, 'DNI'].mean(),
                  cloud6.loc[cloud6['Hour'] == 16, 'DNI'].mean(),
                  cloud6.loc[cloud6['Hour'] == 17, 'DNI'].mean(),
                  cloud6.loc[cloud6['Hour'] == 18, 'DNI'].mean()
            ]

# cloud 7 DNI: cloud 7 = cirrus
cloud7data = [cloud7.loc[cloud7['Hour'] == 7, 'DNI'].mean(),
                  cloud7.loc[cloud7['Hour'] == 8, 'DNI'].mean(),
                  cloud7.loc[cloud7['Hour'] == 9, 'DNI'].mean(),
                  cloud7.loc[cloud7['Hour'] == 10, 'DNI'].mean(),
                  cloud7.loc[cloud7['Hour'] == 11, 'DNI'].mean(),
                  cloud7.loc[cloud7['Hour'] == 12, 'DNI'].mean(),
                  cloud7.loc[cloud7['Hour'] == 13, 'DNI'].mean(),
                  cloud7.loc[cloud7['Hour'] == 14, 'DNI'].mean(),
                  cloud7.loc[cloud7['Hour'] == 15, 'DNI'].mean(),
                  cloud7.loc[cloud7['Hour'] == 16, 'DNI'].mean(),
                  cloud7.loc[cloud7['Hour'] == 17, 'DNI'].mean(),
                  cloud7.loc[cloud7['Hour'] == 18, 'DNI'].mean()
            ]

# cloud 8 DNI: cloud 8 = overlapping
cloud8data = [cloud8.loc[cloud8['Hour'] == 7, 'DNI'].mean(),
                  cloud8.loc[cloud8['Hour'] == 8, 'DNI'].mean(),
                  cloud8.loc[cloud8['Hour'] == 9, 'DNI'].mean(),
                  cloud8.loc[cloud8['Hour'] == 10, 'DNI'].mean(),
                  cloud8.loc[cloud8['Hour'] == 11, 'DNI'].mean(),
                  cloud8.loc[cloud8['Hour'] == 12, 'DNI'].mean(),
                  cloud8.loc[cloud8['Hour'] == 13, 'DNI'].mean(),
                  cloud8.loc[cloud8['Hour'] == 14, 'DNI'].mean(),
                  cloud8.loc[cloud8['Hour'] == 15, 'DNI'].mean(),
                  cloud8.loc[cloud8['Hour'] == 16, 'DNI'].mean(),
                  cloud8.loc[cloud8['Hour'] == 17, 'DNI'].mean(),
                  cloud8.loc[cloud8['Hour'] == 18, 'DNI'].mean()
            ]

# cloud 9 DNI: cloud 9 = overshooting
cloud9data = [cloud9.loc[cloud9['Hour'] == 7, 'DNI'].mean(),
                  cloud9.loc[cloud9['Hour'] == 8, 'DNI'].mean(),
                  cloud9.loc[cloud9['Hour'] == 9, 'DNI'].mean(),
                  cloud9.loc[cloud9['Hour'] == 10, 'DNI'].mean(),
                  cloud9.loc[cloud9['Hour'] == 11, 'DNI'].mean(),
                  cloud9.loc[cloud9['Hour'] == 12, 'DNI'].mean(),
                  cloud9.loc[cloud9['Hour'] == 13, 'DNI'].mean(),
                  cloud9.loc[cloud9['Hour'] == 14, 'DNI'].mean(),
                  cloud9.loc[cloud9['Hour'] == 15, 'DNI'].mean(),
                  cloud9.loc[cloud9['Hour'] == 16, 'DNI'].mean(),
                  cloud9.loc[cloud9['Hour'] == 17, 'DNI'].mean(),
                  cloud9.loc[cloud9['Hour'] == 18, 'DNI'].mean()
            ]

# cloud 10 DNI: cloud 10 = unknown
cloud10data = [cloud10.loc[cloud10['Hour'] == 7, 'DNI'].mean(),
                  cloud10.loc[cloud10['Hour'] == 8, 'DNI'].mean(),
                  cloud10.loc[cloud10['Hour'] == 9, 'DNI'].mean(),
                  cloud10.loc[cloud10['Hour'] == 10, 'DNI'].mean(),
                  cloud10.loc[cloud10['Hour'] == 11, 'DNI'].mean(),
                  cloud10.loc[cloud10['Hour'] == 12, 'DNI'].mean(),
                  cloud10.loc[cloud10['Hour'] == 13, 'DNI'].mean(),
                  cloud10.loc[cloud10['Hour'] == 14, 'DNI'].mean(),
                  cloud10.loc[cloud10['Hour'] == 15, 'DNI'].mean(),
                  cloud10.loc[cloud10['Hour'] == 16, 'DNI'].mean(),
                  cloud10.loc[cloud10['Hour'] == 17, 'DNI'].mean(),
                  cloud10.loc[cloud10['Hour'] == 18, 'DNI'].mean()
            ]

# cloud 11 DNI: cloud 11 = dust
cloud11data = [cloud11.loc[cloud11['Hour'] == 7, 'DNI'].mean(),
                  cloud11.loc[cloud11['Hour'] == 8, 'DNI'].mean(),
                  cloud11.loc[cloud11['Hour'] == 9, 'DNI'].mean(),
                  cloud11.loc[cloud11['Hour'] == 10, 'DNI'].mean(),
                  cloud11.loc[cloud11['Hour'] == 11, 'DNI'].mean(),
                  cloud11.loc[cloud11['Hour'] == 12, 'DNI'].mean(),
                  cloud11.loc[cloud11['Hour'] == 13, 'DNI'].mean(),
                  cloud11.loc[cloud11['Hour'] == 14, 'DNI'].mean(),
                  cloud11.loc[cloud11['Hour'] == 15, 'DNI'].mean(),
                  cloud11.loc[cloud11['Hour'] == 16, 'DNI'].mean(),
                  cloud11.loc[cloud11['Hour'] == 17, 'DNI'].mean(),
                  cloud11.loc[cloud11['Hour'] == 18, 'DNI'].mean()
            ]

# cloud 12 DNI: cloud 12 = smoke
cloud12data = [cloud12.loc[cloud12['Hour'] == 7, 'DNI'].mean(),
                  cloud12.loc[cloud12['Hour'] == 8, 'DNI'].mean(),
                  cloud12.loc[cloud12['Hour'] == 9, 'DNI'].mean(),
                  cloud12.loc[cloud12['Hour'] == 10, 'DNI'].mean(),
                  cloud12.loc[cloud12['Hour'] == 11, 'DNI'].mean(),
                  cloud12.loc[cloud12['Hour'] == 12, 'DNI'].mean(),
                  cloud12.loc[cloud12['Hour'] == 13, 'DNI'].mean(),
                  cloud12.loc[cloud12['Hour'] == 14, 'DNI'].mean(),
                  cloud12.loc[cloud12['Hour'] == 15, 'DNI'].mean(),
                  cloud12.loc[cloud12['Hour'] == 16, 'DNI'].mean(),
                  cloud12.loc[cloud12['Hour'] == 17, 'DNI'].mean(),
                  cloud12.loc[cloud12['Hour'] == 18, 'DNI'].mean()
            ]

# all cloud types plotted by cloud type for dni avg vs hour
plt.plot([7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], cloud0data, c = 'black', label = '0: clear')
plt.plot([7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], cloud1data, c = 'red', label = '1: probably clear')
plt.plot([7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], cloud2data, c = 'darkorange', label = '2: fog')
plt.plot([7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], cloud3data, c = 'gold', label = '3: water')
plt.plot([7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], cloud4data, c = 'yellow', label = '4:super-cooled water')
plt.plot([7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], cloud5data, c = 'lawngreen', label = '5: mixed')
plt.plot([7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], cloud6data, c = 'darkgreen', label = '6: opaque ice')
plt.plot([7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], cloud7data, c = 'lightseagreen', label = '7: cirrus')
plt.plot([7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], cloud8data, c = 'deepskyblue', label = '8: overlapping')
plt.plot([7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], cloud9data, c = 'blue', label = '9: overshooting')
plt.plot([7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], cloud10data, c = 'darkviolet', label = '10: unknown')
plt.plot([7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], cloud11data, c = 'violet', label = '11: dust')
plt.plot([7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], cloud12data, c = 'deeppink', label = '12: smoke')
plt.xlabel("Hour in Military Time")
plt.ylabel("DNI")
plt.legend(fontsize = 2.7)
plt.show()



