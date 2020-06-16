import tkinter as tk
import tkinter.font as tf
def buttonValue():
   global x1
   x1='bj'
def buttonValue1():
   global x1
   x1='yf'
def buttonValue11():
   global x1
   x1='gfxf'
def buttonValue12():
    global x1
    x1 = 'ccyl'
def buttonValue0():
   global mrow
   mrow=0
   root.destroy()
def buttonValue01():
   global mrow
   mrow=1
   root.destroy()
def gui():
    global root
    root = tk.Tk()
    root.minsize(500, 700)
    f = tf.Font(family='叶根友毛笔行书2.0版', size=48)
    b1 = tk.Button(root, text='百家', font=f, command=buttonValue, bg='BurlyWood')
    b1.pack()
    b2 = tk.Button(root, text='易方达', font=f, command=buttonValue1, bg='BurlyWood')
    b2.pack()
    b2 = tk.Button(root, text='易方达消费', font=f, command=buttonValue11, bg='BurlyWood')
    b2.pack()
    # b2=tk.Button(root,text = '中欧医疗',font=f,command=buttonValue12,bg='BurlyWood')
    # b2.pack( )
    b3 = tk.Button(root, text='测试数据', font=f, command=buttonValue0, bg='BurlyWood')
    b3.pack()
    b4 = tk.Button(root, text='实际数据', font=f, command=buttonValue01, bg='BurlyWood')
    b4.pack()
    root.mainloop()
    return x1,mrow