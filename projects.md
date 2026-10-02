---
layout: default
title: 项目
---

<h1>项目</h1>
<p class="page-subtitle">多模态智能安防 · ROS2 驱动 · SLAM 建图 · 计算机视觉 · 无人机 · 工具脚本</p>

<div class="project-group">
  <div class="section-title">
    <span class="section-icon-box">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
    </span>
    <div class="filter-bar" id="project-filter"></div>

<h2>地瓜派 RDK X5 · 多模态智能空间安防系统</h2>
  </div>
  <p class="group-desc">基于地平线 8 核 A55 边缘计算平台与 10 TOPS BPU 的软硬件一体化安防中枢，深度融合激光雷达空间感知、InsightFace 工业级人脸识别、半导体指纹与自适应齿条门禁。</p>

  <div class="card-grid">
    <div class="card" data-tags="安防 雷达 嵌入式">
      <div class="card-icon-box icon-purple">
        <svg class="card-svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
      </div>
      <h3>多模态边缘感知与 AI 推理中枢</h3>
      <p>BPU 硬件加速视觉推理、InsightFace 姿态校正人脸识别与激光雷达空间点云聚类决策引擎。</p>
      <div class="card-details">
        • 10 TOPS BPU 硬件加速 YOLOv8 NV12 推理（15~25ms），零 CPU 负荷实时人/物解耦<br>
        • InsightFace SCRFD + ArcFace 512维人脸：双眼 Roll 旋转校正 + 归一化 Yaw 偏航角过滤（≤35°侧脸拦截）<br>
        • 镭神 N10P 跨 0° 闭环防区几何判定 + 3秒自适应背景差分 + 欧氏聚类过滤噪声<br>
        • 有限状态机（FSM）三级威胁仲裁：MONITOR 监控 → WARN 预警 → ALARM 告警
      </div>
      <div class="card-footer-row">
        <a href="{{ "docs/security_system" | relative_url }}" class="card-link">技术方案设计</a>
        <span class="card-status">🔒 专有工程</span>
      </div>
    </div>

    <div class="card" data-tags="安防 雷达 嵌入式">
      <div class="card-icon-box icon-orange">
        <svg class="card-svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2"/><path d="M7 7h10"/><path d="M7 12h10"/><path d="M7 17h10"/></svg>
      </div>
      <h3>智能物理执行联动与态势大屏</h3>
      <p>ML-FPM007 半导体指纹模组、360° 伺服舵机自适应齿条门禁、车规声学破拆感知与 Web 态势大屏。</p>
      <div class="card-details">
        • ML-FPM007 面阵半导体指纹：UART 小端序 LE 驱动 + 3次按压采集合成 + Pin 11 触控中断唤醒<br>
        • 360° 连续旋转伺服舵机门禁：毫秒微积分虚拟绝对编码器 + 残余时间动态补偿 + 断电记忆开度持久化<br>
        • TI ADS1115 16位差分声学破拆检测（撬锁冲击波响应≤30ms）+ AHT10 微气象温湿度火警联动<br>
        • FastAPI + 10Hz WebSocket 全双工大屏，双路 720P MJPEG 视频推流 + FIFO 50张自动抓拍相册
      </div>
      <div class="card-footer-row">
        <a href="{{ "docs/security_system" | relative_url }}" class="card-link">技术方案设计</a>
        <span class="card-status">🔒 专有工程</span>
      </div>
    </div>
  </div>
</div>

<div class="project-group">
  <div class="section-title">
    <span class="section-icon-box">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><circle cx="12" cy="12" r="2"/></svg>
    </span>
    <h2>N100 · ROS2 激光雷达 SLAM 工作空间</h2>
  </div>
  <p class="group-desc">整合宇树 L1（3D）与镭神 N10P（2D）双雷达，配套 FAST-LIO2 与 SLAM Toolbox 双建图方案，含自研障碍物检测与位姿优化节点，即拿即用的机器人感知与导航参考实现。</p>

  <div class="card-grid">
    <div class="card" data-tags="雷达SLAM 无人机">
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
      <div class="card-footer-row">
        <a href="{{ "docs/unitree_l1" | relative_url }}" class="card-link">查看文档</a>
        <span class="card-status">🔒 算法闭源</span>
      </div>
    </div>

    <div class="card" data-tags="雷达SLAM 无人机">
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
      <div class="card-footer-row">
        <a href="{{ "docs/leishen_n10p" | relative_url }}" class="card-link">查看文档</a>
        <span class="card-status">🔒 算法闭源</span>
      </div>
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
  <p class="group-desc">覆盖 7 款主流开发板的通用配置参考、A/B/C 分类部署、Fast DDS Discovery Server 多机跨网段通信与 AI Skill 资产库（v2.44）。</p>

  <div class="card-grid">
    <div class="card" data-tags="嵌入式">
      <div class="card-icon-box icon-cyan">
        <svg class="card-svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="16" height="16" x="4" y="4" rx="2"/><rect width="6" height="6" x="9" y="9" rx="1"/><path d="M15 2v2"/><path d="M15 20v2"/><path d="M2 15h2"/><path d="M2 9h2"/><path d="M20 15h2"/><path d="M20 9h2"/><path d="M9 21v1"/><path d="M9 2v1"/></svg>
      </div>
      <h3>嵌入式开发板配置参考与 AI 资产库</h3>
      <p>7 款主流开发板从零到可用的一键自动化部署参考、ROS2 跨板网络通信与 AI Skill 多平台同步体系。</p>
      <div class="card-details">
        • A/B/C 三类板精准分类（Ubuntu裸装 / Debian+LXC / 边缘AI与串口）<br>
        • Fast DDS Discovery Server 中枢组网（A7Z:11811 打通跨设备互通）<br>
        • 46 个跨板自动化运维脚本库 + YOLOv8 边缘视觉实时检测<br>
        • AI Skill 唯一真源（v2.44），支持 Codex / DeepSeek / WorkBuddy / Gemini
      </div>
      <div class="card-footer-row">
        <a href="{{ "docs/rpi4_deploy" | relative_url }}" class="card-link">树莓派实战指南</a>
        <span class="card-status">🔒 内部规范资产</span>
      </div>
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
    <div class="card" data-tags="视觉">
      <div class="card-icon-box icon-purple">
        <svg class="card-svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z"/><circle cx="12" cy="12" r="3"/><path d="M12 9v6"/><path d="M9 12h6"/></svg>
      </div>
      <h3>OpenCV 综合视觉识别系统</h3>
      <p>基于 OpenCV 的综合计算机视觉识别系统，支持 11 种颜色自适应检测、几何轮廓分析与实心/空心圆分类。</p>
      <div class="card-details">
        • 11 种颜色 HSV/BGR 空间自适应精准识别<br>
        • 几何轮廓形状分类（三角形、矩形、五边形、多边形）<br>
        • 数学圆形度公式（4πA/P²）区分实心圆与空心圆环<br>
        • 双线程并发架构（采集线程 + 预处理线程，帧锁保证线程安全）
      </div>
      <a href="https://github.com/LONEFORME/opencv-vision-system" target="_blank" rel="noopener" class="card-link">查看项目</a>
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
    <div class="card" id="lingxiao">
      <div class="card-icon-box icon-green">
        <svg class="card-svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20M2 12h20"/><circle cx="12" cy="12" r="4"/><circle cx="4" cy="4" r="2.5"/><circle cx="20" cy="4" r="2.5"/><circle cx="4" cy="20" r="2.5"/><circle cx="20" cy="20" r="2.5"/></svg>
      </div>
      <h3>凌霄飞控无人机方案</h3>
      <p>匿名凌霄（ANO_LX）全栈工程与自研空地协同系统：官方基线、协议 V7、2026-D 双任务实飞验证（伴飞抛投 / 移动平台动态降落）、机载雷达感知与历年电赛参考。</p>
      <div class="card-details">
        • 匿名凌霄官方基线源码（STM32F407 / MSP432 / TM4C123）+ 通信协议 V7 与 IMU 减震固件<br>
        • 自研空地协同大闭环（2026-D 实飞验证：伴飞抛投 + 移动平台动态降落）<br>
        • 机载扩展：镭神 N10P 雷达感知 / T265 看门狗自愈 / K230 边缘视觉端侧 AI<br>
        • 历年参考（2022-HUST / 2024-D / UAV-2023）+ 4 段实飞演示 + 目录中文化
      </div>
      <div class="card-footer-row">
        <a href="{{ "/videos" | relative_url }}" class="card-link">飞行演示</a>
        <a href="https://github.com/LONEFORME/lingxiao-drone" target="_blank" rel="noopener" class="card-link">GitHub</a>
      </div>
    </div>

    <div class="card" id="xiyue">
      <div class="card-icon-box icon-orange">
        <svg class="card-svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20M2 12h20"/><circle cx="12" cy="12" r="4"/><circle cx="4" cy="4" r="2.5"/><circle cx="20" cy="4" r="2.5"/><circle cx="4" cy="20" r="2.5"/><circle cx="20" cy="20" r="2.5"/></svg>
      </div>
      <h3>锡月无人机方案</h3>
      <p>2025 年全国大学生电赛无人机全栈方案，基于 STM32F405 飞控、树莓派上位机与 Nextion 触控地面站。</p>
      <div class="card-details">
        • STM32F405 飞控底层（BirdFlight V2.0：PID / ADRC / LQR / uCOS-III）<br>
        • 树莓派上位机（230400bps 高速串口通信 + 自启动服务）<br>
        • DFS 9×7 网格全覆盖自主巡航 + Dijkstra 动态实时绕障重规划<br>
        • T265 姿态解算 + OpenCV 目标识别与精准中心对准降落<br>
        • Nextion 串口触控屏地面站（蓝牙无线通信 + 状态语音播报）
      </div>
      <div class="card-footer-row">
        <a href="{{ "/videos" | relative_url }}" class="card-link">飞行演示</a>
        <span class="card-status">🔒 飞控方案闭源</span>
      </div>
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
    <div class="card" data-tags="3D打印">
      <div class="card-icon-box icon-pink">
        <svg class="card-svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>
      </div>
      <h3>3D 打印模型库</h3>
      <p>机器人结构件、无人机云台与传感器支架的 3D 打印模型全栈库（195+ 款精细模型）。</p>
      <div class="card-details">
        • 195+ 款精细模型（114 STL / 45 SolidWorks SLDPRT 源工程 / 36 拓竹 3MF）<br>
        • 站内在线预览收录 74 款 STL（体积与带宽考量，精选常用件）<br>
        • 覆盖无人机保护罩/缓震平台、双目云台、小车底盘及激光定高支架<br>
        • 自研 Python STL 批量 360° 旋转渲染与 GIF 动图生成引擎<br>
        • 站内 WebGL 3D 交互预览器（支持旋转/平移/缩放/底面平放）
      </div>
      <a href="{{ "/3d-viewer" | relative_url }}" class="card-link">在线 3D 预览</a>
    </div>
  </div>
</div>