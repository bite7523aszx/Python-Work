# 輸入密碼 6-31
# 計算密碼長度
# 數 數字個數
# 數 英文小寫個數
# 數 英文大寫個數
# 數 不是英文 個數不等於零
# 數 不是數字 個數不等於零
# 1.先判斷數字英文是否存在
# 2.在判斷長度
n = input('輸入密碼')
def checkpwd(pwd):

    C1=0        # 數 數字個數
    C2=0        # 數 英文小寫個數
    C3=0        # 數 英文大寫個數
    C4=0        #  數 不是英文 個數不等於零 # 數 不是數字 個數不等於零
    a=len(pwd) # 計算密碼長度
    print(a)
    for i in range(0,a): # i=0 a第零個元素
        if pwd[i] >='0' and pwd[i]<='9':  # 
            C1=C1+1        # 數 數字個數
        elif pwd[i] >='a'and pwd[i] <='z':
            C2=C2+1       # 數 英文小寫個數
        elif pwd[i] >='A'and pwd[i] <='Z':
            C3=C3+1       # 數 英文大寫個數
        else:
            C4=C4+1        #  數不是英文個數 # 數不是數字個數
    if C4==0: # 如果非數字+英文==0,代表正常的密碼
        if C1==0 : # 如果數字個數=0,代表只有英文
            if C2+C3 <6: 
                print('非常不安全的密碼')
            else :
                print('可能是安全的密碼')
        elif C2==0 and C3==0: # 如果英文大小寫個數=0,代表只有數字
            if C1>6:
                print('可能是安全的密碼')
            else :
                print('非常不安全的密碼')
        else:
            if C1+C2+C3<6: # 數字加英文
                print('不安全的密碼')
            elif C1+C2+C3 >=6 and C1+C2+C3<10:
                print('安全的密碼')
            else:
                print('非常安全的密碼')
    else:
        print('錯誤的密碼')
checkpwd(n)