for i in range (-30,30):
    if(i%3) ==0:
        print('\n'f"{i} "'Fizz')
    elif(i%5) ==0:
        print('\n'f"{i} "'Buzz')
    elif (i%5) and (i%3):
        print('\n'f"{i} "'FizzBuzz')
    else : print(i)