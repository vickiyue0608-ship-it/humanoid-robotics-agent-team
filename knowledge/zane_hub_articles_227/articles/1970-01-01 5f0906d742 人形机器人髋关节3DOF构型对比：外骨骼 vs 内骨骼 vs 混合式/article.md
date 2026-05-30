---
title: "人形机器人髋关节3DOF构型对比：外骨骼 vs 内骨骼 vs 混合式"
author: "Zane Zhang"
publish_time: "1970-01-01 08:33:46"
url: "https://mp.weixin.qq.com/s/1uIvfHEJc1tw9C7AxRDfhg"
biz: "MzkxNzY1NTY0MQ=="
image_count: 1
---

# 人形机器人髋关节3DOF构型对比：外骨骼 vs 内骨骼 vs 混合式

在人形机器人的下肢机构设计中，髋关节作为连接躯干与大腿的核心运动枢纽，其构型设计直接影响整机的运动能力、负载特性与结构刚度。当前工业界与学术界针对髋关节三自由度（3DOF）实现，主要形成三种技术路线：外骨骼式（Exoskeleton）、内骨骼式（Endoskeleton）以及二者的混合构型。本文从工程实践出发，系统梳理三类构型的技术特征、优势与局限，供从事相关领域的工程师参考。

一、髋关节三自由度的运动学基础

人体髋关节本质上是一个典型的球窝关节，具备三个主要转动自由度：

屈伸（Flexion/Extension）：大腿相对于骨盆的前后摆动，驱动行走步态的主要运动，关节运动范围约为140度（屈曲）至后伸15度

内收外展（Adduction/Abduction）：大腿相对于骨盆的侧向运动，支撑侧向平衡与重心转移，运动范围约为45度外展、30度内收

内外旋（Internal/External Rotation）：大腿相对于骨盆的轴向旋转，影响步态中足尖指向与姿态调整，运动范围约为各40至45度

![image](https://mmbiz.qpic.cn/mmbiz_png/57Q4MfeLoyDKE6GGGYgpEepjVkda9pNuajPia2PoibaqN04RrrqxawUBib4bibzdLPToKUK7b2ZtbSQoKevF6lk8ww6QgGFoawN8RmFkEQuXcKY/640?wx_fmt=png&from=appmsg)

人形机器人要实现类人运动能力，髋关节必须复现上述运动范围，这对机构设计与驱动器选型提出了严苛要求。三种主流构型的核心差异，正在于如何将这三个自由度具体实现为机械结构。

二、外骨骼式构型

2.1 设计原理

外骨骼式构型的核心特征是将驱动器与传动机构布置于关节的外侧，模拟人体肌肉-骨骼系统的外在支撑方式。以美国罗格斯大学THOR机器人的髋关节设计为例，其采用了两自由度并联万向节与连杆驱动的销轴关节组合方案：通过一对并联串联弹性线性致动器协同驱动偏航与翻滚两个自由度，而俯仰自由度则通过Hoeken连杆机构将线性运动转换为旋转输出。

这种构型下，髋骨（Coxa）与外壳作为刚性支撑框架，位于大腿外侧形成类似骨骼外甲的保护结构，故称“外骨骼”。

2.2 技术优势

结构刚度高：由于驱动器与连杆布置于关节外部，轴承跨距大、支承刚度好，在承受外部载荷时变形量小

散热条件好：驱动器外置便于散热设计，电机与减速器的热耗散不直接影响关节核心区域

维护便捷：驱动单元位于外部空间，装配与检修时无需拆解关节核心部位，降低维护成本

2.3 主要局限

质量偏大：驱动器外置导致整体质量增加，髋关节成为下肢质量分布最集中的部位，抬腿时惯性负载显著

运动惯量大：大腿侧质量较大，高速运动时动态响应特性受限

var first_sceen__time = (+new Date());
            if ("" == 1 && document.getElementById('js_content')) {
              document.getElementById('js_content').addEventListener("selectstart",function(e){ e.preventDefault(); });
            }

预览时标签不可点
