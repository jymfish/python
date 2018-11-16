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



def put_file(action,filename):
    file_size = os.path.getsize(filename) #获取文件的大小字节数
    header_info = {"filename":filename,
                    "filesize":file_size,
                     "action":action
                   }
    header_info_json = json.dumps(header_info).encode("utf-8") #len只能计算字符的长度所以要用序列化
    header_length = struct.pack("i",len(header_info_json))
    ftp_clinet.send(header_length)
    ftp_clinet.send(header_info_json)

    with open(filename, mode="rb") as f:
        for line in f:
            ftp_clinet.send(line)
    ftp_clinet.close()

def get_file(action,filename):
    pass


while 1:
    # login()
    cmd = input("输文ftp命令:")
    if cmd == "":
        continue
    if cmd == "q":
        exit()
    action,filename=cmd.split(" ")
    if action == "put":
        put_file(action,filename)





