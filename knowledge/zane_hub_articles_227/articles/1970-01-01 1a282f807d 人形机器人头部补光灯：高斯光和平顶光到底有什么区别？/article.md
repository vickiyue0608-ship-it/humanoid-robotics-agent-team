---
title: "人形机器人头部补光灯：高斯光和平顶光到底有什么区别？"
author: "Zane Zhang"
publish_time: "1970-01-01 08:33:46"
url: "https://mp.weixin.qq.com/s/p8vHbgx8xi5TPLnGx-Xvtg"
biz: "MzkxNzY1NTY0MQ=="
image_count: 3
---

# 人形机器人头部补光灯：高斯光和平顶光到底有什么区别？

在人形机器人的头部，补光灯并不只是“把画面照亮”的附属件。它直接影响双目或多目相机的曝光一致性、反光控制、边缘细节保留、白平衡稳定性，以及近距离抓取、交互、识别时的图像质量。工程上常说的“高斯光”和“平顶光”，本质上是在描述照度剖面的分布方式：前者中心强、边缘弱，后者在有效区域内尽量均匀。即便实际机器人补光灯通常是LED加二次光学系统，而不是理想激光束，这两个术语仍然非常适合用来讨论头部补光的工程取舍。 Edmund Optics：高斯光束传播Edmund Optics：Why Use a Flat Top Laser BeamAdvanced Illumination：A Practical Guide to Machine Vision Lighting

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/57Q4MfeLoyDWSvrMjsGQcuDHrlibceDQRdbiacTibuptbwoCtrNSl0fTgumibyuv3GqKHoASceEpq5dE0ic6ngcKW4fnVvfPSXBiaJhAp13J6micib8/640?wx_fmt=jpeg&from=appmsg)

图示：人形机器人视觉与相机模组应用场景。图源页面：e-con Systems

先给结论：两者没有绝对优劣，只有任务匹配差异

如果头部补光灯主要服务于近距离识别、手眼协同、二维码/纹理读取、室内交互，以及对整幅画面亮度一致性要求较高的视觉任务，平顶光通常更合适；如果系统更关注中远距离补光、中心照度、结构简单、体积成本控制，且算法能够接受边缘照度衰减，高斯型分布往往更容易实现。换句话说，平顶光追求的是“照得更均匀”，高斯光追求的是“中心更亮、系统更省”。 Edmund Optics：Why Use a Flat Top Laser BeamAdvanced Illumination：A Practical Guide to Machine Vision Lighting

为什么机器人补光灯会讨论“高斯”和“平顶”

在机器视觉照明里，真正决定识别质量的，不只是总光通量，而是落到目标表面的辐照度分布、入射角、反射路径，以及相机与被测物之间的几何关系。对于镜面、半镜面、曲面、纹理弱、颜色反差低的目标，照度分布稍有不均，就可能造成局部过曝、边缘欠曝、特征点丢失和测量不稳定。机器视觉照明的核心目标，是在特征与背景之间建立稳定且可重复的对比度，而不是单纯追求“更亮”。 Advanced Illumination：A Practical Guide to Machine Vision Lighting

什么是高斯光：中心高、边缘低，能量自然下滑

高斯分布的典型特征，是以光轴中心为峰值，离轴距离越大，辐照度越低。Edmund Optics给出的高斯光束表达式表明，其强度沿径向按指数规律衰减；工程上常用1/e²位置定义光束半径，意味着到了该半径位置，辐照度已经降到峰值的13.5%。这类分布的直观结果是：中心区域很亮，外围亮度快速衰减。 Edmund Optics：高斯光束传播

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/57Q4MfeLoyCGdjkr8Y3U8eia3EySRWa7U62WmImhvVweBUEH3TzyFulHBc8XF0VicoOkntf6Em60icvNtGw15YHNoIYibCEY4pT6OETicUzicKic1s/640?wx_fmt=png&from=appmsg)

图示：高斯型光斑强度分布，中心峰值明显、边缘连续衰减。图源页面：Wikimedia Commons

高斯光用于机器人头部补光的优点

第一，容易获得较高的中心照度。对于需要照亮画面中央目标、或相机主视场主要集中在中心区域的系统，高斯型分布更容易在有限功率下把中心区域“打亮”。第二，光学实现相对直接，通常不需要额外复杂的整形组件，系统体积、装配难度和成本控制更友好。第三，在一定条件下，高斯型分布对轻微离焦和装调偏差的容忍度，往往比边界更陡的均匀光斑更宽松。 Edmund Optics：高斯光束传播Edmund Optics：Why Use a Flat Top Laser Beam

高斯光用于机器人头部补光的短板

问题同样很明确。由于中心亮、边缘暗，机器人在观察近距离物体时，画面中心和边缘的曝光余量不一致，容易把自动曝光、自动增益和白平衡推向折中状态：中心可能接近饱和，边缘却仍然偏暗。遇到塑料件、金属件、覆膜标签、玻璃、釉面陶瓷等半镜面或镜面目标时，中心高亮区域更容易产生热点和眩光，反而会压掉真正需要的纹理信息。对于双目或多相机系统，这种不均匀还会增加左右视图亮度匹配难度，降低特征提取和匹配稳定性。 Advanced Illumination：A Practical Guide to Machine Vision LightingEdmund Optics：Why Use a Flat Top Laser Beam

什么是平顶光：有效区域内尽量均匀，边界更可控

平顶光，也常被称作Flat Top或Top Hat分布，强调的是在目标工作区域内保持相对恒定的辐照度。Edmund Optics指出，平顶光的优势在于横截面照度更接近常值，没有高斯光典型的“翅膀”能量浪费，边缘过渡更陡，因而在很多对均匀性、阈值一致性和加工/检测窗口要求高的场景中更可预测。评价真实光束有多接近平顶，ISO 13694给出了平坦度因子定义，即平均辐照度与最大辐照度之比，数值越高，说明分布越均匀。 Edmund Optics：Why Use a Flat Top Laser Beam

![image](https://mmbiz.qpic.cn/mmbiz_png/57Q4MfeLoyDKZeUjwywWt9Z3xkchJvKx5nc0rY6rw7WoLO1uZY252SCFbibSzE52xzDjIpfXQCDdicSUx532UQ3ibTsQTsV00BgS8HLDPRW69k/640?wx_fmt=png&from=appmsg)

图示：平顶光在有效区域内更均匀，边缘下降更陡。图源页面：RP Photonics

平顶光用于机器人头部补光的优点

平顶光最直接的价值，是把“照明问题”从中心一小块区域，扩展到整个有效视场。对于机器人头部常见的近场视觉任务——例如桌面抓取、工位交互、按钮识别、标签读取、手部操作观察——相机往往希望在整幅画面内获得尽量一致的亮度与对比度。平顶光在这类任务上更容易控制反射、抑制热点，并降低算法阈值对位置变化的敏感性。对于镜面件和曲面件，如果再配合漫射、同轴或较大的发光面设计，图像稳定性通常明显优于中心峰值过高的分布。 Advanced Illumination：A Practical Guide to Machine Vision LightingEdmund Optics：Why Use a Flat Top Laser Beam

平顶光的代价在哪里

平顶光不是“白送”的。为了把原本自然衰减的分布整形成更均匀的输出，往往需要额外的光学整形结构，这会带来效率损失、装调灵敏度上升、体积增加、热设计压力增大和成本上升。Edmund Optics明确提到，平顶光通常需要附加的beam shaping assembly，而且这类组件对输入光束直径、x-y对准较敏感；它也不像高斯分布那样在传播和变换中天然保持形态。放到机器人头部设计上，这意味着要同时考虑灯体厚度、光学窗口公差、振动后光轴偏移，以及整机跌落冲击后的重复定位问题。 Edmund Optics：Why Use a Flat Top Laser Beam

放到人形机器人头部，真正该比较的不是“光型名称”，而是这6件事

1. 视场照度一致性

如果机器人头部相机需要覆盖较大的水平视场，或者双目之间还要保证相近的亮度分布，平顶光更容易做出一致性。高斯光在中心区域通常更亮，但视场边缘衰减更明显，容易把照明一致性问题转嫁给ISP和算法。 Edmund Optics：Why Use a Flat Top Laser BeamAdvanced Illumination：A Practical Guide to Machine Vision Lighting

2. 镜面反射与热点控制

机器视觉照明经验非常明确：对高反射表面，几何关系和光型结构比单纯提高亮度更重要。高斯光因为中心峰值更高，更容易在塑壳、屏幕、金属边框、玻璃镜片上打出热点；平顶光如果再结合漫射结构，通常更利于把反射“摊开”，减少局部饱和。 Advanced Illumination：A Practical Guide to Machine Vision Lighting

3. 有效能量利用率

如果任务要求把中心小区域照得很亮，高斯光并不一定吃亏，因为它本来就把能量堆在中心。反过来，如果任务要求整个ROI都达到接近统一的亮度门槛，平顶光的能量利用方式更高效，Edmund Optics甚至直接指出，高斯光在阈值型应用中会同时存在“超过阈值的多余能量”和“低于阈值的外围能量”。 Edmund Optics：Why Use a Flat Top Laser Beam

4. 装调容差与结构复杂度

头部空间通常极其紧张，灯板、镜头、散热件、麦克风、扬声器、面罩、装饰盖板往往都在同一体积内竞争空间。高斯型方案通常光学链路更短、元件更少；平顶型方案为了做均匀化，经常需要增加整形件、扩散件或更复杂的二次光学，因此在公差链、装配节拍、热漂移和振动耐受上要更谨慎。 Edmund Optics：高斯光束传播Edmund Optics：Why Use a Flat Top Laser Beam

5. 工作距离变化

机器人头部面对的对象距离变化很大：从手边20到30厘米，到桌面60到80厘米，再到1到2米的人机交互，都属于常见工况。高斯分布随着距离增加会继续扩展并降低峰值，平顶分布也会因传播而退化，后者并不会永远保持“理想平顶”。因此，头部补光选型不能只看某个标称工作距离下的光斑照片，而要看整个目标距离带内的均匀性、中心照度和边缘衰减。 Edmund Optics：高斯光束传播Edmund Optics：Why Use a Flat Top Laser Beam

6. 人眼安全和整机合规

头部补光灯距离人眼近、朝向不确定、使用频率高，安全问题不能后置。Advanced Illumination在机器视觉照明指南中明确提到，IEC 62471已成为LED灯具和灯系统进行光生物安全评估的重要依据，并按风险分组进行管理；对于靠近操作者、可能有频闪或高辐照度的系统，更应在样机阶段就评估风险组，而不是等到结构冻结后再补救。 Advanced Illumination：A Practical Guide to Machine Vision Lighting

一个面向机器人头部设计的简明对比

维度

高斯光

平顶光

照度分布

中心高、边缘低

有效区域内更均匀

画面一致性

一般，边缘易偏暗

更好，利于整幅画面稳定

热点/眩光风险

较高

较低

中心照度能力

强

需靠总功率与整形效率支撑

光学结构

相对简单

相对复杂

装调敏感性

较低

较高

成本与体积

通常更有优势

通常更高

适合任务

中心目标补光、成本受限

近场识别、均匀检测、双目一致性

头部补光灯该怎么选：按任务，不按概念

适合优先考虑平顶光的情况

如果机器人主要做室内近距离交互、桌面操作、取放、扫码、读标签、看按键、看手势，或者双目/多目视觉对整幅图像亮度一致性比较敏感，那么优先考虑平顶型或接近平顶的均匀补光更稳妥。此时真正有价值的，不是中心那一点最亮，而是在目标常出现的整个区域内，把图像质量拉平。 Advanced Illumination：A Practical Guide to Machine Vision LightingEdmund Optics：Why Use a Flat Top Laser Beam

适合优先考虑高斯光的情况

如果系统的主要任务是中距离照明，目标经常位于视场中央，且头部空间、成本、功耗都很紧，高斯型或弱整形方案会更现实。尤其在总功率有限时，把中心照度做高，往往比追求全视场绝对均匀更容易满足最低可用要求。 Edmund Optics：高斯光束传播

实际产品里更常见的是“折中光型”

真正量产的人形机器人头部补光，很少会选纯粹理想的高斯或理想平顶。更常见的做法，是把中心峰值压低、边缘衰减放缓，做成一种“准平顶”或“弱高斯”的折中剖面，再叠加入射角设计、发光面尺寸、扩散手段和相机曝光策略，使系统在主要工作距离上取得整体最优。这是工程设计，不是教科书图形对比。 Edmund Optics：Why Use a Flat Top Laser BeamAdvanced Illumination：A Practical Guide to Machine Vision Lighting

机械与系统设计上还要补的3个判断

散热路径不能只看LED结温

头部补光灯通常靠近相机、SoC散热通道和面罩件。光学整形件越多，腔体越封闭，热堆积越明显。长期热漂移不只影响寿命，也会改变色温、输出稳定性和局部应力，进而影响标定稳定性与光型一致性。机器视觉照明之所以普遍转向LED，一个重要原因就是其稳定性和寿命优势，但前提仍然是热设计过关。 Advanced Illumination：A Practical Guide to Machine Vision Lighting

结构公差要按“光轴系统”管理

平顶型方案比高斯型方案更怕装偏。对机器人头部来说，镜头、灯板、导光件、窗口片、外观盖板往往分属不同零件链，一旦累积偏差过大，均匀照明就会被破坏。开发阶段应把“中心照度、边缘照度、均匀性、左右相机亮度差”纳入结构验收，而不是只看灯能不能点亮。 Edmund Optics：Why Use a Flat Top Laser Beam

安全评估要覆盖近距离凝视场景

人形机器人不是封闭工站设备。它会靠近人、看向人，也可能在儿童视线高度工作。因此，头部补光的IEC 62471风险评估、频闪策略、占空比控制和默认亮度上限，建议从样机阶段就纳入系统定义。合规不是最后一道文档动作，而是架构约束。 Advanced Illumination：A Practical Guide to Machine Vision Lighting

结语

对人形机器人头部补光灯而言，高斯光和平顶光的差别，归根到底是“把光集中在中心”还是“把光铺平到任务区域”。前者更容易做出高中心照度、结构简单、成本友好的方案；后者更适合近场机器视觉、双目一致性和反光受控的场景。真正成熟的设计，通常不是在概念上二选一，而是围绕目标工作距离、视场大小、目标表面特性、功耗预算、装调公差与安全约束，做出一个对系统最有利的照度分布。用工程语言概括：先定义任务窗口，再定义光型，而不是反过来。 Edmund Optics：高斯光束传播Edmund Optics：Why Use a Flat Top Laser BeamAdvanced Illumination：A Practical Guide to Machine Vision Lighting

参考资料

Edmund Optics，《高斯光束传播》：

https://www.edmundoptics.cn/knowledge-center/application-notes/lasers/gaussian-beam-propagation/

Edmund Optics,Why Use a Flat Top Laser Beam?：

https://www.edmundoptics.com/knowledge-center/application-notes/optics/why-use-a-flat-top-laser-beam/

Advanced Illumination,A Practical Guide to Machine Vision Lighting：

https://advancedillumination.com/a-practical-guide-to-machine-vision-lighting/

e-con Systems,Humanoid Robot Vision - Cameras & Edge AI Compute Solutions：

https://www.e-consystems.com/markets/industrial-cameras/humanoid-robots.asp

RP Photonics,Flat-top Beams：

https://www.rp-photonics.com/flat_top_beams.html

Wikimedia Commons,Gaussian-beam intensity surfaceplot：

https://commons.wikimedia.org/wiki/File:Gaussian-beam_intensity_surfaceplot.png

var first_sceen__time = (+new Date());
            if ("" == 1 && document.getElementById('js_content')) {
              document.getElementById('js_content').addEventListener("selectstart",function(e){ e.preventDefault(); });
            }

预览时标签不可点
