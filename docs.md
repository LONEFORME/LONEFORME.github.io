---
layout: default
title: 文档
---

<h1>文档</h1>
<p class="page-subtitle">激光雷达 SLAM 方案 · 硬件驱动 · 快速上手指南</p>

<div class="card-grid">
  <div class="card">
    <div class="card-icon-box" style="--icon-color: #00ff88; --icon-glow: rgba(0,255,136,0.25);">
      <svg class="card-svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><circle cx="12" cy="12" r="2"/></svg>
    </div>
    <h3>宇树 L1 + FAST-LIO2</h3>
    <p>实时激光雷达-惯性里程计建图方案，适用于室内外实时 3D 建图。</p>
    <div class="card-details">
      <strong>硬件：</strong>Unitree L1 激光雷达<br>
      <strong>软件：</strong>FAST-LIO2 ROS2 版
    </div>
    <a href="{{ "docs/unitree_l1" | relative_url }}" class="card-link">查看文档</a>
  </div>

  <div class="card">
    <div class="card-icon-box" style="--icon-color: #00d4ff; --icon-glow: rgba(0,212,255,0.25);">
      <svg class="card-svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4.9 19.1C1 15.2 1 8.8 4.9 4.9"/><path d="M7.8 16.2c-2.3-2.3-2.3-6.1 0-8.5"/><circle cx="12" cy="12" r="2"/><path d="M16.2 7.8c2.3 2.3 2.3 6.1 0 8.5"/><path d="M19.1 4.9C23 8.8 23 15.1 19.1 19"/></svg>
    </div>
    <h3>镭神 N10P + SLAM Toolbox</h3>
    <p>2D 激光雷达 SLAM 方案，适用于室内导航与避障。</p>
    <div class="card-details">
      <strong>硬件：</strong>Leishen N10P 单线雷达<br>
      <strong>软件：</strong>SLAM Toolbox
    </div>
    <a href="{{ "docs/leishen_n10p" | relative_url }}" class="card-link">查看文档</a>
  </div>

  <div class="card">
    <div class="card-icon-box" style="--icon-color: #06b6d4; --icon-glow: rgba(6,182,212,0.25);">
      <svg class="card-svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="16" height="16" x="4" y="4" rx="2"/><rect width="6" height="6" x="9" y="9" rx="1"/><path d="M15 2v2"/><path d="M15 20v2"/><path d="M2 15h2"/><path d="M2 9h2"/><path d="M20 15h2"/><path d="M20 9h2"/></svg>
    </div>
    <h3>嵌入式开发板配置参考与部署</h3>
    <p>覆盖 7 款主流开发板的通用配置参考手册、一键自动化部署脚本与 AI Skill 资产库。</p>
    <div class="card-details">
      <strong>覆盖：</strong>树莓派4B / N100 / A7A / A7Z / RDK X5 / K230 / RK3506<br>
      <strong>核心：</strong>A/B/C 分类体系 · Fast DDS 组网 · 46个跨板运维脚本 · AI Skill v2.43
    </div>
    <a href="https://github.com/LONEFORME/embedded-board-reference" target="_blank" rel="noopener" class="card-link">GitHub 仓库</a>
    <a href="{{ "docs/rpi4_deploy" | relative_url }}" class="card-link">树莓派指南</a>
  </div>
</div>
