# Humanoid Robotics Paper Library

This is the paper-first library for the humanoid robotics agent team. Treat it as a curated starting map, not as a complete or final literature review. Verify links, publication status, and claims live before using any item for procurement, safety, or design release decisions.

## Motion, Dynamics, WBC, MPC, and Gait

1. Kajita et al., "Biped Walking Pattern Generation by using Preview Control of Zero-Moment Point"  
   DOI: https://doi.org/10.1109/ICRA.2003.1241826  
   Use: classical ZMP preview-control baseline.

2. Pratt et al., "Capture Point: A Step toward Humanoid Push Recovery"  
   DOI: https://doi.org/10.1109/ICHR.2006.321385  
   Use: capture-point push-recovery and dynamic balance.

3. Sentis and Khatib, "Synthesis of Whole-Body Behaviors through Hierarchical Control of Behavioral Primitives"  
   DOI: https://doi.org/10.1177/0278364908093809  
   Use: foundational whole-body behavior control.

4. Sentis and Khatib, "A Whole-Body Control Framework for Humanoids"  
   PDF: https://ai.stanford.edu/manips/publications/pdfs/Sentis_2006_ICRA.pdf  
   Use: early operational-space whole-body control framing.

5. Escande, Mansard, Wieber, "Hierarchical quadratic programming: Fast online humanoid-robot motion generation"  
   DOI: https://doi.org/10.1177/0278364914521306  
   Use: HQP formulation and online humanoid motion generation.

6. "Whole-Body Control of Humanoid Robots"  
   DOI: https://doi.org/10.1007/978-94-007-7194-9_51-2  
   Use: reference chapter covering WBC architectures, limitations, and implementation references.

7. Henze, Roa, Ott, "Passivity-based whole-body balancing for torque-controlled humanoid robots in multi-contact scenarios"  
   DOI: https://doi.org/10.1177/0278364916653815  
   Use: torque-controlled multi-contact balancing and passivity.

8. Henze, "Whole-Body Control for Multi-Contact Balancing of Humanoid Robots: Design and Experiments"  
   DOI: https://doi.org/10.1007/978-3-030-87212-0  
   Use: book-length WBC multi-contact balancing reference.

9. Kuindersma et al., "Optimization-based locomotion planning, estimation, and control design for the Atlas humanoid robot"  
   DOI: https://doi.org/10.1007/s10514-015-9479-3  
   Use: integrated humanoid locomotion planning, estimation, and control on Atlas.

10. Wieber, "Trajectory free linear model predictive control for stable walking in the presence of strong perturbations"  
    DOI: https://doi.org/10.1109/ICHR.2006.321375  
    Use: MPC walking reference.

11. "Simulation of Disturbance Recovery Based on MPC and Whole-Body Dynamics Control of Biped Walking"  
    PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC7288453/  
    Use: accessible MPC/WBC disturbance-recovery example.

12. "Biped Walking Based on Stiffness Optimization and Hierarchical Quadratic Programming"  
    PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC7957877/  
    Use: HQP-style biped walking with stiffness optimization.

13. "A survey: dynamics of humanoid robots"  
    DOI: https://doi.org/10.1080/01691864.2020.1778524  
    Use: humanoid dynamics survey.

## Learning-Based Locomotion and Sim-to-Real

14. "Learning-based legged locomotion: State of the art and future perspectives"  
    DOI: https://doi.org/10.1177/02783649241312698  
    Use: recent learning-based legged locomotion survey, including biped/humanoid trends.

15. "Crossing the Reality Gap: A Survey on Sim-to-Real Transferability of Robot Controllers in Reinforcement Learning"  
    DOI: verify live from source before citation.  
    Use: sim-to-real transfer survey; keep DOI verification step before final reports.

16. "A Survey of Sim-to-Real Transfer Techniques Applied to Reinforcement Learning for Bioinspired Robots"  
    DOI: verify live from source before citation.  
    Use: bioinspired robot RL sim-to-real survey.

17. "Deep Reinforcement Learning for Real-World Humanoid Robot Locomotion Control with Automatic Reward Learning"  
    DOI: https://doi.org/10.34133/research.1123  
    Use: real-world humanoid RL locomotion with automatic reward learning.

18. "Expressive Whole-Body Control for Humanoid Robots"  
    arXiv: https://arxiv.org/abs/2402.16796  
    Use: recent expressive RL/WBC humanoid controller; treat as preprint.

19. "Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation"  
    arXiv: https://arxiv.org/abs/2403.04436  
    Use: humanoid whole-body teleoperation and learning; treat as preprint.

20. "Learning Sim-to-Real Humanoid Locomotion in 15 Minutes"  
    arXiv: https://arxiv.org/abs/2512.01996  
    Use: fast humanoid RL training lead; treat as preprint and verify date/status live.

## Hardware Architecture, Actuators, and Transmission

21. "Bipedal Humanoid Hardware Design: a Technology Review"  
    DOI: https://doi.org/10.1007/s43154-021-00050-9  
    Use: humanoid hardware architecture, actuator classes, and design trade-offs.

22. Santos, Moreira, Silva, "Mechatronic Design of a New Humanoid Robot with Hybrid Parallel Actuation"  
    DOI: https://doi.org/10.5772/51535  
    Use: humanoid mechatronic design and hybrid parallel actuation.

23. "Mechanics of humanoid robot"  
    DOI: https://doi.org/10.1080/01691864.2020.1813624  
    Use: humanoid mechanics review; includes actuator/transmission context.

24. "A review of planetary roller screw mechanism for development and new trends"  
    DOI: https://doi.org/10.1177/09544062221106287  
    Use: planetary roller screw mechanism development and trend review.

25. "Performance and challenges of planetary roller screw mechanism in complex conditions: A comprehensive review of recent progress"  
    DOI: https://doi.org/10.1177/09544062251318929  
    Use: recent PRSM complex-condition performance/challenge review.

26. "Series Elastic Actuator: Design, Analysis and Comparison"  
    DOI: https://doi.org/10.5772/63573  
    Use: SEA design and comparison reference.

27. "Continuously-variable series-elastic actuator"  
    PubMed: https://pubmed.ncbi.nlm.nih.gov/24187221/  
    Use: variable SEA for legged robots/prostheses; verify DOI live if needed.

28. "Energy-Efficient Actuator Design Principles for Robotic Leg Prostheses and Exoskeletons: A Review of Series Elasticity and Backdrivability"  
    Source: https://ouci.dntb.gov.ua/en/works/4EYOWAO4/  
    Use: series elasticity/backdrivability review relevant to legged actuator design; verify publisher/DOI live.

29. "Development of a high-performance direct-drive joint"  
    DOI: https://doi.org/10.1163/156855302760121918  
    Use: direct-drive joint design reference.

30. "Hybrid Adaptive Control for Series Elastic Actuator of Humanoid Robot"  
    arXiv: https://arxiv.org/abs/2201.09458  
    Use: SEA control for humanoid walking; treat as preprint.

## Calibration, VIO, State Estimation, and Sensor Fusion

31. Furgale et al., "Unified temporal and spatial calibration for multi-sensor systems"  
    DOI: https://doi.org/10.1109/IROS.2013.6696514  
    Use: spatiotemporal multi-sensor calibration and Kalibr lineage.

32. Mirzaei and Roumeliotis, "A Kalman Filter-Based Algorithm for IMU-Camera Calibration"  
    PDF: https://www-users.cse.umn.edu/~stergios/papers/TRO_08-IMU-Camera-calibration.pdf  
    Use: IMU-camera calibration observability and filtering foundation.

33. Birbach, Frese, Baeuml, "Rapid calibration of a multi-sensorial humanoid's upper body"  
    DOI: https://doi.org/10.1177/0278364914548201  
    Use: humanoid head/upper-body multisensor calibration with kinematic chain.

34. Li and Mourikis, "High-precision, consistent EKF-based visual-inertial odometry"  
    DOI: https://doi.org/10.1177/0278364913481251  
    Use: EKF VIO consistency and online camera-IMU calibration.

35. "Visual-inertial state estimation with camera and camera-IMU calibration"  
    DOI: https://doi.org/10.1016/j.robot.2019.103249  
    Use: VIO and calibration review/reference.

36. "Camera/IMU calibration revisited"  
    DOI: https://doi.org/10.1109/JSEN.2017.2674307  
    Use: practical camera-IMU calibration reference.

37. "A nonlinear state estimation framework for humanoid robots"  
    DOI: https://doi.org/10.1016/j.robot.2022.104100  
    Use: humanoid IMU/joint/FSR fusion and CoM/DCM state estimation.

38. "Practical whole-body elasto-geometric calibration of a humanoid robot: Application to the TALOS robot"  
    DOI: https://doi.org/10.1016/j.robot.2023.104365  
    Use: whole-body humanoid calibration with elasticity and geometry.

39. "The TUM VI Benchmark for Evaluating Visual-Inertial Odometry"  
    arXiv: https://arxiv.org/abs/1804.06120  
    Use: VIO benchmark and sensor data reference.

40. "Multi-Visual-Inertial System: Analysis, Calibration and Estimation"  
    arXiv: https://arxiv.org/abs/2308.05303  
    Use: multi-camera/multi-IMU calibration/estimation; treat as preprint.

## CAE, Topology Optimization, Fatigue, and Multibody Dynamics

41. Bendsøe and Sigmund, "Topology Optimization: Theory, Methods, and Applications"  
    DOI: https://doi.org/10.1007/978-3-662-05086-6  
    Use: classic topology optimization textbook.

42. Sigmund, "A 99 line topology optimization code written in Matlab"  
    DOI: https://doi.org/10.1007/s001580050176  
    Use: reproducible topology optimization baseline.

43. Suresh, "Fatigue of Materials"  
    DOI: https://doi.org/10.1017/CBO9780511806575  
    Use: classic fatigue mechanics reference.

44. Shabana, "Dynamics of Multibody Systems"  
    DOI: https://doi.org/10.1017/9781108757553  
    Use: multibody dynamics reference.

45. "Topology optimization for additive manufacturing using a component of a humanoid robot"  
    DOI: https://doi.org/10.1016/j.procir.2018.03.270  
    Use: topology optimization for AM using humanoid robot component.

46. "Optimal design of lightweight serial robots by integrating topology optimization and parametric system optimization"  
    DOI: https://doi.org/10.1016/j.mechmachtheory.2018.10.015  
    Use: integrated lightweight robot topology/system optimization.

47. "A topology optimization method of robot lightweight design based on the finite element model of assembly and its applications"  
    DOI: https://doi.org/10.1177/0036850420936482  
    Use: robot lightweight topology optimization with assembly-level FEA.

48. "Topology optimization design of a lightweight integrated manifold with low pressure loss in a hydraulic quadruped robot actuator"  
    URL: https://ms.copernicus.org/articles/12/249/2021/index.html  
    Use: actuator/manifold lightweight topology optimization lead; verify DOI/source details live.

## Diagnosis, Testing, and Fault Handling

49. "Fault Types and Diagnostic Methods of Manipulator Robots: A Review"  
    URL: https://www.mdpi.com/1424-8220/25/6/1716  
    Use: robot fault categories and diagnostic methods review.

50. "System-Level Fault Diagnosis for an Industrial Wafer Transfer Robot with Multi-Component Failure Modes"  
    DOI: https://doi.org/10.3390/app131810243  
    Use: system-level multi-component robot fault diagnosis.

51. "A Robust Online Diagnostic Strategy of Inverter Open-Circuit Faults for Robotic Joint BLDC Motors"  
    URL: https://www.mdpi.com/2075-1702/12/7/430  
    Use: joint BLDC/inverter open-circuit diagnostic reference; verify DOI live if used formally.

52. "Fault accommodation in compliant quadruped robot through a moving appendage mechanism"  
    DOI: https://doi.org/10.1016/j.mechmachtheory.2017.10.011  
    Use: legged robot joint/sensor fault accommodation.

53. "A survey on control of humanoid fall over"  
    DOI: https://doi.org/10.1016/j.robot.2023.104443  
    Use: humanoid fall prediction, recovery, and controlled falling.

