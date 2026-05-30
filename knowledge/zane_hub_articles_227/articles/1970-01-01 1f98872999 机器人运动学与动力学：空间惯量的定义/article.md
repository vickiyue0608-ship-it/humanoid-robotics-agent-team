---
title: "机器人运动学与动力学：空间惯量的定义"
author: "Zane Zhang"
publish_time: "1970-01-01 08:33:45"
url: "https://mp.weixin.qq.com/s/OZ3x7_6HCM-Me62pEpppvg"
biz: "MzkxNzY1NTY0MQ=="
image_count: 5
---

# 机器人运动学与动力学：空间惯量的定义

1. 引言

在经典力学中，描述质点动力学的核心是牛顿第二定律f = ma。对于仅有质量属性的质点，其惯性特性由一个标量m即可完整描述。然而，刚体的运动是在六维空间（三维平动+三维转动）中进行的，其动力学行为远比质点复杂。

为了在旋量理论框架下统一描述刚体的动力学，我们需要将牛顿-欧拉方程推广为旋量形式F = IA。在这个公式中，F是六维力旋量，A是六维空间加速度，而I则演变为一个 6×6 的对称矩阵——空间惯量矩阵。这一矩阵不仅包含了传统的质量和转动惯量，还通过非对角项描述了平动与转动的耦合效应，是机器人动力学建模的核心参数。

2. 空间惯量矩阵的数学定义

2.1 力平衡方程中的惯量

在旋量代数中，刚体的完整动力学方程（旋量形式的牛顿-欧拉方程）表达为：F = I · A + V ×*(I · V)

其中I作为一个线性算子，充当了力与加速度之间的桥梁。它本质上是一个十维的物理量（由于刚体的对称性和质量分布特性），但在数学上被组织为一个 6×6 的对称矩阵。

2.2 四块矩阵的物理意义

空间惯量矩阵I具有清晰的分块结构，每一个分块都对应着明确的物理意义：

![image](https://mmbiz.qpic.cn/mmbiz_png/2YFlzKTpOib962ficMm3trlGicQeuibDpcoWbTIZLCmiaJbmOyafmjAhuayqXMibqia2E9MVHsRoCkB3hUTJDuKUPH8ww/640?wx_fmt=png&from=appmsg)

左上角 (3×3)：
m · E，其中m是刚体质量，E是单位矩阵。这部分描述了刚体的平动惯性。

右下角 (3×3)：
IO，是刚体绕参考点 O 的转动惯量张量。注意这里的参考点通常不是质心。

非对角块 (3×3)：
m · [c]×及其转置。其中c是从参考点 O 指向质心 C 的位置矢量，[c]×是该矢量的反对称矩阵。这部分反映了由于参考点不在质心而引入的平动-转动耦合效应。

3. 刚体在宇宙空间中的积分定义

3.1 刚体的数学建模

从微观角度看，刚体可以被视为分布在无限宇宙空间中的质量密度函数ρ(r)。对于刚体占据的体积V，密度非零；而在其他空间，密度为零。因此，刚体的惯性参数可以通过对整个空间进行体积分来获得。

3.2 质量与质心的计算

质量积分：对密度函数进行全空间积分，即可得到标量质量m：

m = ∫∫∫ ρ(r) dV

质心位置：质心c是质量分布的加权平均位置：

c = (1/m) ∫∫∫ r · ρ(r) dV

3.3 转动惯量张量

绕参考点 O 的转动惯量张量IO定义为：

IO= ∫∫∫ [r]×T· [r]×ρ(r) dV

该张量包含了三个主转动惯量 (Ixx, Iyy, Izz) 和三个惯量积 (Ixy, Ixz, Iyz)。

4. 空间惯量的坐标系变换

惯量矩阵的一个重要特性是其随坐标系变换的规律。在刚体固连坐标系 {B} 下，惯量矩阵IB是常数。当我们需要在其他坐标系（如全局坐标系 {O}）下描述动力学时，必须进行坐标变换。

4.2 变换公式

设T*为力螺旋的坐标变换矩阵（6×6 Adjoint Matrix），则惯量矩阵的变换遵循以下“合同变换”规律：

IO= T*· IB· (T*)T

其中变换矩阵T*构造如下：

![image](https://mmbiz.qpic.cn/mmbiz_png/2YFlzKTpOib962ficMm3trlGicQeuibDpcoWSOaIVQVod71rTicmeiaQDGdu9ctVr8yVBZLM3hADIHNzUHKQLD6JTicibw/640?wx_fmt=png&from=appmsg)

这种变换实际上是平行轴定理在六维旋量空间中的广义形式。它保证了变换后的矩阵IO依然保持对称性。

5. 空间惯量矩阵的微分

在动力学分析中，经常需要计算惯量矩阵对时间的导数。虽然在固连坐标系下IB是常数，但在全局坐标系下IO随刚体运动而时刻变化。

对变换公式求导，并利用Ṫ*= V ×*· T*，我们可以得到简洁的微分公式：

İ = V ×*· I - I · V×

这一公式揭示了惯量矩阵的变化率完全由刚体本身的速度V决定，与加速度无关。该性质在推导动力学方程中的非线性项（科氏力与离心力）时至关重要，特别是恒等式İ·V + I·V̇ = V×*·(I·V)的成立，极大地简化了计算。

6. 案例分析：计算 O 点惯量矩阵

6.1 问题描述

已知某刚体质量m = 4 kg，质心 C 相对参考点 O 的位置为c = [1, 0, 0]T。在质心坐标系下，转动惯量为单位阵IC= E。求该刚体在 O 点的空间惯量矩阵IO。

6.2 计算过程

步骤 1：写出质心坐标系下的惯量矩阵

![image](https://mmbiz.qpic.cn/mmbiz_png/2YFlzKTpOib962ficMm3trlGicQeuibDpcoWwmcVvnZSfXz2uD7RHWz7WT0KAMib1k2AYGB6WiauYfJZJfpv8XAmm9Cg/640?wx_fmt=png&from=appmsg)

步骤 2：构建变换矩阵 T*

由于质心位于 [1,0,0]，对应位移矢量p = [-1, 0, 0]（从 O 到 C），其反对称矩阵[p]×有非零元素。变换矩阵为：

![image](https://mmbiz.qpic.cn/mmbiz_png/2YFlzKTpOib962ficMm3trlGicQeuibDpcoWiaqVekTapuNK4icVygrPk0ZTcMGXCShMzPmF2ZqJyv3VNadjoQxFfbeg/640?wx_fmt=png&from=appmsg)

步骤 3：应用变换公式

计算IO= T*· IC· (T*)T，得到最终结果：

![image](https://mmbiz.qpic.cn/mmbiz_png/2YFlzKTpOib962ficMm3trlGicQeuibDpcoWUQY7zyqsXk0aJjsryicicGAhowzYNs98ia7slKBYooIaqh7254UbNG5Vg/640?wx_fmt=png&from=appmsg)

结果分析：左上角质量块保持不变。右下角转动惯量发生变化（1 → 5），体现了平行轴定理（I = IC+ md2= 1 + 4×12= 5）。非对角块出现的非零项反映了质心偏移造成的耦合。
