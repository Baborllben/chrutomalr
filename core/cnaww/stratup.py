import platform
import os
windows = [""]
linux = [""]
if __name__ == '__main__':
    sys = platform.system()
    if sys == "Windows":
        operating_system = windows
        print("It's Windows")
    elif sys == "Linux":
        operating_system = linux
        print("It's Linux")
        pass
    else:
        pass
current_path = os.path.abspath(os.path.dirname(__file__))
os.system('python3 '+current_path+'\\email-0.py')
# 窗口不消失
os.system("pause")