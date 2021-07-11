import random
item=[0,1,2,3,4,5,6,7,8,9]
random.shuffle(item)
print(item)
def answer():
    global item
    
    for i in range(4):
        ans+=str(item[i])
    return ans

