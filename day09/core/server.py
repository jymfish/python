import socket
from socket import SOL_SOCKET,SO_REUSEADDR
import subprocess
import struct
import json
import hashlib


ftp_server = socket.socket()
ftp_server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
ftp_server.bind(("127.0.0.1",8090))
ftp_server.listen(5)


def authentication():
    conn, addr = ftp_server.accept()
    user_md5 = conn.recv(1024).decode('utf8')
    passwd_md5 = conn.recv(1024).decode('utf8')
    with open(r"userfile",mode="r") as f:
        for line in f:
            user,passwd = line.split("|")
            server_user_md5 = hashlib.md5()
            server_user_md5.update(user.encode("gbk"))
            server_user_md5_value = server_user_md5.hexdigest()

            server_passwd_md5 = hashlib.md5()
            server_passwd_md5.update(passwd.encode("gbk"))
            server_passwd_md5_value = server_passwd_md5.hexdigest()
            if user_md5 == server_user_md5_value and  passwd_md5 == server_passwd_md5_value:
                conn.send(b"login success")
            else:
                conn.send(b"login false")
    conn.close()


def put_file():
 #   conn, addr = ftp_server.accept()
    header_length = conn.recv(4)
    header_info_len = struct.unpack("i",header_length)[0]
    header_json = conn.recv(header_info_len)
    header_info = json.loads(header_json)
    action = header_info.get("action")
    filename = header_info.get("filename")
    filesize = header_info.get("filesize")

    with open("test"+"/" + filename,mode="wb") as f:
        has_rev = 0
        while filesize > has_rev:
            img = conn.recv(1024)
            f.write(img)
            has_rev += len(img)
    conn.close()



# while 1:
#     conn, addr = ftp_server.accept()
#     while 1:
#         put_file()

conn, addr = ftp_server.accept()
put_file()





