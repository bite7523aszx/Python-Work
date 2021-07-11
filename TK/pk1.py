import random

y=int(input('數字'))
s=0
i=int(random.randint(1,99))
while True:
    minn=0
    maxx=99
    if y==i:
        s=s+1
        print('猜對了','總共猜了',s,'次')
        break
    elif y<i:
        s=s+1
        print('你猜的數字太小了')
    elif y>i:
        s=s+1
        print('你猜的數字太大了')