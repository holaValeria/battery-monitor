# 电池守护程序 Battery Monitor

一个运行在 Windows 后台的轻量程序，当笔记本电量充到 **80%** 时自动发出声音并弹窗提醒你拔掉充电器。

> 锂电池长期保持高电量会加速老化。将充电上限控制在 80% 左右，可以显著延长电池寿命。

---

## 适用环境

- **系统：** Windows 10 / Windows 11
- **设备：** 任何使用锂电池的 Windows 笔记本电脑
- **依赖：** Python 3.x（需提前安装）

> 台式机无电池，程序会自动检测并退出。

---

## 功能

- 每 10 分钟自动检查一次电量
- 充电状态下电量达到 80% 时，播放提示音并弹出置顶警告窗口
- 每次充电周期只提醒一次，不反复打扰
- 后台静默运行，无命令行黑窗口
- 支持开机自动启动

---

## 安装与使用

**1. 安装 Python**

前往 [python.org](https://www.python.org/downloads/) 下载并安装 Python 3。

**2. 安装依赖库**

```bash
pip install psutil
```

**3. 克隆项目**

```bash
git clone https://github.com/holaValeria/battery-monitor.git
cd battery-monitor
```

**4. 运行程序**

```bash
python main.py
```

**5. 设置开机自启（可选）**

```bash
python setup_startup.py
```

运行一次即可，之后每次开机程序会自动在后台启动。

---

## 自定义设置

打开 `config.py`，可以修改以下参数：

```python
BATTERY_THRESHOLD = 80        # 提醒阈值（%），可改为 75 或 85
CHECK_INTERVAL_SECONDS = 600  # 检查间隔（秒），600 = 10 分钟
NOTIFICATION_TITLE = "电池提醒"
NOTIFICATION_MESSAGE = "电量已达到 80%，建议拔掉充电器以保护电池！"
```

---

## 取消开机自启

删除以下文件即可：

```
C:\Users\你的用户名\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\battery-monitor.vbs
```

---

## 项目结构

```
battery-monitor/
├── config.py           # 配置项
├── monitor.py          # 读取电池状态
├── notifier.py         # 发出声音与弹窗
├── main.py             # 主循环
├── run.vbs             # 静默启动脚本（隐藏黑窗口）
└── setup_startup.py    # 一次性开机自启配置工具
```
