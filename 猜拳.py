import random
gesture = ['石頭' , '剪刀', '布']
wins = 0 
print("數字含義 : 1:石頭 ,2:剪刀 ,3:布 ,0:退出遊戲")
for i in range(20):
    user = int(input("請出拳:"))
    if user ==0:
        print("退出遊戲")
        break
    if user in range(1,4):
        computer = int(random.randint(1,3))
        print("computer出拳:",computer)
        print("玩家: {0} VS 計算機: {1}".format(gesture[user-1],gesture[computer-1]))
        if(user == computer):
            print("兩位心有靈犀,是平局哦")
        elif(user == 1 and computer == 2) or (user == 2 and computer == 3) or (user == 3 and computer == 1):
            print("玩家獲勝,電腦弱爆了!")
            wins = wins + 1
        else:
            print("電腦獲勝,玩家表示不服,要決戰到天亮")
    else:
        print("您的出拳不符合規則,請重新出拳")
print("兩位交戰 ", i,"次")
print("玩家獲勝次數: ", wins,"次")
print("玩家獲勝機率:",round(wins/i,2))













