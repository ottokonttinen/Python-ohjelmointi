print('Kerro huominen sääennuste:')
lämpö=int(input('Lämpötila:'))
sade=str(input('Sataako (kyllä/ei):'))
tulostus='Pue housut ja t-paita'
if lämpö <= 20:
    tulostus+='\nOta myös pitkähihainen paita'
if lämpö <= 10:
    tulostus+='\nPue päälle takki'
if lämpö <= 5:
    tulostus+='\nSuosittelen lämmintä takkia\nKannattaa ottaa myös hanskat'
if sade == 'kyllä':
    tulostus+='\nMuista sateenvarjo!'
print(tulostus)