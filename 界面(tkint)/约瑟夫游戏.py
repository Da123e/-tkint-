from tkinter import *
from tkinter.messagebox import *
import json
import random

class Denglu:
    def __init__(self,rot):
        self.root=rot
        self.root.title("约瑟夫生死者游戏")
        self.js=self.yanse()
        self.root.configure(bg=self.js)
        self.root.geometry("600x450+100+200")
        le=Label(self.root,text="账 号 管 理 系 统",font=("kaiti",35),bg="red",fg="white")
        le.pack(pady=30)

#用户名1
        self.fr1=Frame(self.root,bg=self.js)
        self.fr1.pack(pady=14)
        self.la1=Label(self.fr1,text="用户名 ",font=("KaiTi",20),bg="white",fg="black")
        self.la1.pack(side=LEFT,padx=10)
        self.en1=Entry(self.fr1,font=("KaiTi",20),width=15)
        self.en1.pack(side=LEFT)
        self.la1 = Label(self.fr1, text="  ", font=("KaiTi", 20), bg=self.js)
        self.la1.pack(side=LEFT, padx=10)

#密码2
        self.fr2 = Frame(self.root, bg=self.js)#创建密码输入框框架
        self.fr2.pack(pady=14)
        self.la2 = Label(self.fr2, text="密   码", font=("KaiTi", 20),bg="white",fg="black")
        self.la2.pack(side=LEFT, padx=10)
        self.en2 = Entry(self.fr2, font=("KaiTi", 20), width=15,show="*")#
        self.en2.pack(side=LEFT)
        self.la2 = Label(self.fr2, text="  ", font=("KaiTi", 20), bg=self.js)
        self.la2.pack(side=LEFT, padx=10)

#验证码3
        self.fr3 = Frame(self.root, bg=self.js)
        self.fr3.pack(pady=14)
        self.la21 = Label(self.fr3, text="  ", font=("KaiTi", 20), bg=self.js)
        self.la21.pack(side=LEFT, padx=10)
        self.la3 = Label(self.fr3, text="验证码 ", font=("KaiTi", 20),bg="white",fg="black")
        self.la3.pack(side=LEFT, padx=10)
        self.en3 = Entry(self.fr3, font=("KaiTi", 20), width=15)
        self.en3.pack(side=LEFT)
        self.la3 = Label(self.fr3, text=self.yanzheng(), font=("KaiTi", 20), bg=self.js)
        self.la3.pack(side=LEFT, padx=10)

#登录4
        self.fr4=Frame(self.root,bg=self.js)
        self.fr4.pack(pady=14)
        self.bu4=Button(self.fr4,text="登录",font=("KaiTi", 18),activebackground=self.yanse(),activeforeground=self.yanse(),command=self.denglu)
        self.bu4.pack(side=LEFT,padx=30)

#注册5
        self.bu5=Button(self.fr4,text="注册",font=("KaiTi", 18),activebackground=self.yanse(),activeforeground=self.yanse(),command=self.zhuce)
        self.bu5.pack(side=LEFT,padx=30)

#退出6
        self.bu6=Button(self.fr4,text="退出",font=("KaiTi", 18),activebackground=self.yanse(),activeforeground=self.yanse(),command=self.tuichu)
        self.bu6.pack(side=LEFT,padx=30)

#提示7
        self.fr7 = Frame(self.root, bg=self.js)#创建密码输入框框架
        self.fr7.pack(pady=14, fill=X)
        self.la7 = Label(self.fr7, text="温馨提示：\n未满16周岁禁止玩游戏", font=("KaiTi", 15),bg=self.js,fg="black")
        self.la7.pack(side=RIGHT, padx=10)

    @staticmethod
    def tuichu():
        root.destroy()

    def  zhuce(self):
        self.cf = Toplevel(root)
        self.cf.title("注册")
        self.cf.geometry("500x250+500+300")
        self.bu5.config(activebackground=self.yanse(), activeforeground=self.yanse())  # 刷新按钮

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
            # 使用相对路径访问信息管理.txt文件
            import os
            # 获取当前脚本所在目录
            script_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(script_dir, "信息管理.txt")
            with open(file_path, "a",encoding="utf-8") as file:
                file.write("{\"用户名\":\"")
                file.write(aa)
                file.write("\",\"密码\":\"")
                file.write(bb)
                file.write("\",\"游戏次数\":0")
                file.write("}\n")
                showinfo("欢迎", "注册成功")
            self.cf.destroy()
        else:
            showinfo("error","密码不一致")

    @staticmethod
    def yanse():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = f"#{r:02x}{g:02x}{b:02x}"
        return color

    def denglu(self):
        a=self.en1.get()
        b =self.en2.get()
        c=self.en3.get()
        found = False
        user=False
        import os
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "信息管理.txt")
        with open(file_path, "a+",encoding="utf-8") as file:
            file.seek(0)
            for i in file.readlines():
                i = json.loads(i)
                data_str = {key: str(value) for key, value in i.items()}
                if a == data_str["用户名"] and b == data_str["密码"] and c == self.la3.cget("text"):
                    showinfo(f"welcome", f"欢迎您:{a}")
                    found = True
                    self.root.withdraw()
                    game_window = Toplevel(self.root)
                    YuesefuGame(game_window, a)
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

class YuesefuGame:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.root.title("约瑟夫生死者游戏")
        self.root.geometry("1000x700+100+50")
        # 现代色彩方案
        self.colors = {
            "bg": "#1a1a2e",  # 深蓝色背景
            "accent": "#16213e",  # 深靛蓝色
            "primary": "#0f3460",  # 主色调
            "success": "#4ecdc4",  # 成功绿色
            "danger": "#e94560",  # 危险红色
            "warning": "#f39c12",  # 警告黄色
            "text": "#ffffff",  # 白色文本
            "text_dark": "#000000",  # 深色文本
            "border": "#333355",  # 边框颜色
            "input_bg": "#2a2a4a",  # 输入框背景
            "highlight": "#6c5ce7"  # 高亮色
        }
        self.root.configure(bg=self.colors["bg"])
        main_frame = Frame(self.root, bg=self.colors["bg"])
        main_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)
        title_frame = Frame(main_frame, bg=self.colors["primary"])
        title_frame.pack(fill=X, pady=(0, 20))
        title_frame.pack_propagate(False)
        title_frame.configure(height=80)
        title_label = Label(title_frame, text="约瑟夫生死者游戏", font=("Microsoft YaHei", 32, "bold"), 
                           bg=self.colors["primary"], fg=self.colors["text"])
        title_label.pack(expand=True, fill=BOTH)
        content_frame = Frame(main_frame, bg=self.colors["bg"])
        content_frame.pack(fill=BOTH, expand=True)
        left_frame = Frame(content_frame, bg=self.colors["accent"], bd=2, relief="groove", 
                          highlightbackground=self.colors["border"], highlightthickness=2)
        left_frame.pack(side=LEFT, fill=Y, padx=(0, 20), pady=10, ipadx=20, ipady=20)
        left_frame.configure(width=400)
        # 游戏说明
        info_label = Label(left_frame, text="游戏规则", font=("Microsoft YaHei", 20, "bold"), 
                          bg=self.colors["accent"], fg=self.colors["success"])
        info_label.pack(anchor=W, pady=(0, 10))
        rule_text = "N个人围成一圈，从第k个人开始报数，每数到m的人出圈，最后剩下的人获胜。"
        rule_label = Label(left_frame, text=rule_text, font=("Microsoft YaHei", 12), 
                          bg=self.colors["accent"], fg=self.colors["text"], wraplength=350, justify=LEFT)
        rule_label.pack(anchor=W, pady=(0, 20))
        param_label = Label(left_frame, text="游戏参数", font=("Microsoft YaHei", 20, "bold"), 
                          bg=self.colors["accent"], fg=self.colors["success"])
        param_label.pack(anchor=W, pady=(0, 15))
        param_frame = Frame(left_frame, bg=self.colors["accent"])
        param_frame.pack(fill=X, pady=5)
        Label(param_frame, text="总人数(N):", font=("Microsoft YaHei", 14), 
              bg=self.colors["accent"], fg=self.colors["text"]).grid(row=0, column=0, sticky=E, padx=10, pady=10)
        self.n_var = IntVar(value=10)
        n_entry = Entry(param_frame, textvariable=self.n_var, font=("Microsoft YaHei", 14), 
                       width=12, bg=self.colors["input_bg"], fg=self.colors["text"], 
                       insertbackground=self.colors["text"], relief="groove", bd=2)
        n_entry.grid(row=0, column=1, padx=10, pady=10)
        Label(param_frame, text="起始位置(k):", font=("Microsoft YaHei", 14), 
              bg=self.colors["accent"], fg=self.colors["text"]).grid(row=1, column=0, sticky=E, padx=10, pady=10)
        self.k_var = IntVar(value=1)
        k_entry = Entry(param_frame, textvariable=self.k_var, font=("Microsoft YaHei", 14), 
                       width=12, bg=self.colors["input_bg"], fg=self.colors["text"], 
                       insertbackground=self.colors["text"], relief="groove", bd=2)
        k_entry.grid(row=1, column=1, padx=10, pady=10)
        Label(param_frame, text="报数间隔(m):", font=("Microsoft YaHei", 14), 
              bg=self.colors["accent"], fg=self.colors["text"]).grid(row=2, column=0, sticky=E, padx=10, pady=10)
        self.m_var = IntVar(value=3)
        m_entry = Entry(param_frame, textvariable=self.m_var, font=("Microsoft YaHei", 14), 
                       width=12, bg=self.colors["input_bg"], fg=self.colors["text"], 
                       insertbackground=self.colors["text"], relief="groove", bd=2)
        m_entry.grid(row=2, column=1, padx=10, pady=10)
        button_frame = Frame(left_frame, bg=self.colors["accent"])
        button_frame.pack(fill=X, pady=(20, 0))
        self.start_btn = Button(button_frame, text="开始游戏", font=("Microsoft YaHei", 16, "bold"), 
                               bg=self.colors["success"], fg=self.colors["text_dark"], 
                               activebackground=self.colors["highlight"], activeforeground=self.colors["text"],
                               relief="flat", bd=0, padx=20, pady=10, command=self.start_game, cursor="hand2")
        self.start_btn.pack(side=LEFT, padx=(0, 10), pady=10, fill=X, expand=True)
        self.return_btn = Button(button_frame, text="返回登录", font=("Microsoft YaHei", 16, "bold"), 
                               bg=self.colors["primary"], fg=self.colors["text"], 
                               activebackground=self.colors["highlight"], activeforeground=self.colors["text"],
                               relief="flat", bd=0, padx=20, pady=10, command=self.return_login, cursor="hand2")
        self.return_btn.pack(side=LEFT, padx=5, pady=10, fill=X, expand=True)
        self.exit_btn = Button(button_frame, text="退出游戏", font=("Microsoft YaHei", 16, "bold"), 
                             bg=self.colors["danger"], fg=self.colors["text"], 
                             activebackground=self.colors["highlight"], activeforeground=self.colors["text"],
                             relief="flat", bd=0, padx=20, pady=10, command=self.exit_game, cursor="hand2")
        self.exit_btn.pack(side=LEFT, padx=(10, 0), pady=10, fill=X, expand=True)
        right_frame = Frame(content_frame, bg=self.colors["accent"], bd=2, relief="groove",
                          highlightbackground=self.colors["border"], highlightthickness=2)
        right_frame.pack(side=RIGHT, fill=BOTH, expand=True, pady=10, ipadx=20, ipady=20)
        process_label = Label(right_frame, text="游戏过程", font=("Microsoft YaHei", 20, "bold"), 
                             bg=self.colors["accent"], fg=self.colors["success"])
        process_label.pack(anchor=W, pady=(0, 15))
        
        self.process_text = Text(right_frame, font=("Microsoft YaHei", 12), 
                               bg=self.colors["input_bg"], fg=self.colors["text"], 
                               insertbackground=self.colors["text"], relief="groove", bd=2,
                               wrap="word", height=15)
        self.process_text.pack(fill=BOTH, expand=True, pady=(0, 20))
        process_scrollbar = Scrollbar(self.process_text, command=self.process_text.yview)
        process_scrollbar.pack(side=RIGHT, fill=Y)
        self.process_text.config(yscrollcommand=process_scrollbar.set)
        result_label = Label(right_frame, text="游戏结果", font=("Microsoft YaHei", 20, "bold"), 
                           bg=self.colors["accent"], fg=self.colors["success"])
        result_label.pack(anchor=W, pady=(0, 15))
        
        self.result_text = Text(right_frame, font=("Microsoft YaHei", 12), 
                              bg=self.colors["input_bg"], fg=self.colors["text"], 
                              insertbackground=self.colors["text"], relief="groove", bd=2,
                              wrap="word", height=8)
        self.result_text.pack(fill=BOTH, expand=True)
        result_scrollbar = Scrollbar(self.result_text, command=self.result_text.yview)
        result_scrollbar.pack(side=RIGHT, fill=Y)
        self.result_text.config(yscrollcommand=result_scrollbar.set)
    def start_game(self):
        try:
            n = self.n_var.get()
            k = self.k_var.get()
            m = self.m_var.get()
            if n < 1 or k < 1 or m < 1:
                showinfo("错误", "请输入正整数")
                return
            # 清空之前的内容
            self.process_text.delete(1.0, END)
            self.result_text.delete(1.0, END)
            players = list(range(1, n + 1))
            # 游戏过程 - 添加彩色文本和动态效果
            self.process_text.tag_config("title", foreground=self.colors["success"], font=("Microsoft YaHei", 14, "bold"))
            self.process_text.tag_config("normal", foreground=self.colors["text"])
            self.process_text.tag_config("out", foreground=self.colors["danger"])
            self.process_text.tag_config("highlight", foreground=self.colors["warning"])
            self.process_text.insert(END, f"🎮 游戏开始！\n", "title")
            self.process_text.insert(END, f"👥 共有 {n} 名玩家围成一圈\n", "normal")
            self.process_text.insert(END, f"🎯 从第 {k} 名玩家开始报数\n", "normal")
            self.process_text.insert(END, f"🔢 每数到 {m} 的玩家出圈\n\n", "normal")
            
            # 起始索引，确保在合法范围内
            index = (k - 1) % n
            out_order = []
            round_count = 1
            self.root.update()
            self.root.after(500)  # 1秒延迟
            while len(players) > 1:
                index = index % len(players)
                self.process_text.insert(END, f"\n🔄 第 {round_count} 轮报数开始！\n", "highlight")
                self.process_text.insert(END, f"   当前玩家列表：{players}\n", "normal")
                self.process_text.insert(END, f"   从玩家 {players[index]} 开始报数\n", "normal")
                self.root.update()
                self.root.after(1500)  # 1.5秒延迟
                index = (index + m - 1) % len(players)
                out_player = players.pop(index)
                out_order.append(out_player)
                self.process_text.insert(END, f"   ❌ 玩家 {out_player} 报数到 {m}，出圈！\n", "out")
                self.process_text.insert(END, f"   ✅ 剩余玩家：{players}\n", "normal")
                self.root.update()
                self.root.after(2000)
                round_count += 1
            winner = players[0]
            self.process_text.insert(END, f"\n🏆 游戏结束！\n", "title")
            self.process_text.insert(END, f"   获胜者是：玩家 {winner}\n", "highlight")
            self.process_text.insert(END, f"   总共进行了 {round_count - 1} 轮\n", "normal")
            self.process_text.see(END)
            self.result_text.tag_config("title", foreground=self.colors["success"], font=("Microsoft YaHei", 16, "bold"))
            self.result_text.tag_config("normal", foreground=self.colors["text"])
            self.result_text.tag_config("winner", foreground=self.colors["warning"], font=("Microsoft YaHei", 14, "bold"))
            
            self.result_text.insert(END, f"🎉 游戏结束！\n", "title")
            self.result_text.insert(END, f"\n🏆 获胜者：玩家 {winner}\n", "winner")
            self.result_text.insert(END, f"\n📋 游戏统计：\n", "normal")
            self.result_text.insert(END, f"   - 初始玩家数：{n}\n", "normal")
            self.result_text.insert(END, f"   - 起始位置：{k}\n", "normal")
            self.result_text.insert(END, f"   - 报数间隔：{m}\n", "normal")
            self.result_text.insert(END, f"   - 总轮数：{round_count - 1}\n", "normal")
            self.result_text.insert(END, f"   - 出圈顺序：{out_order}\n", "normal")
            self.update_game_count()
            
        except Exception as e:
            showinfo("错误", f"游戏出错：{str(e)}")
    def update_game_count(self):
        """更新用户游戏次数"""
        try:
            users = []
            import os
            script_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(script_dir, "信息管理.txt")
            with open(file_path, "r", encoding="utf-8") as file:
                for line in file:
                    user = json.loads(line.strip())
                    users.append(user)
            updated = False
            target_user = None
            for user in users:
                if str(user["用户名"]) == self.username:
                    if "游戏次数" not in user:
                        user["游戏次数"] = 0
                    user["游戏次数"] += 1
                    updated = True
                    target_user = user
                    break
            with open(file_path, "w", encoding="utf-8") as file:
                for user in users:
                    file.write(json.dumps(user, ensure_ascii=False) + "\n")
            if updated and target_user:
                showinfo("提示", f"游戏次数已更新！您已玩了 {target_user['游戏次数']} 次游戏")
            else:
                showinfo("错误", "未找到用户信息")
        except Exception as e:
            showinfo("错误", f"更新游戏次数失败：{str(e)}")
    
    def return_login(self):
        # 返回登录界面，因为或许别人也想玩
        self.root.destroy()
        root.deiconify()
    
    def exit_game(self):
        self.root.destroy()
        root.destroy()

if __name__ == '__main__':
    root = Tk()
    Denglu(root)
    root.mainloop()