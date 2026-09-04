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
  <p class="group-desc">整合宇树 L1（3D）与镭神 N10P（2D）双雷达，配套 FAST-LIO2 与 SLAM Toolbox 双建图方案，含自研障碍物检测与位姿优化节点，即拿即用的机器人感知与导航参考实现。</p>

  <div class="card-grid">
    <div class="card">
      <div class="card-icon-box icon-green">
        <svg class="card-svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><circle cx="12" cy="12" r="2"/></svg>
      </div>
      <h3>宇树 L1 + FAST-LIO2（3D）</h3>
      <p>Unitree L1 3D 激光雷达 + FAST-LIO2 激光惯性里程计，基于 IKD-Tree 动态点云树与 6-DoF 紧耦合位姿估计。</p>
      <div class="card-details">
        • 宇树 L1 点云驱动 + 硬件 IMU 紧耦合融合<br>
        • FAST-LIO2 实时 6-DoF 里程计，3D PCD 地图输出<br>
        • 坐标零点校准 + 静止漂移抑制 + 自研一键启动脚本<br>
        • x86_64 / aarch64 双架构 SDK 支持
      </div>
      <a href="{{ "docs/unitree_l1" | relative_url }}" class="card-link">查看文档</a>
      <a href="https://github.com/LONEFORME/N100" target="_blank" rel="noopener" class="card-link">GitHub</a>
    </div>

    <div class="card">
      <div class="card-icon-box icon-blue">
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
      <div class="card-icon-box icon-cyan">
        <svg class="card-svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="16" height="16" x="4" y="4" rx="2"/><rect width="6" height="6" x="9" y="9" rx="1"/><path d="M15 2v2"/><path d="M15 20v2"/><path d="M2 15h2"/><path d="M2 9h2"/><path d="M20 15h2"/><path d="M20 9h2"/><path d="M9 21v1"/><path d="M9 2v1"/></svg>
      </div>
      <h3>嵌入式开发板配置参考与 AI 资产库</h3>
      <p>7 款主流开发板从零到可用的一键自动化部署参考、ROS2 跨板网络通信与 AI Skill 多平台同步体系。</p>
      <div class="card-details">
        • A/B/C 三类板精准分类（Ubuntu裸装 / Debian+LXC / 边缘AI与串口）<br>
        • Fast DDS Discovery Server 中枢组网（A7Z:11811 打通跨设备互通）<br>
        • 46 个跨板自动化运维脚本库 + YOLOv8 边缘视觉实时检测<br>
        • AI Skill 唯一真源（v2.43），支持 Codex / DeepSeek / WorkBuddy / Gemini
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
      <div class="card-icon-box icon-purple">
        <svg class="card-svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z"/><circle cx="12" cy="12" r="3"/><path d="M12 9v6"/><path d="M9 12h6"/></svg>
      </div>
      <h3>ZCode 视觉识别系统</h3>
      <p>基于 OpenCV 的综合计算机视觉识别与硬件联动系统，支持 11 种颜色检测、几何轮廓分析与树莓派 GPIO 控制。</p>
      <div class="card-details">
        • 11 种颜色 HSV/BGR 空间自适应精准识别<br>
        • 几何轮廓形状分类 + 圆形度公式（4πA/P²）区分实心/空心圆<br>
        • 双线程并发架构（采集线程 + 预处理线程，帧锁保证线程安全）<br>
        • 树莓派 GPIO 硬件联动（风扇 PWM 调速/正反转 + 蜂鸣器通断）
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
      <div class="card-icon-box icon-green">
        <svg class="card-svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20M2 12h20"/><circle cx="12" cy="12" r="4"/><circle cx="4" cy="4" r="2.5"/><circle cx="20" cy="4" r="2.5"/><circle cx="4" cy="20" r="2.5"/><circle cx="20" cy="20" r="2.5"/></svg>
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
      <div class="card-icon-box icon-orange">
        <svg class="card-svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20M2 12h20"/><circle cx="12" cy="12" r="4"/><circle cx="4" cy="4" r="2.5"/><circle cx="20" cy="4" r="2.5"/><circle cx="4" cy="20" r="2.5"/><circle cx="20" cy="20" r="2.5"/></svg>
      </div>
      <h3>锡月无人机方案</h3>
      <p>2025 年全国大学生电赛无人机全栈方案，基于 STM32F405 飞控、地平线 RDK X5 上位机与 Nextion 触控地面站。</p>
      <div class="card-details">
        • STM32F405 飞控底层（BirdFlight V2.0：PID / ADRC / LQR / uCOS-III）<br>
        • 地平线 RDK X5 上位机（230400bps 高速串口通信 + 自启动服务）<br>
        • DFS 9×7 网格全覆盖自主巡航 + Dijkstra 动态实时绕障重规划<br>
        • T265 姿态解算 + OpenCV 目标识别与精准中心对准降落<br>
        • Nextion 串口触控屏地面站（蓝牙无线通信 + 状态语音播报）
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
      <div class="card-icon-box icon-pink">
        <svg class="card-svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>
      </div>
      <h3>3D 打印模型库</h3>
      <p>机器人结构件、无人机云台与传感器支架的 3D 打印模型全栈库（195+ 款精细模型）。</p>
      <div class="card-details">
        • 195+ 款精细模型（114 STL / 45 SolidWorks SLDPRT 源工程 / 36 拓竹 3MF）<br>
        • 覆盖无人机保护罩/缓震平台、双目云台、小车底盘及激光定高支架<br>
        • 自研 Python STL 批量 360° 旋转渲染与 GIF 动图生成引擎<br>
        • 站内 WebGL 3D 交互预览器（支持旋转/平移/缩放/底面平放）
      </div>
      <a href="{{ "/3d-viewer" | relative_url }}" class="card-link">在线 3D 预览</a>
      <a href="https://github.com/LONEFORME/3d-models" target="_blank" rel="noopener" class="card-link">查看项目</a>
    </div>
  </div>
</div>
