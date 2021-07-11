import random
sum = 0
print('數字到6結束遊戲')
while True:
    Start = input("請輸入Y/N開始遊戲").lower()
    if Start == "y":
        a = random.randint(1,6)
        if a < 6 :
            sum = sum + 1
            print('數字 :',a)
        else :
            print('數字 :',a)
            print('遊戲結束')
            break 
    # else :
    #     print(a)
    #     print("已關閉遊戲")
    #     break
# import 輸入(輸出) random 模組
# while True 無窮迴圈
# break 休息(中斷)