from tkinter import *
from tkinter.messagebox import *
import json
import random
import matplotlib.colors as mcolors

class Denglu:
    def __init__(self,rot):
        self.root=rot
        self.root.title("图书管理系统")
        self.root.configure(bg='black')
        self.root.geometry("600x400+100+200")
        le=Label(self.root,text="图 书 管 理 系 统",font=("KaiTi",35),bg="black",fg="white")
        le.pack(pady=30)

#用户名1
        self.fr1=Frame(self.root,bg="black")
        self.fr1.pack(pady=14)
        self.la1=Label(self.fr1,text="用户名 ",font=("KaiTi",20),bg="white",fg="black")
        self.la1.pack(side=LEFT,padx=10)
        self.en1=Entry(self.fr1,font=("KaiTi",20),width=15)
        self.en1.pack(side=LEFT)
        self.la1 = Label(self.fr1, text="  ", font=("KaiTi", 20), bg="black")
        self.la1.pack(side=LEFT, padx=10)

#密码2
        self.fr2 = Frame(self.root, bg="black")
        self.fr2.pack(pady=14)
        self.la2 = Label(self.fr2, text="密   码", font=("KaiTi", 20),bg="white",fg="black")
        self.la2.pack(side=LEFT, padx=10)
        self.en2 = Entry(self.fr2, font=("KaiTi", 20), width=15,show="*")
        self.en2.pack(side=LEFT)
        self.la2 = Label(self.fr2, text="  ", font=("KaiTi", 20), bg="black")
        self.la2.pack(side=LEFT, padx=10)

#验证码3
        self.fr3 = Frame(self.root, bg="black")
        self.fr3.pack(pady=14)
        self.la21 = Label(self.fr3, text="  ", font=("KaiTi", 20), bg="black")
        self.la21.pack(side=LEFT, padx=10)
        self.la3 = Label(self.fr3, text="验证码 ", font=("KaiTi", 20),bg="white",fg="black")
        self.la3.pack(side=LEFT, padx=10)
        self.en3 = Entry(self.fr3, font=("KaiTi", 20), width=15)
        self.en3.pack(side=LEFT)
        self.la3 = Label(self.fr3, text=self.yanzheng(), font=("KaiTi", 20), bg="white")
        self.la3.pack(side=LEFT, padx=10)

#登录4
        self.fr4=Frame(self.root,bg="black")
        self.fr4.pack(pady=14)
        self.bu4=Button(self.fr4,text="登录",font=("KaiTi", 18),activebackground=self.yanse(),activeforeground=self.yanse(),command=self.denglu)
        self.bu4.pack(side=LEFT,padx=30)

#注册5
        self.bu5=Button(self.fr4,text="注册",font=("KaiTi", 18),activebackground=self.yanse(),activeforeground=self.yanse(),command=self.zhuce)
        self.bu5.pack(side=LEFT,padx=30)

#退出6
        self.bu6=Button(self.fr4,text="退出",font=("KaiTi", 18),activebackground=self.yanse(),activeforeground=self.yanse(),command=self.tuichu)
        self.bu6.pack(side=LEFT,padx=30)

    @staticmethod
    def tuichu():
        root.destroy()

    def  zhuce(self):
        self.cf = Toplevel(root)
        self.cf.title("注册")
        self.cf.geometry("500x250+500+300")

    # 用户名行
        f1 = Frame(self.cf)
        f1.pack(pady=5,fill=X)
        Label(f1, text="用户名:", font=("KaiTi", 20)).pack(side=LEFT,padx=5)
        self.ee_user = Entry(f1, font=("KaiTi", 20), width=10)
        self.ee_user.pack(side=RIGHT, padx=50)

    # 密码行
        f2 = Frame(self.cf)
        f2.pack(pady=5,fill=X)
        Label(f2, text="请输入密码:", font=("KaiTi", 20)).pack(side=LEFT,padx=5)
        self.en5 = Entry(f2, font=("KaiTi", 20), width=10, show="*")
        self.en5.pack(side=RIGHT, padx=50)

    # 确认密码行
        f3 = Frame(self.cf)
        f3.pack(pady=5,fill=X)
        Label(f3, text="请再次输入密码:", font=("KaiTi", 20)).pack(side=LEFT)
        self.en6 = Entry(f3, font=("KaiTi", 20), width=10, show="*")
        self.en6.pack(side=RIGHT, padx=50)
        self.qr=Button(self.cf,text="确认注册",font=("KaiTi", 15),activebackground=self.yanse(),activeforeground=self.yanse(),command=self.zqr)
        self.qr.pack(pady=20,padx=50)

    def zqr(self):
        if self.ee_user.get()=="" or self.en5.get()=="" or self.en6.get()=="":
            showinfo("error","请填写完整")
            self.qr.config(activebackground=self.yanse(),activeforeground=self.yanse())
            return
        if self.en5.get()==self.en6.get():
            aa=self.ee_user.get()
            bb=self.en5.get()
            with open("信息管理.txt", "a",encoding="utf-8") as file:
                file.write("{\"用户名\":")
                file.write(aa)
                file.write(",\"密码\":")
                file.write(bb)
                file.write("}\n")
                showinfo("欢迎", "注册成功")
            self.cf.destroy()
        else:
            showinfo("error","密码不一致")

    @staticmethod
    def yanse():
        colour = list(mcolors.CSS4_COLORS.keys())
        xs = random.choice(colour)
        return xs

    def denglu(self):
        a=self.en1.get()
        b =self.en2.get()
        c=self.en3.get()
        found = False
        user=False
        with open("信息管理.txt", "a+",encoding="utf-8") as file:
            file.seek(0)
            for i in file.readlines():
                i = json.loads(i)
                data_str = {key: str(value) for key, value in i.items()}
                if a == data_str["用户名"] and b == data_str["密码"] and c == self.la3.cget("text"):
                    showinfo("welcome", "欢迎您:python")
                    found = True
                    break
                if a==data_str["用户名"]:
                    user=True
            if not found:
                if user:
                    showinfo("error", "输入错误！\n请重新输入！")
                else:
                    showinfo("error", "用户不存在,\n请先注册!")
                    self.en1.delete(0, END)#清空
                self.en2.delete(0, END)
                self.en3.delete(0, END)
                self.la3.config(text=self.yanzheng())#刷新验证码
                self.bu4.config(activebackground=self.yanse(),activeforeground=self.yanse())#刷新按钮

    @staticmethod
    def yanzheng():
        s = ""
        for i in range(6):
            if random.randint(0, 1) == 0:
                s += str(random.randint(0, 9))
            else:
                if random.randint(0, 1) == 0:
                    s += chr(random.randint(65, 90))
                else:
                    s += chr(random.randint(97, 122))
        return s

if __name__ == '__main__':
    root = Tk()
    Denglu(root)
    root.mainloop()