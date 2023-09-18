while True:
    a=int(input())
    if a==0:break
    b=input()
    if any(c in'AEIOUaeiou'for c in b):print(a)
    elif a>=42:print(a)
    else:print(b)