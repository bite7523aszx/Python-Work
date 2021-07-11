
#巢狀for迴圈 請印出 N層 等腰三角形 step1:等腰三角形A,B,C step2:將A,B要素分別完成 step3:將step2統整
n=int(input('輸入n值'))
# 最外層迴圈 A
for i in range(1,n+1): 
    # 印出空格 B
    for j in range(n-i,0,-1):
        print(' ',end='')
        # 印出星星符號 C
    for a in range(1,i*2):
        print('*',end='')
    print()
    # 印出跳行
    