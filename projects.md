---
layout: default
title: 项目
---

# 项目

## ROS2 激光雷达驱动

### 宇树 L1/L2/L3 系列

Unitree 激光雷达的 ROS2 封装驱动，支持 L1、L2、L3 系列。

- 点云发布与可视化
- IMU 数据融合
- 多平台支持（x86_64 / aarch64）
- 自动启动脚本

### 镭神 M10P / N10P

Leishen 单线激光雷达 ROS2 驱动，适用于室内导航与建图。

- UART 串口通信
- SLAM Toolbox 集成
- 障碍物检测节点

## SLAM 建图

### FAST-LIO2 + Unitree

基于 FAST-LIO2 框架的实时激光雷达-惯性里程计，适配宇树 L 系列。

- 实时 6-DoF 位姿估计
- 3D 点云地图构建
- IMU 紧耦合

### SLAM Toolbox + 镭神

基于 SLAM Toolbox 的 2D 激光 SLAM 方案。

- 2D 栅格地图构建
- Nav2 导航支持
- 地图保存与复用

## 工具

- **T265 自动 Boot** — Intel RealSense T265 追踪相机的固件加载脚本
