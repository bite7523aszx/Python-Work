#  2-5-1
# 耳機=int(input("耳機數量"))
# 電腦=int(input("電腦數量"))
# 手機=int(input("手機數量"))
# total=(耳機*1950)+(電腦*23500)+(手機*1800)
# print("總金額",total)
# 2-5-2
# 長半軸=float(input('請輸入長半軸 :'))
# 短半軸=float(input('請輸入短半軸 :'))
# print("橢圓形面積為 :",3.14159*長半軸*短半軸)
#  2-5-3
# 身高=float(input('請輸入身高'))
# 體重=float(input('請輸入體重'))
# a=(身高/100)
# bmi = 體重/((a*a))
# print(bmi)
# 2-5-4
# 本金=int(input('請輸入本金 :'))
# 利率=float(input('請輸入利率 :'))
# a1=0.0
# for x in range(10,15):
#     a1+=(本金*((1+利率/100)**x))
# print(a1)
# A10=(本金*((1+利率/100)**10))
# A11=(本金*((1+利率/100)**11))
# A12=(本金*((1+利率/100)**12))
# A13=(本金*((1+利率/100)**13))
# A14=(本金*((1+利率/100)**14))
# print(A10+A11+A12+A13+A14)
# CH三習題3-23
# a=input("請輸入英文句子")
# #  an apple a day keeps the doctor away
# # print(a)
# print(b.title())
# print(' '.join(b))
# b=a.split(" ")
# print(b)

# A=set(['jOHN','Mary','Tina','Fiona','Claire','Eva','Ben','Bill','Bert'])
# # 全班學生
# B=set(['jOHN','Mary','Fiona','Claire','Ben','Bill'])
# # 英文及格
# C=set(['Mary','Fiona','Claire','Eva','Ben'])
# # 數學及格

# print("英文與數學及格",B&C)
# print("數學不及格",A-C)
# print('英文及格且數學不及格',B&A-C)
# print('英文與數學不及格',B&C) 
# print('數學或英文不及格',A^C)
# print('英文不及格',A-B)
# a='紅豆生南國,春來發幾枝?願君多采擷,此物最相思<作者:王維>'
# b='春眠不覺曉，處處聞啼鳥。夜來風雨聲，花落知多少? <作者:孟浩然>'
# x=set(a)
# x.remove(',')
# x.remove('?')
# x.remove('<')
# x.remove(':')
# x.remove('>')
# y=set(b)
# y.remove('，')
# y.remove('。')
# y.remove('?')
# y.remove('<')
# y.remove(':')
# y.remove('>')
# print(x&y)

姓名=[]
電子郵件=[]
x=input("請輸入姓名 :")
姓名.append(x)
y=input("請輸入電子郵件 :")
電子郵件.append(y)
x=input("請輸入姓名 :")
姓名.append(x)
y=input("請輸入電子郵件 :")
電子郵件.append(y)
x=input("請輸入姓名 :")
姓名.append(x)
y=input("請輸入電子郵件 :")
電子郵件.append(y)
A={'姓名':姓名,'電子郵件':電子郵件}
B

# print(A)
# Q=A.index
# G1=input('請輸入要查詢的郵件')
# print(Q)



























