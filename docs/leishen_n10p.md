---
layout: default
title: 镭神 N10P + SLAM Toolbox
---

# 镭神 N10P + SLAM Toolbox 方案

## 硬件要求

| 组件 | 规格 |
|------|------|
| 激光雷达 | Leishen N10P / M10P |
| 接口 | UART |
| ROS2 | Humble 或更高版本 |

## 快速开始

```bash
# 编译
cd ~/ros2_ws
colcon build --packages-select lslidar_driver slam_toolbox_config
source install/setup.bash

# 启动雷达 + SLAM
ros2 launch slam_toolbox_config slam_final.launch.py

# 可视化
ros2 launch slam_toolbox_config lslidar_rviz.launch.py
```

## 保存地图

```bash
ros2 run nav2_map_server map_saver_cli -f ~/map
```

## 配置参考

### 雷达参数
`src/Lslidar_ROS2_driver-M10P-N10P/lslidar_driver/params/lidar_uart_ros2/lsn10p.yaml`

### SLAM 参数
`src/slam_toolbox_config/config/slam_final.yaml`
