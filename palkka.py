palkka=float(input('Tuntipalkka:')) 
tunnit=float(input('Työtunnit:'))
päivä=str(input('Viikonpäivä:'))
tuplapalkka=1
if päivä =='sunnuntai':
    tuplapalkka=2
print(f'Palkka {palkka*tunnit*tuplapalkka} euroa')

