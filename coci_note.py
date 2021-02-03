origin = list(map(int,input().split()))
sort_list = sorted(origin)
temp = reversed(sort_list)
print(type(temp))
if sort_list == origin:
    print("ascending")
elif list(temp) == origin:
    print("descending")
else:
    print("mixed")

#xzCZXczXC