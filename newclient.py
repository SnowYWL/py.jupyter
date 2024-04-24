#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import filedialog
import socket
from Crypto.Cipher import AES
import time  # 导入time模块

# 创建 socket 对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务，指定主机和端口
host = '127.0.0.1'
port = 12345
client_socket.connect((host, port))

# 加密函数，使用AES加密文件内容
def encrypt_file(file_path, key):
    cipher = AES.new(key, AES.MODE_EAX)
    with open(file_path, 'rb') as file:
        data = file.read()
        ciphertext, tag = cipher.encrypt_and_digest(data)
    return ciphertext, tag, cipher.nonce

# 选择文件并触发加密传输操作
def choose_file_and_send():
    file_path = filedialog.askopenfilename()  # 弹出文件选择对话框
    key = b'Sixteen byte key'  # 16字节的密钥
    ciphertext, tag, nonce = encrypt_file(file_path, key)

    start_time = time.perf_counter()  # 开始传输的时间
    client_socket.send(ciphertext)
    client_socket.send(tag)
    client_socket.send(nonce)
    end_time = time.perf_counter()  # 结束传输的时间

    print(f"传输耗时：{end_time - start_time}秒")
    client_socket.close()

# 创建GUI应用程序窗口
root = tk.Tk()
root.title("加密文件传输")

# 添加按钮用于选择文件并触发加密传输操作
select_button = tk.Button(root, text="选择文件并传输", command=choose_file_and_send)
select_button.pack(pady=20)

# 运行应用程序
root.mainloop()


# In[ ]:




