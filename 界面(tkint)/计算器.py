from tkinter import *
class Jsq:
    def __init__(self, rot):
        self.current_expression =''
        self.root = rot

        # 菜单
        menu = Menu(self.root)
        fmenu = Menu(menu)
        fmenu.add_command(label="退出", command=self.quit)
        menu.add_cascade(label="菜单", menu=fmenu)
        self.root['menu']=menu#添加菜单

        # 输入框
        self.enter = Entry(self.root, width=20, font=('Arial', 14),justify=RIGHT)
        self.enter.grid(row=0, column=1, columnspan=3)

        # 回退按钮
        self.back_button = Button(self.root, text="回退", width=16, height=2, command=self.backspace)
        self.back_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # 清空按钮
        self.clear_button = Button(self.root, text="清空", width=16, height=2, command=self.clear)
        self.clear_button.grid(row=1, column=2, columnspan=2, padx=5, pady=5)

        # 数字和运算符按钮
        buttons = [
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),#  行，列
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3)
        ]

        for (text, row, col) in buttons:
            btn = Button(self.root, text=text, width=7, height=2, command=lambda t=text: self.button_click(t))
            btn.grid(row=row, column=col, padx=5, pady=5)

    def button_click(self, text):
        if text == '=':
            try:
                result = eval(self.current_expression)
                self.current_expression = str(result)
            except Exception:
                self.current_expression = '错误'
        else:
            self.current_expression += text#输入框显示
        self.enter.delete(0, END)#清空输入框
        self.enter.insert(0, self.current_expression)#输入框显示

    def backspace(self):
        self.current_expression = self.current_expression[:-1]
        self.enter.delete(0, END)
        self.enter.insert(0, self.current_expression)#输入框显示

    def clear(self):
        self.current_expression = ''#清空输入框
        self.enter.delete(0, END)#清空输入框

    def quit(self):
        self.root.quit()

if __name__=="__main__":
    root = Tk()
    root.title("计算器")

    Jsq(root)
    root.mainloop()