withdraw = int(input("인출할 금액을 입력하세요 : "))
balance = float(input("계좌의 금액을 입력하세요 : "))

if(withdraw % 5 == 0):
    balance = balance - withdraw - 0.5
else:
    pass

print(balance)
