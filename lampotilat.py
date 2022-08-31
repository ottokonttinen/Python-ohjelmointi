F=int(input('Anna lämpötila (F):'))
C=(F-32)/1.8
print(f'{F} fahrenheit-astetta on {C} celsius-astetta')
if C < 0:
    print('paleltaa')