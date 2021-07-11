bb = 6
for ii in range(0,30,1) :
    print(ii+1," ==> ",end=" ")
    col = ii // bb # 求整數
    row = ii % bb # 求餘數
    print("(",col+1,",",row+1,")")