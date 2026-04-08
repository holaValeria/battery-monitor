# monitor.py —— 电量监控模块
# 这个文件只负责一件事：读取当前电池状态。
# 使用第三方库 psutil（需要安装，见 README）。

import psutil  # 用于读取系统信息（电池、CPU、内存等）

def get_battery():
    """
    读取当前电池信息。
    返回一个字典，包含：
      - percent:  当前电量百分比（例如 75.3）
      - plugged:  是否正在充电（True / False）
    如果设备没有电池（台式机），返回 None。
    """
    battery = psutil.sensors_battery()

    if battery is None:
        return None  # 台式机没有电池

    return {
        "percent": battery.percent,
        "plugged": battery.power_plugged,
    }
