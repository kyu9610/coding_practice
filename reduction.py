image_x,image_y,copy_x,copy_y = map(int,input("복사할 이미지의 가로 세로 크기, 복사용지의 가로 세로 크기를 차례로 입력하세요. : ").split())

if copy_x >= image_x and copy_y >= image_y:
    print("100%")
elif copy_x >= image_y and copy_y >= image_x:
    print("100%")
else:
    min_rate = min((min(copy_x,copy_y)/min(image_x,image_y)),(max(copy_x,copy_y)/max(image_x,image_y)))
    print(int(min_rate*100),"%")

        