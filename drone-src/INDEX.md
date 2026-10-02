# 📚 电赛无人机全栈技术知识库 (Knowledge Base)

> **知识库定位**：本知识库为电赛无人机方向的结构化工程理论与实战经验集。  
> 彻底打通“**机械结构 $\rightarrow$ 硬件电路 $\rightarrow$ 底层控制律 $\rightarrow$ 机载定位避障 $\rightarrow$ 机器视觉 $\rightarrow$ 图论规划 $\rightarrow$ 合规地面交互**”的全流程链条。  
> 兼容 **Obsidian 双链网状笔记** 与 **标准 Markdown 索引**，可脱机浏览、全文检索或作为 AI 上下文底座。

---

## 🧭 六大核心技术模块 · 全景交互导航

<div class="nav-overview-chain">
  <div class="chain-node">🛠️ 机械结构</div>
  <div class="chain-arrow">➔</div>
  <div class="chain-node">⚡ 硬件底座</div>
  <div class="chain-arrow">➔</div>
  <div class="chain-node">🎛️ 飞控算法</div>
  <div class="chain-arrow">➔</div>
  <div class="chain-node">📍 自主定位</div>
  <div class="chain-arrow">➔</div>
  <div class="chain-node">👁️ 机器视觉</div>
  <div class="chain-arrow">➔</div>
  <div class="chain-node">🧭 路径决策</div>
  <div class="chain-arrow">➔</div>
  <div class="chain-node">📡 地面交互</div>
</div>

<div class="module-cards-grid">

  <!-- 模块 01 -->
  <a href="./01_硬件底座与电气规范" class="module-nav-card">
    <div class="module-card-header">
      <span class="module-badge">MODULE 01</span>
      <span class="module-arrow">深入研读 ➔</span>
    </div>
    <div class="module-card-title">⚡ 硬件底座与电气规范</div>
    <div class="module-card-body">
      <div class="module-item">
        <span class="item-label">核心攻坚：</span>
        <span class="item-text">动力推重比计算（2.0~2.5:1）、三级分级供电网络、STM32F4 硬件原理与引脚映射。</span>
      </div>
      <div class="module-item pain-point">
        <span class="item-label">🔥 关键突破：</span>
        <span class="item-text">彻底解决 T265 开机死锁与电源倒灌，固化 Linux udev 底层访问权限。</span>
      </div>
      <div class="module-item meta-target">
        <span class="item-label">📁 关联工程：</span>
        <span class="item-text"><code>05_凌霄资料包/06.原理图_PCB/</code> · <code>01_锡月/06_官方培训包/</code></span>
      </div>
    </div>
  </a>

  <!-- 模块 02 -->
  <a href="./02_飞控系统与控制算法" class="module-nav-card">
    <div class="module-card-header">
      <span class="module-badge">MODULE 02</span>
      <span class="module-arrow">深入研读 ➔</span>
    </div>
    <div class="module-card-title">🎛️ 飞控系统与控制算法</div>
    <div class="module-card-body">
      <div class="module-item">
        <span class="item-label">核心攻坚：</span>
        <span class="item-text">四旋翼欠驱动动力学解算、串级双闭环 PID（角速度+角度）、ADRC 自抗扰与 LQR 控制。</span>
      </div>
      <div class="module-item pain-point">
        <span class="item-label">🔥 关键突破：</span>
        <span class="item-text">攻克双飞控架构与通信隔离（锡月自研控制律 @ 230400 vs 凌霄 IMU 闭环 @ 460800）。</span>
      </div>
      <div class="module-item meta-target">
        <span class="item-label">📁 关联工程：</span>
        <span class="item-text"><code>01_锡月/01_飞控固件/BirdFlight_V2.0/</code> · <code>02_凌霄/自研系统/飞控源码/</code></span>
      </div>
    </div>
  </a>

  <!-- 模块 03 -->
  <a href="./03_室内自主定位与避障" class="module-nav-card">
    <div class="module-card-header">
      <span class="module-badge">MODULE 03</span>
      <span class="module-arrow">深入研读 ➔</span>
    </div>
    <div class="module-card-title">📍 室内自主定位与避障</div>
    <div class="module-card-body">
      <div class="module-item">
        <span class="item-label">核心攻坚：</span>
        <span class="item-text">T265 双目 VIO 姿态解算与 NED 坐标映射、T265 看门狗自愈、2D 镭神雷达免 ROS 直驱。</span>
      </div>
      <div class="module-item pain-point">
        <span class="item-label">🔥 关键突破：</span>
        <span class="item-text">免 ROS 超轻量化雷达直驱与细立柱快速锁定（解算延迟 &lt; 15ms，16 项 pytest 全绿）。</span>
      </div>
      <div class="module-item meta-target">
        <span class="item-label">📁 关联工程：</span>
        <span class="item-text"><code>03_激光雷达SLAM避障/</code> · <code>02_凌霄/自研系统/部署/watchdog/</code></span>
      </div>
    </div>
  </a>

  <!-- 模块 04 -->
  <a href="./04_机器视觉与目标检测" class="module-nav-card">
    <div class="module-card-header">
      <span class="module-badge">MODULE 04</span>
      <span class="module-arrow">深入研读 ➔</span>
    </div>
    <div class="module-card-title">👁️ 机器视觉与目标检测</div>
    <div class="module-card-body">
      <div class="module-item">
        <span class="item-label">核心攻坚：</span>
        <span class="item-text">赛场光照频闪抑制与自动曝光锁定、11 色自适应阈值分割、同心圆起降靶心严格几何判定。</span>
      </div>
      <div class="module-item pain-point">
        <span class="item-label">🔥 关键突破：</span>
        <span class="item-text">单目针孔相机结合 ToF 激光将像素偏差精准反投影为厘米级世界位移量。</span>
      </div>
      <div class="module-item meta-target">
        <span class="item-label">📁 关联工程：</span>
        <span class="item-text"><code>04_OpenCV视觉检测系统/</code> · <code>01_锡月/04_视觉识别/OpenVision.py</code></span>
      </div>
    </div>
  </a>

  <!-- 模块 05 -->
  <a href="./05_路径规划与自主决策" class="module-nav-card">
    <div class="module-card-header">
      <span class="module-badge">MODULE 05</span>
      <span class="module-arrow">深入研读 ➔</span>
    </div>
    <div class="module-card-title">🧭 路径规划与自主决策</div>
    <div class="module-card-body">
      <div class="module-item">
        <span class="item-label">核心攻坚：</span>
        <span class="item-text">赛场连续空间离散化为 63 单元格拓扑图、DFS 蛇形全覆盖遍历、Dijkstra 动态重规划。</span>
      </div>
      <div class="module-item pain-point">
        <span class="item-label">🔥 关键突破：</span>
        <span class="item-text">有限状态机（FSM）闭环流转，彻底解决机载端异步任务调度与防死锁保护。</span>
      </div>
      <div class="module-item meta-target">
        <span class="item-label">📁 关联工程：</span>
        <span class="item-text"><code>01_锡月/02_树莓派机载主控/自启动/</code>（<code>path_generator.py</code> 与 <code>A_fly_deal.py</code>）</span>
      </div>
    </div>
  </a>

  <!-- 模块 06 -->
  <a href="./06_合规交互与机械结构" class="module-nav-card">
    <div class="module-card-header">
      <span class="module-badge">MODULE 06</span>
      <span class="module-arrow">深入研读 ➔</span>
    </div>
    <div class="module-card-title">🛡️ 合规交互与机械结构</div>
    <div class="module-card-body">
      <div class="module-item">
        <span class="item-label">核心攻坚：</span>
        <span class="item-text">电赛严禁通用计算机红线应对、Nextion 串口触摸屏协议封包、蓝牙通信、语音报靶。</span>
      </div>
      <div class="module-item pain-point">
        <span class="item-label">🔥 关键突破：</span>
        <span class="item-text">45cm 严苛尺寸包络设计、全包覆安全防撞网、多款云台与传感器高刚性减震选型。</span>
      </div>
      <div class="module-item meta-target">
        <span class="item-label">📁 关联工程：</span>
        <span class="item-text"><code>01_锡月/03_地面站/</code> · <code>06_3D打印结构模型库/</code></span>
      </div>
    </div>
  </a>

</div>

<style>
/* 流程链视觉样式 */
.nav-overview-chain {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 8px;
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
  border-radius: 12px;
  padding: 14px 18px;
  margin: 18px 0 26px;
  font-size: 13.5px;
  font-weight: 600;
}
.chain-node {
  color: var(--vp-c-text-1);
}
.chain-arrow {
  color: var(--vp-c-brand-1);
  font-size: 14px;
}

/* 模块网格 */
.module-cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 18px;
  margin: 20px 0 32px;
}
@media (min-width: 960px) {
  .module-cards-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
@media (min-width: 1300px) {
  .module-cards-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

/* 模块导航卡片 */
.module-nav-card {
  display: flex;
  flex-direction: column;
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
  border-radius: 12px;
  padding: 20px;
  text-decoration: none !important;
  color: inherit !important;
  transition: all 0.25s ease;
  position: relative;
  overflow: hidden;
}
.module-nav-card:hover {
  transform: translateY(-3px);
  border-color: var(--vp-c-brand-1);
  box-shadow: 0 10px 24px rgba(0, 0, 0, 0.08);
}
.module-card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}
.module-badge {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.5px;
  padding: 2px 8px;
  border-radius: 6px;
  background: var(--vp-c-brand-soft);
  color: var(--vp-c-brand-1);
}
.module-arrow {
  font-size: 12.5px;
  font-weight: 600;
  color: var(--vp-c-brand-1);
  opacity: 0.85;
  transition: transform 0.2s ease;
}
.module-nav-card:hover .module-arrow {
  transform: translateX(3px);
  opacity: 1;
}
.module-card-title {
  margin: 0 0 12px !important;
  padding: 0 !important;
  font-size: 16px !important;
  font-weight: 700 !important;
  color: var(--vp-c-text-1) !important;
  border: none !important;
  line-height: 1.4 !important;
}
.module-card-body {
  display: flex;
  flex-direction: column;
  gap: 8px;
  font-size: 13px;
  line-height: 1.6;
  color: var(--vp-c-text-2);
}
.module-item {
  display: flex;
  flex-direction: column;
}
.item-label {
  font-weight: 600;
  color: var(--vp-c-text-1);
  margin-bottom: 2px;
}
.pain-point .item-label {
  color: #e06c75;
}
.meta-target {
  margin-top: 4px;
  font-size: 12px;
}
.meta-target code {
  font-size: 11.5px;
  padding: 2px 4px;
}
</style>

## 🎓 推荐梯次化研读顺序

1. **第 1 步 · 建立物理直觉**：
   * 读 **`01 硬件底座`** 与 **`06 合规交互与机械结构`**，搞清无人机推重比、分级供电电路、防炸机防护框以及为什么现场不能用笔记本电脑。
2. **第 2 步 · 吃透底层控制律**：
   * 读 **`02 飞控系统与控制算法`**，理解四旋翼是如何通过倾斜机身产生水平分力的，搞懂串级双闭环 PID 的数学公式与调参消震手法。
3. **第 3 步 · 攻克定位与视觉核心**：
   * 读 **`03 室内自主定位与避障`** 与 **`04 机器视觉与目标检测`**，牢记 T265 必须插黑色 USB 2.0 口的实测避坑铁律，掌握单目相机结合 ToF 激光将像素偏差反投影为米制位移的闭环算法。
4. **第 4 步 · 赛题自主通关大闭环**：
   * 读 **`05 路径规划与自主决策`**，学会如何将电赛场地转化为 63 格拓扑图，体验从输入禁飞区到 Dijkstra 毫秒级重规划并在地面触摸屏上实时刷新的完整实战闭环。
