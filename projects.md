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
    <h2>N100 · ROS2 激光雷达 SLAM 工作空间</h2>
  </div>
  <p class="group-desc">整合宇树 L1（3D）与镭神 N10P（2D）双雷达，配套 Point-LIO 与 SLAM Toolbox 双建图方案，含自研障碍物检测与位姿优化节点，即拿即用的机器人感知与导航参考实现。</p>

  <div class="card-grid">
    <div class="card">
      <div class="card-icon-box" style="--icon-color: #00ff88; --icon-glow: rgba(0,255,136,0.25);">
        <svg class="card-svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><circle cx="12" cy="12" r="2"/></svg>
      </div>
      <h3>宇树 L1 + Point-LIO（3D）</h3>
      <p>Unitree L1 3D 激光雷达 + Point-LIO 紧耦合里程计，实时 6-DoF 位姿估计与稠密点云建图。</p>
      <div class="card-details">
        • 点云发布 + IMU 数据融合<br>
        • 6-DoF 实时里程计，3D PCD 地图输出<br>
        • 坐标零点校准 + 静止漂移抑制<br>
        • x86_64 / aarch64 双平台支持
      </div>
      <a href="{{ "docs/unitree_l1" | relative_url }}" class="card-link">查看文档</a>
      <a href="https://github.com/LONEFORME/N100" target="_blank" rel="noopener" class="card-link">GitHub</a>
    </div>

    <div class="card">
      <div class="card-icon-box" style="--icon-color: #00d4ff; --icon-glow: rgba(0,212,255,0.25);">
        <svg class="card-svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4.9 19.1C1 15.2 1 8.8 4.9 4.9"/><path d="M7.8 16.2c-2.3-2.3-2.3-6.1 0-8.5"/><circle cx="12" cy="12" r="2"/><path d="M16.2 7.8c2.3 2.3 2.3 6.1 0 8.5"/><path d="M19.1 4.9C23 8.8 23 15.1 19.1 19"/></svg>
      </div>
      <h3>镭神 N10P + SLAM Toolbox（2D）</h3>
      <p>Leishen N10P 单线激光雷达 + SLAM Toolbox，2D 栅格地图建图，配套自研障碍物检测与位姿滤波。</p>
      <div class="card-details">
        • UART 串口驱动，驱动 bug 修复（数组波动）<br>
        • 2D 栅格地图 + 回环检测 + 地图保存<br>
        • 障碍物检测：BFS 聚类 + PCA 墙识别 + 多帧确认<br>
        • 位姿优化：卡尔曼滤波 + 静止检测 + 未来位置预测
      </div>
      <a href="{{ "docs/leishen_n10p" | relative_url }}" class="card-link">查看文档</a>
      <a href="https://github.com/LONEFORME/N100" target="_blank" rel="noopener" class="card-link">GitHub</a>
    </div>
  </div>
</div>

<div class="project-group">
  <div class="section-title">
    <span class="section-icon-box">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="16" height="16" x="4" y="4" rx="2"/><rect width="6" height="6" x="9" y="9" rx="1"/><path d="M15 2v2"/><path d="M15 20v2"/><path d="M2 15h2"/><path d="M2 9h2"/><path d="M20 15h2"/><path d="M20 9h2"/><path d="M9 21v1"/><path d="M9 2v1"/></svg>
    </span>
    <h2>嵌入式开发板与多机通信</h2>
  </div>
  <p class="group-desc">覆盖 7 款主流开发板的通用配置参考、A/B/C 分类部署、Fast DDS Discovery Server 多机跨网段通信与 AI Skill 资产库（v2.43）。</p>

  <div class="card-grid">
    <div class="card">
      <div class="card-icon-box" style="--icon-color: #06b6d4; --icon-glow: rgba(6,182,212,0.25);">
        <svg class="card-svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="16" height="16" x="4" y="4" rx="2"/><rect width="6" height="6" x="9" y="9" rx="1"/><path d="M15 2v2"/><path d="M15 20v2"/><path d="M2 15h2"/><path d="M2 9h2"/><path d="M20 15h2"/><path d="M20 9h2"/><path d="M9 21v1"/><path d="M9 2v1"/></svg>
      </div>
      <h3>嵌入式开发板配置参考与 AI 资产库</h3>
      <p>7 款主流开发板从零到可用的一键自动化部署参考、ROS2 跨板网络通信与 AI Skill 多平台同步体系。</p>
      <div class="card-details">
        • A/B/C 三类板精准分类（Ubuntu裸装 / Debian+LXC / 边缘AI与串口）<br>
        • Fast DDS Discovery Server 中枢组网（A7Z:11811 打通跨设备互通）<br>
        • 46 个跨板自动化运维脚本库 + YOLOv8 边缘视觉实时检测<br>
        • AI Skill 唯一真源（v2.43，支持 Codex / DeepSeek / WorkBuddy / Gemini）
      </div>
      <a href="https://github.com/LONEFORME/embedded-board-reference" target="_blank" rel="noopener" class="card-link">查看项目</a>
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
      <div class="card-icon-box" style="--icon-color: #00ff88; --icon-glow: rgba(0,255,136,0.25);">
        <svg class="card-svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M2 12h20"/><circle cx="12" cy="12" r="4"/><circle cx="4" cy="4" r="2.5"/><circle cx="20" cy="4" r="2.5"/><circle cx="4" cy="20" r="2.5"/><circle cx="20" cy="20" r="2.5"/></svg>
      </div>
      <h3>凌霄飞控无人机方案</h3>
      <p>基于匿名凌霄飞控（ANO_LX）的全国电赛全栈开发体系与实战工程，支持多主控平台与硬件级 VIO 空间导航。</p>
      <div class="card-details">
        • 匿名凌霄飞控官方源码（STM32F407 / MSP432 / TM4C123）<br>
        • 匿名通信协议 V7 + 独立硬件 IMU 减震固件（.ano）<br>
        • 嘉楠 K230 边缘视觉端侧 AI + T265 硬件级 VIO 坐标/速度直出<br>
        • 下视激光 ToF 垂直定高 + 历年电赛参考（2022-HUST / NUEDC-2024-D / UAV-2023）
      </div>
      <a href="{{ "/videos" | relative_url }}" class="card-link">飞行演示</a>
      <a href="https://github.com/LONEFORME/lingxiao-drone" target="_blank" rel="noopener" class="card-link">GitHub</a>
    </div>

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
