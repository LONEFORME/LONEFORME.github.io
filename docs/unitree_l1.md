---
layout: default
title: 宇树 L1 + FAST-LIO2
---

# 宇树 L1 + FAST-LIO2 建图方案

## 硬件要求

| 组件 | 规格 |
|------|------|
| 激光雷达 | Unitree L1 / L2 / L3 |
| 平台 | x86_64 / aarch64 |
| ROS2 | Humble 或更高版本 |

## 快速开始

```bash
# 克隆仓库
cd ~/ros2_ws/src
git clone <repo_url>/unilidar_fastlio_ros2-ros2.git

# 编译
cd ~/ros2_ws
colcon build --packages-select unilidar_fastlio_ros2
source install/setup.bash

# 运行
ros2 launch unilidar_fastlio_ros2 mapping.launch.py
```

## 配置说明

编辑 `config/` 目录下的 YAML 文件选择对应雷达型号：

| 文件 | 适用型号 |
|------|----------|
| `mid360.yaml` | L1 / L2 |
| `unilidar_l2.yaml` | L3 |
| `avia.yaml` | Avia |

## 输出

- 实时 3D 点云地图
- 6 自由度位姿估计
- 可保存 PCD 格式点云
