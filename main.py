# main.py —— 程序入口
# 这是程序的"指挥中心"：把其他模块组合在一起，形成完整逻辑。
# 运行这个文件就等于启动了整个程序。

import time

# 从其他模块导入我们需要的功能
from config import BATTERY_THRESHOLD, CHECK_INTERVAL_SECONDS, NOTIFICATION_TITLE, NOTIFICATION_MESSAGE
from monitor import get_battery
from notifier import notify

def main():
    print("电池监控程序已启动...")
    print(f"将在电量达到 {BATTERY_THRESHOLD}% 时提醒你拔掉充电器。")
    print("按 Ctrl+C 可以停止程序。\n")

    # 这个变量用来"记住"我们是否已经提醒过了。
    # 避免每 60 秒就不停地弹窗，只在每次充电周期里提醒一次。
    already_notified = False

    while True:  # 无限循环，直到用户手动停止
        battery = get_battery()

        if battery is None:
            print("未检测到电池（可能是台式机），程序退出。")
            break

        percent = battery["percent"]
        plugged = battery["plugged"]

        # 打印当前状态（方便调试，看到程序在正常运行）
        status = "充电中" if plugged else "未充电"
        print(f"当前电量：{percent:.1f}%  状态：{status}")

        # 核心判断逻辑：
        # 1. 正在充电
        # 2. 电量已达到阈值
        # 3. 这次充电周期还没有提醒过
        if plugged and percent >= BATTERY_THRESHOLD and not already_notified:
            notify(NOTIFICATION_TITLE, NOTIFICATION_MESSAGE)
            already_notified = True
            print("已发出提醒！")

        # 如果拔掉了充电器，或者电量降回阈值以下，重置提醒标志
        # 这样下次再插上充电器充到 80% 时，还会再提醒
        if not plugged or percent < BATTERY_THRESHOLD - 5:
            already_notified = False

        # 等待一段时间再检查（默认 60 秒）
        time.sleep(CHECK_INTERVAL_SECONDS)


if __name__ == "__main__":
    # "__main__" 判断：确保只有直接运行这个文件时才启动程序
    # 如果是被其他文件"导入"的，就不会自动运行
    main()
