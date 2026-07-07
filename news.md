---
layout: default
title: 热点新闻
---

# 📰 热点新闻速览

> AI 精选 · 来源可溯 · 每日更新

## 🚀 项目进展

### 2026-07-06 — Orbbec Astra Pro 相机驱动开发完成

为镭神 N10P SLAM 项目集成 Orbbec Astra Pro 相机：

- 创建 ROS2 包 `astra_pro_camera`，基于 Python + OpenCV 编写稳定驱动节点
- 相机以 ~26 FPS 稳定发布 `/image_raw` 和 `/camera_info` 话题
- 解决 OrbbecSDK_ROS2 v2.8.7 不支持老款 Astra Pro 的问题
- 替代方案 `ros-humble-usb-cam` 存在 V4L2_CAP_TIMEPERFRAME 内核 bug，已绕过
- 完成 udev 规则配置，确保相机权限正常
- 编写 launch 文件与 YAML 配置，支持参数化启动

### 2026-07-05 — 宇树雷达 L1 集成 SLAM

- 宇树雷达 L1 已正常启动并发布 /scan 话题
- 激光数据成功接入 SLAM 建图

---

<p class="news-updated">🕐 更新于 2026-07-07</p>
