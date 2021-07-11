import random
i = random.randint(0,100)
x = 0
y = 100
b = 0
while True:
    xy = "請輸入猜的數字(" + str(x) + "~" + str(y) + ")"
    a = int(input(xy))
    b = b + 1
    if i == a :
        print("你總共猜了",b,"次","恭喜你猜對了")
        break
    elif i > a :
        x = a + 1
        print("你總共猜了",b,"次","在猜大一點")
    elif i < a :
        y = a - 1
        print("你總共猜了",b,"次","在猜小一點")
# import random 輸入 random 模組
# .randint(0,0) 隨機產生數字(範圍內)
# str 將你輸入的物件轉成字串