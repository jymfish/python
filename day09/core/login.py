import socket
import struct
import os,sys
import json
import hashlib

ftp_clinet = socket.socket()
ftp_clinet.connect(("127.0.0.1",8090)) #ip 和端口的绑定


def login():
    username = input("用户名：")
    passwd = input("密码：")
    user_md5 = hashlib.md5()
    user_md5.update(username.encode("gbk"))
    user_md5_value = user_md5.hexdigest()
    ftp_clinet.send(user_md5_value.encode("utf8"))


    passwd_md5 = hashlib.md5()
    passwd_md5.update(passwd.encode('gbk'))
    passwd_md5_value = passwd_md5.hexdigest()
    ftp_clinet.send(passwd_md5_value.encode("utf8"))
    print(ftp_clinet.recv(1024).decode("utf8"))
login()


# md5 = hashlib.md5()
# md5.update(b"aaaa")
# print(md5.hexdigest())
# md5.update(b"aaaa")
# print(md5.hexdigest())