import csv
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

# CITIES
#   0 = Istanbul
#   1 = London
#   2 = Prague
#   3 = Amsterdam
#   4 = Antalya
#   5 = Dubrovnik
#   6 = Ibiza
#   7 = Hvar
#   8 = Verbier
#   9 = Vogel
#   10 = Bangkok
#   11 = Sao Paulo

# season thing

#   0 = spring
#   1 = autumn
#   2 = winter
#   3 = summer

#distribution of 12 classes per 100 samples:
#22 percent x2 = 44
#12 percent x2 = 24
#5.5 percent x2 = 11
#4.5 percent x2 =  9
#3.5 percent x2 =  7
#2.3 percent x2 =  4.6

#   istanbul, amsterdam, sao paulo, bangkok, vogel, verbier - dubrovnik, hvar, ibiza, antalya, london, prague  ---distribution

row = [['age', 'budget', 'season', 'destination']]

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

sample_count = 1

#update sample count with passed argument.
if len(sys.argv) == 2:
     sample_count = int(sys.argv[1])

#generator applies 68-95-99 rule.
def generate_data(n):
    for i in range(int(n*0.22)):
        age = random.randint(18, 40) #young category
        budget = random.randint(2501, 5000) #rich category
        season = 2 #winter
        destination = vrb
        data = [age, budget, season, destination]
        row.append(data)

    for i in range(int(n*0.22)):
        age = random.randint(40, 65) #old category
        budget = random.randint(2501, 5000) #rich category
        season = 3 #summer
        destination = dbr
        data = [age, budget, season, destination]
        row.append(data)

    for i in range(int(n*0.12)):
        age = random.randint(18, 40) #young category
        budget = random.randint(500, 2500) #poor category
        season = 2 #winter
        destination = vgl
        data = [age, budget, season, destination]
        row.append(data)

    for i in range(int(n*0.12)):
        age = random.randint(18, 40) #old category
        budget = random.randint(500, 2500) #poor category
        season = 3 #summer
        destination = hvr
        data = [age, budget, season, destination]
        row.append(data)

    for i in range(int(n*0.055)):
        age = random.randint(40, 65) #old category
        budget = random.randint(2501, 5000) #rich category
        season = 2 #winter
        destination = bng
        data = [age, budget, season, destination]
        row.append(data)

    for i in range(int(n*0.055)):
        age = random.randint(18, 40) #young category
        budget = random.randint(2501, 5000) #rich category
        season = 3 #summer
        destination = ibz
        data = [age, budget, season, destination]
        row.append(data)

    for i in range(int(n*0.045)):
        age = random.randint(40, 65) #old category
        budget = random.randint(500, 2501) #poor category
        season = 2 #winter
        destination = sao
        data = [age, budget, season, destination]
        row.append(data)

    for i in range(int(n*0.045)):
        age = random.randint(40, 65) #old category
        budget = random.randint(500, 2501) #rich category
        season = 3 #summer
        destination = ant
        data = [age, budget, season, destination]
        row.append(data)

    for i in range(int(n*0.035)):
        age = random.randint(18, 40) #young category
        budget = random.randint(2501, 5000) #rich category
        season_rand = random.randint(0, 100)
        if season_rand > 50:
            season = 0
        else:
            season = 1
        destination = ams
        data = [age, budget, season, destination]
        row.append(data)

    for i in range(int(n*0.035)):
        age = random.randint(40, 65) #old category
        budget = random.randint(2501, 5000) #rich category
        season_rand = random.randint(0, 100)
        if season_rand > 50:
            season = 0
        else:
            season = 1
        destination = lnd
        data = [age, budget, season, destination]
        row.append(data)

    for i in range(int(n*0.023)):
        age = random.randint(40, 65) #old category
        budget = random.randint(500, 2500) #poor category
        season_rand = random.randint(0, 100)
        if season_rand > 50:
            season = 0
        else:
            season = 1
        destination = ist
        data = [age, budget, season, destination]
        row.append(data)

    for i in range(int(n*0.023)):
        age = random.randint(18, 40) #young category
        budget = random.randint(500, 2500) #poor category
        season_rand = random.randint(0, 100)
        if season_rand > 50:
            season = 0
        else:
            season = 1
        destination = prg
        data = [age, budget, season, destination]
        row.append(data)


generate_data(sample_count)

with open('normalDistributionData.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(row)
csvFile.close()
