import py_compile
import os

# 获取 .py 文件所在目录
dirname = os.path.dirname(os.path.abspath(__file__))

filedir = './run.py'
finish = 'run.pyc'
# 将 example.py 文件压缩为 example.pyc 并放置在与 example.py 同级的目录下
py_compile.compile(filedir, cfile=os.path.join(dirname, finish))