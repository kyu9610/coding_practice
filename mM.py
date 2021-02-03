#http://220.89.64.243/30stair/mM/mM.php?pname=mM
numList = list(map(int,input("7 개의 수를 입력하세요 : ").split()))
min = numList[0]
max = numList[0]

for i in numList:
    if i > max:
        max = i

    if i < min:
        min = i

print("최댓값 : ",max,"최솟값 : ",min)