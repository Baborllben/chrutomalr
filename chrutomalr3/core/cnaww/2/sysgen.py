import multiprocessing as mp
import time

def gen_msgs(pipe):
    msgs = ['msg1', 'msg2', 'msg3', 'msg4', 'msg5']
    for msg in msgs:
        pipe.send(msg)
        time.sleep(1)
    pipe.send('done')  # 通知接收进程数据传输完毕

if __name__ == '__main__':
    parent_pipe, child_pipe = mp.Pipe(duplex=True)  # 创建双向管道

    proc = mp.Process(target=gen_msgs, args=(child_pipe,))
    proc.start()

    # 关闭子进程的写入管道，避免死锁
    child_pipe.close()

    while True:
        try:
            msg = parent_pipe.recv()
            if msg == 'done':
                break
            print(f'Received message: {msg}')
        except EOFError:
            break  # 通常发生在所有的写入子进程的管道都被关闭之后

    proc.join()