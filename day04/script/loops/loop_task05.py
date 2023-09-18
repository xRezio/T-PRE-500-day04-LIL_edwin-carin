n = int(input("entre ta variable n: "))

for i in range(2, n // 2 +1): # +1 sinon on voit pas la valeur qui peut pas devenir =n
    multiples = []
    for k in range(n - 1, 1, -1):
        if k % i == 0 and k < n:
            multiples.append(k) ### append : ajoute K à la fin de la liste
    if multiples:
        print(" ".join(map(str, multiples)))