def hap(num1,num2):
    return num1+num2

a,b,c,d = map(int,input("네 정수를 입력하세요 : ").split())
print(hap(a,b)+hap(c,d))