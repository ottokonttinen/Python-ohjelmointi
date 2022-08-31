# Kirjoita ratkaisu tähän
M=int(input('Montako kertaa viikossa syöt Unicafessa?')) 
U=float(input('Unicafe-lounaan hinta?'))
P=float(input('Paljonko käytät viikossa ruokaostoksiin?'))
print(f'Kustannukset keskimäärin:\nPäivässä {(M*U+P)/7} euroa\nViikossa {M*U+P} euroa')