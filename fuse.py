#computer = 1.5 + 1.0 , printer = 2.0 , router = 0.5
com,prt,rout = map(int,input("컴퓨터 , 프린터 , 라우터의 갯수를 차례대로 입력하세요 : ").split())
fuse = (com*(1.5 + 1.0) + prt * 2.0 + rout * 0.5) * 2
fuse = (fuse // 10)*10 + 10
print(fuse,"amperes")