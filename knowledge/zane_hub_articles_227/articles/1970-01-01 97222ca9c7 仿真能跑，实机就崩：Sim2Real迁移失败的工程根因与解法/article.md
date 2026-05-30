---
title: "仿真能跑，实机就崩：Sim2Real迁移失败的工程根因与解法"
author: "Zane Zhang"
publish_time: "1970-01-01 08:33:46"
url: "https://mp.weixin.qq.com/s/rImRXADwVu4eB2EKJE1Ilg"
biz: "MzkxNzY1NTY0MQ=="
image_count: 5
---

# 仿真能跑，实机就崩：Sim2Real迁移失败的工程根因与解法

强化学习在足式机器人领域的应用，近两年有明显提速。越来越多的开发者开始用 RL 训练四足机器人的运动策略，但上机部署时普遍遭遇同一类问题：Isaac Sim 里表现稳定的策略，部署到真实机器人后控制异常，轻则步态失调，重则发散趴倒。

这个现象在学术界有一个专有名词：Sim2Real Gap，也叫 Reality Gap。问题通常不是某一个参数调错了，而是仿真与真实之间存在多个层次的系统性偏差，同时叠加作用。

Sim2Real 失败的根源：四个层次的偏差

从机器人控制闭环的角度拆解，仿真和真实之间的差距可以归纳为四个层次。

环境建模层：物理仿真器无法准确复现真实世界的摩擦系数、接触力模型和地面反弹系数。足式机器人的落足稳定性高度依赖接触力的准确性，仿真中能稳健运动的策略，在真实地面上往往因为接触力失真而失控。

感知层：仿真中的传感器读数是干净的。真实传感器存在噪声，且观测是部分可得的——IMU 在剧烈运动中有漂移，关节编码器有量化误差，这些在仿真里通常默认不存在。

本体建模层：仿真模型中的电机通常被视为理想执行器，直接按 PD 控制指令响应。真实电机有摩擦、死区和响应延迟，实际输出扭矩与仿真值存在系统性偏差。这一层的误差往往是 Sim2Real 失败中贡献最大的来源之一。

控制层：从控制指令下发到关节实际执行，真实系统存在通信延迟和机械传动延迟。仿真中这个延迟通常为零，实机上可能达到 10–20 ms。对于高速步态控制，这个量级的延迟足以让策略出现相位错误。

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/57Q4MfeLoyDSpeVjZNkOAbrvK72yAzxdUTShxr4MicqbwkibFWj0Rdd3lzT04jSE7IsGaN8O4ZAtE4akuDpXTmaktaSyuyDBicicR7DoWUGOG7I/640?wx_fmt=png&from=appmsg)

图1：机器人控制闭环中仿真与真实环境的主要差异维度（来源：小米机器人工程师 刘天林）

域随机化：有效，但不是万能的

应对 Reality Gap，最常见的工程方法是域随机化（Domain Randomization）：在训练过程中随机化仿真环境的物理参数，使策略在大范围参数分布下都能工作，从而把真实世界视为训练分布中的一个采样点。

域随机化在足式机器人上确实有效，NVIDIA Isaac Lab 也内置了较完整的随机化参数接口，但这个方法有两个固有局限。

第一，随机化范围需要人工指定。范围过窄，真实世界的参数可能超出分布；范围过宽，训练难以收敛或策略过于保守。这个范围的设定依赖大量工程经验，且对不同硬件平台需要重新标定，不能直接移植。

第二，域随机化对电机执行器的非线性特性处理有限。随机化是在已知分布上做扰动，无法精确建模特定执行器的摩擦、死区等系统性行为。

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/57Q4MfeLoyAWeJkLu1SITUsaFibfWCgtJsb0rEe97PAiapzu6lzkroS49nvuKWLI6eic0Iciaba0Eq4TPX4cHlgAkiaKlgw6mtlhaIpQ6XgA1YTY/640?wx_fmt=png&from=appmsg)

图2：域随机化的工作原理——将真实世界视为仿真参数分布中的一个采样（来源：Lilian Weng, lilianweng.github.io）

执行器网络：针对电机建模的工程补丁

针对执行器建模不准确的问题，ETH 苏黎世联邦理工的团队提出了 Actuator Net 方法：用神经网络拟合从 PD 控制误差（位置误差、速度误差）到关节实际输出扭矩的映射关系。网络的训练数据来自真实硬件采集，离线训练后嵌入仿真器，替代原有的理想电机模型。

这个方法的工程意义在于：它把一个难以用解析公式精确描述的非线性系统，用数据驱动的方式建模，显著缩小了执行器行为在仿真和真实之间的差距。ETH 在 ANYmal 四足平台上对这个方法做了系统验证，后续被多个足式机器人项目沿用。

Teacher-Student 框架：解决特权观测问题

Sim2Real 中另一个值得单独讨论的问题是特权观测（Privileged Observations）。

仿真训练时，策略往往依赖一些在真实传感器上无法直接获得的状态量。典型例子是机器人基座的线速度：仿真中可以直接读取，但真实机器人上通常没有对应传感器，IMU 只能提供角速度，线速度需要积分估算，存在漂移误差。如果训练好的策略直接依赖线速度输入，部署时输入质量的下降会直接导致控制失败。

当前学界和工业界较主流的解法是 Teacher-Student 蒸馏框架，分三个阶段进行：

第一阶段，训练 Teacher 策略，允许使用仿真中可得的所有特权观测值，充分发挥仿真的信息优势，让 Teacher 尽可能学好。

第二阶段，训练 Student 策略。Student 只使用真实传感器可以提供的观测量，通过行为克隆（Behavior Cloning）模仿 Teacher 的动作输出，用历史观测序列来弥补无法直接获取的状态信息。

第三阶段，对 Student 策略用强化学习做微调，在真实传感器约束下进一步提升性能。

RMA（Rapid Motor Adaptation，快速运动适应）是这个框架的代表实现。Student 网络通过读取历史动作和观测窗口，推断出环境的隐变量，替代无法直接测量的物理参数。在 ANYmal 等四足平台上，RMA 实现了较好的 zero-shot 迁移效果。Isaac Lab 官方文档目前也内置了基于这套框架的 Unitree G1 Sim2Real 工作流。

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/57Q4MfeLoyC0CP0fMxP6eb1j7h9mWvBnJ5XUIyq6dcE839N3jHlay2qh2gicCqjbjQ3GibNYNp4BweROraNsouq4xkodqHBRsdOT0qAQiaaIWI/640?wx_fmt=png&from=appmsg)

图3：RMA Teacher-Student 框架结构，Student 通过历史序列推断环境隐变量（来源：Kumar et al., RSS 2021）

Isaac Lab + rl_sar 在 智元D1 平台上的工程定位

上述技术路径在工具链层面，目前比较完整的组合是 Isaac Lab 负责训练侧，实机部署侧需要对应平台的工程实现。

Isaac Lab 提供了 GPU 并行化仿真环境、域随机化参数接口、Teacher-Student 训练流程，以及.pt/.onnx格式的策略导出能力，解决的是"如何高效训练"的问题。

实机部署侧面临的挑战则包括：控制频率与仿真帧率对齐、真实传感器数据的预处理与滤波、安全限位与急停逻辑、以及通信延迟补偿。这些工程细节高度依赖具体硬件，通常无法跨平台复用，也是公开资料中最难找到完整实现的部分。

rl_sar是目前在智元 D1 硬件上实际跑通过的实机部署工具链，覆盖了上述部署侧的主要环节，提供了从训练策略到实机落地的完整工程参考，这类硬件绑定的实现在开源社区中属于稀缺资源。

延伸资源

智元实验室联合 NVIDIA 与古月居，邀请「敢敢のWings」团队出品了一套针对智元 D1 四足机器狗的强化学习全链路课程，覆盖 Isaac Lab 环境搭建、奖励函数设计、rl_sar 部署与实机调优。讲师团队有 Google、Amazon 一线算法工程背景，课程免费，3 月 23 日起直播，感兴趣可以扫码了解。

![image](https://mmbiz.qpic.cn/mmbiz_png/57Q4MfeLoyApILGH5MWricraNu8mmn8HEZamJuY0n1WaydzcHOBASibkVuJ0garBjx3zQP0LiaLFiayau4M3Rnx2tqa2gvtzWpicqpVBjX4VdJ8s/640?wx_fmt=png&from=appmsg)

另附该免费课程海报

![image](https://mmbiz.qpic.cn/mmbiz_png/57Q4MfeLoyByZTT9er7ib8x7CUMsicEZveIKmcqvXa4WaLe468eU80zTBGaJmKgSQiaiaCWBxvYF19HXGO91QhicjL6XWicDMb0ACbwzn3BtJ8BEk/640?wx_fmt=png&from=appmsg)

本文技术内容参考来源：小米工程师刘天林的足式机器人 Sim2Real 综述、NVIDIA Isaac Lab 官方文档与开发者博客、Kumar et al. RMA 论文（RSS 2021）。
