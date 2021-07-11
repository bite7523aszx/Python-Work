a = int(input("請輸入購買飲料的罐數?"))
b = (a // 12 * 200) + (a % 12 * 20)
print("需花費",b)

# if 條件判斷式
# else 動作2(如果不是if執行else)
# input 輸入

#%%
a = int(input("請輸入購買飲料的罐數?"))
if a // 12 ==0:
    print("需花費",(a // 12) *200)
else :
    print("需花費",(a // 12 * 200) + (a % 12 * 20))