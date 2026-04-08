# main.py —— 程序入口
# 这是程序的"指挥中心"：把其他模块组合在一起，形成完整逻辑。
# 运行这个文件就等于启动了整个程序。

import time

# 从其他模块导入我们需要的功能
from config import BATTERY_THRESHOLD, CHECK_INTERVAL_SECONDS, REMINDER_INTERVAL_SECONDS, NOTIFICATION_TITLE, NOTIFICATION_MESSAGE
from monitor import get_battery
from notifier import notify

def main():
    print("电池监控程序已启动...")
    print(f"将在电量达到 {BATTERY_THRESHOLD}% 时提醒你拔掉充电器。")
    print("按 Ctrl+C 可以停止程序。\n")

    # 记录上次提醒的时间（None 表示本次充电周期还没提醒过）
    # 用时间戳而不是简单的 True/False，是为了判断"距上次提醒是否已过 3 分钟"
    last_notified_time = None

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
        # 3. 还没提醒过，或距上次提醒已超过 3 分钟
        if plugged and percent >= BATTERY_THRESHOLD:
            never_notified = last_notified_time is None
            enough_time_passed = not never_notified and (time.time() - last_notified_time) >= REMINDER_INTERVAL_SECONDS

            if never_notified or enough_time_passed:
                notify(NOTIFICATION_TITLE, NOTIFICATION_MESSAGE)
                last_notified_time = time.time()
                print("已发出提醒！")

        # 如果拔掉了充电器，或者电量降回阈值以下，重置提醒状态
        # 这样下次再插上充电器充到 80% 时，会重新开始提醒
        if not plugged or percent < BATTERY_THRESHOLD - 5:
            last_notified_time = None

        # 睡眠时长：
        # - 正在提醒模式中（插着电且超过阈值）→ 3 分钟后再检查，准备下一次提醒
        # - 平时 → 10 分钟检查一次就够了
        if plugged and percent >= BATTERY_THRESHOLD and last_notified_time is not None:
            time.sleep(REMINDER_INTERVAL_SECONDS)
        else:
            time.sleep(CHECK_INTERVAL_SECONDS)


if __name__ == "__main__":
    # "__main__" 判断：确保只有直接运行这个文件时才启动程序
    # 如果是被其他文件"导入"的，就不会自动运行
    main()
