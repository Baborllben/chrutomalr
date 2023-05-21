import os
import time
import socket
import threading

theSYSTEM = os.name

# 系统为Windows
if theSYSTEM == 'nt':
    # 线程2：Socket Client
    def thread_2():
        while True:
            time.sleep(0.2)
            # 3. 开启 Socket Client 请求端
            global s2
            s2 = socket.socket()
            s2.connect(('127.0.0.1', int(20132)))
            s2.settimeout(3)
            sendinfo = 'WEYTUHEGRHWOIJHGIWHOGHOHGOROGHUIEGUIGU||DEBUG||'
            s2.send(sendinfo.encode())
            s2.close
            pass
        pass
    pass

    # 开启多个线程运行不同的操作
    if __name__ == '__main__':
        p1 = threading.Thread(target=thread_2)
        p1.start()