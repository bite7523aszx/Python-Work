import random
ans=[]
for k in range(4):
    xxx=random.sample(range(0,9),4)
    ans=xxx
print(ans)
x=(input('輸入數字'))
y=list(x)
for j in range(4):
    y[j]=int(y[j])
print(y)

def calla(b): 
    global ans
    A=0
    for i in range(0,4):
        if ans[i] == b[i]:
            A=A+1
    return A
print(calla(y))