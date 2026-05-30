---
title: "机器人运动学与动力学 | 速度螺旋与点速度的关系"
author: "Zane Zhang"
publish_time: "1970-01-01 08:33:45"
url: "https://mp.weixin.qq.com/s/bDE5JUZIKBQdjSYZdsr7YA"
biz: "MzkxNzY1NTY0MQ=="
image_count: 92
---

# 机器人运动学与动力学 | 速度螺旋与点速度的关系

一、速度螺旋的核心优势

1.1 无需定义参考点

速度螺旋（Velocity Screw）作为刚体运动描述的高阶方法，其根本优势在于：描述刚体运动时不需要在刚体上定义任何特定点。

传统三维方法的局限：

必须定义参考点
：例如描述一个iPhone的运动，需要先在其上选定某个特定点
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgKpawtsTFC2to3kV3LlY5tLDlbPdEVqqXF5gaZE5KuVw2Ck0gcDH4iba6gYPm9E22D/640?wx_fmt=svg&from=appmsg)

每点速度各异
：刚体上每一点的线速度都不相同，需要分别计算

表达形式复杂
：不同点的速度需要独立描述，计算繁琐

速度螺旋的优势：

只需转轴信息
：仅需要知道当前瞬时转轴的位置和角速度

统一表达形式
：用六维向量
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgOd8HwBhDjicF2udmbjscZa2QV8u4ryQjOiaEPxQeZZC2B6XNjctKCUZClcKbz1tXfP/640?wx_fmt=svg&from=appmsg)
即可完整描述刚体运动

![image](https://mmbiz.qpic.cn/mmbiz_png/2YFlzKTpOibicUy7wia70iaWlibufjWGnHwSbLVWMnial1rouHDwYZBEHrwyezORib2Eib6byPCibGWwzuVVIicuib8cYwFUw/640?wx_fmt=png&from=appmsg)

图1：速度螺旋的几何表示

1.2 运动不变性的优越表达

对于同速度螺旋，其表达是不变的。这是相对于三维方法的重要优势：

三维方法的问题：

选择不同参考点时，速度的表达形式会发生变化

每个点的线速度数值和方向都不同

即使是恒定转动，描述该点的速度向量也在不断变化

速度螺旋的优势：

只要运动模式不变，地面坐标系不变，其数值表达始终恒定

真实反映刚体运动的本质特征

与具体点的选择无关，具有坐标系不变性

典型例子：考虑刚体绕固定轴做匀速转动

三维方法：
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgKpawtsTFC2to3kV3LlY5tLDlbPdEVqqXF5gaZE5KuVw2Ck0gcDH4iba6gYPm9E22D/640?wx_fmt=svg&from=appmsg)
点的速度向量从垂直向上变为水平向左，数值和方向都在变化

速度螺旋：
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgTRZU65urhlwIKkg0HibyfMermicyia44qDcdMqKtNeMiaAmjzyeFRR6GQFcWcwqcrGlic/640?wx_fmt=svg&from=appmsg)
和
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvg2ic9VkK5V8cAgoY5kH5icgb9pRb9SGjg1bUae9fcC2PmchOHA8ichrgcdUmfSaVfQic5/640?wx_fmt=svg&from=appmsg)
始终保持不变，准确反映"恒定转动"的本质

二、速度螺旋的三重理解

2.1 第一重理解：轴线迁移定理

通过轴线迁移定理，将刚体绕某转轴的角速度和该点速度迁移到坐标系原点O处，得到速度螺旋：

![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgF8ib4x9TTgE2UOucWmefFvT6icOgAHCxvRC1ZqYOaMN62TD0iard7sgPiaoeIGK9NYHV/640?wx_fmt=svg&from=appmsg)

关键参数的含义：

![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgFLuhlTf8ma5TW7CbZs7QPb4XxPM2XxsJ48T1DF6KBpQMfamKianicvTvvy2zCeqFzV/640?wx_fmt=svg&from=appmsg)

：刚体上
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgKpawtsTFC2to3kV3LlY5tLDlbPdEVqqXF5gaZE5KuVw2Ck0gcDH4iba6gYPm9E22D/640?wx_fmt=svg&from=appmsg)
点的线速度

![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgTRZU65urhlwIKkg0HibyfMermicyia44qDcdMqKtNeMiaAmjzyeFRR6GQFcWcwqcrGlic/640?wx_fmt=svg&from=appmsg)

：刚体的角速度（与参考点选择无关）

![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgpw8IiawUecwa3lafibvYoFLWfhVsYLcWfGtAYalVxLHC5OhgjeoRGicvV5aT4NGabD6/640?wx_fmt=svg&from=appmsg)

：从O点到P点的位置矢量

这是旋量（Screw Theory）引入的初始方式。

2.2 第二重理解：瞬时重合点速度

速度旋量的线速度分量
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvg2ic9VkK5V8cAgoY5kH5icgb9pRb9SGjg1bUae9fcC2PmchOHA8ichrgcdUmfSaVfQic5/640?wx_fmt=svg&from=appmsg)
实际上是：刚体在当前时刻与地面坐标系原点O重合的那一点的线速度。

需要注意的关键点：

刚体在概念上被视为充满整个宇宙的无限延伸体

不同时刻与O点重合的是刚体上不同的物理点

![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvg2ic9VkK5V8cAgoY5kH5icgb9pRb9SGjg1bUae9fcC2PmchOHA8ichrgcdUmfSaVfQic5/640?wx_fmt=svg&from=appmsg)

描述的是"瞬时重合点"的速度，而非某个固定物质点的速度

角速度轴线此时恰好通过原点O

2.3 第三重理解：点速度场描述

这是对速度螺旋最深刻的理解：速度螺旋描述的是刚体运动的点速度场。

速度场的概念：

刚体虽然在物理上可能很小，但在动力学分析中被视为充满整个三维空间。刚体上每一点的线速度构成一个速度场（类似于重力场、电场）：

![image](https://mmbiz.qpic.cn/mmbiz/2YFlzKTpOibicUy7wia70iaWlibufjWGnHwSbDNkWusrYHx3Ej6rCdhz4Z5GCicia75oLESdRzOgVx3QONoof55uJw8Uw/640?wx_fmt=other&from=appmsg)

图2：刚体速度场分布

速度场的分布特点：

在转轴上的点：线速度为零

离转轴越远：线速度越大

线速度方向：垂直于转轴和位置矢量构成的平面

速度螺旋的强大之处：仅用六个数字就能描述刚体上任意点的速度！

三、速度螺旋与点速度的转换关系

3.1 从速度螺旋求点速度

给定速度螺旋
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgOd8HwBhDjicF2udmbjscZa2QV8u4ryQjOiaEPxQeZZC2B6XNjctKCUZClcKbz1tXfP/640?wx_fmt=svg&from=appmsg)
和空间中任意点的位置矢量
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgcQL8W19SB8ibcCfwUNF0fPeraaXq77W46FF4DhvjQRtfwSiaIwkArYwRoImDW6YPtK/640?wx_fmt=svg&from=appmsg)
，该点的线速度为：

![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgOMdDWCjib9031f6ibsQnp8bjHzH20RMMcgy9FtXibbMxrKWKgCyCibw4vbovoASh7mO5/640?wx_fmt=svg&from=appmsg)

物理意义：

![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvg2ic9VkK5V8cAgoY5kH5icgb9pRb9SGjg1bUae9fcC2PmchOHA8ichrgcdUmfSaVfQic5/640?wx_fmt=svg&from=appmsg)

：原点处（与O重合点）的线速度

![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvglIsguXNdo8F6WIMa7ia4WnSypaPs3WSUbV9b7Jmqbn8T1eGiaW77ecoB9Qcy7JXctD/640?wx_fmt=svg&from=appmsg)

：由转动引起的附加速度

两者叠加得到空间任意点的速度

特殊情况：当
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgUDI8be54Q8DsWJjx541EA7kgSlqk28X5eWVdiaaqlmvGfUicpOVtdxUJ6fqqnB0Oia7/640?wx_fmt=svg&from=appmsg)
时，
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgx2ON3Av0O2txmH1j81tseTRHCyWibMamZBG7Gic05WAxz4icygyfUvcQVuwnR7iaw2icq/640?wx_fmt=svg&from=appmsg)
，验证了第二重理解。

3.2 从点速度求速度螺旋

反过来，已知某点
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgcQL8W19SB8ibcCfwUNF0fPeraaXq77W46FF4DhvjQRtfwSiaIwkArYwRoImDW6YPtK/640?wx_fmt=svg&from=appmsg)
及其线速度
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvga1ib4OGJyH86RGfu8tr2tWEh82Ta9JiaG8DIMDcJVbD1ibicTHNr9fj5ibV8cZDtQDRVp/640?wx_fmt=svg&from=appmsg)
，以及刚体角速度
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgTRZU65urhlwIKkg0HibyfMermicyia44qDcdMqKtNeMiaAmjzyeFRR6GQFcWcwqcrGlic/640?wx_fmt=svg&from=appmsg)
，可以反推速度螺旋：

![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvg2ic9VkK5V8cAG8HWqjOzmUqGG7IeOOeDUMYq7OMX8Qd2ypwQyCqEicqEUtPejAAYibX/640?wx_fmt=svg&from=appmsg)

或利用叉乘的反对称性：

![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgN652zM7tC3uHXAghjP3buicFKEryPHLoAxKBzqgoMsicnk9q5RYPMHJGKUrT8HeAdo/640?wx_fmt=svg&from=appmsg)

因为
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgINf9I5PuicrmKtOGtXG29oTAEHoQ5hkZ2U1icG6UEYzM3TibTrIQt5WqlAqiaDwowryh/640?wx_fmt=svg&from=appmsg)
。

3.3 叉乘的矩阵表示

所有叉乘运算都可以转换为矩阵形式。对于向量
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgKSFY07bFmD5mdmlD45qnOQ5mu6IVH716UKacPfGMeGTVw56oaFPXlr2rUEHoNsvE/640?wx_fmt=svg&from=appmsg)
，其叉乘矩阵（反对称矩阵）为：

![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgbwJKQgMopFicm2fDVs83HhnVriaHY1iaBWOI7hmdYt8cLPtq7vSoHnoTK2731F5rT2p/640?wx_fmt=svg&from=appmsg)

则
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgMnF26C6CkZbqZP8HO3SPWzFn4CAh7ZytsJp2giaAL3a0tN3nlqffaTMmktNVWlLZz/640?wx_fmt=svg&from=appmsg)

重要性质：

反对称矩阵：
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgnia4tYjJMO6sX0ur42K7KhhJlECwzpORWB1Ex17ajVP7AuMZUFej13rhkrOy1cXibJ/640?wx_fmt=svg&from=appmsg)

多重叉乘的结合律：
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgyGMhLb72ge4qrEibVfnIuCHyiaticAkUCPRlxoWN2rB9N2sR8tkcBSLoR9hngrUd6SI/640?wx_fmt=svg&from=appmsg)

两个反对称矩阵相乘不再是反对称矩阵

四、速度螺旋与旋转矩阵的关系

4.1 旋转矩阵的微分

旋转矩阵
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvg6cIoZWMlribXZ7yJeRqLaBsSIAtqRKBhZ50cXjEARgBnDeUXTwTDllOClwptric8Dd/640?wx_fmt=svg&from=appmsg)
满足正交性条件：
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvg2q2Oouf4e73apqdaIUMbR70uJ9k7BCACjaHKh21aUyKP2rrmkSsj8qFiaPW4z3LUH/640?wx_fmt=svg&from=appmsg)
（其中
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvg6lk7nN36UnOuROicsEcsJLwv4OQE22BEic6d10GkraUyqm3dsUrMxwFLDsy6ianAmk3/640?wx_fmt=svg&from=appmsg)
为单位矩阵）

对两边求时间导数：

![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgHr7DpLzCwR1iajxUZGRerXsxEs60Dr2M6Cu9kZCLvJRV1MqQurRicgUeDkMHWYvZqD/640?wx_fmt=svg&from=appmsg)

![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgT6ocTVSJ6GiafM5XOO1Fpd6vEEHHfIKJVSch368ibTExYicTXmyGoSiacuiazxyMVulpe/640?wx_fmt=svg&from=appmsg)

这表明
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgSdtah7Gea8wDJIFRr2d8FDumtZFTRQANJwPmvjqU66rfguz9NA2fqlDCZ6hBmSNic/640?wx_fmt=svg&from=appmsg)
是一个反对称矩阵，因此可以表示为某个向量的叉乘矩阵：

![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgGFtVd4zEIWRb490dZQpTicwWKR1ZZP9bQ5Xicry06h3PFaRK0Fdn269CZYu0lHRp73/640?wx_fmt=svg&from=appmsg)

由此得到：

![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgZwsEKtaJEJJu9mJaCIPRaUZ1XlYmk5MJ7eXcicSCKqicDDmTeo3n8iceRe0xc0fIKZg/640?wx_fmt=svg&from=appmsg)

这就是角速度的定义来源：角速度
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgTRZU65urhlwIKkg0HibyfMermicyia44qDcdMqKtNeMiaAmjzyeFRR6GQFcWcwqcrGlic/640?wx_fmt=svg&from=appmsg)
本质上来自旋转矩阵的时间导数。

4.2 角速度的本质

从上述推导可以看出：

角速度不是凭空定义的物理量

它来自于旋转矩阵（描述姿态）对时间的微分

这个定义在更高维的旋转群（如
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvg3eQHribiaEsK0T5HZDicpOEBLqvskYwAA0r0N5778qM6lWVD0jcCdL1ibngXopjQ6N8c/640?wx_fmt=svg&from=appmsg)
）中同样适用

维基百科等权威资料都采用这种定义方式

五、罗德里格斯公式与指数映射

5.1 罗德里格斯公式的作用

罗德里格斯公式（Rodrigues' Formula）解决以下问题：已知旋转轴（单位向量
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgTRZU65urhlwIKkg0HibyfMermicyia44qDcdMqKtNeMiaAmjzyeFRR6GQFcWcwqcrGlic/640?wx_fmt=svg&from=appmsg)
，
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgca43xlWQNR3xEMW8bjCT2ZrmowDEhJiaug10YZMNgoc0V1lJ98cPStbR3eMEJJPwu/640?wx_fmt=svg&from=appmsg)
）和旋转角度
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgKVZLyiciboXVhiay8L8a1ntCN40dCqc9wn1xPdq5Uetyia0B7V4I7dcaoAOqz7ItsRAk/640?wx_fmt=svg&from=appmsg)
，求旋转矩阵
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvg6cIoZWMlribXZ7yJeRqLaBsSIAtqRKBhZ50cXjEARgBnDeUXTwTDllOClwptric8Dd/640?wx_fmt=svg&from=appmsg)
。

物理意义：刚体以恒定角速度
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgTRZU65urhlwIKkg0HibyfMermicyia44qDcdMqKtNeMiaAmjzyeFRR6GQFcWcwqcrGlic/640?wx_fmt=svg&from=appmsg)
转动时间
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvg00HQqWSRUGSSghhghLmAul7ADHedFN4qJgfL1L59Cq8mpBeYy9A9ictJibkrvInz83/640?wx_fmt=svg&from=appmsg)
，产生的旋转为
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvg7zXM7icv2aBU5UZdicpAZw2nLIn2ZEib6ldmrxujYiaPNIB36edQRicp1gGzohQ3SFktT/640?wx_fmt=svg&from=appmsg)
。

![image](https://mmbiz.qpic.cn/mmbiz/2YFlzKTpOibicUy7wia70iaWlibufjWGnHwSbnvTsan59JWAYSTf28yv25tAVLVxJ9QK1AgSX6G0Koj8pkCia7kt4Cdw/640?wx_fmt=other&from=appmsg)

图3：罗德里格斯公式的几何意义

5.2 从常微分方程到指数映射

从
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgZwsEKtaJEJJu9mJaCIPRaUZ1XlYmk5MJ7eXcicSCKqicDDmTeo3n8iceRe0xc0fIKZg/640?wx_fmt=svg&from=appmsg)
出发，这是一个矩阵常微分方程。

类比标量情况：
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgKjpbwGqOT3rw0DannGmulYGeWXEExj5MeKV6Adk72ia5lHv9lcFRO7EQ0wSzW0kyz/640?wx_fmt=svg&from=appmsg)
的解为
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgEEl9cTqN8zdLBu7CcWiatWfZCJ8IK558xOFfMnYiaz1z0JFYTKJzY8twlicgCpMIS8T/640?wx_fmt=svg&from=appmsg)

对于矩阵方程，解应该具有类似形式：

![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgBMMjfmSzxmheZicdia0H5eUmtzgZ2F0bdJPfXxxNicYYkgbvymWV4OTyhdGzZIneUvz/640?wx_fmt=svg&from=appmsg)

当初始姿态为
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvg9OKdmBIrw0LmywH78bHRaQLR3CadfT3cDFYUazQLHpcopt4rx0ibwDEEfpoTQgCqA/640?wx_fmt=svg&from=appmsg)
时：

![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgc3ALiaOIPoClfVibJYBZ5usowVdg6DiapVj0iaibUNGGbfbyb2HpvWu4iaNleYia6J0jtJD/640?wx_fmt=svg&from=appmsg)

这个从
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgo7LOWDTaicVHo6Fe1Ar0ZXYU3acbicP3erex9jib1C4P6mJCeNtb98HgQboO9XZibefz/640?wx_fmt=svg&from=appmsg)
到
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvg6cIoZWMlribXZ7yJeRqLaBsSIAtqRKBhZ50cXjEARgBnDeUXTwTDllOClwptric8Dd/640?wx_fmt=svg&from=appmsg)
的映射称为指数映射（Exponential Map），是李群与李代数理论的核心内容。

5.3 罗德里格斯公式的推导

矩阵指数的定义是通过泰勒级数展开：

![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgDcLch7xnqf5Ek96QhAlL1fLDWCV1G0YuSbdjSvic8msKeZWGyBibV4N2ph4ek6jicVC/640?wx_fmt=svg&from=appmsg)

利用反对称矩阵的性质（
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgca43xlWQNR3xEMW8bjCT2ZrmowDEhJiaug10YZMNgoc0V1lJ98cPStbR3eMEJJPwu/640?wx_fmt=svg&from=appmsg)
）：

![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgEbcJibrOuGnKYCvrKf8fyLnwczrT7Cj2XmTemm9bsSPHV2UF4cMcJ5ibnibm3LSmC8H/640?wx_fmt=svg&from=appmsg)

![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgdxUCyJmEk7vwhKibCryz1zNYCwv26wl4hblrmrRdpEAoMEiarRcKxqRtt7bEVK8mnv/640?wx_fmt=svg&from=appmsg)

![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvggPQJgia4neBVZa41sLhmniaGaTKC1Yrhg2xaUkfJrJXGJghQu9N1vcAtqGqiaEtOmVg/640?wx_fmt=svg&from=appmsg)

![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgr17AqTUgwl8iajoHs7jz9YMDksic3mnxr3un7sn7iajeCYEZibSlGbkv8JnquG5iajfVf/640?wx_fmt=svg&from=appmsg)

将级数按
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvg0IEqJd0K8XHpye5Kib7WrbrahWsr74iaia8gmxt9XeSTkkic0DcSEXfPC9c5L9H7BXsf/640?wx_fmt=svg&from=appmsg)
和
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgPaQcSLibJIBwa5bnBjA8Ilyl9X3OPVuLMd9uN2Sbyakibh90UPibib53UOkib0sQq96n8/640?wx_fmt=svg&from=appmsg)
重新组合：

![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgS08nKbib3fqdM1GBX7A6c6akoS1ZprapPaaWeEL1eGcmLKOicKS7xbicqEhmz87UTE1/640?wx_fmt=svg&from=appmsg)

识别出
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgxibwDpVzyBnRloQBZQTTXL8JJpiaxLd2pgd2q9CqicVD5mb5CNKcJ1JxOIC6jNfqHCc/640?wx_fmt=svg&from=appmsg)
和
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgdHOKuVEVW8TDsuSicVFGOXDHjRPZtYGOpDXA275O8Lxrors7CFGRsCxobW2loMJFP/640?wx_fmt=svg&from=appmsg)
的泰勒级数，得到罗德里格斯公式：

![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgLWriaWVcOQNnlOkmsj8icq3K1zC81anZpUSQCMk5TXYxD2IJ4RvXN8Z4ZticEzZfVKV/640?wx_fmt=svg&from=appmsg)

注意：不同教材可能写作
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgib3x31Ua4g9KglkQYmNSwo5LOQTM2YssicbkibK1L9UlRicxw4dqbS6picTsK0x8GABGl/640?wx_fmt=svg&from=appmsg)
，其中
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgvKuLegXOWT5KgGHCaGBOlxFQgMwKV1eiaRDAYJNO4kvqUjibqJbS13FqPezCnBNSG7/640?wx_fmt=svg&from=appmsg)
是旋转向量（Rotation Vector），但本质相同。

六、位置矩阵的微分与速度螺旋

6.1 齐次变换矩阵的微分

刚体的位姿用齐次变换矩阵表示：

![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvg8AvvAmYmk6BaKVNoapaC5GygQaT7EMjqrDSN3lmDibicZxSNBNuajj8lw5vpSicQf68/640?wx_fmt=svg&from=appmsg)

其中
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvg6cIoZWMlribXZ7yJeRqLaBsSIAtqRKBhZ50cXjEARgBnDeUXTwTDllOClwptric8Dd/640?wx_fmt=svg&from=appmsg)
为旋转矩阵，
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgcQL8W19SB8ibcCfwUNF0fPeraaXq77W46FF4DhvjQRtfwSiaIwkArYwRoImDW6YPtK/640?wx_fmt=svg&from=appmsg)
为位置向量。

对
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgjH7ib15wgy1YNMtjicsuiaoCzkAAaicRqahHUUwo8wgUp0FmLqUicKbNwThnb3mNk3ww4/640?wx_fmt=svg&from=appmsg)
求时间导数：

![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgyyP8XQJPUlsBfcBZBFBekBibdviaMAuESbpKIx0VDDfsKdVdv60Xt9S59SYV7e0TG4/640?wx_fmt=svg&from=appmsg)

代入
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgZwsEKtaJEJJu9mJaCIPRaUZ1XlYmk5MJ7eXcicSCKqicDDmTeo3n8iceRe0xc0fIKZg/640?wx_fmt=svg&from=appmsg)
和点速度公式
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgGkldhrdc4uHGOfWOfksyESp2eaYkBMFosOqFqphibV3zKRhA3oviae6bbpWR49gBOc/640?wx_fmt=svg&from=appmsg)
：

![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgFZJmpwAMl6ibK81DOXAtFzVw5QdKsfdrvWlHRAialozUic3A6G6hgAFu4DtibKydjX4g/640?wx_fmt=svg&from=appmsg)

可以验证：

![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvghHkbNRS3e2tN1xA5YngLmAcjcxTwzrriarw5f7GfneAHUkBicnnyEYfrU8dMgpKRh2/640?wx_fmt=svg&from=appmsg)

其中
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgibYNq3NbKEL7WzyMuCLpGLzwa8q6DarehAJgQbLVQuGicfObiaTLibzD70yvQtyE3cLD/640?wx_fmt=svg&from=appmsg)
是速度螺旋的矩阵表示。

6.2 应用实例

问题1：已知刚体当前位姿
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgjH7ib15wgy1YNMtjicsuiaoCzkAAaicRqahHUUwo8wgUp0FmLqUicKbNwThnb3mNk3ww4/640?wx_fmt=svg&from=appmsg)
和速度螺旋
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgOd8HwBhDjicF2udmbjscZa2QV8u4ryQjOiaEPxQeZZC2B6XNjctKCUZClcKbz1tXfP/640?wx_fmt=svg&from=appmsg)
，求位姿的时间导数
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgUzF8ONdlwYUZ29GAB7fuKD6rHy12CjHctCbQ9UP56GZNkNiadonMNCNVLuPviaQ4bt/640?wx_fmt=svg&from=appmsg)
。

解答：

分别对旋转和平移部分求导

![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgZwsEKtaJEJJu9mJaCIPRaUZ1XlYmk5MJ7eXcicSCKqicDDmTeo3n8iceRe0xc0fIKZg/640?wx_fmt=svg&from=appmsg)

![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgGkldhrdc4uHGOfWOfksyESp2eaYkBMFosOqFqphibV3zKRhA3oviae6bbpWR49gBOc/640?wx_fmt=svg&from=appmsg)

组合得到
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgUzF8ONdlwYUZ29GAB7fuKD6rHy12CjHctCbQ9UP56GZNkNiadonMNCNVLuPviaQ4bt/640?wx_fmt=svg&from=appmsg)

问题2：已知刚体上某点
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgcQL8W19SB8ibcCfwUNF0fPeraaXq77W46FF4DhvjQRtfwSiaIwkArYwRoImDW6YPtK/640?wx_fmt=svg&from=appmsg)
的位置和速度螺旋
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgkv4rVmBBbcjul1A3nO3tMicgEHMNJib9tkPB6Js2DYHBRlbdAuZw8ZMclZicN9TJCSf/640?wx_fmt=svg&from=appmsg)
，求该点的线速度
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvga1ib4OGJyH86RGfu8tr2tWEh82Ta9JiaG8DIMDcJVbD1ibicTHNr9fj5ibV8cZDtQDRVp/640?wx_fmt=svg&from=appmsg)
。

解答：直接应用公式
![image](https://mmbiz.qpic.cn/mmbiz_svg/7N2JRaWooRA8piaib6hD0CQGoOQcqNtTvgOMdDWCjib9031f6ibsQnp8bjHzH20RMMcgy9FtXibbMxrKWKgCyCibw4vbovoASh7mO5/640?wx_fmt=svg&from=appmsg)

七、总结与展望

7.1 速度螺旋的核心价值

速度螺旋理论提供了一种优雅而强大的刚体运动描述方法：

统一性
：用六维向量统一描述刚体的线速度和角速度

不变性
：表达形式与参考点选择无关，真实反映运动本质

完整性
：可以完整描述刚体运动的速度场

计算效率
：仅需六个数字即可计算任意点的速度

7.2 与传统方法的对比

对比项

传统三维方法

速度螺旋方法

参考点需求

必须定义刚体上的点

不需要定义点

表达量

9个量（点位置3+点速度3+角速度3）

6个量（速度螺旋）

恒定运动描述

数值随时间变化

数值保持不变

计算复杂度

每点需单独计算

统一公式计算任意点

物理直观性

依赖点的选择

直接反映运动本质
