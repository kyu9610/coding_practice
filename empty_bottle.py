bottle = int(input("처음 산 음료수의 병 수는? : "))
first = bottle // 4
f_remain = bottle % 4
second = first // 4
s_remain = first % 4

max = bottle + first + second
remain = f_remain + s_remain

print(max, remain)