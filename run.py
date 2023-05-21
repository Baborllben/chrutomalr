from tkinter import *
import tkinter.font
import os
import socket
import tkinter
import time
import configparser
import threading
theSYSTEM = os.name


# 系统为Windows
if theSYSTEM == 'nt':
    # 主线程：控制台线程
    class theGUI:
        def __init__(self):
            global window
            self.root = tkinter.Tk()
            window = self.root
            global basic
            basic = tkinter.font.Font(family='Raster Fonts',size=12)
            global Consolas
            Consolas = tkinter.font.Font(family='Consolas',size=12)

            global isBREAK
            isBREAK = False
        def run(self):
            # 标题
            window.title("Chrutomalr Snapshot")
            window.resizable(False, False)
            window.geometry("960x480")
            current_dir = os.path.abspath(os.path.dirname(__file__))
            icoPath = current_dir+'\\core\\taskbar.png'
            window.iconphoto(True, tkinter.PhotoImage(file=icoPath))
            # 内背景
            window.configure(bg="#0C0C0C")
            # 框框
            global text
            global textDel
            text = Text(self.root,state=NORMAL,fg='#FFFFFF',bg="#0C0C0C",font=basic,borderwidth=0)
            textDel = text.delete(1.0, tkinter.END)
            # 信息输入
            global commandConsole
            commandConsole = Entry(self.root,fg='gray',bg="#0C0C0C",font=Consolas,borderwidth=1,insertbackground='#FFFFFF')
            commandConsole.insert(0, "Please Input Commands In This Console >>>")

            ##### 显示框框的地方
            # commandConsole.place(x=0,y=450,width=960,height=30)
            ##### 显示框框的地方

            # 三个终端事件
            # 当Entry被选中的时候
            commandConsole.bind("<FocusIn>", on_click)
            # 当Entry非选中的时候
            commandConsole.bind("<FocusOut>", on_leave)
            text.place(width=960, height=460)
            addInfo('Loadding Files...','DEBUG')
            window.after(10, COPYRIGHT)
            self.root.mainloop()
            pass
        pass



    def addInfo(theInfo, type):
        text.config(state='normal')
        # 获取时间（输出前面加上的东西）
        dateAndTime = time.localtime()
        # 时
        if dateAndTime.tm_hour < 10:
            houR = '0'+str(dateAndTime.tm_hour)
            pass
        else:
            houR = str(dateAndTime.tm_hour)
            pass
        # 分
        if dateAndTime.tm_min < 10:
            minutE = '0'+str(dateAndTime.tm_min)
            pass
        else:
            minutE = str(dateAndTime.tm_min)
            pass
        # 秒
        if dateAndTime.tm_sec < 10:
            seconD = '0'+str(dateAndTime.tm_sec)
            pass
        else:
            seconD = str(dateAndTime.tm_sec)
            pass
        timE = '['+houR+':'+minutE+':'+seconD

        if type == 'INFO':
            text.tag_configure('color1', foreground='#FFFFFF')
            text.insert(END, timE+' INFO] '+theInfo+'\n', 'color1')
            pass
        elif type == 'WARN':
            text.tag_configure('color2', foreground='#FFA500')
            text.insert(END, timE+' WARN] '+theInfo+'\n', 'color2')
            pass
        elif type == 'ERROR':
            text.tag_configure('color3', foreground='#FF0000')
            text.insert(END, timE+' ERROR] '+theInfo+'\n', 'color3')
            pass
        elif type == 'DEBUG':
            text.tag_configure('color4', foreground='#00CCCC')
            text.insert(END, timE+' DEBUG] '+theInfo+'\n', 'color4')
            pass
        elif type == 'REMOTE':
            text.tag_configure('color5', foreground='#8E62CC')
            text.insert(END, timE+' REMOTE] '+theInfo+'\n', 'color5')
            pass
        elif type == 'HELP':
            text.tag_configure('color6', foreground='#6A9955')
            text.insert(END, timE+' HELP] '+theInfo+'\n', 'color6')
            pass
        text.config(state='disabled')
        # text.see('end')
        # window.after(1000, addInfo,'Chrutomalr 23w19a Snapshot!!!!!','ERROR')
        # PING()
        pass

    # 添加回调函数以将插入光标移动到0号位置
    def on_click(event):
        if commandConsole.get() == "Please Input Commands In This Console >>>":
            commandConsole.delete(0, "end")
            commandConsole.config(fg="#FFFFFF")

    # 添加回调函数以在无输入时重新添加提示文本
    def on_leave(event):
        if not commandConsole.get():
            commandConsole.insert(0, 'Please Input Commands In This Console >>>')
            commandConsole.config(fg="gray")


    ##### 启动1，开始
    def COPYRIGHT(): 
        window.update()
        time.sleep(1)
        addInfo('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■','INFO')
        window.update()
        time.sleep(0.01)
        window.update()
        addInfo('□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□','INFO')
        window.update()
        time.sleep(0.01)
        window.update()
        addInfo('■■■■■□■■■■■□■■■■■□□■■■□□■■■■■□■□□□□□■□□□■','INFO')
        window.update()
        time.sleep(0.01)
        window.update()
        addInfo('■□□□□□■□□□■□□□■□□□■□□□■□□□■□□□■□□□□□■□□□■','INFO')
        window.update()
        time.sleep(0.01)
        window.update()
        addInfo('■□□□□□■□□□■□□□■□□□■□□□■□□□■□□□■□□□□□□■□■□','INFO')
        window.update()
        time.sleep(0.01)
        window.update()
        addInfo('■■■■□□■□□□■□□□■□□□■■■■■□□□■□□□■□□□□□□□■□□','INFO')
        window.update()
        time.sleep(0.01)
        window.update()
        addInfo('■□□□□□■□□□■□□□■□□□■□□□■□□□■□□□■□□□□□□■□■□','INFO')
        window.update()
        time.sleep(0.01)
        window.update()
        addInfo('■□□□□□■□□□■□□□■□□□■□□□■□□□■□□□■□□□□□■□□□■','INFO')
        window.update()
        time.sleep(0.01)
        window.update()
        addInfo('■□□□□□■■■■■□□□■□□□■□□□■□■■■■■□■■■■■□■□□□■','INFO')
        window.update()
        time.sleep(0.01)
        window.update()
        addInfo('□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□','INFO')
        window.update()
        time.sleep(0.01)
        window.update()
        addInfo('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■','INFO')
        time.sleep(0.01)
        window.update()
        addInfo('- Version 23w19a Snapshot','INFO')
        window.update()
        addInfo('Authlib-injector: 1.2.2 by yushijinhun','INFO')
        window.update()
        addInfo('Proxy (Velocity): 3.1.2 SNAPSHOT-184 by PaperMC','INFO')
        window.update()
        CONFIG()
        window.update()
        pass

    ##### 启动2，检测文件完整性
    # 1. 配置文件读取函数
    def CONFIG():
        # 1.1 配置文件存在与否
        current_dir = os.path.abspath(os.path.dirname(__file__))
        configINIPath = current_dir+'\\config.ini'
        if os.path.exists(configINIPath):
            # ZHENZHENJIAJIAJIAZHENZHENZHEN 为 True，往下执行
            global ZHENZHENJIAJIAJIAZHENZHENZHEN
            ZHENZHENJIAJIAJIAZHENZHENZHEN = True
            pass
        else:
            ZHENZHENJIAJIAJIAZHENZHENZHEN = False
            # ZHENZHENJIAJIAJIAZHENZHENZHEN 为 False，结束执行
            pass
        pass
        # 1.2 配置文件读取基本参数
        if ZHENZHENJIAJIAJIAZHENZHENZHEN == True:
            config = configparser.ConfigParser()
            config.read(configINIPath)
            global runPort
            runPort = config.get('corefig', 'runPort')
            window.after(10, addInfo,'Socket well openning on ['+runPort+'].','INFO')
            ##### 启动Socket线程
            thread1 = threading.Thread(target=threadSocketServer)
            thread1.start()
            pass
        else:
            window.after(10, addInfo,'Sorry, config.ini is an improtant file. Where is it now?','ERROR')
            ZHENZHENJIAJIAJIAZHENZHENZHEN = False
            # ZHENZHENJIAJIAJIAZHENZHENZHEN 为 False，结束执行
            pass
        pass


    # 线程：Socket Server
    def threadSocketServer():
        # 2.1 检测端口占用情况
        def PORTSOCCUPANCY(port, host='127.0.0.1'):
            PortOccupancyQuery = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                PortOccupancyQuery.connect((host, int(port)))
                PortOccupancyQuery.settimeout(1)
                PortOccupancyQuery.shutdown(2)
                return True
            except:
                return False
            pass
        # 2.2 检测客户端服务端端口占用情况(实际操作)
        if PORTSOCCUPANCY(runPort) == False:
            window.after(10, addInfo,'Ports are free.','INFO')
            ZHENZHENJIAJIAJIAZHENZHENZHEN = True
            pass
        else:
            window.after(10, addInfo,'Sorry, one or both of the two ports are already occupied by other programs, go to the config .ini modify the ports or close the program that occupies both ports.','ERROR')
            window.after(20, addInfo,'ON ['+runPort+']','ERROR')
            ZHENZHENJIAJIAJIAZHENZHENZHEN = False
            pass
        # 3. 开启 Socket Server 处理端
        if ZHENZHENJIAJIAJIAZHENZHENZHEN == True:

            #### 启动下一个线程
            thread2 = threading.Thread(target=threadCommandConsole)
            thread2.start()

            #### setPort线程
            threadSetPort = threading.Thread(target=threadSetPoer)
            threadSetPort.start()

            window.after(10, addInfo, 'Socket Server Open Succeed.', 'INFO')
            s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s1.bind(('127.0.0.1', int(runPort)))
            while True:
                s1.listen(128)
                sock, addr = s1.accept()
                print('Connect client: ', addr)
                info = sock.recv(1024).decode()
                print(info)
                fuckinfo = str(info).split('||')
                window.after(10, addInfo,fuckinfo[0],fuckinfo[1])
                pass
            pass
        else:
            window.after(30, addInfo,'我不知道这里还要写什么报错，这里有一个else不得不弄一个东西来填充这里（不然代码运行不了）。所以凑合着看吧','ERROR')
            pass
        pass


    # 线程：setPort
    def threadSetPoer():
        window.after(10, addInfo,'Syslog Open:','DEBUG')
        def DIRGET(directory):
            returnList = []
            # 获取指定目录下的所有项目
            with os.scandir(directory) as entries:
                for entry in entries:
                    # 判断当前项目是否为文件或目录
                    if entry.is_file():
                        returnList.append(str(directory) + '\\' + str(entry.name))
                        pass
                    elif entry.is_dir():
                        returnList.append(str(directory) + '\\' + str(entry.name) + '|||')
                        pass
                    pass
                print('dirget ok')
                return returnList
                pass
            pass
        # 开始循环扫描目录
        current_dir = os.path.abspath(os.path.dirname(__file__))
        useDir = current_dir+'\\core'
        global directoryList
        directoryList = DIRGET(useDir)
        # 定义最终输出的 fileListr
        global fileListr
        fileListr = []
        # 获取目录下的子目录及文件
        whileRange = len(directoryList)
        while whileRange >= 0:
            time.sleep(0.01)
            ## 定义列表行数 = 循环次数 - 1
            directoryListLine = whileRange - 1
            ## 多次循环与终止循环：
            if directoryList != []:
                if directoryListLine <= -1:
                    whileRange = len(directoryList)
                    directoryListLine = whileRange - 1
                    pass
                pass
            else:
                print(fileListr)
                break
                pass
            ## 检测是否为目录：
            if '|||' in str(directoryList[directoryListLine]):
                sonDirectory = DIRGET(str(directoryList[directoryListLine]).replace('|||',''))
                ### 模块目录处理方案：
                if 'module' in str(directoryList[directoryListLine]).lower():
                    window.after(10, addInfo,'Module Directory: ' + str(directoryList[directoryListLine]).replace('|||',''),'INFO')
                    print('a Module Directory')
                    del directoryList[directoryListLine]
                    pass
                ### 空目录处理方案：
                elif sonDirectory == []:
                    window.after(10, addInfo,'Null Directory: ' + str(directoryList[directoryListLine]).replace('|||',''),'INFO')
                    print('a Null Directory')
                    del directoryList[directoryListLine]
                    pass
                ### 好目录处理方案：
                elif sonDirectory != []:
                    window.after(10, addInfo,'Directory: ' + str(directoryList[directoryListLine]).replace('|||',''),'INFO')
                    for i in range(len(sonDirectory)):
                        directoryList.append(sonDirectory[i-1])
                        whileRange = whileRange + 1
                        pass
                    del directoryList[directoryListLine]
                    print('a Nice Directory')
                    pass
                pass
            ## 检测结果为文件：
            else:
                window.after(10, addInfo,'File: ' + str(directoryList[directoryListLine]).replace('|||',''),'INFO')
                fileListr.append(directoryList[directoryListLine])
                print('a File ' + directoryList[directoryListLine])
                del directoryList[directoryListLine]
                pass
            whileRange = whileRange - 1
            pass
        pass


    # 线程：Command Console
    def threadCommandConsole():
        # 显示命令栏
        commandConsole.place(x=0,y=450,width=960,height=30)
        # Console控制台与终端
        # 内置console控制父命令
        # 将Entry中的内容转移至变量
        def on_submit(event):
            input_str = commandConsole.get()
            print("Submit:", input_str)
            runCommandConsole(input_str)
            # 删除终端输入栏的数据
            commandConsole.delete(0, "end")
            # You >>>
            window.after(1, addInfo,'You >>> ' + input_str,'DEBUG')
            pass

        # 当用户在Entry中按下回车（Enter）的时候
        commandConsole.bind("<Return>", on_submit)

        # 指令库部分：（runCommandConsole）
        def runCommandConsole(command):
            # 输入信息处理：
            # 将指令库从输入信息分离出来（split在遇到没有包含目标字符的字符串时，会把字符串原封不动的封装进一个列表中）
            commandModule = str(command).split('.',1)
            # 判断命令库的名字是不是混进了稀奇古怪的字符（非ACSll）
            if all(ord(c) < 128 for c in commandModule[0]) == True:
                ## 如果没有混进：
                ## 将成功通过的字符串全部变为小写
                commandModuleString = str(commandModule[0]).lower()
                ## 检测是不是原有支持的命令库
                if commandModuleString == 'console':
                    ### 执行命令库子级命令：
                    ### 检测是不是只输入了 Console：
                    if '.' in command:
                        #### 如果不是直接输入了一个 Console：
                        commandFunctionString = str(commandModule[1].split('[')[0]).lower()
                        if commandFunctionString == 'help':
                            ##### 指令： Console.help
                            def RETURN1():
                                window.after(10, addInfo,'This is the information contained in the Console Command Module: ','HELP')
                                window.after(20, addInfo,'Console in Chrutomalr 3.1 ','HELP')
                                window.after(30, addInfo,'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━','HELP')
                                window.after(40, addInfo,'- Console.help','HELP')
                                window.after(50, addInfo,'  Query Help/Open Help List','HELP')
                                window.after(60, addInfo,'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━','HELP')
                                window.after(70, addInfo,'- Console.log[\'filename\']','HELP')
                                window.after(80, addInfo,'  filename | String :','HELP')
                                window.after(90, addInfo,'  The name of the file to save (including the file extension needs to be entered yourself, if you do no                      tenter it, it is not by default)','HELP')
                                window.after(100, addInfo,'  Release logs already saved in Syslogs early','HELP')
                                window.after(110, addInfo,'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━','HELP')
                                window.after(120, addInfo,'- Console.install[\'libURL\',\'cmname\']','HELP')
                                window.after(130, addInfo,'  libURL | String : The download source for the Command Module (HTTP or HTTPS)','HELP')
                                window.after(140, addInfo,'  cmname | String : The name of the Command Module','HELP')
                                window.after(150, addInfo,'  This command will download the library from the specified download source','HELP')
                                window.after(160, addInfo,'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━','HELP')
                                window.after(170, addInfo,'- Console.delete[\'cmname\']','HELP')
                                window.after(180, addInfo,'  cmname | String : The name of the Command Module','HELP')
                                window.after(190, addInfo,'  Delete existing Command Module (irreversible!) ','HELP')
                                window.after(200, addInfo,'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━','HELP')
                                window.after(210, addInfo,'- Console.clear','HELP')
                                window.after(220, addInfo,'  Clear the screen','HELP')
                                window.after(230, addInfo,'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━','HELP')
                                window.after(240, addInfo,'- Console.lock','HELP')
                                window.after(250, addInfo,'  Locks the number of visible rows to the position of the output','HELP')
                                window.after(260, addInfo,'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━','HELP')
                                window.after(270, addInfo,'- Console.unlock','HELP')
                                window.after(280, addInfo,'  Liberalize the number of visible rows','HELP')
                                window.after(290, addInfo,'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━','HELP')
                                window.after(300, addInfo,'- Console.list','HELP')
                                window.after(310, addInfo,'  Lists all installed Command Module','HELP')
                                window.after(320, addInfo,'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━','HELP')
                                window.after(330, addInfo,'- Console.close','HELP')
                                window.after(340, addInfo,'  Close the Console input box','HELP')
                                window.after(350, addInfo,'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━','HELP')
                                window.after(360, addInfo,'- Console.hung','HELP')
                                window.after(370, addInfo,'  Suspend Chrutomalr (abbreviates Chrutomalr\'s window, but does not exit)','HELP')
                                window.after(380, addInfo,'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━','HELP')
                                window.after(390, addInfo,'- Console.stop & end','HELP')
                                window.after(400, addInfo,'  Close Chrutomalr and all modules','HELP')
                                pass
                            RETURN1()
                            pass
                        elif commandFunctionString == 'log':
                            ##### 指令：Console.log
                            def RETURN2(filename=str(time.time())+'.log'):
                                allText = text.get('1.0', 'end')
                                ###### 检测输入的文件名称是否合法以及是否被占用
                                current_dir = os.path.abspath(os.path.dirname(__file__))
                                logPath = current_dir+'\\syslogs\\' + filename
                                if os.path.exists(logPath):
                                    ####### 如果文件被占用则进行这一步
                                    window.after(10, addInfo,'The file name you entered is occupied by another file! Unable to create new log','WARN')
                                    pass
                                else:
                                    ####### 如果文件未被占用则进行这一步
                                    ####### 这一步检查文件名称是否合法：
                                    ####### 1. <
                                    if '<' in filename:
                                        window.after(10, addInfo,'The file name is invalid! Unable to create new log','WARN')
                                        pass
                                    ####### 2. >
                                    elif '>' in filename:
                                        window.after(10, addInfo,'The file name is invalid! Unable to create new log','WARN')
                                        pass
                                    ####### 3. :
                                    elif ':' in filename:
                                        window.after(10, addInfo,'The file name is invalid! Unable to create new log','WARN')
                                        pass
                                    ####### 4. "
                                    elif '"' in filename:
                                        window.after(10, addInfo,'The file name is invalid! Unable to create new log','WARN')
                                        pass
                                    ####### 5. /
                                    elif '/' in filename:
                                        window.after(10, addInfo,'The file name is invalid! Unable to create new log','WARN')
                                        pass
                                    ####### 6. \
                                    elif '\\' in filename:
                                        window.after(10, addInfo,'The file name is invalid! Unable to create new log','WARN')
                                        pass
                                    ####### 7. |
                                    elif '|' in filename:
                                        window.after(10, addInfo,'The file name is invalid! Unable to create new log','WARN')
                                        pass
                                    ####### 8. ?
                                    elif '?' in filename:
                                        window.after(10, addInfo,'The file name is invalid! Unable to create new log','WARN')
                                        pass
                                    ####### 9. *
                                    elif '*' in filename:
                                        window.after(10, addInfo,'The file name is invalid! Unable to create new log','WARN')
                                        pass
                                    else:
                                        ######## 文件合法性通过：
                                        ######## 创建并写入文件内容：
                                        with open(logPath, 'w', encoding='utf-8') as f:
                                            f.write(allText)
                                            window.after(10, addInfo,'The log file was written successfully: ' + filename,'INFO')
                                        pass
                                    pass
                                pass
                            ###### 查玩家输入的参数
                            if len(commandModule[1].split('[')) == 1:
                                ####### 如果玩家只输入了一个log
                                RETURN2()
                                pass
                            elif len(commandModule[1].split('[')) == 2:
                                ####### 如果玩家输入了log[xxx]
                                if commandModule[1].split('[')[1] == '':
                                    ######## 如果用户输入的是一个空字符串：Console.log[
                                    RETURN2()
                                    pass
                                elif commandModule[1].split('[')[1] == "'']":
                                    ######## Console.log['']
                                    RETURN2()
                                    pass
                                elif commandModule[1].split('[')[1] == ']':
                                    ######## Console.log[]
                                    RETURN2()
                                    pass
                                else:
                                    ######## 玩家输入了正常的东西：Console['xxx']
                                    if '"' in commandModule[1].split('[')[1]:
                                        window.after(10, addInfo,'The file name is invalid! Unable to create new log','WARN')
                                        pass
                                    else:
                                        filename = commandModule[1].split('[')[1].split("'")[1]
                                        RETURN2(filename)
                                        pass
                                    pass
                                pass
                            pass
                        elif commandFunctionString == 'install':
                            ##### 指令：Console.install['libURL','cmname']
                            window.after(10, addInfo,'Version incompatible!','ERROR')
                            pass
                        elif commandFunctionString == 'delete':
                            ##### 指令：Console.delete['cmname']
                            window.after(10, addInfo,'Version incompatible!','ERROR')
                            pass
                        elif commandFunctionString == 'clear':
                            ##### 指令：Console.clear
                            text.config(state='normal')
                            window.after(10, addInfo, 'Last(5)', 'INFO')
                            window.after(1010, addInfo, 'Last(4)', 'INFO')
                            window.after(2010, addInfo, 'Last(3)', 'INFO')
                            window.after(3010, addInfo, 'Last(2)', 'INFO')
                            window.after(4010, addInfo, 'Last(1)', 'INFO')
                            window.after(5010, addInfo, 'Please wait...', 'INFO')
                            window.after(5010, lambda: text.config(state='normal'))
                            window.after(5210, text.delete, 1.0, tkinter.END)
                            window.after(5410, lambda: text.config(state='disabled'))
                            text.config(state='disabled')
                            print(1)
                            pass
                        elif commandFunctionString == 'lock':
                            window.after(10, addInfo,'The last line of visible locks has been locked and Console.unlock is restored','INFO')
                            global isBREAK
                            isBREAK = False
                            pass
                        elif commandFunctionString == 'unlock':
                            window.after(10, addInfo,'The last line of visible locks has been unlocked and Console.lock is restored','INFO')
                            isBREAK = True
                            pass
                        elif commandFunctionString == 'list':
                            filelist = []
                            directoryList = []
                            #### 获取目录下的所有子目录
                            def RETURN6(directory):
                                for file in os.listdir(directory):
                                    if os.path.isdir(os.path.join(directory, file)):
                                        filelist.append(str(file))
                                        pass
                                    pass
                                ##### 输出是一个完整的子目录
                                return filelist
                                pass
                            #### 获取子目录下是否存在库判定文件
                            def RETURN6_1(filelist):
                                filelistLine = len(filelist)
                                for i in range(filelistLine):
                                    current_dir = os.path.abspath(os.path.dirname(__file__))
                                    bzdPath = current_dir+'\\console\\' + filelist[i-1] + '\\_FODEX.py'
                                    if os.path.exists(bzdPath):
                                        directoryList.append(filelist[i-1])
                                        pass
                                    pass
                                return directoryList
                                pass
                            #### 开始运算：
                            directory = os.path.abspath(os.path.dirname(__file__)) + '\\console'
                            filelist_ = RETURN6(directory)
                            if filelist_ == []:
                                window.after(10, addInfo,'You do not have any libraries. Where did I give you the preset go?','ERROR')
                                pass
                            else:
                                directoryList_ = RETURN6_1(filelist_)
                                finishNum = len(directoryList_)
                                #### 测试用的
                                print(filelist_)
                                print(directoryList_)
                                if directoryList_ == []:
                                    window.after(10, addInfo,'You do not have any libraries. Where did I give you the preset go?','ERROR')
                                    pass
                                else:
                                    window.after(10, addInfo,'You have Command Modules:','INFO')
                                    for i in range(finishNum):
                                        window.after(20, addInfo,'- ' + directoryList_[i-1],'INFO')
                                        pass
                                    window.after(30, addInfo,'Finish List.','INFO')
                                    pass
                                pass
                            pass
                        elif commandFunctionString == 'close':
                            #### Console.close
                            commandConsole.pack_forget()
                            window.after(10, addInfo,'You successfully hid the input box. The bad thing is that you have to restart the program to make                         it appear again!','ERROR')
                            window.after(20, addInfo,'看样子好像 Close 不掉，算你赢了。','INFO')
                            pass
                        elif commandFunctionString == 'hung':
                            #### Console.hung
                            window.after(10, addInfo,'Version incompatible!','ERROR')
                            pass
                        elif commandFunctionString == 'stop':
                            #### Console.stop
                            ######################################################################################################################以后再写
                            pass
                        pass
                    else:
                        #### 如果是直接输入了一个 Console：
                        window.after(10, addInfo,'This is the information contained in the Console Command Module: ','HELP')
                        window.after(20, addInfo,'Console in Chrutomalr 3.1 ','HELP')
                        window.after(30, addInfo,'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━','HELP')
                        window.after(40, addInfo,'- Console.help','HELP')
                        window.after(50, addInfo,'  Query Help/Open Help List','HELP')
                        window.after(60, addInfo,'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━','HELP')
                        window.after(70, addInfo,'- Console.log[\'filename\']','HELP')
                        window.after(80, addInfo,'  filename | String :','HELP')
                        window.after(90, addInfo,'  The name of the file to save (including the file extension needs to be entered yourself, if you do no                      tenter it, it is not by default)','HELP')
                        window.after(100, addInfo,'  Release logs already saved in Syslogs early','HELP')
                        window.after(110, addInfo,'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━','HELP')
                        window.after(120, addInfo,'- Console.install[\'libURL\',\'cmname\']','HELP')
                        window.after(130, addInfo,'  libURL | String : The download source for the Command Module (HTTP or HTTPS)','HELP')
                        window.after(140, addInfo,'  cmname | String : The name of the Command Module','HELP')
                        window.after(150, addInfo,'  This command will download the library from the specified download source','HELP')
                        window.after(160, addInfo,'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━','HELP')
                        window.after(170, addInfo,'- Console.delete[\'cmname\']','HELP')
                        window.after(180, addInfo,'  cmname | String : The name of the Command Module','HELP')
                        window.after(190, addInfo,'  Delete existing Command Module (irreversible!) ','HELP')
                        window.after(200, addInfo,'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━','HELP')
                        window.after(210, addInfo,'- Console.clear','HELP')
                        window.after(220, addInfo,'  Clear the screen','HELP')
                        window.after(230, addInfo,'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━','HELP')
                        window.after(240, addInfo,'- Console.lock','HELP')
                        window.after(250, addInfo,'  Locks the number of visible rows to the position of the output','HELP')
                        window.after(260, addInfo,'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━','HELP')
                        window.after(270, addInfo,'- Console.unlock','HELP')
                        window.after(280, addInfo,'  Liberalize the number of visible rows','HELP')
                        window.after(290, addInfo,'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━','HELP')
                        window.after(300, addInfo,'- Console.list','HELP')
                        window.after(310, addInfo,'  Lists all installed Command Module','HELP')
                        window.after(320, addInfo,'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━','HELP')
                        window.after(330, addInfo,'- Console.close','HELP')
                        window.after(340, addInfo,'  Close the Console input box','HELP')
                        window.after(350, addInfo,'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━','HELP')
                        window.after(360, addInfo,'- Console.hung','HELP')
                        window.after(370, addInfo,'  Suspend Chrutomalr (abbreviates Chrutomalr\'s window, but does not exit)','HELP')
                        window.after(380, addInfo,'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━','HELP')
                        window.after(390, addInfo,'- Console.stop & end','HELP')
                        window.after(400, addInfo,'  Close Chrutomalr and all modules','HELP')
                        pass
                    pass
                else:
                    ### 尝试向Console请教（Socket的POST）
                    pass
                pass
            else:
                ## 如果混进了：
                window.after(10, addInfo,'The command you entered mixed in unsupported characters (non-ASCll)','WARN')
                pass
            pass


    if __name__ == '__main__':
        # Console.lock/unlock
        def threadLOCK():
            time.sleep(2.5)
            def LOCK():
                while True:
                    time.sleep(0.01)
                    text.see('end-1c')
                    if isBREAK == True:
                        RESTARTLOCK()
                        break
                pass
            def RESTARTLOCK():
                while True:
                    time.sleep(0.01)
                    if isBREAK == False:
                        LOCK()
                        break
                    pass
                pass
            while True:
                LOCK()
        threadLOCKr = threading.Thread(target=threadLOCK)
        threadLOCKr.start()
        # 启动GUI
        theGUI().run()
        pass
    pass
pass