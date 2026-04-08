# config.py —— 配置文件
# 把所有"可调整的数字"集中放在这里，方便以后修改。
# 比如你想改成 85% 提醒，只需要改这一个文件。

# 电量达到多少 % 时提醒（建议 80）
BATTERY_THRESHOLD = 80

# 每隔多少秒检查一次电量（10 分钟 = 600 秒）
CHECK_INTERVAL_SECONDS = 600

# 提醒窗口的标题和内容
NOTIFICATION_TITLE = "电池提醒"
NOTIFICATION_MESSAGE = "电量已达到 80%，建议拔掉充电器以保护电池！"
