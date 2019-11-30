#import module and something Command
import tkinter
import tkinter.messagebox
import os
import sys
import glob
from tkinter import *
from tkinter.font import Font
map=r'*.txt'
os.system('title 帳號管理員執行視窗')
#Def
def aea():
    def r():
        #r Code
        m=glob.glob(map)
        label11.config(text=m)
        mainWin.after(500, r)
    def seoa():
        def edit():
            def ep():
                #ep Code
                a = Entry31.get()
                b = Entry32.get()
                a1 = '帳號:'+a
                b1 = '密碼:'+b
                f=open(gfn,'w')
                f.truncate()
                f.write(a1)
                f.write('\n')
                f.write(b1)
                f.close()
                tkinter.messagebox.showinfo('帳號管理員', '完成更改')
                mainWin.destroy()
            #edit Code
            mainWin = tkinter.Tk()
            mainWin.title('編輯帳號')
            label31 = tkinter.Label(mainWin, text=gfn2)
            label32 = tkinter.Label(mainWin, text='新帳號')
            Entry31 = tkinter.Entry(mainWin, text='帳號', width='40')
            label33 = tkinter.Label(mainWin, text='新密碼')
            Entry32 = tkinter.Entry(mainWin, text='密碼', width='40')
            Button31 = tkinter.Button(mainWin, text='                              \n更改\n', command=ep)
            label31.pack()
            label32.pack()
            Entry31.pack()
            label33.pack()
            Entry32.pack()
            Button31.pack()
            mainWin.mainloop()
        def delfile():
            #delfile Code
            gfn3='del "'+gfn
            gfn4=gfn3+'"'
            os.system(gfn4)
            mainWin.destroy()
        #seoa Code
        getfilename = findaccount.get()
        gfn=getfilename+'.txt'
        if os.path.isfile(gfn):
            gfn2 = '編輯 '+getfilename+' 的資料'
            mainWin = tkinter.Tk()
            mainWin.title('新增和編輯帳號')
            mainWin.geometry('270x270')
            label21 = tkinter.Label(mainWin, text=gfn2)
            button21 = tkinter.Button(mainWin, text='                              \n更改帳號與密碼\n', command=edit)
            button22 = tkinter.Button(mainWin, text='                              \n刪除帳號與密碼\n', command=delfile)
            label21.pack()
            button21.pack()
            button22.pack()
            mainWin.mainloop()
        else:
            def create():
                a1 = Entry41.get()
                bb2 = Entry42.get()
                a12 = '帳號:'+a1
                bb21 = '密碼:'+bb2
                f=open(gfn,'w')
                f.truncate()
                f.write(a12)
                f.write('\n')
                f.write(bb21)
                f.close()
                tkinter.messagebox.showinfo('成功','建立成功')
                mainWin.destroy()
            gfnadd = '因為沒有 '+getfilename+' 的帳號紀錄，所以開始建立'
            mainWin = tkinter.Tk()
            mainWin.title('新增帳號')
            label41 = tkinter.Label(mainWin, text=gfnadd)
            label42 = tkinter.Label(mainWin, text='帳號')
            Entry41 = tkinter.Entry(mainWin, text='na', width='40')
            label43 = tkinter.Label(mainWin, text='密碼')
            Entry42 = tkinter.Entry(mainWin, text='np', width='40')
            Button41 = tkinter.Button(mainWin, text='                              \n建立\n', command=create)
            label41.pack()
            label42.pack()
            Entry41.pack()
            label43.pack()
            Entry42.pack()
            Button41.pack()
            mainWin.mainloop()
    #aea Code
    mainWin = tkinter.Tk()
    mainWin.title('新增和編輯帳號')
    label11 = Label(mainWin)
    label12 = tkinter.Label(mainWin, text='以上是所有此軟體紀錄的帳號\n輸入帳號名稱在下面(不用加.txt)，如果沒有紀錄則是新增，有的話是編輯\n(不能在名稱包含/\:?*"<>|)')
    findaccount = tkinter.Entry(mainWin, text='Search', width='40')
    button11 = tkinter.Button(mainWin, text='                              \n送出\n', command=seoa)
    label13 = tkinter.Label(mainWin, text='')
    label11.pack()
    label12.pack()
    findaccount.pack()
    button11.pack()
    label13.pack()
    r()
    mainWin.mainloop()
def read():
    def r():
        #r Code
        m=glob.glob(map)
        label11.config(text=m)
        mainWin.after(500, r)
    def readaccount():
        getfilename1 = findaccount1.get()
        gfn21=getfilename1+'.txt'
        if os.path.isfile(gfn21):
            f=open(gfn21,'r')
            rc=f.read()
            tkinter.messagebox.showinfo('閱讀帳號',rc)
        else:
            tkinter.messagebox.showinfo('錯誤','沒有這個帳號紀錄')
    mainWin = tkinter.Tk()
    mainWin.title('閱讀帳號')
    label11 = Label(mainWin)
    label12 = tkinter.Label(mainWin, text='以上是所有此軟體紀錄的帳號\n輸入帳號名稱在下面來閱讀(不用加.txt)')
    findaccount1 = tkinter.Entry(mainWin, text='Searched', width='40')
    button11 = tkinter.Button(mainWin, text='                              \n送出\n', command=readaccount)
    label13 = tkinter.Label(mainWin, text='\n')
    label11.pack()
    label12.pack()
    findaccount1.pack()
    button11.pack()
    label13.pack()
    r()
    mainWin.mainloop()
def about():
    mainWin = tkinter.Tk()
    mainWin.title('關於帳號管理員')
    mainWin.geometry('400x400')
    labelabout = tkinter.Label(mainWin, text='關於帳號管理員')
    Fontset = Font(family="Microsoft JhengHei", size=15)
    labelabout1 = tkinter.Label(mainWin, text='帳號管理員', font=Fontset)
    Fontset2 = Font(family="Microsoft JhengHei", size=2)
    labelabout2 = tkinter.Label(mainWin, text='原名為帳號與密碼管理軟體\n\n版本:3.0\n介面模組:Tkinter\n作者:梁承樸', font=Fontset2)
    labelabout.pack()
    labelabout1.pack()
    labelabout2.pack()
    mainWin.mainloop()
def quit():
    sys.exit()
mainWin = tkinter.Tk()
mainWin.title("帳號管理員")
mainWin.geometry("400x400")
labelhome1 = tkinter.Label(mainWin, text='首頁')
button=tkinter.Button(mainWin, text='                              \n新增和編輯帳號\n', command=aea)
button2=tkinter.Button(mainWin, text='                              \n閱讀帳號\n',command=read)
button3=tkinter.Button(mainWin, text='                              \n關於帳號管理員\n', command=about)
button4=tkinter.Button(mainWin, text='                              \n離開\n', command=quit)
Fontset = Font(family="Microsoft JhengHei", size=15)
labelhome2 = tkinter.Label(mainWin, text='帳號管理員', font=Fontset)
labelhome1.pack()
button.pack()
button2.pack()
button3.pack()
button4.pack()
labelhome2.pack(side='bottom')
mainWin.mainloop()