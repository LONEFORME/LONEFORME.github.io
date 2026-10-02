---
layout: home

hero:
  name: "旧梦如常"
  text: "机器人感知与导航 · 个人技术空间"
  tagline: "嵌入式系统开发者 · ROS2 · 激光雷达 SLAM · 计算机视觉 · 无人机全栈"
  image:
    src: /assets/og-image.png
    alt: 旧梦如常
  actions:
    - theme: brand
      text: 🚁 无人机全栈知识库
      link: /drone/INDEX
    - theme: alt
      text: 📖 技术文档
      link: /docs/
    - theme: alt
      text: 📂 精选项目
      link: /projects

features:
  - icon: 🛰️
    title: 激光雷达 SLAM & 3D 建图
    details: 宇树 L1 (Point-LIO) 实时 3D 建图与镭神 N10P (免 ROS 纯 Python 直驱) 细立柱追踪，毫秒级感知闭环。
  - icon: 🚁
    title: 电赛无人机全栈工程
    details: STM32F405 (BirdFlight_V2.0/ADRC) + 树莓派机载计算 + T265 双目 VIO 室内全自主巡查与避障。
  - icon: 👁️
    title: 计算机视觉 & 端侧 AI
    details: OpenCV 11色自适应提取、同心圆靶心精确判据与树莓派 4B / RDK X5 轻量 YOLO 边缘推理。
  - icon: 🛠️
    title: 嵌入式 Linux & 开发板矩阵
    details: 覆盖 7 款主流开发板，Fast DDS 跨机组网与系统级看门狗自愈机制。
  - icon: 📰
    title: AI 科技与财经日报
    details: GitHub Actions 每日三次自动聚合国内外前沿 AI 资讯与全球金融市场数据。
  - icon: 🧊
    title: 3D 打印结构设计
    details: 100+ 款自研无人机机架配件、传感器云台与切片工程，SolidWorks 与 STL 原生展示。
---

<div class="custom-home-content" style="max-width: 1152px; margin: 40px auto 0; padding: 0 24px;">

## 👨‍💻 关于作者 & 核心技术栈

热衷于嵌入式 Linux、自主机器人感知与全栈无人机研发。在各类电子设计竞赛、机器人工程实战中积累了大量软硬件协同调试与底层破局经验。

| 领域 | 核心技术与掌握工具 | 对应工程与代表作 |
| :--- | :--- | :--- |
| **底层微控制器** | STM32F4 / C语言 / uCOS-III / 寄存器级外设驱动 / DMA / PWM | `BirdFlight_V2.0`、串级 PID 控制律、ADRC 自抗扰算法 |
| **单板边缘计算** | 树莓派 CM3/4B / 地平线 RDK X5 / Ubuntu Linux / systemd / Python | 机载上位机状态机、多线程串口解耦、T265 硬件看门狗自愈 |
| **SLAM 与感知** | 激光雷达 (镭神 N10P / 宇树 L1) / Point-LIO / Fast-LIO / SLAM Toolbox | 免 ROS 纯 Python 直驱极坐标点云解析、16 项 pytest 单测避障 |
| **空间位姿与导航** | Intel RealSense T265 双目 VIO / 空间四元数解算 / 离散网格图论 | 450×350cm 63单元格 DFS 全覆盖、Dijkstra 毫秒级避障重规划 |
| **计算机视觉** | OpenCV / HSV 双色彩空间自适应 / 几何轮廓逼近 / 单目反投影 / YOLO | 起降同心圆 ($4\pi A / P^2$) 靶标判定、OpenVision UDP 图传流 |
| **硬件与机械** | SolidWorks 三维建模 / 立创 EDA PCB 设计 / 拓竹 3D 打印切片 | 全包覆一体化安全框、前视长短臂支架、陶晶驰手持屏外壳 |

---

## 📬 联系方式与交流

- **GitHub**：[@LONEFORME](https://github.com/LONEFORME)
- **电子邮箱**：[lonefasf@qq.com](mailto:lonefasf@qq.com)
- **开源主页**：[https://loneforme.github.io](https://loneforme.github.io)

</div>
