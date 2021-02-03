#http://220.89.64.243/30stair/seq/seq.php?pname=seq
x,y = map(int,input("두 수를 입력하세요 : ").split())

for i in range(min(x,y),max(x,y)+1):
    print(i,end=' ')