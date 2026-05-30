---
title: "机器人运动学与动力学 | 螺旋系的坐标转换"
author: "Zane Zhang"
publish_time: "1970-01-01 08:33:45"
url: "https://mp.weixin.qq.com/s/Ma9Z3d99OUYhCue7u_R0zQ"
biz: "MzkxNzY1NTY0MQ=="
image_count: 17
---

# 机器人运动学与动力学 | 螺旋系的坐标转换

一、引言

在机器人运动学的深入研究中，螺旋理论为我们提供了一个统一的数学框架来描述刚体的运动和受力。然而，当面对复杂的多连杆机器人系统时，我们不能仅仅满足于在单一坐标系下的分析。实际工程中，每个关节和连杆都有其自然的局部坐标系，而整个系统的运动分析往往需要在一个统一的全局坐标系下进行。

局部坐标系是固定在特定连杆上的坐标系，它能够最直观地描述该连杆的几何特性和运动特征。相对而言，全局坐标系（通常称为世界坐标系或基础坐标系）是一个固定的参考系，用于描述整个机器人系统在空间中的绝对位置和姿态。

因此，本文需要解决的核心问题是：如何将一个坐标系下定义的螺旋（无论是速度螺旋还是力螺旋）准确地转换到另一个坐标系下进行表达？这个问题的解决，将为我们使用螺旋理论分析复杂机器人系统奠定数学基础。

二、为什么需要坐标系转换

机器人多连杆系统具有以下特点：每个连杆都可以看作一个刚体，连杆之间通过关节连接，形成开链或闭链结构。在这种系统中，如果我们试图在一个统一的全局坐标系下直接描述每个关节的运动螺旋和约束螺旋，往往会导致数学表达式异常复杂，缺乏物理直觉。

局部坐标系的定义带来了显著的优势。例如，对于一个转动关节，如果我们将局部坐标系的z轴与关节轴重合，那么该关节的运动螺旋就具有非常简洁的形式。类似地，对于移动关节，如果局部坐标系的某个轴与移动方向一致，约束螺旋的表达也会大大简化。

然而，为了分析整个机器人的运动学和动力学特性，我们必须将这些在不同局部坐标系下定义的螺旋统一转换到同一个全局坐标系中。这种统一不仅是数学上的需要，更是工程实现的前提——只有在统一的坐标系下，我们才能进行雅可比矩阵计算、奇点分析、轨迹规划等关键任务。

三、速度螺旋的坐标系转换

![image](https://mmbiz.qpic.cn/mmbiz_png/2YFlzKTpOibib9tbqtchNOzTP5ZbXETryNnI1Nm8wuYXKOKrH4PwsHEjNARIrjzQnmABpDhPK2rGwNvjJ9OVqVUQ/640?from=appmsg)

速度螺旋是描述刚体运动状态的基本工具，其一般形式为：

![image](https://mmbiz.qpic.cn/mmbiz_png/2YFlzKTpOibib9tbqtchNOzTP5ZbXETryN8nddh8wxkLX0wfbgySzfw3OxgicmOqgTMLyADka4GYb0b95KlIY4OWg/640?wx_fmt=png&from=appmsg)

其中ω∈R3是角速度向量，v∈R3是线速度向量。接下来我们将分三种情况讨论速度螺旋在不同坐标系间的转换。

3.1 纯转动情况

考虑两个坐标系{A}和{O}，它们的原点重合，但存在相对旋转。设从坐标系{A}到{O}的旋转矩阵为R∈ SO(3)。

由于角速度和线速度都是三维向量，当坐标系发生旋转时，根据向量的坐标变换规律，我们需要将它们分别左乘旋转矩阵R。因此，速度螺旋的转换矩阵为完整的6×6形式：

![image](https://mmbiz.qpic.cn/mmbiz_png/2YFlzKTpOibib9tbqtchNOzTP5ZbXETryNKpVAiatcRPQicfqHMAEGSqZSXMLZ3yicR9USKHQsYEm0X3UvtgFjLXORA/640?wx_fmt=png&from=appmsg)

其中rij为旋转矩阵的第i行第j列元素。这是一个块对角矩阵，左上角3×3块和右下角3×3块都是旋转矩阵，而其他位置为零。

相应的转换关系为：

![image](https://mmbiz.qpic.cn/mmbiz_png/2YFlzKTpOibib9tbqtchNOzTP5ZbXETryNFVc3xLTgZAa2TRQkncANhUQdJAUMn7qTLMLPHgj72NlUqdVib8uzia8w/640?wx_fmt=png&from=appmsg)

![image](https://mmbiz.qpic.cn/mmbiz_png/2YFlzKTpOibib9tbqtchNOzTP5ZbXETryNXxr0FC0UQ8mQbbtSZbRAgpf6Sicm0MWAIGemRx0dDoa59GzpOZVTU0A/640?wx_fmt=png&from=appmsg)

3.2 纯平动情况

现在考虑两个坐标系{A}和{O}姿态相同（即旋转矩阵为单位矩阵），但原点之间存在平移向量P= [px,py,pz]T。

根据刚体运动学的基本原理：

角速度不变，因为它与参考点的选择无关

线速度根据速度迁移定理变换：vO=vA+p×ωA

为了写成矩阵形式，我们首先定义平移向量P对应的反对称矩阵：

![image](https://mmbiz.qpic.cn/mmbiz_png/2YFlzKTpOibib9tbqtchNOzTP5ZbXETryNpYftUQJOaly2RvjoQZnJJUQccW9zkntlCR7h9LqGujCOia4KIcMTia4g/640?wx_fmt=png&from=appmsg)

则纯平动的速度螺旋转换矩阵的完整6×6展开形式为：

![image](https://mmbiz.qpic.cn/mmbiz_png/2YFlzKTpOibib9tbqtchNOzTP5ZbXETryNiczmdhWpuLsedkH8PiaA2k0xicKMib1be07DjrJict2NTA2tefT0vzVL4nQ/640?wx_fmt=png&from=appmsg)

矩阵结构分析：

左上角3×3块为单位矩阵E3x3，对应角速度的直接传递

右上角3×3块为反对称矩阵[p]x，体现了平移对线速度的耦合影响

左下角为3×3零矩阵，表明线速度不影响角速度

右下角为单位矩阵E3x3，对应线速度的直接传递

3.3 一般情况：刚体运动（平动+转动）

在最一般的情况下，坐标系{A}和{O}之间既有平移又有旋转。，可以通过复合变换的方法来推导转换矩阵。

推导采用两步法：

先进行旋转：

再进行平移：

将这两个变换矩阵相乘，得到通用速度螺旋转换矩阵的完整6×6x6展开形式：

![image](https://mmbiz.qpic.cn/mmbiz_png/2YFlzKTpOibib9tbqtchNOzTP5ZbXETryNu7pzHJWEiarlAhOno2Dj6KscJfoibia3G92kXuoqSMz2MsXRmtgDTZe3Q/640?wx_fmt=png&from=appmsg)

或者用更清晰的块矩阵表示：

![image](https://mmbiz.qpic.cn/mmbiz_png/2YFlzKTpOibib9tbqtchNOzTP5ZbXETryNeCZVDyzAKFia5iaYbZ82v8pGywEVMnX8uETj71Aw5iaF1fFFnXFziaficNw/640?wx_fmt=png&from=appmsg)

矩阵结构详解：

左上角3×3块：旋转矩阵R，作用于角速度分量

右上角3×3块：[p]xR矩阵，体现了平移和旋转对线速度的耦合影响

左下角3×3块：零矩阵，表明线速度不影响角速度的变换

右下角3×3块：旋转矩阵R，作用于线速度分量

上述完整展开的6×6矩阵清楚地显示了每个元素的具体表达式。前三列对应角速度的变换系数，后三列对应线速度的变换系数。右上角块的元素是反对称矩阵与旋转矩阵相乘的结果，反映了速度迁移定理
![image](https://mmbiz.qpic.cn/mmbiz_png/2YFlzKTpOibib9tbqtchNOzTP5ZbXETryN07nV0SGJnia3Pz7V738nRY6vlTAqlwaH2JYPARHy0xtJKx3nmt6qgEg/640?wx_fmt=png&from=appmsg)
的矩阵形式。

重要性质：

这个6×6矩阵与4×4齐次变换矩阵在数学上是同构的

它完整地编码了两个坐标系间的位姿关系（旋转R和平移p）

在李群理论中，这个矩阵被称为伴随矩阵（Adjoint Matrix）

![image](https://mmbiz.qpic.cn/mmbiz_png/2YFlzKTpOibib9tbqtchNOzTP5ZbXETryN3dB7ib49yAOuPCkZgtwScSt1ibcqeyibtdR7bornh1GayXQMIMCuica05A/640?from=appmsg)

四、力螺旋的坐标系转换

力螺旋用于描述作用在刚体上的力和力矩，其基本形式为：

![image](https://mmbiz.qpic.cn/mmbiz_png/2YFlzKTpOibib9tbqtchNOzTP5ZbXETryNvwjZ4UHRPlOyiavQBH43tgtn2MwADKsiamd9qXjsThOiauw3cCqakVB3A/640?wx_fmt=png&from=appmsg)

其中f是力向量，τ是力矩向量。

4.1 推导过程

力螺旋的坐标系转换推导过程与速度螺旋类似，也采用先旋转再平移的两步法。然而，关键区别在于力和力矩在参考点迁移时遵循不同的物理定律：

力向量f在坐标系旋转时需要进行相同的旋转变换

力矩向量τ不仅要进行旋转变换，还要考虑力臂变化带来的附加力矩

4.2 力螺旋转换矩阵

经过详细推导，力螺旋转换矩阵的完整块矩阵形式为：

![image](https://mmbiz.qpic.cn/mmbiz_png/2YFlzKTpOibib9tbqtchNOzTP5ZbXETryNF2WRMqwcaSBIv3xxQlVvBkGwP87AyczVfPoYjGKZE7WznPUPyPcL7A/640?wx_fmt=png&from=appmsg)

关键差异分析：

与速度螺旋转换矩阵相比较，我们发现项位于左下角而非右上角。这个结构上的根本差异反映了以下物理事实：

速度的耦合：角速度影响线速度（通过速度迁移定理）

力的耦合：力影响力矩（通过力矩迁移定理）

这种"转置"关系正是速度和力在对偶空间中相互共轭的数学体现。

五、速度与力螺旋转换矩阵的对偶关系

5.1 数学关系

速度螺旋转换矩阵和力螺旋转换矩阵之间存在着深刻的对偶关系：

![image](https://mmbiz.qpic.cn/mmbiz_png/2YFlzKTpOibib9tbqtchNOzTP5ZbXETryNPIJg48ybmxORHDlIWaicTUAmPMcHh7xFHLMmk6YZl4PqEmwRnaSaWCw/640?wx_fmt=png&from=appmsg)

即：力螺旋转换矩阵等于速度螺旋转换矩阵的逆的转置。这个关系在李群理论中被称为伴随表示的对偶性。

5.2 物理本质

这种对偶关系的物理本质源于功率不变性原理：

![image](https://mmbiz.qpic.cn/mmbiz_png/2YFlzKTpOibib9tbqtchNOzTP5ZbXETryNRcdXiblAZ8ruaeoSE2HOWXsZrPlQpNZPjV5qp6pym0q36901FBvf2Bg/640?wx_fmt=png&from=appmsg)

在任何坐标系下，力螺旋与速度螺旋的内积（代表瞬时功率）都必须保持不变。这是能量守恒定律在螺旋理论框架下的数学表述。

具体而言，如果我们有

![image](https://mmbiz.qpic.cn/mmbiz_png/2YFlzKTpOibib9tbqtchNOzTP5ZbXETryN8xUmZa1VzNJy2exCeOHick9yLfo1QO5qV07kfw9MnYpxAppOWbunKGg/640?wx_fmt=png&from=appmsg)

则功率不变性要求：

![image](https://mmbiz.qpic.cn/mmbiz_png/2YFlzKTpOibib9tbqtchNOzTP5ZbXETryNFW8aa4UVsziaIqnVEOuwuP63u9CdwicAutAv8X8LlneWd7zLE6TAln4w/640?wx_fmt=png&from=appmsg)

将转换关系代入，即可证明。

5.3 工程意义

这种对偶关系在工程实践中具有重要意义：

计算效率
：只需计算一个转换矩阵，另一个可以通过逆转置直接得到

数值验证
：可以作为检验计算正确性的理论依据

能量一致性
：在机器人动力学分析中自动保证能量守恒

控制设计
：在基于能量的控制方法中提供理论基础

六、工程应用要点

6.1 计算步骤

位姿测量
：确定两个坐标系之间的相对位姿，获得旋转矩阵和平移向量

矩阵选择
：根据转换对象选择适当的转换矩阵（速度螺旋用，力螺旋用）

矩阵计算
：构造完整的6×6转换矩阵

螺旋转换
：执行矩阵乘法完成坐标系转换

6.2 注意事项

坐标系一致性
：确保所有坐标系都采用右手法则定义

旋转矩阵验证
：检查且

反对称矩阵
：正确构造，注意符号约定

单位统一
：确保角量和线量采用一致的单位制

6.3 数值实现优化

块矩阵利用
：利用块结构避免冗余计算，特别是重复的旋转矩阵元素

对偶关系
：当同时需要速度和力螺旋转换时，利用对偶关系减少一半计算量

库函数集成
：在实际编程中，可以直接利用现有的齐次变换矩阵库函数

数值稳定性
：对于接近奇异的旋转矩阵，采用四元数等数值稳定的表示方法
