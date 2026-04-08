' run.vbs —— 静默启动脚本
' VBScript 是 Windows 内置的脚本语言。
' 这个文件的唯一作用：用"隐藏窗口"的方式启动 Python 程序。
' 如果直接运行 python main.py，会出现一个黑色命令行窗口，这里避免了这一点。

Set objShell = CreateObject("WScript.Shell")

' %USERPROFILE% 是 Windows 环境变量，自动替换为当前用户的主目录
' 例如：C:\Users\你的用户名
' 这样别人克隆这个项目后，只要放在相同的相对位置，也能直接使用
Dim projectPath
projectPath = objShell.ExpandEnvironmentStrings("%USERPROFILE%\Desktop\code\battery-monitor\main.py")

' Run 的第二个参数 0 = 隐藏窗口（不显示黑色命令行）
' Run 的第三个参数 False = 不等待程序结束，直接返回
objShell.Run "python """ & projectPath & """", 0, False
