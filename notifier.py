# notifier.py —— 通知模块
# 这个文件只负责一件事：发出提醒（声音 + 弹窗）。
# 其他模块不关心"怎么提醒"，只需要调用 notify() 就行。

import winsound       # Python 内置：Windows 蜂鸣声
import tkinter        # Python 内置：图形界面库
from tkinter import messagebox

def notify(title, message):
    """
    播放提示音，并弹出一个警告窗口。
    用户点击"确定"后，窗口关闭，程序继续运行。
    """
    # 播放蜂鸣声：频率 1000Hz，持续 800 毫秒
    winsound.Beep(1000, 800)

    # 创建一个隐藏的主窗口（tkinter 必须有主窗口才能弹对话框）
    root = tkinter.Tk()
    root.withdraw()              # 隐藏主窗口，只显示对话框
    root.attributes("-topmost", True)  # 让窗口出现在最前面

    # 弹出警告对话框
    messagebox.showwarning(title, message)

    # 对话框关闭后，销毁主窗口，释放资源
    root.destroy()
