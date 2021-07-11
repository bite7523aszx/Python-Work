x=int(input('輸入國文成績 :'))
y=int(input('輸入英文成績 :'))
z=int(input('輸入數學成績 :'))
if x>90 and y>90 and z>90:
    print("全能資優生")
elif x>=60 or y>=60 or z>=60 :
    if x>90 and y>90:
        print('雙語資優')
    elif x>90 and z>90:
        print('國數資優')
    elif y>90 and z>90:
        print('英數資優')
    else:
        print('還不錯')
elif x<=60 or y<=60 or z<=60:
    print('下次再加油')
else:
    print('下次再努力')

    


        



