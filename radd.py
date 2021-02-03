#입력한 숫자가 몇개의 자리수인지 나타내는 함수 작성!
def show_digits(x):
    if x == 0:
        return 0
    
    while(x != 0):
        return 1+show_digits(x//10)
    
    return 0

number = int(input("숫자를 입력하세요 : "))
print(show_digits(number))