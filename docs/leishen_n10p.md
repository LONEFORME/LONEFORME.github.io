# 镭神 N10P + SLAM Toolbox 操作手册

## 一、环境准备

```bash
# 编译项目
cd ~/ros2_ws
colcon build
source install/setup.bash
```

## 二、建图流程（2个终端）

### 终端 1 — 雷达 + SLAM 建图

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch slam_toolbox_config slam_final.launch.py
```

### 终端 2 — RViz 可视化（查看地图）

```bash
source ~/ros2_ws/install/setup.bash
rviz2 -d ~/ros2_ws/src/slam_toolbox_config/rviz/lslidar.rviz
```

> 注意：`lslidar_rviz.launch.py` 不含 SLAM，跑它看不到地图。
> 看地图必须跑 `slam_final.launch.py` 建图后，再另开终端手动开 RViz。

### 终端 3 — 实时坐标输出

```bash
source ~/ros2_ws/install/setup.bash
ros2 run slam_toolbox_config robot_status.py
```

### 终端 4 — 障碍物检测

```bash
source ~/ros2_ws/install/setup.bash
ros2 run slam_toolbox_config obstacle_detector.py
```

## 三、保存地图

建图完成后，在任意终端执行：

```bash
ros2 run nav2_map_server map_saver_cli -f ~/map
```

保存结果：
- `~/map.pgm` — 栅格地图图片
- `~/map.yaml` — 地图参数文件

查看地图：

```bash
eog ~/map.pgm
```

## 四、只启动雷达（不建图）

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch lslidar_driver lsn10p_launch.py
```

## 五、Python 获取坐标与速度

建图时可用 Python 订阅实时坐标和速度数据，供后续开发使用。

### 快速测试

```bash
# 终端 1：建图
ros2 launch slam_toolbox_config slam_final.launch.py

# 终端 2：运行数据订阅示例
ros2 run slam_toolbox_config robot_data_subscriber.py
```

输出示例：
```
位置: (1.234, 0.567)  朝向: 45.3°  速度: (0.123, 0.045)  角速度: 0.012 rad/s
```

### 在自己的代码中使用

```python
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped, TwistStamped
import math


class MyRobot(Node):
    def __init__(self):
        super().__init__('my_robot')
        self.x = self.y = self.yaw = 0.0
        self.vx = self.vy = self.vyaw = 0.0

        self.create_subscription(PoseStamped, '/robot_pose', self.pose_cb, 10)
        self.create_subscription(TwistStamped, '/robot_velocity', self.vel_cb, 10)

    def pose_cb(self, msg):
        self.x = msg.pose.position.x
        self.y = msg.pose.position.y
        q = msg.pose.orientation
        self.yaw = math.atan2(
            2.0 * (q.w * q.z + q.x * q.y),
            1.0 - 2.0 * (q.y * q.y + q.z * q.z))

    def vel_cb(self, msg):
        self.vx = msg.twist.linear.x
        self.vy = msg.twist.linear.y
        self.vyaw = msg.twist.angular.z

    def get_pose(self):
        return self.x, self.y, self.yaw

    def get_velocity(self):
        return self.vx, self.vy, self.vyaw


def main(args=None):
    rclpy.init(args=args)
    robot = MyRobot()
    rclpy.spin(robot)

if __name__ == '__main__':
    main()
```

### 可用话题

| 话题 | 类型 | 说明 |
|------|------|------|
| `/robot_pose` | PoseStamped | 滤波后位姿 (x, y, 四元数) |
| `/robot_position` | PointStamped | 位置点 |
| `/robot_yaw` | Float32 | 航向角 (弧度) |
| `/robot_velocity` | TwistStamped | 线速度 + 角速度 |
| `/robot_predicted` | PointStamped | 预测位置 (100ms 前馈) |

---

## 六、常用诊断命令

```bash
# 查看所有话题
ros2 topic list

# 检查话题频率
ros2 topic hz /scan          # 雷达频率，正常 ~12Hz
ros2 topic hz /robot_pose    # 位姿频率，正常 ~100Hz

# 查看坐标输出
ros2 topic echo /robot_pose
ros2 topic echo /robot_position

# 查看 TF 树
ros2 run tf2_tools view_frames.py

# 查看节点
ros2 node list
```

## 七、RViz 基本操作

| 操作 | 方法 |
|------|------|
| 旋转视角 | 鼠标左键拖动 |
| 平移视角 | 鼠标中键拖动 |
| 缩放 | 滚轮滚动 |
| 添加话题 | 左下角 Add → By topic |
| Fixed Frame | 顶部设为 `map` |

## 八、关键文件位置

| 文件 | 说明 |
|------|------|
| `src/slam_toolbox_config/launch/slam_final.launch.py` | 启动文件 |
| `src/slam_toolbox_config/config/slam_final.yaml` | SLAM 参数 |
| `src/slam_toolbox_config/scripts/slam_fix_node.py` | 数据修复 + 坐标发布 |
| `src/slam_toolbox_config/scripts/obstacle_detector.py` | 障碍物检测 |
| `src/slam_toolbox_config/scripts/robot_status.py` | 坐标输出 |
| `src/Lslidar_ROS2_driver-M10P-N10P/lslidar_driver/params/lidar_uart_ros2/lsn10p.yaml` | 雷达参数 |
| `src/slam_toolbox_config/rviz/lslidar.rviz` | RViz 配置 |

## 九、坐标系关系

```
map → odom → laser
```

- `map`：地图坐标系（全局）
- `odom`：里程计坐标系
- `laser`：雷达坐标系（机器人本体）

## 十、话题列表

| 话题 | 类型 | 说明 |
|------|------|------|
| `/scan` | LaserScan | 原始雷达数据 |
| `/scan_fixed` | LaserScan | 修复后的雷达数据 |
| `/map` | OccupancyGrid | 栅格地图 |
| `/robot_pose` | PoseStamped | 机器人位姿（滤波后） |
| `/robot_position` | PointStamped | 机器人坐标 |
| `/robot_yaw` | Float32 | 航角（弧度） |
| `/robot_velocity` | TwistStamped | 实时速度 |
| `/robot_predicted` | PointStamped | 预测位置 |
| `/obstacle_markers` | MarkerArray | 障碍物可视化标记 |

## 十一、常见问题

### SLAM_ERROR Speed
移动太快时 SLAM 跟不上，放慢速度即可。

### 坐标更新有延迟
SLAM Toolbox scan matching 计算需要时间，位姿更新频率约 5-8Hz，属于算法特性。

### 雷达数据丢包
检查串口连接：`ls -la /dev/wheeltec_lidar`

### 编译报重复包名
确保 `src/` 下只有一个 `lslidar_msgs` 目录。

### 启动报 TF 错误
等待几秒让 SLAM 初始化完成，`map` 帧建立后会自动恢复。

## 十二、Python 启动/关闭建图

使用 `subprocess` 在 Python 中控制 SLAM 的启停，并获取坐标数据。

### 快速测试

```bash
# 启动建图 + 每秒打印坐标速度，CTRL+C 自动关闭
ros2 run slam_toolbox_config robot_app.py

# 或直接跑 Python 文件
source ~/ros2_ws/install/setup.bash
python3 ~/ros2_ws/src/slam_toolbox_config/scripts/robot_app.py
```

### 两个脚本的区别

| 脚本 | 功能 | 适用场景 |
|------|------|----------|
| `robot_app.py` | subprocess 自动启停建图 + 订阅坐标 | 一键启动，退出自动清理 |
| `robot_data_subscriber.py` | 只订阅坐标，不管理建图 | 建图已由别的方式启动，只需读数据 |

运行方式：
```bash
# 方法1：ros2 run
ros2 run slam_toolbox_config robot_app.py

# 方法2：直接 python3（效果一样）
source ~/ros2_ws/install/setup.bash
python3 ~/ros2_ws/src/slam_toolbox_config/scripts/robot_data_subscriber.py
```

### 在你的代码中使用

```python
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped, TwistStamped
import math
import subprocess, os, time


class MyRobot(Node):
    def __init__(self):
        super().__init__('my_robot')
        self.x = self.y = self.yaw = 0.0
        self.vx = self.vy = self.vyaw = 0.0

        self.create_subscription(PoseStamped, '/robot_pose', self.pose_cb, 10)
        self.create_subscription(TwistStamped, '/robot_velocity', self.vel_cb, 10)

    def pose_cb(self, msg):
        self.x = msg.pose.position.x
        self.y = msg.pose.position.y
        q = msg.pose.orientation
        self.yaw = math.atan2(2*(q.w*q.z+q.x*q.y), 1-2*(q.y*q.y+q.z*q.z))

    def vel_cb(self, msg):
        self.vx = msg.twist.linear.x
        self.vy = msg.twist.linear.y
        self.vyaw = msg.twist.angular.z

    def start_slam(self):
        """subprocess 启动建图"""
        env = os.environ.copy()
        self.slam_proc = subprocess.Popen(
            ['ros2', 'launch', 'slam_toolbox_config', 'slam_final.launch.py'],
            env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(3)

    def stop_slam(self):
        """终止建图"""
        if hasattr(self, 'slam_proc') and self.slam_proc:
            self.slam_proc.terminate()
            self.slam_proc.wait()


def main():
    rclpy.init()
    robot = MyRobot()
    robot.start_slam()
    try:
        rclpy.spin(robot)
    except KeyboardInterrupt:
        pass
    finally:
        robot.stop_slam()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
```

### 暂停/恢复建图

`robot_app.py` 运行时支持键盘控制：

| 按键 | 功能 |
|------|------|
| `p` | 暂停建图（不退出程序） |
| `r` | 恢复建图 |
| `q` | 退出 |

### 开机自启动

使用 systemd 服务，开机自动运行建图：

```bash
# 编辑服务文件
sudo nano /etc/systemd/system/robot-slam.service
```

内容如下：
```ini
[Unit]
Description=ROS2 SLAM Robot App
After=network.target

[Service]
Type=simple
User=n100
Environment=HOME=/home/n100
WorkingDirectory=/home/n100/ros2_ws
ExecStart=/home/n100/ros2_ws/src/slam_toolbox_config/scripts/robot_app.py
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```

启用：
```bash
sudo systemctl enable robot-slam.service   # 开机自启
sudo systemctl start robot-slam.service    # 立即启动
sudo systemctl stop robot-slam.service     # 停止
sudo systemctl status robot-slam.service   # 查看状态
```
```

---

## 十三、备份与恢复

### 打包源码（排除编译产物）

```bash
cd ~/ros2_ws
zip -r -q ~/ros2_ws_src_backup.zip src/ docs/ CLAUDE.md README.md \
  -x "src/unilidar_fastlio_ros2-ros2/doc/*" "src/*/Log/*" "src/*/*.pcd" "src/*/*.pgm"
```

### 恢复

```bash
cd ~/ros2_ws
unzip ~/ros2_ws_src_backup.zip
colcon build
source install/setup.bash
```

## 十四、任务目标对应功能

| 任务目标 | 实现方式 | 启动命令 |
|----------|----------|----------|
| 环境建图 | SLAM Toolbox 建图 + 回环检测 | `ros2 launch slam_toolbox_config slam_final.launch.py` |
| 自身定位 | TF 变换 + 卡尔曼滤波 | `ros2 run slam_toolbox_config robot_status.py` |
| 障碍物检测 | 聚类算法 + Marker 可视化 | `ros2 run slam_toolbox_config obstacle_detector.py` |
| 保存地图 | map_saver_cli | `ros2 run nav2_map_server map_saver_cli -f ~/map` |
