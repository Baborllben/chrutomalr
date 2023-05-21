import multiprocessing as mp
import time

def process_msgs(pipe):
    pipe.close()  # 关闭父进程的读取管道，避免死锁

    while True:
        try:
            msg = pipe.recv()
            print(f'Received message: {msg}')
            time.sleep(0.5)
        except EOFError:
            break  # 通常发生在所有的写入子进程的管道都被关闭之后

    pipe.send('done')  # 通知发送进程数据接收完毕
    pipe.close()  # 关闭发送进程的管道

if __name__ == '__main__':
    parent_pipe, child_pipe = mp.Pipe(duplex=True)

    proc = mp.Process(target=process_msgs, args=(parent_pipe,))
    proc.start()

    # 关闭父进程的写入管道，避免死锁
    parent_pipe.close()

    for i in range(5):
        child_pipe.send(f'msg{i}')
        time.sleep(1)

    child_pipe.close()  # 数据发送完毕，关闭管道

    while True:
        try:
            msg = parent_pipe.recv()
            if msg == 'done':
                break
        except EOFError:
            break  # 通常发生在所有的写入子进程的管道都被关闭之后

    proc.join()