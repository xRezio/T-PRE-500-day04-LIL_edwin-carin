texte = "Hello world"
encryption = 4
stack =" "
for i in range(len(texte)):
    checkMot = texte[i]

    if checkMot==" ":
        stack+=" "
    elif (checkMot.isupper()):
        stack+= chr((ord(checkMot) + encryption-65) % 26 + 65)

    else:
        stack+= chr((ord(checkMot) + encryption-97) % 26 + 97)

print("Le texte de base est :" +texte)
print("le pattern d'encryption est de :" +str(encryption))
print("Le texte Cipher est :" +stack)