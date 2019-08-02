import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ist = 0
lnd = 1
prg = 2
ams = 3
ant = 4
dbr = 5
ibz = 6
hvr = 7
vrb = 8
vgl = 9
bng = 10
sao = 11

data = pd.read_csv('normalDistributionData.csv')

istanbul = data['destination'].value_counts(ascending=True).get(ist)
amsterdam = data['destination'].value_counts(ascending=True).get(ams)
sao_paulo = data['destination'].value_counts(ascending=True).get(sao)
bangkok = data['destination'].value_counts(ascending=True).get(bng)
vogel = data['destination'].value_counts(ascending=True).get(vgl)
verbier = data['destination'].value_counts(ascending=True).get(vrb)
dubrovnik = data['destination'].value_counts(ascending=True).get(dbr)
hvar = data['destination'].value_counts(ascending=True).get(hvr)
ibiza = data['destination'].value_counts(ascending=True).get(ibz)
antalya = data['destination'].value_counts(ascending=True).get(ant)
london = data['destination'].value_counts(ascending=True).get(lnd)
prague = data['destination'].value_counts(ascending=True).get(prg)

_map = {'Istanbul': istanbul,
        'Amsterdam': amsterdam,
        'Sao Paulo': sao_paulo,
        'Bangkok': bangkok,
        'Vogel': vogel,
        'Verbier': verbier,
        'Dubrovnik': dubrovnik,
        'Hvar': hvar,
        'Ibiza': ibiza,
        'Antalya': antalya,
        'London': london,
        'Prague': prague
        }

x, y = zip(*_map.items())
plt.plot(x, y)
plt.xlabel('Cities')
plt.ylabel('Data Samples')
plt.show()
