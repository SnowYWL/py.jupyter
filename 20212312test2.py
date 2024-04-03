#!/usr/bin/env python
# coding: utf-8

# In[7]:


import tkinter as tk
import math

def calculate():
    try:
        user_input = entry.get()
        if user_input.startswith(('sin', 'cos', 'tan', 'ln')):
            calculate_advanced(user_input)
        else:
            result = eval(user_input)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_advanced(input):
    try:
        if input.startswith(('sin', 'cos', 'tan')):
            operation, value = input.split('(')
            value = value.replace(')', '')
            angle = math.radians(float(value))
            if operation == 'sin':
                result = math.sin(angle)
            elif operation == 'cos':
                result = math.cos(angle)
            elif operation == 'tan':
                result = math.tan(angle)
        elif input.startswith('ln'):
            value = float(input[2:].strip('(').rstrip(')'))
            result = math.log(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"{result:.3f}")
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def log_input():
    dialog = tk.Toplevel(root)
    dialog.title("对数运算")

    tk.Label(dialog, text="输入真数和底数，用英文逗号隔开 (e.g., 10,2):").pack()
    
    input_entry = tk.Entry(dialog)
    input_entry.pack(pady=5)
    
    def on_submit():
        try:
            value, base = map(float, input_entry.get().split(','))
            result = math.log(value, base)
            entry.delete(0, tk.END)
            entry.insert(tk.END, f"{result:.3f}")
        except ValueError:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
        dialog.destroy()

    submit_button = tk.Button(dialog, text="确定", command=on_submit)
    submit_button.pack(pady=5)

# 创建窗口
root = tk.Tk()
root.title("20212312计算器")

# 创建输入框
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

# 创建按钮
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('0', 4, 1),
    ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3),
    ('.', 4, 0), 
    ('=', 4, 2), ('C', 4, 4), ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2),
    ('ln', 5, 3), ('log', 5, 4)
]

for text, row, col in buttons:
    action = lambda x=text: command(x)
    if text == 'log':
        tk.Button(root, text=text, width=9, height=3, command=log_input).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, width=9, height=3, command=action).grid(row=row, column=col)


def command(x):
    if x == '=':
        calculate()
    elif x == 'C':
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, x + '(') if x in ['sin', 'cos', 'tan', 'ln', 'log'] else entry.insert(tk.END, x) if x not in ['=', 'C'] else entry.delete(0, tk.END) if x == 'C' else calculate()

# 运行主循环
root.mainloop()


# In[ ]:





# In[ ]:




