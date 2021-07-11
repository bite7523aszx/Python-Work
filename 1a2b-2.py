import random
print("/*******************************猜数字游戏***********************************/ \
   游戏规则：系统随机给出1-9的4位数字，您可以输入您猜测的4位数字，系统会比较并给予反馈，A表示数字对，且位置对，B表示数字对位置不对，如1A2B表示有1位您猜对了数字和位置，有2位您猜对数字，但位置不对。您总共有6次机会，加油哦！")
total='123456789'
answer=random.sample(total,4)
for guessTimes in range(6):
   guess=""
   for inputErros in range(3):
      guess=input("请输入4位1-9的不重复数字：") 
      if guess.isdigit()==True and len(guess)==4:
         guessSet=set(guess)
         if len(guessSet)==4 and guessSet.isdisjoint(set('0')):
            break
   else:
      print("您没有理解游戏规则，游戏结束。")
      break   
   A=0
   B=0
   for j in range(4):
      if guess[j]==answer[j]:
         A+=1
      else:
         for k in range(4):
            if guess[j]==answer[k]:
               B+=1
   if A<4:
      if guessTimes<5:
         print("%dA%dB，您还有%d次机会。" %(A,B,5-guessTimes))
      else:
         print("很遗憾您没有猜对，答案是%s，再玩一局吧。" %(answer))   
   else:
      print("恭喜您猜对了！")
      break