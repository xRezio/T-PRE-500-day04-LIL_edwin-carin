valeur =[]
for i in range(1, 10000):
    if (i%7==0) :
        valeur.append(str(i))

print (','.join(valeur))