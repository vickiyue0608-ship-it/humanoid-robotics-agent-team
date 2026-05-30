---
title: "机器人运动学与动力学 | 力与力矩"
author: "Zane Zhang"
publish_time: "1970-01-01 08:33:45"
url: "https://mp.weixin.qq.com/s/JmYCKF2JXhUGaAKxE97gQg"
biz: "MzkxNzY1NTY0MQ=="
image_count: 6
---

# 机器人运动学与动力学 | 力与力矩

在学习机器人运动学与动力学时，深刻理解作用在刚体上的力与力矩是至关重要的一步。这不仅仅是高中物理的延伸，更是在更高维度上对力的作用进行精确描述与数学建模。本文将深入剖析刚体动力学中的核心概念，从纯力与纯力偶的区别，到力的迁移，最终引出强大的分析工具——力旋量（Wrench）。

第一章 纯力：重新定义力的三要素

传统物理学告诉我们，力的三要素是大小、方向和作用点。然而，在刚体动力学中，这个定义需要进行修正。

![image](https://mmbiz.qpic.cn/mmbiz_png/2YFlzKTpOibibYskAbRCgGq0qKKgqXsWfEf3wwqodaGls4rJ6vDjXoYPiaqhHeSwCNw0PmE0XpiamibaKwygP6x0S6g/640?wx_fmt=png&from=appmsg)

纯力：一个"滑动矢量"

对于一个刚体而言，一个纯力（Pure Force）的作用效果不仅取决于其大小和方向，更关键的是它的作用线（Line of Action）。

刚体动力学中的力的三要素：大小、方向、作用线。

这意味着，只要力的大小和方向不变，它在其作用线上任意"滑动"，对刚体的整体运动影响是完全相同的。例如，在物体后方沿作用线推它，和在物体前方沿同一作用线拉它，产生的效果是等效的。因此，纯力也被称为滑动矢量（Sliding Vector）。

![image](https://mmbiz.qpic.cn/mmbiz_png/2YFlzKTpOibibYskAbRCgGq0qKKgqXsWfEvVoAPEIKlph0BYtfJnRBA2ibALabVbSLoQpia3j7UEFo5Xcx0NVm6tug/640?wx_fmt=png)

图3：纯力作为滑动矢量的特性演示

第二章 纯力偶：一个"自由矢量"

与纯力不同，纯力偶（或称力矩，Torque）的作用效果只由其大小和方向决定，与其作用在刚体的哪个具体位置无关。你可以将一个力偶从刚体的一端"移动"到另一端，只要其矢量本身（大小和方向）不变，它对刚体产生的旋转效果就是完全一致的。因此，纯力偶是一个自由矢量（Free Vector）。

![image](https://mmbiz.qpic.cn/mmbiz_png/2YFlzKTpOibibYskAbRCgGq0qKKgqXsWfEiaIGLQLvlwzA506XruMVibMkgMAqzfBjeJPFA8AocLWC3UyYDNC4Dhgw/640?wx_fmt=png&from=appmsg)

图4：纯力偶作为自由矢量的特性演示

力偶的物理本质

力偶由两个大小相等、方向相反、作用线不重合的平行力组成。这种配置确保了：

合力为零，不产生平移运动

合力矩不为零，产生纯旋转效果

旋转效果与力偶在刚体上的具体位置无关

第三章 力的迁移定理：统一参考点的数学工具

为了方便分析作用在刚体上不同位置的多个力，我们需要将它们统一迁移到一个共同的参考点，通常是坐标系的原点O。力的迁移遵循特定的定理。

![image](https://mmbiz.qpic.cn/mmbiz_png/2YFlzKTpOibibYskAbRCgGq0qKKgqXsWfE8s45ZWekyowlqqcYsnlr0Vkbxic4kibIPMWUhLJJFZH88icDWMaU4ib8zg/640?wx_fmt=png)

图5：力的迁移定理详细示意图

迁移纯力的数学表述

当我们将一个作用在R点的纯力F迁移到坐标原点O时，为了保持力学等效性，必须进行如下操作：

力的分量
：迁移后，力的矢量F保持不变。

附加力矩
：由于作用点发生改变，会额外产生一个力矩τ。

这个附加力矩的计算公式为：

τ = r × F

其中r是从新的参考点O指向原作用线上任意一点R的矢量，×代表向量的叉乘。

迁移纯力偶

由于纯力偶是自由矢量，将它从一点迁移到另一点时，其矢量本身不会发生任何改变，也不会产生任何附加的力或力矩。这是力偶作为自由矢量的重要特性。

第四章 力旋量：统一描述力的强大工具

通过力的迁移定理，我们可以将作用在刚体上任意复杂的力系（包含多个力和力偶）等效为作用在同一个参考点O上的一个合力和一个合力矩。为了将这两者统一成一个数学实体，我们引入了力旋量（Wrench）的概念。

![image](https://mmbiz.qpic.cn/mmbiz_png/2YFlzKTpOibibYskAbRCgGq0qKKgqXsWfETsq3DGbqDMZibFEANnUbm6AIw8rBL394sBjBicvJdH6VKIygeQtQ61uw/640?wx_fmt=png&from=appmsg)

图6：力旋量的六维矢量表示

力旋量的数学定义

力旋量是一个六维矢量，它将三维的力矢量F和三维的力矩矢量τ组合在一起：

Wrench = [F_x, F_y, F_z, τ_x, τ_y, τ_z]^T

通过力旋量，空间中任何复杂的力系都可以被简洁地表示为在特定参考点（如坐标原点O）的一个六维矢量。这极大地简化了机器人动力学的分析与计算。

力的线性空间：力运算的数学本质

所有可能作用在刚体上的力旋量，共同构成了一个六维的实数线性空间（Linear Space），记作F⁶。

![image](https://mmbiz.qpic.cn/mmbiz_png/2YFlzKTpOibibYskAbRCgGq0qKKgqXsWfEj6Uw55nibGtjy2306ZjpwOkYNbypAKlibcRjwIicBOyIRFOHmIqBz2Vibg/640?wx_fmt=png&from=appmsg)

图7：力的线性空间F⁶及其运算规律

这个概念揭示了力运算的深刻数学本质：

力的叠加
：当多个力同时作用于一个刚体时，其总效果对应着各个力的力旋量在这个线性空间中的矢量加法。即 W_total = W₁ + W₂。

力的缩放
：将一个力的大小放大或缩小n倍，其效果对应着力旋量与标量n的数乘运算。即 W_new = n × W。

这个线性空间满足加法交换律、结合律、封闭性等一系列运算公理，为我们分析和叠加多个力的作用提供了严谨的数学框架。

值得注意：我们用符号ζ (Zeta)表示的力是一个客观存在的物理实体，与坐标系无关。而用F或力旋量表示的力，则是我们在选定了特定坐标系后，得到的六维矢量表示。
