# 請定義一個函式允許輸入m的數值n數值與印出的字元,可以印出m列n行個字元 6-31

def f1(a,b,c):
    for i in range(0,a):
        for j in range(0,b):
            print(c,end='')
        print()

m=int(input('請輸入行數'))
n=int(input('請輸入列數'))
y=(input('請輸入要顯示的字元'))
f1(m,n,y)