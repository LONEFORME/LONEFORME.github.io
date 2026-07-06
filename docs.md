---
layout: default
title: 文档
---

# 文档
<p class="page-subtitle">激光雷达 SLAM 方案 · 硬件驱动 · 快速上手指南</p>

<div class="card-grid">
  <div class="card">
    <div class="card-icon">📡</div>
    <h3>宇树 L1 + FAST-LIO2</h3>
    <p>实时激光雷达-惯性里程计建图方案，适用于室内外实时 3D 建图。</p>
    <div class="card-details">
      <strong>硬件：</strong>Unitree L1/L2/L3 激光雷达<br>
      <strong>软件：</strong>FAST-LIO2 ROS2 版
    </div>
    <a href="{{ "docs/unitree_l1" | relative_url }}" class="card-link">查看文档</a>
  </div>

  <div class="card">
    <div class="card-icon">🔭</div>
    <h3>镭神 N10P + SLAM Toolbox</h3>
    <p>2D 激光雷达 SLAM 方案，适用于室内导航与避障。</p>
    <div class="card-details">
      <strong>硬件：</strong>Leishen N10P/M10P 单线雷达<br>
      <strong>软件：</strong>SLAM Toolbox + Nav2
    </div>
    <a href="{{ "docs/leishen_n10p" | relative_url }}" class="card-link">查看文档</a>
  </div>

  <div class="card">
    <div class="card-icon">🫐</div>
    <h3>树莓派 4B 部署</h3>
    <p>将镭神 N10P + SLAM Toolbox 部署到树莓派 4B 的完整指南。</p>
    <div class="card-details">
      <strong>平台：</strong>Ubuntu 22.04 ARM64<br>
      <strong>优化：</strong>性能调参 · 无头模式 · 故障排查
    </div>
    <a href="{{ "docs/rpi4_deploy" | relative_url }}" class="card-link">查看指南</a>
  </div>
</div>
