number = int(input("주사위 숫자의 합 : "))
x=0
y=0
for i in range (1,5):
    for j in range(1,7):
        if(i+j == number):
            print(i,j)