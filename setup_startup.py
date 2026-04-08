# setup_startup.py —— 一次性设置脚本
# 运行这个文件，就会把程序添加到 Windows 开机启动。
# 只需要运行一次，之后每次开机都会自动启动电池监控。

import os
import shutil

# 当前项目文件夹的路径
project_dir = os.path.dirname(os.path.abspath(__file__))

# run.vbs 的完整路径
vbs_source = os.path.join(project_dir, "run.vbs")

# Windows 开机启动文件夹的路径
# os.environ["APPDATA"] 会自动获取当前用户的 AppData 路径
startup_folder = os.path.join(
    os.environ["APPDATA"],
    "Microsoft", "Windows", "Start Menu", "Programs", "Startup"
)

# 复制 run.vbs 到开机启动文件夹
dest = os.path.join(startup_folder, "battery-monitor.vbs")
shutil.copy(vbs_source, dest)

print(f"成功！已添加到开机启动。")
print(f"文件位置：{dest}")
print(f"\n下次开机后，电池监控程序会自动在后台运行。")
print(f"如果想取消开机启动，删除以下文件即可：")
print(f"{dest}")
