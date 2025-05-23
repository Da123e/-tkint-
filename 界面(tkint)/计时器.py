from tkinter import *
class TimerApp:
    def __init__(self,rot):
        self.root=rot
        self.root.title("计时器")
        self.time=0
        self.running=False
        self.t=0
    # 创建标签
        self.label=Label(self.root,text="00:00:00",font=("Arial",40))
        self.label.place(relx=0.25,rely=0.35)

    # 创建"开始"按钮
        self.start_button=Button(self.root,text="开始",command=self.start)
        self.start_button.place(relx=0.25,rely=0.55)

    # 创建"暂停"按钮
        self.pause_button=Button(self.root,text="暂停",command=self.pause)
        self.pause_button.place(relx=0.4,rely=0.55)

    # 创建"重置"按钮
        self.reset_button=Button(self.root,text="重置",command=self.reset)
        self.reset_button.place(relx=0.54,rely=0.55)

    # 创建"停止"按钮
        self.stop_button=Button(self.root,text="退出",command=self.stop)
        self.stop_button.place(relx=0.68,rely=0.55)

    def start(self):
        self.t += 1
        if not self.running:
            self.time += 1
            minutes, seconds = divmod(self.time, 60)
            hours, minutes = divmod(minutes, 60)
            self.label.config(text='{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds))
            self.root.after(1000,self.start)  # 每秒更新一次标签
        if self.t !=0:
            self.running=False

    def pause(self):
        self.running=True

    def reset(self):
        self.running=True
        self.time=0
        self.label.config(text="00:00:00")

    @staticmethod
    def stop():
        quit()
if __name__ == '__main__':
    root = Tk()
    root.resizable(True, True)  # 设置窗口可调大小
    root.geometry("400x350+500+200")  # 设置窗口大小和位置

    TimerApp(root)
    root.mainloop()