---
title: "机器人运动学与动力学：外力计算与力平衡方程"
author: "Zane Zhang"
publish_time: "1970-01-01 08:33:45"
url: "https://mp.weixin.qq.com/s/7YZwsuZeHs0c4SPT6gQSnw"
biz: "MzkxNzY1NTY0MQ=="
image_count: 3
---

# 机器人运动学与动力学：外力计算与力平衡方程

1. 引言

在掌握了单个刚体的力平衡方程之后，我们面对的下一个挑战是如何将其应用于复杂的多刚体系统。对于串联或并联机器人而言，动力学建模的两大核心任务是：精确计算各部件受到的所有外力，以及构建系统级的力平衡方程组。

本文将从实际应用出发，详细探讨重力、约束力及环境接触力的计算方法，并最终推导出一个能够统一解决动力学正解与逆解问题的通用线性模型。该模型具有极强的普适性，能够描述任意拓扑结构的机器人系统。

![image](https://mmbiz.qpic.cn/mmbiz_png/2YFlzKTpOib962ficMm3trlGicQeuibDpcoWn1tic9ajicPJMbhiaeAZ14H0Wt0wq29nl5zIRr1FDrmQ7IMTyT2TEf7bQ/640?wx_fmt=png&from=appmsg)
图1：多体系统的约束动力学方程组构建
2. 外力的分类与计算

对于系统中的任意一个杆件i，其所受的合外力旋量Fnet通常由以下三部分组成：

2.1 重力 (Gravity)

重力是作用在刚体质心上的体积力。在惯性坐标系中，重力加速度旋量g通常表示为[0, 0, 0, 0, 0, -9.8]T（假设Z轴垂直向上）。则杆件受到的重力旋量为：

FG= I · g

注意，由于空间惯量矩阵I是随杆件位姿变化的，因此重力旋量FG在不同构型下也需实时计算。

2.2 约束力 (Constraint Force)

关节约束力是连接杆件的物理接口产生的反作用力。对于一个具有k维自由度的关节，其约束力位于一个(6-k)维的子空间中。我们可以用单位约束力矩阵C和约束力坐标向量η来表达：

FC= C · η

这里η是待求的未知量，其维数取决于约束的类型。

3. 约束力矩阵的构建

在多体系统中，我们可以将所有杆件和关节的约束信息整合为一个系统级的大矩阵Csys。

列：
对应系统中的每一个关节约束。

行：
对应系统中的每一个杆件。

该矩阵具有稀疏性，仅在杆件与其相连关节对应的位置上有非零块。通过这种方式，我们建立起了从局部关节约束力到全局杆件受力的映射关系。

![image](https://mmbiz.qpic.cn/mmbiz_jpg/2YFlzKTpOib962ficMm3trlGicQeuibDpcoWWppyoaEEbqAOaZ9Fojibsf3tVTTbXo0Fg4FgMaYkW0j81l3dj6Hn2Ug/640?wx_fmt=jpeg)

图2：基于约束力矩阵的全身动力学建模

4. 通用力平衡方程组与模型求解

结合牛顿-欧拉方程和约束力表达式，我们对每一个杆件列写力平衡方程：

I · A + V ×*(I · V) = FG+ C · η + Fext

为了封闭求解，我们还需要联立运动学约束方程（即加速度约束）：

CT· A = ca

将上述两组方程整合，我们得到了一个优美的对称线性方程组，即通用动力学模型：

![image](https://mmbiz.qpic.cn/mmbiz_png/2YFlzKTpOib962ficMm3trlGicQeuibDpcoWjQsu44FQMNQfkWIbDU856cN0qfeza7l3WicZV2xQFG1mibLDibF3sec2g/640?wx_fmt=png&from=appmsg)

其中Fp包含了重力、科氏力等所有已知的外力项。

正逆解问题的统一求解

动力学逆解（Inverse Dynamics）：
已知期望的运动（即加速度A），求解需要的驱动力（即η的一部分）。代入方程即可直接解出η。

动力学正解（Forward Dynamics）：
已知驱动力，求解系统的运动响应（加速度A）。此时η中的驱动项已知，约束项未知，通过求解上述线性方程组，可同时获得系统的加速度A和未知的约束反力。

.cls-1{fill:#001e36;}.cls-2{fill:#31a8ff;}

.cls-1{fill:#001e36;}.cls-2{fill:#31a8ff;}

.cls-1{fill:#001e36;}.cls-2{fill:#31a8ff;}

.cls-1{fill:#001e36;}.cls-2{fill:#31a8ff;}

.cls-1{fill:#001e36;}.cls-2{fill:#31a8ff;}

var first_sceen__time = (+new Date());
            if ("" == 1 && document.getElementById('js_content')) {
              document.getElementById('js_content').addEventListener("selectstart",function(e){ e.preventDefault(); });
            }

预览时标签不可点
