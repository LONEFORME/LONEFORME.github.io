---
layout: default
title: 项目
---

# 项目
<p class="page-subtitle">ROS2 驱动 · SLAM 建图 · 计算机视觉 · 无人机 · 工具脚本</p>

<div class="project-group">
  <div class="section-title">
    <span class="section-icon">📡</span>
    <h2>ROS2 激光雷达驱动</h2>
  </div>

  <div class="card-grid">
    <div class="card">
      <div class="card-icon">📡</div>
      <h3>宇树 L1 系列</h3>
      <p>Unitree L1 激光雷达的 ROS2 封装驱动。</p>
      <div class="card-details">
        • 点云发布与可视化<br>
        • IMU 数据融合<br>
        • 多平台支持（x86_64 / aarch64）<br>
        • 自动启动脚本
      </div>
      <a href="https://github.com/LONEFORME/N100" class="card-link">查看项目</a>
    </div>

    <div class="card">
      <div class="card-icon">🔭</div>
      <h3>镭神 N10P</h3>
      <p>Leishen 单线激光雷达 ROS2 驱动，适用于室内导航与建图。</p>
      <div class="card-details">
        • UART 串口通信<br>
        • SLAM Toolbox 集成<br>
        • 障碍物检测节点
      </div>
      <a href="https://github.com/LONEFORME/N100" class="card-link">查看项目</a>
    </div>
  </div>
</div>

<div class="project-group">
  <div class="section-title">
    <span class="section-icon">🗺️</span>
    <h2>SLAM 建图</h2>
  </div>

  <div class="card-grid">
    <div class="card">
      <div class="card-icon">🧭</div>
      <h3>Point-LIO + Unitree</h3>
      <p>基于 Point-LIO 框架的实时激光雷达-惯性里程计，适配宇树 L 系列。</p>
      <div class="card-details">
        • 实时 6-DoF 位姿估计<br>
        • 3D 点云地图构建<br>
        • IMU 紧耦合<br>
        • 坐标输出优化 + 启动脚本
      </div>
      <a href="{{ "docs/unitree_l1" | relative_url }}" class="card-link">查看文档</a>
    </div>

    <div class="card">
      <div class="card-icon">🗺️</div>
      <h3>SLAM Toolbox + 镭神</h3>
      <p>基于 SLAM Toolbox 的 2D 激光 SLAM 方案。</p>
      <div class="card-details">
        • 2D 栅格地图构建<br>
        • 地图保存与复用<br>
        • 障碍物检测节点集成
      </div>
      <a href="{{ "docs/leishen_n10p" | relative_url }}" class="card-link">查看文档</a>
    </div>
  </div>
</div>

<div class="project-group">
  <div class="section-title">
    <span class="section-icon">👁️</span>
    <h2>计算机视觉</h2>
  </div>

  <div class="card-grid">
    <div class="card">
      <div class="card-icon">👁️</div>
      <h3>ZCode 视觉识别系统</h3>
      <p>综合视觉识别工程，支持多种输入源与目标检测。</p>
      <div class="card-details">
        • 图片 / 视频文件输入<br>
        • 圆形识别与几何检测<br>
        • 多目标检测与跟踪<br>
        • 无摄像头测试图生成脚本
      </div>
      <a href="https://github.com/LONEFORME/ZCodeProject" class="card-link">查看项目</a>
    </div>
  </div>
</div>

<div class="project-group">
  <div class="section-title">
    <span class="section-icon">🚁</span>
    <h2>无人机</h2>
  </div>

  <div class="card-grid">
    <div class="card">
      <div class="card-icon">🚁</div>
      <h3>锡月无人机方案</h3>
      <p>2025 年电子设计竞赛无人机项目，完整的飞控到上位机方案。</p>
      <div class="card-details">
        • STM32F4 飞控固件（PID / ADRC / LQR）<br>
        • 树莓派上位机主控程序<br>
        • 视觉识别模块集成<br>
        • T265 位姿数据融合与路径规划
      </div>
      <a href="https://github.com/LONEFORME/xiyue-drone" class="card-link">查看项目</a>
    </div>
  </div>
</div>

<div class="project-group">
  <div class="section-title">
    <span class="section-icon">🖨️</span>
    <h2>3D 打印</h2>
  </div>

  <div class="card-grid">
    <div class="card">
      <div class="card-icon">🖨️</div>
      <h3>3D 打印模型库</h3>
      <p>常用机械结构与配件的 3D 打印模型文件集合。</p>
      <div class="card-details">
        • STL / 3MF / SLDPRT 格式<br>
        • Git LFS 大文件管理
      </div>
      <a href="https://github.com/LONEFORME/3d-models" class="card-link">查看项目</a>
    </div>
  </div>
</div>

<div class="project-group">
  <div class="section-title">
    <span class="section-icon">🔧</span>
    <h2>工具</h2>
  </div>

  <div class="card-grid">
    <div class="card">
      <div class="card-icon">🔄</div>
      <h3>T265 自动 Boot</h3>
      <p>Intel RealSense T265 追踪相机的固件加载脚本。</p>
      <a href="https://github.com/LONEFORME/N100" class="card-link">查看项目</a>
    </div>
  </div>
</div>