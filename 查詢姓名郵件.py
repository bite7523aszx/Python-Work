# 姓名 = []
# 電子郵件 = []
# x=input("請輸入姓名 :")
# 姓名.append(x)
# y=input("請輸入電子郵件 :")
# 電子郵件.append(y)
# x=input("請輸入姓名 :")
# 姓名.append(x)
# y=input("請輸入電子郵件 :")
# 電子郵件.append(y)
# x=input("請輸入姓名 :")  
# 姓名.append(x)
# y=input("請輸入電子郵件 :")
# 電子郵件.append(y)
# mane = input('請輸入要查詢電子郵件的姓名')
# num1 = {姓名[0]:電子郵件[0]}
# num2 = {姓名[1]:電子郵件[1]}
# num3 = {姓名[2]:電子郵件[2]}
# num1 .update(num2)
# num1 .update(num3)
# print(num1 .get(mane,"找不到此電子郵件的姓名"))

#%%
姓名 = []
電子郵件 = []
ans= "y"
while (ans!="n"):
    x = input('請輸入姓名')
    姓名.append(x)
    y = input('請輸入電子郵件')
    電子郵件.append(y)
    ans = input("還需要輸入嗎?(y/n)").lower()
    if ans == 'n' :
        查詢 = input('請輸入要查詢電子郵件的姓名').lower()
字典 = {姓名 : 電子郵件 for 姓名, 電子郵件 in zip(姓名,電子郵件)}
# 
#  zip() 函式將兩個串列結合為一個字典：
#  zip() 函式將兩個串列打包，並在每次迴圈回覆一個 Tuple 物件，內含配對元素
print('你的郵件 :',字典.get(查詢,"找不到此電子郵件的姓名"))
# print(字典)



# input 輸入
# .append() 加到串列的最後
# .update 兩個字典合併



























