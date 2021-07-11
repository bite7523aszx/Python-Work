# 判斷完全數
for i in range(2,1001):#外迴圈
    sum=1
    for j in range(2,i):#內迴圈
        if i%j==0:
            sum=sum+j
        else:
            sum==sum
    if sum==i:
        print(i)        