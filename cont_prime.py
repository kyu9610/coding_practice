n,k = map(int,input("n이 k-연속 소수체인지 판단하려할때 n과 k를 순서대로 입력하세요. : ").split())
sum = 0
count = 0
out = 0
number = 3
primeList = [1]

for i in range(2,n):
    prime = True

    for j in range(2,i):
        if i%j == 0:
            prime = False
    
    if prime == True:
        primeList.append(i)

print(primeList)
    
for i in primeList:
    sum = sum + i
    count += 1

    if count == k+1:
        sum = sum - primeList[out]
        count -= 1
        out += 1

    #print(sum,count)

    if count == k and sum == n:
        print("yes")
        sum = 0
        break

if sum != 0:
    print("no")