---
layout: page
title: 演示稿库
layout_class: layout-wide
permalink: /slides/
---

<div class="hero">
  <div class="hero-badge">
    <svg class="hero-badge-svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
    <span>DeckKit · 交互式技术演示文稿</span>
  </div>
  <h1>演示稿库 · Slides</h1>
  <div class="tagline">浏览器原生全屏放映 · 键盘交互 · 嵌入式与机器人答辩汇报</div>
  <div class="hero-desc">脱离传统 PowerPoint 限制，基于现代 Web 动画与舞台渲染技术构建。支持键盘全屏翻页、高帧率动效、离线独立放映。</div>
</div>

<div class="section-title">
  <span class="section-icon-box">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="18" height="18" x="3" y="3" rx="2"/><path d="m9 8 6 4-6 4Z"/></svg>
  </span>
  <h2>精选演示文稿</h2>
</div>

<div class="card-grid">
  <!-- 演示稿 1：雷达安防系统项目介绍（最终版） -->
  <div class="card slide-deck-card">
    <div class="slide-deck-preview">
      <div class="slide-badge-top">旗舰方案 · 12 页</div>
      <div class="slide-mini-stage">
        <div class="slide-mini-title">基于激光雷达的远程安防监控系统</div>
        <div class="slide-mini-subtitle">多模态融合 · 已落地运行 · 项目全景介绍</div>
        <div class="slide-mini-tags">
          <span>激光雷达</span>
          <span>双模态生物识别</span>
          <span>BPU 加速</span>
        </div>
      </div>
    </div>
    <div class="card-body">
      <h3>基于激光雷达的远程安防监控系统 · 项目介绍（最终版）</h3>
      <p>以激光雷达为空间感知核心的多模态安防中枢：雷达防区算法、人脸/指纹双生物识别门禁、BPU 视觉检测、三级报警存证与 Web 远程监控，含实测运行指标。</p>
      <div class="card-tags">
        <span class="tag">全屏放映</span>
        <span class="tag">暗夜极客</span>
        <span class="tag">项目介绍</span>
      </div>
      <div class="slide-action-row">
        <a href="/slides/rdk_x5_security.html" target="_blank" class="card-link slide-play-btn">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
          立即在线放映 (全屏) ↗
        </a>
      </div>
    </div>
  </div>

  <!-- 演示稿 2：激光雷达 SLAM 项目介绍 -->
  <div class="card slide-deck-card">
    <div class="slide-deck-preview" style="background: linear-gradient(135deg, #0e1e38 0%, #162a45 100%);">
      <div class="slide-badge-top" style="background: rgba(0, 212, 255, 0.2); color: #00d4ff;">算法剖析 · 12 页</div>
      <div class="slide-mini-stage">
        <div class="slide-mini-title" style="color: #64b5f6;">3D 激光雷达 SLAM 与多传感器融合</div>
        <div class="slide-mini-subtitle">FAST-LIO 算法推演 · 驱动攻坚 · 已落地实测</div>
        <div class="slide-mini-tags">
          <span>FAST-LIO</span>
          <span>Point-LIO</span>
          <span>ROS2</span>
        </div>
      </div>
    </div>
    <div class="card-body">
      <h3>3D 激光雷达 SLAM 算法推演与工程落地</h3>
      <p>剖析 FAST-LIO / Point-LIO 状态估计原理与双算法互备；宇树 L1 ROS2 适配、双脑架构、T265 独立定位链与网页三维可视化，含实机参数调优与避坑清单。</p>
      <div class="card-tags">
        <span class="tag">算法剖析</span>
        <span class="tag">激光雷达</span>
        <span class="tag">点云建图</span>
      </div>
      <div class="slide-action-row">
        <a href="/slides/lidar_slam_nav.html" target="_blank" class="card-link slide-play-btn">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
          立即在线放映 (全屏) ↗
        </a>
      </div>
    </div>
  </div>

  <!-- 演示稿 3：2D 激光雷达避障与 SLAM -->
  <div class="card slide-deck-card">
    <div class="slide-deck-preview" style="background: linear-gradient(135deg, #0e1e38 0%, #162a45 100%);">
      <div class="slide-badge-top" style="background: rgba(0, 212, 255, 0.2); color: #00d4ff;">实战系统 · 11 页</div>
      <div class="slide-mini-stage">
        <div class="slide-mini-title" style="color: #64b5f6;">2D 激光雷达避障与 SLAM</div>
        <div class="slide-mini-subtitle">镭神 N10P · 世界系立柱追踪 · 迟滞回差避障</div>
        <div class="slide-mini-tags">
          <span>镭神 N10P</span>
          <span>世界系追踪</span>
          <span>迟滞回差</span>
        </div>
      </div>
    </div>
    <div class="card-body">
      <h3>2D 激光雷达避障与 SLAM · 无人机自主绕障全栈</h3>
      <p>电赛立柱穿越场景的实战避障系统：坐标系融合、世界系时序滑窗立柱追踪、迟滞回差状态机、免 ROS 直驱与 16 项 pytest 全量回归。</p>
      <div class="card-tags">
        <span class="tag">避障状态机</span>
        <span class="tag">镭神 N10P</span>
        <span class="tag">SLAM 建图</span>
      </div>
      <div class="slide-action-row">
        <a href="/slides/lidar_2d_nav.html" target="_blank" class="card-link slide-play-btn">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
          立即在线放映 (全屏) ↗
        </a>
      </div>
    </div>
  </div>
</div>
