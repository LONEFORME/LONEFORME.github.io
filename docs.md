---
layout: default
title: 文档
layout_class: layout-wide
---

<h1>文档</h1>
<p class="page-subtitle">激光雷达 SLAM · 嵌入式边缘 AI · 多模态智能安防 · 快速上手指南</p>

<div class="card-grid">
  <div class="card">
    <div class="card-icon-box icon-green">
      <svg class="card-svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><circle cx="12" cy="12" r="2"/></svg>
    </div>
    <h3>宇树 L1 + FAST-LIO2（3D）</h3>
    <p>Unitree L1 3D 激光雷达 + FAST-LIO2 激光惯性里程计，基于 IKD-Tree 动态点云树与 6-DoF 紧耦合位姿估计。</p>
    <div class="card-tags">
      <span class="card-tag">3D LiDAR</span>
      <span class="card-tag">FAST-LIO2</span>
      <span class="card-tag">IMU紧耦合</span>
    </div>
    <div class="card-details">
      • 宇树 L1 点云驱动 + 9轴硬件 IMU 紧耦合融合<br>
      • FAST-LIO2 实时 6-DoF 里程计，3D PCD 地图输出<br>
      • 坐标零点校准 + 静止漂移抑制 + 自研一键启动脚本<br>
      • x86_64 / aarch64 双架构 SDK 支持与低延迟调优
    </div>
    <div class="card-footer-row">
      <a href="{{ "docs/unitree_l1" | relative_url }}" class="card-link">宇树建图指南</a>
      <span class="card-status">🔒 算法闭源</span>
    </div>
  </div>

  <div class="card">
    <div class="card-icon-box icon-blue">
      <svg class="card-svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4.9 19.1C1 15.2 1 8.8 4.9 4.9"/><path d="M7.8 16.2c-2.3-2.3-2.3-6.1 0-8.5"/><circle cx="12" cy="12" r="2"/><path d="M16.2 7.8c2.3 2.3 2.3 6.1 0 8.5"/><path d="M19.1 4.9C23 8.8 23 15.1 19.1 19"/></svg>
    </div>
    <h3>镭神 N10P + SLAM Toolbox（2D）</h3>
    <p>Leishen N10P 单线激光雷达 + SLAM Toolbox，2D 栅格地图建图，配套自研障碍物检测与位姿滤波。</p>
    <div class="card-tags">
      <span class="card-tag">2D LiDAR</span>
      <span class="card-tag">SLAM Toolbox</span>
      <span class="card-tag">栅格建图</span>
    </div>
    <div class="card-details">
      • UART 串口驱动深度调优，460800 高波特率点云稳定解析<br>
      • 2D 栅格地图实时构建 + 闭环回环检测 + 地图序列保存<br>
      • 自研空间聚类滤波 + 卡尔曼位姿预测 + 多帧时序确认<br>
      • 树莓派 4B / RDK X5 嵌入式端轻量化与低 CPU 占用调优
    </div>
    <div class="card-footer-row">
      <a href="{{ "docs/leishen_n10p" | relative_url }}" class="card-link">镭神建图指南</a>
      <span class="card-status">🔒 算法闭源</span>
    </div>
  </div>

  <div class="card">
    <div class="card-icon-box icon-cyan">
      <svg class="card-svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="16" height="16" x="4" y="4" rx="2"/><rect width="6" height="6" x="9" y="9" rx="1"/><path d="M15 2v2"/><path d="M15 20v2"/><path d="M2 15h2"/><path d="M2 9h2"/><path d="M20 15h2"/><path d="M20 9h2"/></svg>
    </div>
    <h3>嵌入式开发板配置参考与部署</h3>
    <p>7 款主流开发板从零到可用的一键自动化部署参考、ROS2 跨板网络通信与 AI Skill 多平台同步体系。</p>
    <div class="card-tags">
      <span class="card-tag">7款开发板</span>
      <span class="card-tag">Fast DDS 组网</span>
      <span class="card-tag">AI Skill v2.44</span>
    </div>
    <div class="card-details">
      • 覆盖树莓派 4B / N100 / A7A / A7Z / RDK X5 / K230 / RK3506<br>
      • A/B/C 三类板通用初始化与国内高速镜像源换源 SOP<br>
      • Fast DDS Discovery Server 跨板组网通信与 ROS2 互通<br>
      • 46 个自动化运维脚本库与端侧 AI 视觉部署参考手册
    </div>
    <div class="card-footer-row">
      <a href="{{ "docs/rpi4_deploy" | relative_url }}" class="card-link">树莓派实战指南</a>
      <span class="card-status">🔒 规范资产闭源</span>
    </div>
  </div>

  <div class="card">
    <div class="card-icon-box icon-purple">
      <svg class="card-svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
    </div>
    <h3>地瓜派 RDK X5 多模态智能安防系统</h3>
    <p>深度融合激光雷达空间测距、BPU 视觉推理、人脸/指纹双重生物识别与自适应齿条门禁的多模态边缘安防中枢。</p>
    <div class="card-tags">
      <span class="card-tag">地瓜派 RDK X5</span>
      <span class="card-tag">10 TOPS BPU</span>
      <span class="card-tag">雷达/人脸/指纹</span>
    </div>
    <div class="card-details">
      • 异构边缘计算：BPU 硬件加速 YOLOv8 目标检测，零 CPU 占用人/物分离<br>
      • 工业生物识别：InsightFace 512维人脸（Roll角校正+偏航角拦截）+ 半导体指纹<br>
      • 空间连续感知：镭神 N10P 跨0°闭环防区判定 + 3秒自适应背景差分 + 欧氏聚类<br>
      • 智能门禁中枢：360° 舵机毫秒微积分虚拟编码器（断电开度记忆）+ 车规声学破拆
    </div>
    <div class="card-footer-row">
      <a href="{{ "docs/security_system" | relative_url }}" class="card-link">系统设计方案</a>
      <span class="card-status">🔒 专有工程</span>
    </div>
  </div>
</div>
