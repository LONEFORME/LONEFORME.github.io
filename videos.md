---
layout: default
title: 飞行演示
---

<div class="news-header-box">
  <div class="news-title-row">
    <div>
      <h1 class="news-main-title">🎬 历年电赛飞行演示</h1>
      <p class="news-main-desc">历年全国大学生电子设计竞赛无人机实战任务录像 · 涵盖机载视觉定位、目标探测识别、空间航点规划与厘米级精准着陆</p>
    </div>
    <div class="news-date-tag">
      <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="23 7 16 12 23 17 23 7"></polygon><rect width="15" height="11" x="1" y="6" rx="2" ry="2"></rect></svg>
      <span>4 幕电赛演示 · 剧场影院模式</span>
    </div>
  </div>
</div>

<!-- 🎭 剧场影院模式主工作区 -->
<div class="theater-container">

  <!-- 左侧：主放映舞台 & 任务技术解析 -->
  <div class="theater-stage-col">
    <div class="theater-screen-card">
      <div class="theater-screen-ambient" id="theater-ambient"></div>
      <div class="theater-screen-box">
        <video id="main-player" controls preload="metadata" poster="{{ "/assets/images/videos/poster_qrcode.jpg" | relative_url }}">
          <source id="main-player-src" src="{{ "/assets/videos/二维码.mp4" | relative_url }}" type="video/mp4">
          您的浏览器暂不支持 HTML5 视频播放，请升级或更换现代浏览器。
        </video>
      </div>
    </div>

    <!-- 当前播放任务技术详情卡片 -->
    <div class="theater-detail-card">
      <div class="detail-header-row">
        <div>
          <div class="detail-badge-group" id="detail-badges">
            <span class="theater-chip chip-primary">📱 竖屏机载视角</span>
            <span class="theater-chip">⏱️ 04:02</span>
            <span class="theater-chip">⚡ 9.8 MB (FastStart)</span>
            <span class="theater-chip">OpenCV 视觉闭环</span>
          </div>
          <h2 class="detail-title" id="detail-title">📱 二维码识别与自主精准降落</h2>
        </div>
        <div class="detail-actions">
          <button class="theater-btn" onclick="toggleTheaterFullScreen()" title="全屏沉浸播放">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"></path></svg>
            <span>全屏放映</span>
          </button>
        </div>
      </div>

      <div class="detail-desc-box">
        <h4 class="detail-desc-label">💡 赛题任务与技术实现方案：</h4>
        <p class="detail-desc-text" id="detail-desc">
          无人机自主起飞后沿预设搜索航线巡航，机载下视摄像头采集地面画面。图像算法采用 OpenCV 进行实时畸变矫正、自适应二值化与透视变换，准确定位二维码几何中心并解析位姿误差。上位机通过高速串口将位移偏差传递至 STM32 飞控的 PID 控制环，实现机身平稳减速逼近并在靶标正中心执行精准垂直软着陆。
        </p>
      </div>

      <div class="detail-specs-grid">
        <div class="spec-mini-item">
          <span class="spec-label">核心算法</span>
          <span class="spec-val" id="detail-spec-algo">透视变换 / 位姿估计 / 闭环纠偏</span>
        </div>
        <div class="spec-mini-item">
          <span class="spec-label">视觉机载硬件</span>
          <span class="spec-val">地平线 RDK X5 (Python 3 + OpenCV)</span>
        </div>
        <div class="spec-mini-item">
          <span class="spec-label">姿态与飞控</span>
          <span class="spec-val">STM32F405 + BirdFlight V2.0</span>
        </div>
        <div class="spec-mini-item">
          <span class="spec-label">空间定位基准</span>
          <span class="spec-val" id="detail-spec-pos">机载下视光流 + 单目视觉解算</span>
        </div>
      </div>
    </div>
  </div>

  <!-- 右侧：演示任务选集列表 -->
  <div class="theater-playlist-col">
    <div class="playlist-header">
      <div class="playlist-title-wrap">
        <span class="playlist-title-icon">📑</span>
        <span class="playlist-title-text">电赛任务选集</span>
        <span class="playlist-count">4 幕全收录</span>
      </div>
      <label class="autoplay-toggle" title="当前视频播放完毕后自动放映下一幕">
        <input type="checkbox" id="autoplay-next-checkbox" checked>
        <span class="toggle-slider"></span>
        <span class="toggle-label">自动连播</span>
      </label>
    </div>

    <div class="playlist-items-wrapper">

      <!-- EP 01 -->
      <div class="playlist-card active" onclick="switchVideo(0)" data-index="0">
        <div class="playlist-thumb-box">
          <img src="{{ "/assets/images/videos/poster_qrcode.jpg" | relative_url }}" alt="二维码识别" class="playlist-thumb-img">
          <span class="playlist-duration-badge">04:02</span>
          <div class="playing-indicator">
            <span class="bar bar1"></span>
            <span class="bar bar2"></span>
            <span class="bar bar3"></span>
          </div>
        </div>
        <div class="playlist-card-content">
          <div class="playlist-meta-row">
            <span class="ep-num">EP 01</span>
            <span class="ep-tag tag-vertical">竖屏机载</span>
          </div>
          <h4 class="playlist-card-title">二维码识别与降落</h4>
          <p class="playlist-card-brief">自主搜索二维码靶标并闭环厘米级着陆</p>
        </div>
      </div>

      <!-- EP 02 -->
      <div class="playlist-card" onclick="switchVideo(1)" data-index="1">
        <div class="playlist-thumb-box">
          <img src="{{ "/assets/images/videos/poster_fire.jpg" | relative_url }}" alt="火源识别" class="playlist-thumb-img">
          <span class="playlist-duration-badge">01:30</span>
          <div class="playing-indicator">
            <span class="bar bar1"></span>
            <span class="bar bar2"></span>
            <span class="bar bar3"></span>
          </div>
        </div>
        <div class="playlist-card-content">
          <div class="playlist-meta-row">
            <span class="ep-num">EP 02</span>
            <span class="ep-tag tag-vertical">竖屏机载</span>
          </div>
          <h4 class="playlist-card-title">火源识别与处理动作</h4>
          <p class="playlist-card-brief">HSV 色彩特征提取与多任务状态机协同</p>
        </div>
      </div>

      <!-- EP 03 -->
      <div class="playlist-card" onclick="switchVideo(2)" data-index="2">
        <div class="playlist-thumb-box">
          <img src="{{ "/assets/images/videos/poster_pole.jpg" | relative_url }}" alt="绕杆飞行" class="playlist-thumb-img">
          <span class="playlist-duration-badge">02:13</span>
          <div class="playing-indicator">
            <span class="bar bar1"></span>
            <span class="bar bar2"></span>
            <span class="bar bar3"></span>
          </div>
        </div>
        <div class="playlist-card-content">
          <div class="playlist-meta-row">
            <span class="ep-num">EP 03</span>
            <span class="ep-tag tag-horizontal">横屏全景</span>
          </div>
          <h4 class="playlist-card-title">复杂多障碍绕杆巡航</h4>
          <p class="playlist-card-brief">空间三次样条轨迹平滑与抗地效姿态解耦</p>
        </div>
      </div>

      <!-- EP 04 -->
      <div class="playlist-card" onclick="switchVideo(3)" data-index="3">
        <div class="playlist-thumb-box">
          <img src="{{ "/assets/images/videos/poster_landing.jpg" | relative_url }}" alt="精准降落" class="playlist-thumb-img">
          <span class="playlist-duration-badge">01:12</span>
          <div class="playing-indicator">
            <span class="bar bar1"></span>
            <span class="bar bar2"></span>
            <span class="bar bar3"></span>
          </div>
        </div>
        <div class="playlist-card-content">
          <div class="playlist-meta-row">
            <span class="ep-num">EP 04</span>
            <span class="ep-tag tag-horizontal">横屏全景</span>
          </div>
          <h4 class="playlist-card-title">VIO 辅助室内高精着陆</h4>
          <p class="playlist-card-brief">RealSense T265 视觉惯导融合与柔性接地</p>
        </div>
      </div>

    </div>

    <!-- 底部电赛仓库快速入口 -->
    <div class="playlist-repo-footer">
      <div class="repo-tip-row">
        <span>🔗 源代码与硬件方案已开源</span>
      </div>
      <a href="https://github.com/LONEFORME/lingxiao-drone" target="_blank" rel="noopener" class="repo-action-btn">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
        <span>访问 lingxiao-drone 仓库</span>
        <span class="repo-arrow">→</span>
      </a>
    </div>

  </div>

</div>

<!-- 📊 电赛软硬件系统架构总览 -->
<div class="hardware-overview-card">
  <div class="overview-header">
    <span class="overview-icon">📊</span>
    <h3>电赛无人机系统软硬件拓扑与配置参数</h3>
  </div>
  
  <div class="overview-table-responsive">
    <table class="overview-table">
      <thead>
        <tr>
          <th>系统分层</th>
          <th>采用方案 / 核心芯片</th>
          <th>主频 & 算力 / 传感器规格</th>
          <th>在电赛任务中的核心职责</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>底层飞控系统</strong></td>
          <td><code>STM32F405RGT6</code> + BirdFlight V2.0</td>
          <td>168MHz Cortex-M4 / 双环 PID</td>
          <td>纳秒级姿态解算、电调 PWM 动力输出、故障紧急迫降保护</td>
        </tr>
        <tr>
          <td><strong>边缘上位机</strong></td>
          <td>地平线 <code>RDK X5</code> (ARM A55 + BPU)</td>
          <td>10 TOPS 算力 / Python 3 + OpenCV</td>
          <td>图像实时采集、靶标检测跟踪、透视矫正与高层航线决策</td>
        </tr>
        <tr>
          <td><strong>空间定位系统</strong></td>
          <td><code>Intel RealSense T265</code></td>
          <td>双目鱼眼 + BMI055 IMU 硬件融合</td>
          <td>在无 GPS 的复杂室内电赛场馆中提供毫米级 VIO 空间坐标</td>
        </tr>
        <tr>
          <td><strong>高度与避障测距</strong></td>
          <td>高频激光 <code>ToF</code> + 机载超声波</td>
          <td>量程 0.03m ~ 8m / 刷新率 50Hz</td>
          <td>地面高度精确锁存、防止接地回弹震荡与地效干扰</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="overview-footer-note">
    <span>💡 <strong>流式优化说明</strong>：全站视频均已开启 <code>FastStart</code>（将 MP4 索引头置顶到第 0 字节），并深度压缩为 H.264 + AAC。总码率降低 60%，无论在手机或电脑端，点击选集即可瞬间起播、无需漫长等待。</span>
  </div>
</div>

<script>
// 视频数据库配置
const videoList = [
  {
    title: "📱 二维码识别与自主精准降落",
    src: "{{ "/assets/videos/二维码.mp4" | relative_url }}",
    poster: "{{ "/assets/images/videos/poster_qrcode.jpg" | relative_url }}",
    badges: [
      { text: "📱 竖屏机载视角", cls: "chip-primary" },
      { text: "⏱️ 04:02", cls: "" },
      { text: "⚡ 9.8 MB (FastStart)", cls: "" },
      { text: "OpenCV 视觉闭环", cls: "" }
    ],
    desc: "无人机自主起飞后沿预设搜索航线巡航，机载下视摄像头采集地面画面。图像算法采用 OpenCV 进行实时畸变矫正、自适应二值化与透视变换，准确定位二维码几何中心并解析位姿误差。上位机通过高速串口将位移偏差传递至 STM32 飞控的 PID 控制环，实现机身平稳减速逼近并在靶标正中心执行精准垂直软着陆。",
    algo: "透视变换 / 位姿估计 / 闭环纠偏",
    pos: "机载下视光流 + 单目视觉解算"
  },
  {
    title: "🔥 火源目标识别与协同处理",
    src: "{{ "/assets/videos/火源.mp4" | relative_url }}",
    poster: "{{ "/assets/images/videos/poster_fire.jpg" | relative_url }}",
    badges: [
      { text: "🔥 竖屏机载视角", cls: "chip-primary" },
      { text: "⏱️ 01:30", cls: "" },
      { text: "⚡ 3.2 MB (FastStart)", cls: "" },
      { text: "HSV 阈值分割与状态机", cls: "" }
    ],
    desc: "针对赛题设定的火源标靶，机载边缘处理器通过 HSV 动态色彩空间过滤结合多重矩特征提取，在复杂光照背景下实现毫秒级火源轮廓锁定。任务调度器采用有限状态机（FSM）管理搜索、逼近、悬停与灭火抛投全流程，保证了动作执行的确定性与容错能力。",
    algo: "HSV 色彩分割 / 几何多矩融合 / 有限状态机调度",
    pos: "光流传感器 + 激光测距复合测高"
  },
  {
    title: "🎯 复杂多障碍绕杆连续巡航",
    src: "{{ "/assets/videos/绕杆.mp4" | relative_url }}",
    poster: "{{ "/assets/images/videos/poster_pole.jpg" | relative_url }}",
    badges: [
      { text: "🎯 横屏全景视角", cls: "chip-secondary" },
      { text: "⏱️ 02:13", cls: "" },
      { text: "⚡ 7.5 MB (FastStart)", cls: "" },
      { text: "三次样条平滑轨迹", cls: "" }
    ],
    desc: "无人机在室内电赛密集标杆场地中，根据预载的坐标拓扑在线解算三次样条曲线（Cubic Spline）。飞控算法在航行中实现自适应速度前瞻与偏航角解耦控制，在高速过弯时将向心加速度对姿态传感器的惯性冲击降到最低，平顺完成全场地连续障碍环绕。",
    algo: "三次样条插值 / 自适应速度前瞻 / 抗侧倾姿态解耦",
    pos: "RealSense T265 视觉惯性里程计 (VIO)"
  },
  {
    title: "🛬 VIO 辅助室内高精度柔性着陆",
    src: "{{ "/assets/videos/降落.mp4" | relative_url }}",
    poster: "{{ "/assets/images/videos/poster_landing.jpg" | relative_url }}",
    badges: [
      { text: "🛬 横屏全景视角", cls: "chip-secondary" },
      { text: "⏱️ 01:12", cls: "" },
      { text: "⚡ 5.7 MB (FastStart)", cls: "" },
      { text: "阻尼接地防反弹", cls: "" }
    ],
    desc: "在全封闭电赛室内场地，完全无外部卫星导航条件下，系统利用 Intel RealSense T265 硬件底层融合的双目视觉特征点与高频 IMU 数据，抑制悬停阶段的漂移量在毫米级别。配合底部高频 ToF 激光定高，在着陆阶段分段递减油门输出，彻底杜绝机身弹跳。",
    algo: "多传感器扩展卡尔曼滤波 (EKF) / 分段衰减着陆策略",
    pos: "Intel RealSense T265 (6自由度 VIO)"
  }
];

let currentIndex = 0;

function switchVideo(index, autoPlay = true) {
  if (index < 0 || index >= videoList.length) return;
  currentIndex = index;
  const data = videoList[index];

  const player = document.getElementById("main-player");
  const playerSrc = document.getElementById("main-player-src");
  const titleEl = document.getElementById("detail-title");
  const badgesEl = document.getElementById("detail-badges");
  const descEl = document.getElementById("detail-desc");
  const algoEl = document.getElementById("detail-spec-algo");
  const posEl = document.getElementById("detail-spec-pos");
  const ambientEl = document.getElementById("theater-ambient");

  // 1. 更新选集卡片高亮状态
  document.querySelectorAll(".playlist-card").forEach((card, i) => {
    if (i === index) {
      card.classList.add("active");
    } else {
      card.classList.remove("active");
    }
  });

  // 2. 更新主播放器源与海报
  player.pause();
  player.poster = data.poster;
  playerSrc.src = data.src;
  player.load();

  if (autoPlay) {
    const playPromise = player.play();
    if (playPromise !== undefined) {
      playPromise.catch(e => {
        // 浏览器 autoplay 策略处理：静默不报错
        console.log("Auto-play blocked or waiting user gesture");
      });
    }
  }

  // 3. 更新详情文本与标签
  if (titleEl) titleEl.innerText = data.title;
  if (descEl) descEl.innerText = data.desc;
  if (algoEl) algoEl.innerText = data.algo;
  if (posEl) posEl.innerText = data.pos;

  if (badgesEl) {
    let badgesHtml = "";
    data.badges.forEach(b => {
      badgesHtml += `<span class="theater-chip ${b.cls}">${b.text}</span>`;
    });
    badgesEl.innerHTML = badgesHtml;
  }

  // 4. 环境光与背景平滑自适应
  if (ambientEl) {
    ambientEl.style.backgroundImage = `url('${data.poster}')`;
  }
}

function toggleTheaterFullScreen() {
  const player = document.getElementById("main-player");
  if (!player) return;
  if (player.requestFullscreen) {
    player.requestFullscreen();
  } else if (player.webkitRequestFullscreen) {
    player.webkitRequestFullscreen();
  } else if (player.msRequestFullscreen) {
    player.msRequestFullscreen();
  }
}

// 监听自动连播事件
document.addEventListener("DOMContentLoaded", () => {
  const player = document.getElementById("main-player");
  const autoCheckbox = document.getElementById("autoplay-next-checkbox");

  if (player) {
    player.addEventListener("ended", () => {
      if (autoCheckbox && autoCheckbox.checked) {
        const nextIdx = (currentIndex + 1) % videoList.length;
        switchVideo(nextIdx, true);
      }
    });
  }

  // 初始化环境光底图
  const ambientEl = document.getElementById("theater-ambient");
  if (ambientEl && videoList[0]) {
    ambientEl.style.backgroundImage = `url('${videoList[0].poster}')`;
  }
});
</script>

<style>
/* ==========================================================================
   🎭 剧场影院模式专用响应式样式
   ========================================================================== */
.theater-container {
  display: grid;
  grid-template-columns: 1fr 340px;
  gap: 24px;
  margin: 20px 0 32px;
  align-items: start;
}

/* 舞台左侧列 */
.theater-stage-col {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

/* 播放大屏外框与氛围灯 */
.theater-screen-card {
  position: relative;
  background: #02050b;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md, 14px);
  overflow: hidden;
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.45);
}

.theater-screen-ambient {
  position: absolute;
  top: -20px;
  left: -20px;
  right: -20px;
  bottom: -20px;
  background-size: cover;
  background-position: center;
  filter: blur(48px) brightness(0.28) saturate(1.4);
  opacity: 0.65;
  transition: background-image 0.6s ease;
  pointer-events: none;
}

.theater-screen-box {
  position: relative;
  width: 100%;
  height: 520px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0, 0, 0, 0.65);
  backdrop-filter: blur(10px);
}

.theater-screen-box video {
  width: 100%;
  height: 100%;
  max-height: 520px;
  object-fit: contain;
  display: block;
  outline: none;
}

/* 播放器下方详情卡片 */
.theater-detail-card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md, 14px);
  padding: 22px 24px;
  backdrop-filter: blur(12px);
  box-shadow: var(--shadow-sm);
}

.detail-header-row {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 16px;
  margin-bottom: 16px;
  border-bottom: 1px solid var(--color-border);
  padding-bottom: 16px;
}

.detail-badge-group {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 8px;
}

.theater-chip {
  display: inline-flex;
  align-items: center;
  font-size: 11px;
  font-weight: 600;
  padding: 3px 10px;
  border-radius: 20px;
  background: rgba(127, 127, 127, 0.12);
  color: var(--color-heading);
  border: 1px solid var(--color-border);
}

.theater-chip.chip-primary {
  background: var(--color-primary-dim);
  color: var(--color-primary);
  border-color: rgba(0, 255, 136, 0.3);
}

.theater-chip.chip-secondary {
  background: var(--color-secondary-dim);
  color: var(--color-secondary);
  border-color: rgba(0, 212, 255, 0.3);
}

.detail-title {
  margin: 0;
  font-size: 20px;
  font-weight: 700;
  color: var(--color-heading);
}

.theater-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 8px 14px;
  border-radius: 8px;
  background: var(--color-surface-hover);
  color: var(--color-heading);
  border: 1px solid var(--color-border);
  font-size: 13px;
  font-weight: 500;
  cursor: pointer;
  transition: var(--transition);
}

.theater-btn:hover {
  background: var(--color-primary-dim);
  color: var(--color-primary);
  border-color: var(--color-primary);
  transform: translateY(-1px);
}

.detail-desc-box {
  margin-bottom: 18px;
}

.detail-desc-label {
  margin: 0 0 6px;
  font-size: 13px;
  font-weight: 600;
  color: var(--color-heading);
}

.detail-desc-text {
  margin: 0;
  font-size: 14px;
  line-height: 1.7;
  color: var(--color-body);
}

.detail-specs-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
  background: rgba(127, 127, 127, 0.05);
  border: 1px solid var(--color-border);
  border-radius: 10px;
  padding: 14px 16px;
}

.spec-mini-item {
  display: flex;
  flex-direction: column;
  gap: 3px;
}

.spec-label {
  font-size: 11px;
  color: var(--color-muted);
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.spec-val {
  font-size: 13px;
  font-weight: 600;
  color: var(--color-heading);
}

/* 右侧选集控制台 */
.theater-playlist-col {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md, 14px);
  padding: 18px 16px;
  backdrop-filter: blur(12px);
  box-shadow: var(--shadow-sm);
  display: flex;
  flex-direction: column;
}

.playlist-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-bottom: 14px;
  margin-bottom: 14px;
  border-bottom: 1px solid var(--color-border);
}

.playlist-title-wrap {
  display: flex;
  align-items: center;
  gap: 6px;
}

.playlist-title-icon {
  font-size: 16px;
}

.playlist-title-text {
  font-size: 15px;
  font-weight: 700;
  color: var(--color-heading);
}

.playlist-count {
  font-size: 11px;
  padding: 2px 7px;
  border-radius: 10px;
  background: rgba(127, 127, 127, 0.15);
  color: var(--color-muted);
}

/* 连播开关 */
.autoplay-toggle {
  display: flex;
  align-items: center;
  gap: 6px;
  cursor: pointer;
  user-select: none;
}

.autoplay-toggle input {
  display: none;
}

.toggle-slider {
  position: relative;
  width: 32px;
  height: 18px;
  background: rgba(127, 127, 127, 0.3);
  border-radius: 20px;
  transition: 0.25s;
}

.toggle-slider:before {
  content: "";
  position: absolute;
  width: 14px;
  height: 14px;
  left: 2px;
  top: 2px;
  background: #fff;
  border-radius: 50%;
  transition: 0.25s;
}

.autoplay-toggle input:checked + .toggle-slider {
  background: var(--color-primary);
}

.autoplay-toggle input:checked + .toggle-slider:before {
  transform: translateX(14px);
}

.toggle-label {
  font-size: 12px;
  color: var(--color-body);
}

/* 选集列表包装区 */
.playlist-items-wrapper {
  display: flex;
  flex-direction: column;
  gap: 12px;
  flex: 1;
}

/* 单个选集卡片 */
.playlist-card {
  display: flex;
  gap: 12px;
  padding: 10px;
  border-radius: 10px;
  background: var(--color-surface-hover);
  border: 1px solid transparent;
  cursor: pointer;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
}

.playlist-card:hover {
  background: rgba(255, 255, 255, 0.08);
  border-color: rgba(255, 255, 255, 0.15);
  transform: translateX(2px);
}

.playlist-card.active {
  background: var(--color-primary-dim);
  border-color: rgba(0, 255, 136, 0.45);
  box-shadow: 0 4px 16px rgba(0, 255, 136, 0.12);
}

/* 缩略图 */
.playlist-thumb-box {
  position: relative;
  width: 96px;
  height: 64px;
  border-radius: 6px;
  overflow: hidden;
  background: #000;
  flex-shrink: 0;
}

.playlist-thumb-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s;
}

.playlist-card:hover .playlist-thumb-img {
  transform: scale(1.05);
}

.playlist-duration-badge {
  position: absolute;
  bottom: 3px;
  right: 4px;
  font-size: 10px;
  font-weight: 600;
  padding: 1px 4px;
  border-radius: 3px;
  background: rgba(0, 0, 0, 0.75);
  color: #fff;
}

/* 正在播放动态跳动音量条 */
.playing-indicator {
  display: none;
  position: absolute;
  top: 5px;
  left: 5px;
  background: rgba(0, 0, 0, 0.7);
  padding: 3px 5px;
  border-radius: 4px;
  align-items: flex-end;
  gap: 2px;
  height: 16px;
}

.playlist-card.active .playing-indicator {
  display: flex;
}

.playing-indicator .bar {
  width: 2px;
  background: var(--color-primary);
  border-radius: 1px;
  animation: barBounce 0.8s infinite ease-in-out alternate;
}

.playing-indicator .bar1 { height: 6px; animation-delay: 0.1s; }
.playing-indicator .bar2 { height: 12px; animation-delay: 0.3s; }
.playing-indicator .bar3 { height: 8px; animation-delay: 0.2s; }

@keyframes barBounce {
  0% { height: 3px; }
  100% { height: 12px; }
}

/* 卡片文本内容 */
.playlist-card-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  min-width: 0;
  flex: 1;
}

.playlist-meta-row {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 4px;
}

.ep-num {
  font-size: 10px;
  font-weight: 700;
  color: var(--color-primary);
  letter-spacing: 0.5px;
}

.ep-tag {
  font-size: 9px;
  padding: 1px 5px;
  border-radius: 3px;
  font-weight: 500;
}

.ep-tag.tag-vertical {
  background: rgba(99, 102, 241, 0.2);
  color: #a5b4fc;
}

.ep-tag.tag-horizontal {
  background: rgba(14, 165, 233, 0.2);
  color: #7dd3fc;
}

.playlist-card-title {
  margin: 0 0 4px;
  font-size: 13px;
  font-weight: 600;
  color: var(--color-heading);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.playlist-card.active .playlist-card-title {
  color: var(--color-primary);
}

.playlist-card-brief {
  margin: 0;
  font-size: 11px;
  color: var(--color-muted);
  line-height: 1.4;
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

/* 选集底部仓库入口 */
.playlist-repo-footer {
  margin-top: 18px;
  padding-top: 14px;
  border-top: 1px solid var(--color-border);
}

.repo-tip-row {
  font-size: 11px;
  color: var(--color-muted);
  margin-bottom: 8px;
}

.repo-action-btn {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  padding: 9px 12px;
  background: var(--color-surface-hover);
  border: 1px solid var(--color-border);
  border-radius: 8px;
  color: var(--color-heading);
  text-decoration: none;
  font-size: 12px;
  font-weight: 600;
  transition: var(--transition);
}

.repo-action-btn:hover {
  background: var(--color-primary-dim);
  border-color: var(--color-primary);
  color: var(--color-primary);
  transform: translateY(-1px);
}

.repo-arrow {
  font-size: 14px;
  transition: transform 0.2s;
}

.repo-action-btn:hover .repo-arrow {
  transform: translateX(3px);
}

/* ==========================================================================
   📊 硬件架构与参数对比表格
   ========================================================================== */
.hardware-overview-card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md, 14px);
  padding: 24px;
  margin-top: 24px;
  box-shadow: var(--shadow-sm);
}

.overview-header {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 16px;
}

.overview-header h3 {
  margin: 0;
  font-size: 17px;
  font-weight: 700;
  color: var(--color-heading);
}

.overview-icon {
  font-size: 20px;
}

.overview-table-responsive {
  width: 100%;
  overflow-x: auto;
}

.overview-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 13px;
  text-align: left;
}

.overview-table th {
  padding: 12px 14px;
  background: rgba(127, 127, 127, 0.08);
  color: var(--color-heading);
  font-weight: 600;
  border-bottom: 2px solid var(--color-border);
  white-space: nowrap;
}

.overview-table td {
  padding: 12px 14px;
  border-bottom: 1px solid var(--color-border);
  color: var(--color-body);
  line-height: 1.5;
}

.overview-table tr:hover td {
  background: rgba(127, 127, 127, 0.04);
}

.overview-table code {
  font-family: var(--font-mono);
  color: var(--color-primary);
  background: var(--color-code-bg);
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 12px;
}

.overview-footer-note {
  margin-top: 16px;
  padding: 12px 16px;
  border-radius: 8px;
  background: rgba(0, 255, 136, 0.04);
  border-left: 3px solid var(--color-primary);
  font-size: 13px;
  color: var(--color-body);
  line-height: 1.6;
}

/* ==========================================================================
   📱 响应式断点控制
   ========================================================================== */
@media (max-width: 1024px) {
  .theater-container {
    grid-template-columns: 1fr;
    gap: 20px;
  }
  .theater-screen-box {
    height: 440px;
  }
}

@media (max-width: 640px) {
  .theater-screen-box {
    height: 280px;
  }
  .detail-specs-grid {
    grid-template-columns: 1fr;
  }
  .detail-header-row {
    flex-direction: column;
  }
  .playlist-card {
    gap: 10px;
    padding: 8px;
  }
  .playlist-thumb-box {
    width: 80px;
    height: 52px;
  }
}
</style>
