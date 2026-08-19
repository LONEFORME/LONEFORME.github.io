---
layout: default
title: 项目
---

<h1>项目</h1>
<p class="page-subtitle">ROS2 驱动 · SLAM 建图 · 计算机视觉 · 无人机 · 工具脚本</p>

<div class="project-group">
  <div class="section-title">
    <span class="section-icon-box">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><circle cx="12" cy="12" r="2"/></svg>
    </span>
    <h2>ROS2 激光雷达驱动</h2>
  </div>

  <div class="card-grid">
    <div class="card">
      <div class="card-icon-box" style="--icon-color: #00ff88; --icon-glow: rgba(0,255,136,0.25);">
        <svg class="card-svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><circle cx="12" cy="12" r="2"/></svg>
      </div>
      <h3>宇树 L1 系列</h3>
      <p>Unitree L1 激光雷达的 ROS2 封装驱动。</p>
      <div class="card-details">
        • 点云发布与可视化<br>
        • IMU 数据融合<br>
        • 多平台支持（x86_64 / aarch64）<br>
        • 自动启动脚本
      </div>
      <a href="https://github.com/LONEFORME/N100" target="_blank" rel="noopener" class="card-link">查看项目</a>
    </div>

    <div class="card">
      <div class="card-icon-box" style="--icon-color: #00d4ff; --icon-glow: rgba(0,212,255,0.25);">
        <svg class="card-svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4.9 19.1C1 15.2 1 8.8 4.9 4.9"/><path d="M7.8 16.2c-2.3-2.3-2.3-6.1 0-8.5"/><circle cx="12" cy="12" r="2"/><path d="M16.2 7.8c2.3 2.3 2.3 6.1 0 8.5"/><path d="M19.1 4.9C23 8.8 23 15.1 19.1 19"/></svg>
      </div>
      <h3>镭神 N10P</h3>
      <p>Leishen 单线激光雷达 ROS2 驱动，适用于室内导航与建图。</p>
      <div class="card-details">
        • UART 串口通信<br>
        • SLAM Toolbox 集成<br>
        • 障碍物检测节点
      </div>
      <a href="https://github.com/LONEFORME/N100" target="_blank" rel="noopener" class="card-link">查看项目</a>
    </div>
  </div>
</div>

<div class="project-group">
  <div class="section-title">
    <span class="section-icon-box">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="3 6 9 3 15 6 21 3 21 18 15 21 9 18 3 21"/><line x1="9" y1="3" x2="9" y2="18"/><line x1="15" y1="6" x2="15" y2="21"/></svg>
    </span>
    <h2>SLAM 建图</h2>
  </div>

  <div class="card-grid">
    <div class="card">
      <div class="card-icon-box" style="--icon-color: #10b981; --icon-glow: rgba(16,185,129,0.25);">
        <svg class="card-svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/></svg>
      </div>
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
      <div class="card-icon-box" style="--icon-color: #00d4ff; --icon-glow: rgba(0,212,255,0.25);">
        <svg class="card-svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="3 6 9 3 15 6 21 3 21 18 15 21 9 18 3 21"/><line x1="9" y1="3" x2="9" y2="18"/><line x1="15" y1="6" x2="15" y2="21"/></svg>
      </div>
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
    <span class="section-icon-box">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z"/><circle cx="12" cy="12" r="3"/></svg>
    </span>
    <h2>计算机视觉</h2>
  </div>

  <div class="card-grid">
    <div class="card">
      <div class="card-icon-box" style="--icon-color: #a855f7; --icon-glow: rgba(168,85,247,0.25);">
        <svg class="card-svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z"/><circle cx="12" cy="12" r="3"/><path d="M12 9v6"/><path d="M9 12h6"/></svg>
      </div>
      <h3>ZCode 视觉识别系统</h3>
      <p>综合视觉识别工程，支持多种输入源与目标检测。</p>
      <div class="card-details">
        • 图片 / 视频文件输入<br>
        • 圆形识别与几何检测<br>
        • 多目标检测与跟踪<br>
        • 无摄像头测试图生成脚本
      </div>
      <a href="https://github.com/LONEFORME/ZCodeProject" target="_blank" rel="noopener" class="card-link">查看项目</a>
    </div>
  </div>
</div>

<div class="project-group">
  <div class="section-title">
    <span class="section-icon-box">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M2 12h20"/><circle cx="12" cy="12" r="4"/></svg>
    </span>
    <h2>无人机</h2>
  </div>

  <div class="card-grid">
    <div class="card">
      <div class="card-icon-box" style="--icon-color: #f59e0b; --icon-glow: rgba(245,158,11,0.25);">
        <svg class="card-svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M2 12h20"/><circle cx="12" cy="12" r="4"/><circle cx="4" cy="4" r="2.5"/><circle cx="20" cy="4" r="2.5"/><circle cx="4" cy="20" r="2.5"/><circle cx="20" cy="20" r="2.5"/></svg>
      </div>
      <h3>锡月无人机方案</h3>
      <p>2025 年电子设计竞赛无人机项目，完整的飞控到上位机方案。</p>
      <div class="card-details">
        • STM32F4 飞控固件（PID / ADRC / LQR）<br>
        • 树莓派上位机主控程序<br>
        • 视觉识别模块集成<br>
        • T265 位姿数据融合与路径规划
      </div>
      <a href="https://github.com/LONEFORME/xiyue-drone" target="_blank" rel="noopener" class="card-link">查看项目</a>
    </div>
  </div>
</div>

<div class="project-group">
  <div class="section-title">
    <span class="section-icon-box">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/></svg>
    </span>
    <h2>3D 打印</h2>
  </div>

  <div class="card-grid">
    <div class="card">
      <div class="card-icon-box" style="--icon-color: #ec4899; --icon-glow: rgba(236,72,153,0.25);">
        <svg class="card-svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>
      </div>
      <h3>3D 打印模型库</h3>
      <p>常用机械结构与配件的 3D 打印模型文件集合。</p>
      <div class="card-details">
        • STL / 3MF / SLDPRT 格式<br>
        • Git LFS 大文件管理
      </div>
      <a href="https://github.com/LONEFORME/3d-models" target="_blank" rel="noopener" class="card-link">查看项目</a>
    </div>
  </div>
</div>

<div class="project-group">
  <div class="section-title">
    <span class="section-icon-box">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>
    </span>
    <h2>工具</h2>
  </div>

  <div class="card-grid">
    <div class="card">
      <div class="card-icon-box" style="--icon-color: #38bdf8; --icon-glow: rgba(56,189,248,0.25);">
        <svg class="card-svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21.5 2v6h-6M21.34 15.57a10 10 0 1 1-.57-8.38l5.67-5.67"/></svg>
      </div>
      <h3>T265 自动 Boot</h3>
      <p>Intel RealSense T265 追踪相机的固件加载脚本。</p>
      <a href="https://github.com/LONEFORME/N100" target="_blank" rel="noopener" class="card-link">查看项目</a>
    </div>
  </div>
</div>