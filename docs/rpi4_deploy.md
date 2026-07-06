---
layout: default
title: 树莓派 4B 部署
---

# 树莓派 4B 部署指南

将镭神 N10P + SLAM Toolbox 方案部署到树莓派 4B。

---

## 环境要求

| 项目 | 要求 |
|------|------|
| 硬件 | Raspberry Pi 4B（建议 4GB+ RAM） |
| 系统 | Ubuntu Server 22.04 LTS (ARM64) |
| ROS2 | Humble |
| 存储 | 32GB+ SD 卡或 SSD |

---

## 系统准备

### 安装 Ubuntu Server

从 [Ubuntu 官网](https://ubuntu.com/download/raspberry-pi) 下载 **Ubuntu Server 22.04 LTS (64-bit)**，用 Raspberry Pi Imager 烧录到 SD 卡。

### 安装 ROS2 Humble

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install software-properties-common
sudo add-apt-repository universe
sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
sudo apt update
sudo apt install ros-humble-desktop -y
```

### 安装依赖

```bash
sudo apt install -y ros-humble-slam-toolbox ros-humble-nav2-map-server \
  ros-humble-tf2 ros-humble-tf2-ros ros-humble-pcl-conversions \
  ros-humble-pcl-ros libpcap-dev python3-colcon-common-extensions
```

---

## 部署 ROS 工作空间

```bash
# 克隆项目
cd ~
git clone https://github.com/LONEFORME/N100.git ros2_ws
cd ros2_ws

# 删掉 x86 编译产物
rm -rf build/ install/ log/

# 只编译镭神相关包（跳过宇树）
colcon build --parallel-workers 1 \
  --packages-select lslidar_msgs lslidar_driver slam_toolbox_config

# 配置环境
echo "source ~/ros2_ws/install/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

---

## 配置雷达

### 确认串口设备

```bash
ls -l /dev/ttyACM*
```

记录设备名（通常是 `/dev/ttyACM0`），然后修改参数文件：

```bash
nano ~/ros2_ws/src/Lslidar_ROS2_driver-M10P-N10P/lslidar_driver/params/lidar_uart_ros2/lsn10p.yaml
```

将 `device_port` 和 `serial_port_` 改为实际设备名：

```yaml
device_port: /dev/ttyACM0
serial_port_: /dev/ttyACM0
```

### 配置 udev 规则（可选，固定设备名）

```bash
# 创建 udev 规则
echo 'KERNEL=="ttyACM*", ATTRS{idVendor}=="1a86", ATTRS{idProduct}=="55d4", SYMLINK+="wheeltec_lidar", MODE="0666"' | sudo tee /etc/udev/rules.d/99-wheeltec-lidar.rules
sudo udevadm control --reload-rules
sudo udevadm trigger
```

> `idVendor` 和 `idProduct` 用 `lsusb` 查看实际值。

---

## 调优（Pi 4B 性能优化）

Pi 4B CPU 性能有限，建议调整 SLAM 参数降低负载：

```bash
nano ~/ros2_ws/src/slam_toolbox_config/config/slam_final.yaml
```

| 参数 | 默认值 | 建议值（Pi 4B） | 说明 |
|------|--------|-----------------|------|
| `resolution` | `0.05` | `0.10` | 降低地图分辨率，减少计算量 |
| `map_update_interval` | `0.2` | `0.5` | 降低地图更新频率（5Hz → 2Hz） |
| `scan_buffer_size` | `50` | `20` | 减少扫描缓存帧数 |
| `loop_search_maximum_distance` | `3.0` | `2.0` | 缩小回环搜索范围 |

修改后重新编译：

```bash
cd ~/ros2_ws && colcon build --packages-select slam_toolbox_config && source install/setup.bash
```

（Python 脚本无需编译，直接生效）

---

## 启动

```bash
# 终端 1：建图
ros2 launch slam_toolbox_config slam_final.launch.py

# 终端 2（SSH 另开窗口）：RViz 可视化（需显示器或远程）
rviz2 -d ~/ros2_ws/src/slam_toolbox_config/rviz/lslidar.rviz

# 保存地图
ros2 run nav2_map_server map_saver_cli -f ~/map
```

---

## 无头模式（无显示器）

树莓派通常没有显示器，可通过 SSH 操作并用 `rosbag` 录数据：

```bash
# 录数据
ros2 bag record -a -o ~/rosbag_output

# 传到 PC 后用 RViz 回放
# PC 上：
ros2 bag play ~/rosbag_output
rviz2 -d ~/ros2_ws/src/slam_toolbox_config/rviz/lslidar.rviz
```

---

## 常见问题

### 编译卡死 / OOM

```bash
# 限制并行数
colcon build --parallel-workers 1
# 或增加 swap
sudo fallocate -l 4G /swapfile && sudo chmod 600 /swapfile && sudo mkswap /swapfile && sudo swapon /swapfile
```

### 雷达不出数据

```bash
# 检查设备
ls -l /dev/ttyACM*
ls -l /dev/wheeltec_lidar

# 检查权限
sudo usermod -a -G dialout $USER
# 重新登录后生效

# 检查串口
sudo apt install minicom
minicom -D /dev/ttyACM0 -b 921600
```

### SLAM 卡顿

降低地图分辨率或增加 `map_update_interval`，参考上方的调优参数。

---

## 文件位置汇总

| 文件 | 说明 |
|------|------|
| `~/ros2_ws/src/Lslidar_ROS2_driver-M10P-N10P/lslidar_driver/params/lidar_uart_ros2/lsn10p.yaml` | 雷达参数（串口、型号） |
| `~/ros2_ws/src/slam_toolbox_config/config/slam_final.yaml` | SLAM 参数（分辨率、频率） |
| `~/ros2_ws/src/slam_toolbox_config/launch/slam_final.launch.py` | 建图启动文件 |
