---
layout: default
title: 项目
---

# 项目
<p class="page-subtitle">ROS2 驱动 · SLAM 建图 · 工具脚本</p>

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
      <h3>FAST-LIO2 + Unitree</h3>
      <p>基于 FAST-LIO2 框架的实时激光雷达-惯性里程计，适配宇树 L 系列。</p>
      <div class="card-details">
        • 实时 6-DoF 位姿估计<br>
        • 3D 点云地图构建<br>
        • IMU 紧耦合
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
        • 地图保存与复用
      </div>
      <a href="{{ "docs/leishen_n10p" | relative_url }}" class="card-link">查看文档</a>
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
