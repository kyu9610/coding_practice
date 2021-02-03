number = 1
turn = 1

while(number != 31):
    # computer 4*turn - 2 까지만 부른다.
    print("computer : ",end='')
    for i in range(number,4*turn-1):
        print(number,end=' ')
        number += 1
    print('')
    turn += 1
    user_number = list(map(int,input("user :  ").split()))

    for j in user_number:
        if number == 31:
            print('')
            print('***************************************')
            print("               you lose                ")
            print('***************************************')
            break
        number +=1
