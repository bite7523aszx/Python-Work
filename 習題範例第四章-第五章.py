# cost=int(input('輸入購買金額 :'))
# 數量=int(input('購買數量 :'))
# 總金額=cost*數量
# if 數量>=3 and 總金額>=2000:
#     print(int(總金額*0.9*0.7))
# if 數量>=3 and 總金額<=2000:
#     print(int(總金額))
# if 數量<3 and 總金額>=2000:
#     print(int(總金額*0.9))
# if 數量<3 and 總金額<2000:
#     print(總金額)


#   判斷BMI 體重/(身高*身高) 身高(公尺)

# kg=float(input('請輸入體重(公斤) :'))
# cm=float(input('請輸入身高(公分) :'))/100
# bmi=kg/(cm**2)
# if bmi <18:
#     print('BMI值',int(bmi),'體重過輕')
# elif bmi <24:
#     print('BMI值',int(bmi),'體重正常')
# elif bmi <27:
#     print('BMI值',int(bmi),'體重過重')
# else :
#   print('BMI值',int(bmi),'體重肥胖')

# s=(input('請輸入要查詢字元 :'))
# for i in s:
#     print(i,'=',ord(i))
#     # 查詢ASCII 

#  登入失敗三次跳出程式 !1
# acc='abc'
# pwd='123'
# i=3
# for x in range(i):
#     i=i-1
#     acc=input('輸入帳號')
#     pwd=input('輸入密碼')
#     if (acc=='abc'and pwd=='123'):
#         print('登入成功')
#         break
#     elif (acc!='abc' and pwd=='123'):
#         print('帳號錯誤')
#     elif (acc=='abc'and pwd!='123'):
#         print('密碼錯誤') 
#     elif (i==0):
#         print('錯誤超過三次')
#         break
#  登入失敗三次跳出程式 !2
# acc='abc'
# pwd='123'
# i=0
# while True :
#     acc=input('輸入帳號')
#     pwd=input('輸入密碼')
#     if (acc=='abc'and pwd=='123'):
#         print('登入成功')
#         break
#     elif (acc!='abc' and pwd=='123'):
#         i=i+1
#         print('帳號錯誤')
#         if i>=3:
#             print('錯誤超過',i,'次')
#             break
#     elif (acc=='abc'and pwd!='123'):
#         i=i+1
#         print('密碼錯誤')
#         if i>=3:
#             print('錯誤超過',i,'次')
#             break            
# 剪刀,石頭,布
# import random
# # t=random.randint(1,4)
# g=0
# a=0
# y=0
# x=0
# # H=x/(a+y+x)*100
# while True:
#     t=random.randint(1,4) 
#     g=int(input('請輸入1到3數字,1=剪刀,2=石頭,3=布 : '))        
#     if g==t:
#         a=a+1
#         H=x/(a+y+x)*100
#         print('平手',a,'次')   
#         d=input('還要繼續嗎 Y/N :')
#         if (d=='n'):
#             print('勝率為',int(H),'%')
#             break
#     elif g==1 and t==3 or g==2 and t==1 or g==3 and t==2 :
#         #  剪刀贏布, 布贏石頭, 石頭贏剪刀,
#         x=x+1
#         H=x/(a+y+x)*100
#         print('你贏了',x,'次')
#         d=input('還要繼續嗎 Y/N :')
#         if (d=='n'):
#             print('勝率為',int(H),'%')
#             break
#     else:
#     # elif g==1 and t==2 or g==2 and t==3 or g==3 and t==1  :
#         # 剪刀輸石頭,石頭輸布, 布輸剪刀 ,
#         y=y+1
#         H=x/(a+y+x)*100
#         print('你輸了',y,'次')
#         d=input('還要繼續嗎 Y/N :')
#         if (d=='n'):
#             print('勝率為',int(H),'%')
#             break
# a=int(input('請輸入年分 :'))
# if a%4!=0:
#     print(a,'不是閏年')
# elif a%4==0 and a%100!=0 :
#     print(a,'是閏年')
# elif a%100==0 and a%400!=0:
#     print(a,'不是閏年')
# elif a%400==0:
#     print(a,'是閏年')   

for i in range(18,20):
    for j in range(1,20):
        print(i,'*',j,'=',i*j,"\t",sep='',end='',)
    print()
    
    
        

        
        
             
    
        

    
    

            
        
                
                
               
    
            
        

        









