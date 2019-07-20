import csv
import random

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

row = [['age', 'budget', 'season', 'destination']]

def generateData(numb):
    season = 0
    budget = 500
    age = 18

    if numb < 9:
        if numb % 2 == 0:
            season = 0
        else:
            season = 1
    else:
        if numb % 2 == 0:
            season = 3
        else:
            season = 2

    budget = random.randint(500, 5000)
    age = random.randint(18, 65)

    destination = 0

    innerRandomizer = random.randint(1, 100)

    # IF SPRING, WE HAVE SOFT AGE BOUNDARIES
    if season == 0:
        if age <= 40 and budget <= 2500:
            if age > 37 and innerRandomizer % 2 == 0:
                destination = 0
            else:
                destination = 2 # majority destination
        elif age <= 40 and budget > 2500:
            if age > 37 and innerRandomizer % 2 == 0:
                destination = 1
            else:
                destination = 3 # majority destination
        elif age > 40 and budget <= 2500:
            if age < 43 and innerRandomizer % 2 == 0:
                destination = 2
            else:
                destination = 0 # majority destination
        elif age > 40 and budget > 2500:
            if age < 43 and innerRandomizer % 2 == 0:
                destination = 3
            else:
                destination = 1 # majority destination

    # IF AUTUMN, WE HAVE SOFT BUDGET BOUNDARIES
    elif season == 1:
        if age <= 40 and budget <= 2500:
            if budget > 2300 and innerRandomizer % 2 == 0:
                destination = 3
            else:
                destination = 2 # majority destination
        elif age <= 40 and budget > 2500:
            if budget < 2700 and innerRandomizer % 2 == 0:
                destination = 2
            else:
                destination = 3 # majority destination
        elif age > 40 and budget <= 2500:
            if budget > 2300 and innerRandomizer % 2 == 0:
                destination = 1
            else:
                destination = 0 # majority destination
        elif age > 40 and budget > 2500:
            if budget < 2700 and innerRandomizer % 2 == 0:
                destination = 0
            else:
                destination = 1 # majority destination

    # HERE YOUNGS WILL CARE ABOUT BUDGET WHERE OLDER CARE ABOUT AGE:
    elif season == 2:
        if age <= 40 and budget <= 2500:
            if budget > 2300 and innerRandomizer % 2 == 0:
                destination = 8
            else:
                destination = 9 # majority destination
        elif age <= 40 and budget > 2500:
            if budget < 2700 and innerRandomizer % 2 == 0:
                destination = 9
            else:
                destination = 8 # majority destination
        elif age > 40 and budget <= 2500:
            if age < 43 and innerRandomizer % 2 == 0:
                destination = 9
            else:
                destination = 11 # majority destination
        elif age > 40 and budget > 2500:
            if age < 43 and innerRandomizer % 2 == 0:
                destination = 8
            else:
                destination = 10 # majority destination

    # HERE YOUNGS WILL CARE ABOUT AGE WHERE OLDER CARE ABOUT BUDGET:
    elif season == 3:
        if age <= 40 and budget <= 2500:
            if age > 37 and innerRandomizer % 2 == 0:
                destination = 4
            else:
                destination = 7 # majority destination
        elif age <= 40 and budget > 2500:
            if age > 37 and innerRandomizer % 2 == 0:
                destination = 5
            else:
                destination = 6 # majority destination
        elif age > 40 and budget <= 2500:
            if budget > 2300 and innerRandomizer % 2 == 0:
                destination = 5
            else:
                destination = 4 # majority destination
        elif age > 40 and budget > 2500:
            if budget < 2700 and innerRandomizer % 2 == 0:
                destination = 4
            else:
                destination = 5 # majority destination

    data = [age, budget, season, destination]
    row.append(data)


for i in range(6000):
    k = random.randint(1, 20)
    generateData(k)

with open('myDataNumericRandomized.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(row)
csvFile.close()
