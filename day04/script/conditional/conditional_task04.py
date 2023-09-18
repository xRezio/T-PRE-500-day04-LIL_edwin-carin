valeur = int(input())

if valeur ==42:
    print("ok")
elif valeur <= 21:
    print("ok")
elif (valeur % 2) ==0:
    print("ok")
elif (valeur / 2) <21:
    print("ok")
elif (valeur  % 2) >0 and valeur>45 :
    print("ok")

else:
    print("you got wrong my poor friend")
