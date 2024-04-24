#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
from Crypto.Cipher import AES

# 创建 socket 对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名和端口
host = '127.0.0.1'
port = 12345

# 绑定端口
server_socket.bind((host, port))

# 设置最大连接数，超过后排队
server_socket.listen(5)

while True:
    # 建立客户端连接
    client_socket, addr = server_socket.accept()
    print('连接地址：', addr)

    # 接收加密后的文件数据和nonce
    ciphertext = client_socket.recv(1024)
    tag = client_socket.recv(16)
    nonce = client_socket.recv(16)

    key = b'Sixteen byte key'  # 16字节的密钥

    # 使用密钥解密文件数据
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    decrypted_data = cipher.decrypt_and_verify(ciphertext, tag)

    # 将解密后的数据保存为文件
    with open('received.txt', 'wb') as file:
        file.write(decrypted_data)

    print('文件接收并解密完成！')
    client_socket.close()


# In[ ]:





# In[ ]:




