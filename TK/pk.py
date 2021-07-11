import tkinter as tk
import math
import random

window = tk.Tk()
window.title('猜數字')
window.geometry('800x600')
window.configure(background='yellow')
i = random.randint(0,100)
print(i) 
x=0
y=100
cc=0
def calculate_bmi_number():
    a=int(t_entry.get()) # 抓取資料.get
    #計算BMI
    result = '你猜的數字：{} {}'.format(a,get_bmi_status_description(a))
    # 回傳計算好的BMI
    print(result)
    result_label.configure(text=result)
    # 顯示在label text=result

def get_bmi_status_description(a):
    global x
    global y
    global cc
    xy = "請輸入猜的數字(" + str(x) + "~" + str(y) + ")"
    if a==i:
        cc=cc+1
        return '\n恭喜你猜對了''\n''總共猜了'+ str(cc)+'次'
    elif a>i:
        cc=cc+1
        x=i-1
        xy = "請輸入猜的數字(" + str(x) + "~" + str(y) + ")"
        return '\n猜小一點' +xy+'\n'+ str(cc)
    elif a<i:  
        cc=cc+1
        y=i+1
        xy = "請輸入猜的數字(" + str(x) + "~" + str(y) + ")"
        return '\n猜大一點' +xy+'\n'+str(cc)

        # view_label.configure(text=view)
header_label = tk.Label(window, text='猜數字', font=('Arial', 30))
input_label = tk.Label(window, text='輸入', font=('Arial', 30))
t_entry = tk.Entry (window, font=('Arial', 30))
total_btn = tk.Button(window, text='馬上猜',command=calculate_bmi_number,font=('Arial', 30))
result_label = tk.Label(window, font=('Arial', 20), width=30, height=3 )
# 版面配置
header_label.grid(row=0, column=0, columnspan=2)
input_label.grid(row=1,column=0)
t_entry.grid(row=1, column=1)
total_btn.grid(row=3, column=0)  # 馬上猜
result_label.grid(row=3, column=1)  # 顯示結果


window.mainloop()