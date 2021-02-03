import random

def random_pick(n=7):
    nums = list(range(1,46))
    random.shuffle(nums)
    return nums[:7]

def comp(winning,mynum):
    return len(set(winning) & set(mynum))

number = int(input('로또를 몇 개 구매하시겠습니까? : '))

winning = random_pick()
print("현재 당첨번호는 {}  보너스 번호는 {} 입니다.".format(winning[:-1],winning[-1]))

for i in range(number):
    mynum = random_pick()
    print("구매하신 추첨번호는 {}  보너스 번호는 {} 입니다.".format(mynum[:-1],mynum[-1]))
    result = comp(winning,mynum)
    if(result >= 4):
        print("....",8-result,"등 이다!!!!!")