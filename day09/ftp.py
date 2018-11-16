"""
练习题：
1、new方法和init方法执行的执行顺序
2、call方法在什么时候被调用
3、请用写一个类，用反射为这个类添加一个静态属性
4、请用反射为上题的类的对象添加一个属性name,值为你的名字
5、请使用new方法实现一个单例模式
6、校验两个文件的一致性
7、加盐的密文登陆
8、完成一个既可以向文件输出又可以向屏幕输出的日志设置

作业：
1. 多用户同时登陆
2. 用户登陆，加密认证
3. 上传/下载文件，保证文件一致性
4. 传输过程中现实进度条
5. 不同用户家目录不同，且只能访问自己的家目录
6. 对用户进行磁盘配额、不同用户配额可不同
7. 用户登陆server后，可在家目录权限下切换子目录
8. 查看当前目录下文件，新建文件夹
9. 删除文件和空文件夹
10. 充分使用面向对象知识
11. 支持断点续传
"""
import  hashlib
import pickle
import json
import sys,os
# class Person:
#     nationality = "China"
#     def __init__(self,name,sex):
#         self.name = name
#         self.sex = sex
#
#     def run(self):
#         print("i can run")
#
# obj = Person("lilei","man")
# ret = getattr(obj,"nationality")
#
# setattr(obj,"nationality","中国")
# setattr(obj,"name","honghong")
# ret = getattr(obj,"nationality")
# ret1 = getattr(obj,"name")
#
# print(ret,ret1)
# base_path = os.path.dirname(os.path.dirname(__file__))
# ret =sys.path.append(base_path)
# file_name = base_path + "/1111.rar"
# md5 = hashlib.md5()
# md5.update(b"file_name")
# print(file_name)
# print(md5.hexdigest())
# print(os.getcwd())
# print(os.path.split("F:\oldboy\day09"))
# print(os.path.dirname("F:\oldboy\day09"))
# print(__file__)


