---
layout: default
title: 镭神 N10P + SLAM Toolbox
---

# 镭神 N10P + SLAM Toolbox 方案

## 硬件要求

| 组件 | 规格 |
|------|------|
| 激光雷达 | Leishen N10P / M10P（串口版） |
| 设备节点 | `/dev/wheeltec_lidar` |
| ROS2 | Humble |

---

## 代码结构

```
ros2_ws/src/
├── Lslidar_ROS2_driver-M10P-N10P/     # 镭神官方驱动
│   ├── lslidar_msgs/                   # 自定义消息类型
│   │   └── msg/
│   │       ├── LslidarScan.msg         # 单帧扫描
│   │       ├── LslidarSweep.msg        # 完整扫描
│   │       ├── LslidarPoint.msg        # 单点云
│   │       ├── LslidarPacket.msg       # 原始数据包
│   │       └── LslidarDifop.msg        # 诊断信息
│   └── lslidar_driver/
│       ├── src/
│       │   ├── lslidar_driver_node.cc  # ROS2 节点入口
│       │   ├── lslidar_driver.cc       # 驱动核心（串口/网口通信）
│       │   ├── input.cc                # 数据输入层
│       │   └── lsiosr.cpp              # 串口 IO 操作
│       ├── launch/lsn10p_launch.py     # LSN10P 专用启动
│       ├── params/lidar_uart_ros2/
│       │   └── lsn10p.yaml             # 参数配置
│       └── rviz/lslidar.rviz           # RViz 配置
│
└── slam_toolbox_config/                # SLAM 工具配置
    ├── scripts/
    │   ├── slam_fix_node.py            # 卡尔曼滤波 + 坐标输出
    │   ├── obstacle_detector.py        # 障碍物检测
    │   ├── obstacle_plotter.py         # 障碍物可视化
    │   ├── obstacle_printer.py         # 障碍物打印
    │   └── robot_status.py             # 状态监控
    ├── config/slam_final.yaml          # SLAM 参数
    ├── launch/
    │   ├── slam_final.launch.py        # 完整建图启动
    │   └── lslidar_rviz.launch.py      # 纯可视化启动
    └── rviz/lslidar.rviz              # 可视化配置
```

---

## 快速开始

```bash
# 编译
cd ~/ros2_ws
colcon build --packages-select lslidar_driver lslidar_msgs slam_toolbox_config
source install/setup.bash

# 启动雷达 + SLAM 建图（推荐）
ros2 launch slam_toolbox_config slam_final.launch.py

# 或仅查看雷达数据（不含 SLAM）
ros2 launch slam_toolbox_config lslidar_rviz.launch.py

# 或仅启动驱动
ros2 launch lslidar_driver lsn10p_launch.py
```

---

## 启动文件详解

### `slam_final.launch.py` — 完整建图

启动 4 个节点：

| 节点 | 功能 | Topic |
|------|------|-------|
| `lslidar_driver_node` | 雷达驱动 | `/scan` |
| `slam_fix_node` | 数据修正 | `/scan` → `/scan_fixed` |
| `async_slam_toolbox_node` | SLAM 建图 | `/scan_fixed` |
| `static_transform_publisher` | TF: `odom` → `laser` | — |

### `lslidar_rviz.launch.py` — 纯可视化

启动 3 个节点：雷达驱动 + slam_fix + RViz。**不含 SLAM**，用于调试雷达数据，看不到地图。

### `lsn10p_launch.py` — 仅驱动

启动 2 个节点：雷达驱动 + RViz（不含修正和SLAM）

---

## 可视化（查看地图）

建图时查看实时地图有两个方式：

### 方式一：建图 + 可视化分两个终端

```bash
# 终端 1：启动建图
ros2 launch slam_toolbox_config slam_final.launch.py

# 终端 2：打开 RViz 查看地图
source ~/ros2_ws/install/setup.bash
rviz2 -d ~/ros2_ws/src/slam_toolbox_config/rviz/lslidar.rviz
```

### 方式二：仅查看已保存的地图

```bash
ros2 run nav2_map_server map_server ./my_map.yaml
rviz2  # 手动添加 Map 话题
```

### RViz 基本操作

| 操作 | 方法 |
|------|------|
| 旋转视角 | 鼠标左键拖动 |
| 平移视角 | 鼠标中键拖动 |
| 缩放 | 滚轮 |
| Fixed Frame | 顶部设为 `map` |
| 添加话题 | 左下角 Add → By topic |

---

## 坐标输出话题

`slam_fix_node.py` 通过卡尔曼滤波输出以下话题：

| 话题 | 类型 | 说明 |
|------|------|------|
| `/scan_fixed` | LaserScan | 修正后的雷达数据 |
| `/robot_pose` | PoseStamped | 滤波后位姿 (map 坐标系) |
| `/robot_position` | PointStamped | 位置点 (map 坐标系) |
| `/robot_yaw` | Float32 | 航向角 (弧度) |
| `/robot_velocity` | TwistStamped | 线速度/角速度 |
| `/robot_predicted` | PointStamped | 预测位置 (100ms 前馈) |
| `/robot_debug` | Float32MultiArray | [x, y, yaw°, vx, vy, vyaw, x_pred, y_pred] |

滤波特性：静止时自动清零速度，防止零漂。

---

## 障碍物检测

| 节点 | 功能 | 输出 |
|------|------|------|
| `obstacle_detector.py` | 从 `/scan_fixed` 检测障碍物 | `/obstacles` |
| `obstacle_plotter.py` | RViz 可视化标记 | Marker 阵列 |
| `obstacle_printer.py` | 终端打印障碍物信息 | 控制台输出 |

---

## 保存地图

```bash
ros2 run nav2_map_server map_saver_cli -f ~/my_map
```

生成 `~/my_map.pgm`（栅格图）和 `~/my_map.yaml`（元数据）。

---

## 参数配置

### 雷达参数

文件：`Lslidar_ROS2_driver-M10P-N10P/lslidar_driver/params/lidar_uart_ros2/lsn10p.yaml`

| 参数 | 当前值 | 说明 |
|------|--------|------|
| `interface_selection` | `serial` | 接口: `serial` / `net` |
| `device_port` | `/dev/wheeltec_lidar` | 串口设备 |
| `lidar_name` | `N10_P` | 型号: `M10` / `M10_P` / `N10` / `N10_P` / `L10` |
| `frame_id` | `laser` | 激光坐标系 |
| `scan_topic` | `/scan` | 输出话题 |
| `min_range` / `max_range` | `0.0` / `200.0` | 距离过滤 |
| `pubScan` | `true` | 是否发布 scan |
| `pubPointCloud2` | `false` | 是否发布点云 |

### SLAM 参数

文件：`slam_toolbox_config/config/slam_final.yaml`

| 参数 | 当前值 | 说明 |
|------|--------|------|
| `mode` | `mapping` | 模式: `mapping` / `localization` |
| `resolution` | `0.05` | 地图分辨率 (米/像素) |
| `map_update_interval` | `0.2` | 地图更新间隔 (秒) |
| `max_laser_range` | `25.0` | 最大有效距离 |
| `do_loop_closing` | `true` | 回环检测 |
| `scan_topic` | `/scan_fixed` | 输入话题 |

---

## 常见问题

**Q: 串口权限不足**
```bash
sudo usermod -a -G dialout $USER
# 重新登录后生效
```

**Q: 驱动编译报错找不到依赖**
```bash
sudo apt install ros-humble-tf2 ros-humble-tf2-ros \
                 ros-humble-pcl-conversions ros-humble-pcl-ros \
                 libpcap-dev
```

**Q: 雷达不出数据**
1. 检查 `/dev/wheeltec_lidar` 是否存在
2. 检查 `lsn10p.yaml` 中的串口路径和型号参数
3. 运行 `ls -l /dev/wheeltec_lidar` 确认设备权限
