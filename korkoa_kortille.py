pisteet = float(input("Kuinka paljon pisteitä? "))
bonus=15
if pisteet < 100:
    bonus = 10
print(f'Sait {bonus} % bonusta\nPisteitä on nyt, {pisteet*(bonus/100+1)}')