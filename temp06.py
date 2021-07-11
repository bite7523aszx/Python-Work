# aa = True
# print(type(aa))

# if aa :
#    print("is True")
# eles :
#    print(is False)


aa = input("請輸入目前溫度 :")
#print(type(aa))
#print(aa)

bb = int(aa)
#print(type(bb))
#print(bb)

if bb > 30 :
    print("Temp.", bb, "is too hot.")
elif bb < 10 :
    print("Temp.", bb, "is too hot.")
else :
   print("Temp.", bb, "is OK.")


print("="*60)
cc = bb > 30
print(type(cc))
print(cc)

print("="*60)
dd = not (bb < 30)
print(type(cc))
print(cc)

# if 條件判斷式
# else 動作2(判斷2)
# input 輸入