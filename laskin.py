from codecs import latin_1_decode


l1=int(input('Luku 1:'))
l2=int(input('Luku 2:'))
k=str(input('Komento:'))
if k=='summa':
    print(f'{l1} + {l2} = {l1+l2}')
if k=='tulo':
    print(f'{l1} * {l2} = {l1*l2}')
if k=='erotus':
    print(f'{l1} - {l2} = {l1-l2}')