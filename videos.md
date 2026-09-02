---
layout: default
title: 飞行演示
---

<div class="news-header-box">
  <div class="news-title-row">
    <div>
      <h1 class="news-main-title">🎬 无人机飞行演示</h1>
      <p class="news-main-desc">2025 电赛无人机项目实际飞行演示视频，包含二维码识别、火源检测、绕杆飞行与精准降落</p>
    </div>
    <div class="news-date-tag">
      <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="23 7 16 12 23 17 23 7"></polygon><rect width="15" height="11" x="1" y="6" rx="2" ry="2"></rect></svg>
      <span>4 段演示视频</span>
    </div>
  </div>
</div>

## 📹 视频列表

<div class="video-grid">

  <!-- 二维码识别 -->
  <div class="video-card">
    <div class="video-card-header">
      <h3>📱 二维码识别与降落</h3>
      <span class="video-badge">竖屏 · 32MB</span>
    </div>
    <div class="video-wrapper">
      <video controls preload="metadata" poster="">
        <source src="{{ "/assets/videos/二维码.mp4" | relative_url }}" type="video/mp4">
        您的浏览器不支持视频播放，请 <a href="{{ "/assets/videos/二维码.mp4" | relative_url }}">点击下载</a>。
      </video>
    </div>
    <p class="video-desc">无人机识别地面二维码并执行精准降落，展示视觉定位与自主降落能力。</p>
  </div>

  <!-- 火源检测 -->
  <div class="video-card">
    <div class="video-card-header">
      <h3>🔥 火源识别与处理</h3>
      <span class="video-badge">竖屏 · 11MB</span>
    </div>
    <div class="video-wrapper">
      <video controls preload="metadata" poster="">
        <source src="{{ "/assets/videos/火源.mp4" | relative_url }}" type="video/mp4">
        您的浏览器不支持视频播放，请 <a href="{{ "/assets/videos/火源.mp4" | relative_url }}">点击下载</a>。
      </video>
    </div>
    <p class="video-desc">无人机检测地面火源并执行相应处理动作，展示目标识别与任务执行能力。</p>
  </div>

  <!-- 绕杆飞行 -->
  <div class="video-card">
    <div class="video-card-header">
      <h3>🎯 绕杆飞行</h3>
      <span class="video-badge">横屏 · 9MB</span>
    </div>
    <div class="video-wrapper">
      <video controls preload="metadata" poster="">
        <source src="{{ "/assets/videos/绕杆.mp4" | relative_url }}" type="video/mp4">
        您的浏览器不支持视频播放，请 <a href="{{ "/assets/videos/绕杆.mp4" | relative_url }}">点击下载</a>。
      </video>
    </div>
    <p class="video-desc">无人机沿预设航点绕杆飞行，展示路径规划与稳定飞行控制能力。</p>
  </div>

  <!-- 精准降落 -->
  <div class="video-card">
    <div class="video-card-header">
      <h3>🛬 精准降落</h3>
      <span class="video-badge">横屏 · 10MB</span>
    </div>
    <div class="video-wrapper">
      <video controls preload="metadata" poster="">
        <source src="{{ "/assets/videos/降落.mp4" | relative_url }}" type="video/mp4">
        您的浏览器不支持视频播放，请 <a href="{{ "/assets/videos/降落.mp4" | relative_url }}">点击下载</a>。
      </video>
    </div>
    <p class="video-desc">无人机执行精准降落动作，展示高度控制与着陆稳定性。</p>
  </div>

</div>

## 📊 项目信息

| 项目 | 说明 |
|------|------|
| **赛事** | 2025 年全国大学生电子设计竞赛 |
| **飞控** | STM32F405 + BirdFlight V2.0 |
| **上位机** | Raspberry Pi 4B + Python 3 |
| **视觉** | OpenCV（形状/颜色/二维码检测） |
| **定位** | Intel RealSense T265（VIO） |
| **源码仓库** | [xiyue-drone](https://github.com/LONEFORME/xiyue-drone) |

> 💡 视频已压缩为 H.264 + AAC 格式，支持所有现代浏览器原生播放。原始视频总计 1.14GB，压缩后仅 62MB，压缩率 94.5%。

<style>
.video-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 24px;
  margin: 24px 0;
}
.video-card {
  background: var(--card-bg, #1a1a2e);
  border: 1px solid var(--border-color, #2a2a4a);
  border-radius: 12px;
  overflow: hidden;
  transition: transform 0.2s, box-shadow 0.2s;
}
.video-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0,0,0,0.3);
}
.video-card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 14px 16px;
  border-bottom: 1px solid var(--border-color, #2a2a4a);
}
.video-card-header h3 {
  margin: 0;
  font-size: 16px;
}
.video-badge {
  font-size: 12px;
  padding: 3px 10px;
  border-radius: 20px;
  background: var(--accent-bg, rgba(99,102,241,0.15));
  color: var(--accent-color, #818cf8);
  white-space: nowrap;
}
.video-wrapper {
  position: relative;
  width: 100%;
  background: #000;
}
.video-wrapper video {
  width: 100%;
  height: auto;
  display: block;
  max-height: 480px;
  object-fit: contain;
}
.video-desc {
  padding: 12px 16px 16px;
  margin: 0;
  font-size: 14px;
  color: var(--text-secondary, #9ca3af);
  line-height: 1.6;
}
@media (max-width: 640px) {
  .video-grid {
    grid-template-columns: 1fr;
    gap: 16px;
  }
}
</style>
