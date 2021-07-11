import random
import tkinter as tk
from tkinter import *
window = tk.Tk()
window.title('1A2B')
window.geometry('800x600')
window.configure(background='black')
a=0
b=0
item=[0,1,2,3,4,5,6,7,8,9]
random.shuffle(item)
print(item)
ans=""
for i in range(4):
    ans+=str(item[i])
print(ans)
def start():
    global a
    global b
    global ans
    n=syin_entry.get()
    for Q in range(100):
        if n==ans:
            final='恭喜猜對了\n答案就是{}'.format(ans)
            view_Label.configure(text=final)
        elif len(n)!=len(ans):
            final='請輸入正確4位元數字'
            view_Label.configure(text=final)
        else:
            for j in range(4):
                for k in range(4):
                    if j==k and n[j]==ans[k]:
                        a+=1
                    elif n[j]==ans[k]:
                        b+=1
            final='{0}\n顯示結果:{1}a{2}b'.format(n,a,b)
            view_Label.configure(text=final)
            a=0
            b=0
def clear():
    window.destroy()
title_label = tk.Label(window, text='1A2B', font=('Arial', 15))
sy_label = tk.Label(window, text='輸入數字', font=('Arial', 15))
syin_entry = tk.Entry(window, font=('Arial', 30))
# syou_label = tk.Label(window, text='產生幾位數', font=('Arial', 15))
# syoo_entry = tk.Entry(window, font=('Arial', 30))
stbt_btn= tk.Button(window, text='確定答案',command=start,font=('Arial', 15))
# stbb_btn= tk.Button(window, text='產生位數',command=new,font=('Arial', 15))
# stan_btn= tk.Button(window, text='產生答案',command=answer,font=('Arial', 15))
view_Label=tk.Label(window, font=('Arial', 20), width=30, height=3)
clear_brn=tk.Button(window, text='退出遊戲',command=clear,font=('Arial', 15))
# ans_btn= tk.Button(window, text='顯示答案', command=answer,font=('Arial', 30))
# ans1_Label = tk.Entry(window, font=('Arial', 30))
title_label.grid(row=0, column=2, columnspan=3)
# syou_label.grid (row=1,column=1)
# syoo_entry.grid (row=1,column=2)
#
#
sy_label.grid(row=3, column=1)
syin_entry.grid(row=3, column=2)
#
#
# stbt_btn.grid(row=4, column=4, columnspan=4)
# stbb_btn.grid(row=4, column=1, columnspan=4)
# stan_btn.grid(row=4, column=3, columnspan=4)
view_Label.grid(row=5,column=2)
clear_brn.grid(row=6,column=2)
stbt_btn.grid(row=6, column=3)
# ans_btn.grid(row=7,column=1)
# ans1_Label.grid(row=7,column=2)
window.mainloop()