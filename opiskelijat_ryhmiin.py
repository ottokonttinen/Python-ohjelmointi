# Kirjoita ratkaisu tähän
mo=int(input('Montako opiskelijaa?'))
rk=int(input('Mikä on ryhmän koko?'))
tulos=mo//rk
if mo % rk >0:
    tulos=tulos +1

print(f'Ryhmien määrä: {tulos}')