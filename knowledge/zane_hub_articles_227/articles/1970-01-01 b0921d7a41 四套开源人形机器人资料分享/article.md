---
title: "四套开源人形机器人资料分享"
author: "Zane Zhang"
publish_time: "1970-01-01 08:33:45"
url: "https://mp.weixin.qq.com/s/ZsuVlzgTUOOXJS6I84P0Zw"
biz: "MzkxNzY1NTY0MQ=="
image_count: 5
---

# 四套开源人形机器人资料分享

Hello，大家好，我是Zane。近期搜集到4套开源的人形机器人资料，分别是智元机器人的灵犀X1，北京人形机器人创新中心的天工TG11，傅利叶的N1，以及国家地方共建人形机器人创新中心的青龙机器人。包括三维图、BOM和装配SOP。现将其特点和资料分享出来供大家学习参考。

智元机器人 灵犀X1

![image](https://mmbiz.qpic.cn/mmbiz_png/2YFlzKTpOib9nqkYPZ0chGrX30nmKPpk8LtjMLenmkf99AWTNsbzm7b0quXG2tzXUSZS8chnQUiaXXRwd3sImtTg/640?wx_fmt=png&from=appmsg)

技术规格：

整体尺寸：130cm × 33kg

自由度配置：全身多自由度设计

设计风格：外观亲和，偏向家用服务场景

开源资料特色： 智元机器人在开源资料的完整性方面表现出色，提供了详细的工具包清单、完整的BOM表（196项明细）以及图文并茂的装配SOP。其3D模型采用平铺式设计，便于学习者理解各部件的装配关系。

技术亮点：

腰部三自由度设计：采用并联结构配合万向节和鱼眼球轴承

关节刚性增强：所有模组输出端增加主轴承设计

装配友好性：详细的DIY装配说明和材料采购链接

傅利叶智能 N1

![image](https://mmbiz.qpic.cn/mmbiz_jpg/2YFlzKTpOib9nqkYPZ0chGrX30nmKPpk83g8SzO6bkmlUzjq7pR2o8eDxia6XXFtlveYfJ0sNF5U0tpvVV7J45ZQ/640?wx_fmt=jpeg&from=appmsg)

技术规格：

整体尺寸：130cm × 38kg

自由度：23个自由度

设计风格：棱角分明的工业化外观

开源资料特色： 傅利叶提供了业内最为详尽的开源资料包，包含4GB以上的装配视频教程，分类清晰的BOM表单以及完整的工艺指导书。资料按五大模块划分：头部与躯干、胸腔外壳、手臂、腰髋、下肢。

技术亮点：

电缆管理：预埋式走线设计，所有关节预留走线空腔

模块化设计：清晰的五大区块划分便于维护和升级

视频教程：提供完整的装配过程视频指导

北京人形机器人创新中心 天工TG11

![image](https://mmbiz.qpic.cn/mmbiz_jpg/2YFlzKTpOib9nqkYPZ0chGrX30nmKPpk87Q9pFIicLAHOO0FUBpPdKqTZsbheG1WLaicmTYExAaX83GqPRyMaiaQxg/640?wx_fmt=jpeg&from=appmsg)

技术规格：

整体尺寸：163cm × 56kg（Pro版）

负载能力：单手负载4kg

自由度：42个自由度

开源资料特色： 天工TG11的开源资料相对精简但结构清晰，主要以STEP文件和PDF技术文档为主。其3D模型层次分明，便于工程应用。

技术亮点：

头部三自由度：标准化接口设计（电源与485通信）

零差云控技术：腰部采用先进的零差云控模组

灵巧手集成：手腕采用俯仰+偏航解耦设计配合灵巧手

国家地方共建人形机器人创新中心 青龙机器人

![image](https://mmbiz.qpic.cn/mmbiz_jpg/2YFlzKTpOib9nqkYPZ0chGrX30nmKPpk8GGibuxZa0uInKa1JicZjM8KLM5RzYHEQ6tkwlYv1qLU4q68fWUu9HRfA/640?wx_fmt=jpeg&from=appmsg)

技术规格：

整体尺寸：185cm × 80kg

自由度：43个自由度

应用定位：大型工业级人形机器人

核心技术模块深度分析

关节系统设计对比

头部关节：

灵犀X1：固定结构，注重稳定性

傅利叶N1：单自由度偏航设计

天工TG11：三自由度全向设计，配备硬限位和标零功能

腰部关节： 灵犀X1的腰部设计最为复杂，实现了三自由度控制（翻滚、俯仰、偏航），采用R86旋转关节配合并联结构。相比之下，傅利叶N1和天工TG11均采用单旋转关节设计，简化了控制复杂度。

手臂关节： 三家产品的前五关节均遵循Pieper原理，采用两两垂直的布局方式。在连接方式上，智元采用抱箍连接，傅利叶使用传统法兰轴向端面连接，天工则采用径向锁螺钉方式。

腿部关节： 髋部前三关节的布局各有特色，智元和傅利叶的设计更接近人体结构。膝关节方面，智元采用直连方式，其他两家采用平行连杆机构。脚部均采用连杆结构，但控制策略有所差异。

电气系统与走线设计

在电气系统设计方面，傅利叶表现最为出色，实现了类似工业六轴机器人的预埋式电缆管理，所有关节都预留了走线空腔。这种设计虽然增加了设备体积，但大大提升了系统的可靠性和维护便利性。

资料获取方式：

关注Zane的公众号，并在公众号里发送对应的下载关键字获取下载链接。

在公众号内发消息：下载|开源人形机器人资料

![image](https://mmbiz.qpic.cn/mmbiz_png/2YFlzKTpOib9nqkYPZ0chGrX30nmKPpk8PbqG72QQR6NRibbTEuEJ6Cg54BaQdBNHnt8Lahm4YrnH2eHRA9NlYiag/640?wx_fmt=png&from=appmsg)
