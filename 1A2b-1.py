# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 11:54:41 2020

@author: HSNL
"""

#1A2B game
import random
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random.shuffle(items)  # 打亂順序
answer=''
a_count=0 # initial A count
b_count=0 # initial B count
c=0
n=int(input('產生幾位元數'))
# number=input('輸入數字: ')

for i in range(n):   
    answer+=str(items[i])  #itme 每個元素放進 answer 注意資料型態 
print(answer)
while(True):
    c+=1
    number=input('輸入{}位元數字 :'.format(n))  #需在迴圈裡面!才能夠每次都猜數字
    if len(number)!=len(answer):  #cheak all input is digit
        print('請輸入正確{}位元數字'.format(n))
    else:
        if number==answer:
                print('恭喜猜對了','總共猜了',c,'次')
                break
        for i in range(n):  
            for j in range(n):
                if i==j and number[i]==answer[j]: 
                    a_count+=1
                elif number[i]==answer[j]:
                    b_count+=1
        print('{0}A{1}B''\n''總共猜了''{2}''次'.format(a_count,b_count,c))
        a_count=0  # 每次迴圈判斷完需為零值
        b_count=0  #