# Source Map

This map lists starting sources for deep research. Verify details live before making current product or standards claims.

For the expanded paper-first list, read `paper-library.md`. It separates papers/books/preprints from standards, vendor documentation, and GitHub implementations.

## Deep Research Skill and Skill Format

- 199-biotechnologies, `claude-deep-research-skill`, GitHub: https://github.com/199-biotechnologies/claude-deep-research-skill — installed skill used as the research workflow foundation.
- OpenAI skills repository: https://github.com/openai/skills — Codex skill packaging reference.

## Local Practical Article Corpus

Use this corpus as Chinese practical engineering and industry-observation material. It is useful for finding realistic design questions, teardown leads, terminology, and failure-check prompts, but it is not a replacement for primary papers, standards, datasheets, simulations, or measured tests.

- Zane Hub topic map: `references/zane-hub-articles.md`
- Zane Hub full title/url/path index: `references/zane-hub-index.jsonl`
- Repository article root: `knowledge/zane_hub_articles_227`
- Evidence tier: default `S4 reputable engineering` for traceable engineering explanations; downgrade to `S5 anecdotal` for uncited market claims, rankings, or unsupported comparisons.

## Open-Source Implementation Starting Points

Use these as implementation leads. Verify license, maintenance state, dependencies, supported hardware/simulator, and runnable examples live before using them in a design decision.

- OpenLoong Dynamics Control, GitHub: https://github.com/loongOpen/Openloong-dyn-control — open humanoid MPC + WBC style control codebase; useful as a humanoid control architecture reference.
- `wb-humanoid-mpc`, GitHub: https://github.com/manumerous/wb-humanoid-mpc — whole-body MPC style humanoid research implementation; inspect paper links and build status before reuse.
- `isaac-whole-body-control`, GitHub: https://github.com/Andy-xiong6/isaac-whole-body-control — Isaac-simulation whole-body-control style implementation lead.
- `humanoid-gym`, GitHub: https://github.com/roboterax/humanoid-gym — humanoid locomotion RL training/deployment lead; verify robot target and sim-to-real assumptions.
- Booster Gym, GitHub: https://github.com/BoosterRobotics/booster_gym — humanoid reinforcement-learning training framework from a robot company; useful for RL workflow comparison.
- Holosoma, GitHub: https://github.com/SysCV/holosoma — project page/repo for whole-body teleoperation and RL style humanoid control; treat as research implementation.
- HECTOR, GitHub: https://github.com/DRCL-USC/HECTOR — humanoid whole-body control research implementation lead from an academic lab.
- RoMoCo, GitHub: https://github.com/DRCL-USC/RoMoCo — robust motion control implementation lead for legged/humanoid control research.
- ETH ASL Kalibr, GitHub: https://github.com/ethz-asl/kalibr — visual-inertial calibration toolbox; strong implementation source for camera-IMU calibration.
- OpenVINS, GitHub: https://github.com/rpng/open_vins — visual-inertial state-estimation implementation and documentation lead.
- OCS2, GitHub: https://github.com/leggedrobotics/ocs2 — optimal-control framework widely used in legged robotics research; useful for MPC/control architecture comparisons.
- TopOpt, GitHub: https://github.com/topopt/TopOpt_in_PETSc — topology optimization implementation lead for large-scale FEA-style optimization.

## Motion, Dynamics, Control, and Gait

- Kajita et al., "Biped Walking Pattern Generation by using Preview Control of Zero-Moment Point", DOI: https://doi.org/10.1109/ICRA.2003.1241826 — classic ZMP preview-control paper.
- Pratt et al., "Capture Point: A Step toward Humanoid Push Recovery", DOI: https://doi.org/10.1109/ICHR.2006.321385 — classic capture-point balance reference.
- Sentis and Khatib, "Synthesis of Whole-Body Behaviors through Hierarchical Control of Behavioral Primitives", DOI: https://doi.org/10.1177/0278364908093809 — foundational whole-body control reference.
- Escande, Mansard, Wieber, "Hierarchical quadratic programming: Fast online humanoid-robot motion generation", DOI: https://doi.org/10.1177/0278364914521306 — HQP formulation and online humanoid motion generation.
- "Whole-Body Control of Humanoid Robots", DOI: https://doi.org/10.1007/978-94-007-7194-9_51-2 — WBC architecture/reference chapter.
- Henze, Roa, Ott, "Passivity-based whole-body balancing for torque-controlled humanoid robots in multi-contact scenarios", DOI: https://doi.org/10.1177/0278364916653815 — multi-contact torque-control balancing reference.
- Kuindersma et al., "Optimization-based locomotion planning, estimation, and control design for the Atlas humanoid robot", DOI: https://doi.org/10.1007/s10514-015-9479-3 — integrated humanoid planning/control/estimation.
- Wieber, "Trajectory free linear model predictive control for stable walking in the presence of strong perturbations", DOI: https://doi.org/10.1109/ICHR.2006.321375 — MPC walking reference.
- "Simulation of Disturbance Recovery Based on MPC and Whole-Body Dynamics Control of Biped Walking", PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC7288453/ — accessible MPC/WBC disturbance recovery example.
- "Expressive Whole-Body Control for Humanoid Robots", arXiv: https://arxiv.org/abs/2402.16796 — recent RL-based whole-body control example; treat as preprint.
- "Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation", arXiv: https://arxiv.org/abs/2403.04436 — recent humanoid RL/teleoperation example; treat as preprint.

## Calibration and Sensing

- ETH ASL Kalibr toolbox, GitHub: https://github.com/ethz-asl/kalibr — widely used visual-inertial calibration toolbox and docs.
- Furgale et al., "Unified temporal and spatial calibration for multi-sensor systems", DOI: https://doi.org/10.1109/IROS.2013.6696514 — Kalibr-related spatiotemporal calibration.
- Mirzaei and Roumeliotis, "A Kalman Filter-Based Algorithm for IMU-Camera Calibration", PDF: https://www-users.cse.umn.edu/~stergios/papers/TRO_08-IMU-Camera-calibration.pdf — observability and calibration basis.
- Birbach, Frese, Baeuml, "Rapid calibration of a multi-sensorial humanoid's upper body", DOI: https://doi.org/10.1177/0278364914548201 — humanoid head/upper-body multi-sensor calibration.
- "Multi-Visual-Inertial System: Analysis, Calibration and Estimation", arXiv: https://arxiv.org/abs/2308.05303 — multi-camera/multi-IMU calibration; treat as preprint.
- Li and Mourikis, "High-precision, consistent EKF-based visual-inertial odometry", DOI: https://doi.org/10.1177/0278364913481251 — EKF VIO consistency and online calibration.
- "Visual-inertial state estimation with camera and camera-IMU calibration", DOI: https://doi.org/10.1016/j.robot.2019.103249 — VIO and calibration reference.
- "A nonlinear state estimation framework for humanoid robots", DOI: https://doi.org/10.1016/j.robot.2022.104100 — humanoid IMU/joint/FSR fusion and CoM/DCM estimation.
- "Practical whole-body elasto-geometric calibration of a humanoid robot: Application to the TALOS robot", DOI: https://doi.org/10.1016/j.robot.2023.104365 — whole-body humanoid calibration reference.

## Simulation, CAE, and Optimization

- Ansys, "What is topology optimization?": https://www.ansys.com/en-gb/simulation-topics/what-is-topology-optimization — official overview of topology optimization and multi-load/multi-physics context.
- Altair OptiStruct documentation: https://help.altair.com/hwsolvers/os/topics/solvers/os/optimization_topology_c.htm — official topology optimization solver reference.
- Abaqus documentation: https://help.3ds.com/ — official nonlinear/contact/explicit/thermal FEA documentation hub.
- Abaqus explicit dynamic analysis docs: https://docs.software.vt.edu/abaqusv2025/English/SIMACAEANLRefMap/simaanl-c-expdynamic.htm — explicit impact/contact analysis reference.
- Abaqus contour value computation docs: https://docs.software.vt.edu/abaqusv2024/English/SIMACAECAERefMap/simacae-c-conconceptcompute.htm — official source for nodal/element/averaging contour interpretation.
- COMSOL Multiphysics documentation: https://doc.comsol.com/ — official multiphysics documentation hub.
- COMSOL Structural Mechanics theory: https://doc.comsol.com/6.3/doc/com.comsol.help.sme/sme_ug_theory.06.001.html — official structural mechanics theory reference.
- COMSOL AC/DC module introduction: https://doc.comsol.com/6.3/doc/com.comsol.help.acdc/acdc_introduction.02.01.html — official low-frequency electromagnetic simulation reference.
- COMSOL Heat Transfer module introduction: https://doc.comsol.com/6.3/doc/com.comsol.help.heat/heat_introduction.02.01.html — official heat-transfer modeling reference.
- MSC Adams documentation: https://hexagon.com/products/adams — multibody dynamics and controls co-simulation product source.
- FMI 3.0.2 specification: https://fmi-standard.org/docs/3.0.2/ — official model exchange/co-simulation interface specification.
- Bendsøe and Sigmund, "Topology Optimization: Theory, Methods, and Applications", DOI: https://doi.org/10.1007/978-3-662-05086-6 — classic topology optimization reference.
- Sigmund, "A 99 line topology optimization code written in Matlab", DOI: https://doi.org/10.1007/s001580050176 — classic reproducible topology optimization paper.
- Suresh, "Fatigue of Materials", DOI: https://doi.org/10.1017/CBO9780511806575 — classic fatigue reference.
- Shabana, "Dynamics of Multibody Systems", DOI: https://doi.org/10.1017/9781108757553 — multibody dynamics reference.
- "Topology optimization for additive manufacturing using a component of a humanoid robot", DOI: https://doi.org/10.1016/j.procir.2018.03.270 — humanoid component AM/topology optimization case.
- "Optimal design of lightweight serial robots by integrating topology optimization and parametric system optimization", DOI: https://doi.org/10.1016/j.mechmachtheory.2018.10.015 — robot lightweight topology/system optimization.
- "A topology optimization method of robot lightweight design based on the finite element model of assembly and its applications", DOI: https://doi.org/10.1177/0036850420936482 — assembly-level robot lightweight topology optimization.

## Joint Actuation and Transmission

- Harmonic Drive technical data/documentation: https://www.harmonicdrive.net/support/technical-documentation — strain-wave reducer primary vendor reference.
- SKF roller screws: https://www.skf.com/group/products/linear-motion/roller-screws — primary vendor reference for roller-screw concepts and selection.
- Bosch Rexroth planetary screw assemblies: https://www.boschrexroth.com/ — primary vendor source; verify exact catalog live.
- ISO 3408-5 ball screws load ratings and life: https://www.iso.org/standard/34618.html — official ball-screw life/load standard listing.
- ISO 3408-4 ball screws static axial rigidity: https://www.iso.org/standard/34617.html — official ball-screw rigidity standard listing.
- THK ball screw service life: https://www.thk.com/sg/en/products/ball_screw/selection/0010/ — vendor selection reference.
- THK ball screw allowable rotational speed PDF: https://www.thk.com/en/products/pdf/en_a15_032.pdf — vendor speed/critical-speed reference.
- FAULHABER Application Note 151: https://www.faulhaber.com/fileadmin/Import/Media/AN151_EN.pdf — motor controller tuning and inertia-factor reference.
- maxon gearhead mass inertia support: https://support.maxongroup.com/hc/en-us/articles/360006129633-Gearhead-Mass-inertia — vendor explanation of inertia reflection.
- NASA Tech Briefs, rotary series elastic actuator: https://www.techbriefs.com/component/content/article/20196-msc-24736-1 — SEA implementation example.
- Techrobots humanoid joint actuator overview: https://techsoft-robots.com/en/news/659 — recent industry article; use as lower-tier market/architecture lead, not final proof.
- Unitree G1-D platform: https://www.unitree.com/G1-D — public humanoid platform page; use for architecture leads only.
- Figure BotQ manufacturing page: https://www.figure.ai/news/botq — public manufacturing/vertical-integration lead; verify current status live.
- "Bipedal Humanoid Hardware Design: a Technology Review", DOI: https://doi.org/10.1007/s43154-021-00050-9 — humanoid hardware and actuator architecture review.
- "Mechanics of humanoid robot", DOI: https://doi.org/10.1080/01691864.2020.1813624 — humanoid mechanics and actuator/transmission context.
- "A review of planetary roller screw mechanism for development and new trends", DOI: https://doi.org/10.1177/09544062221106287 — planetary roller screw review.
- "Performance and challenges of planetary roller screw mechanism in complex conditions: A comprehensive review of recent progress", DOI: https://doi.org/10.1177/09544062251318929 — recent PRSM complex-condition review.
- "Series Elastic Actuator: Design, Analysis and Comparison", DOI: https://doi.org/10.5772/63573 — SEA design/comparison reference.
- "Development of a high-performance direct-drive joint", DOI: https://doi.org/10.1163/156855302760121918 — direct-drive joint design reference.

## Electrical, Sensing, and Synchronization

- IEEE 1588-2019 PTP standard page: https://standards.ieee.org/ieee/1588/6825/ — official precision time synchronization standard.
- Beckhoff EtherCAT Distributed Clocks: https://infosys.beckhoff.com/content/1033/ethercatsystem/2469118347.html — official EtherCAT DC synchronization reference.
- CAN in Automation CAN FD overview: https://can-cia.org/can-knowledge/can-fd-the-basic-idea — official CAN FD overview.
- TI sensored FOC application note: https://www.ti.com/lit/ug/tidub03/tidub03.pdf — official PMSM FOC reference.
- ADI AN-1407 PWM in AC motor control: https://www.analog.com/media/en/technical-documentation/application-notes/an-1407.pdf — official PWM/dead-time reference.
- TI TIDA-01541 current/voltage sensing: https://www.ti.com/tool/TIDA-01541 — official inverter sensing reference design.
- ADI AN-1397 EnDat encoder RS-485: https://www.analog.com/en/resources/app-notes/an-1397.html — official encoder link interface note.
- Bosch BMI088 IMU: https://www.bosch-sensortec.com/en/products/motion-sensors/imus/bmi088 — vendor IMU reference.
- Sony global shutter image sensor: https://www.sony-semicon.com/en/products/is/industry/global-shutter.html — vendor global shutter reference.
- Basler rolling shutter explanation: https://www.baslerweb.com/en-us/learning/cmos-rolling-shutter-cameras/ — vendor rolling shutter explanation.

## Testing and Safety

- ISO 9283:1998, "Manipulating industrial robots - Performance criteria and related test methods": https://webstore.ansi.org/standards/iso/iso92831998 — performance test standard listing.
- ISO 12100:2010 safety of machinery risk assessment: https://www.iso.org/standard/51528.html — official risk-assessment standard listing.
- ISO 13849-1:2023 safety-related control systems: https://www.iso.org/standard/73481.html — official safety-control standard listing.
- ISO 13482:2014 personal care robot safety: https://www.iso.org/standard/53820.html — official service/personal-care robot safety standard listing.
- ISO/TR 23482-1:2020 safety-related test methods: https://www.iso.org/standard/71564.html — official test-method technical report listing.
- ISO/IEC 17025:2017 testing/calibration laboratories: https://www.iso.org/standard/66912.html — official lab competence and traceability standard listing.
- ISO/FDIS 18646-5 legged robot locomotion performance: https://www.iso.org/standard/86850.html — under-development legged robot locomotion performance test reference.
- ISO 10218-1:2025, "Robotics - Safety requirements - Part 1: Industrial robots": https://www.iso.org/standard/73933.html — robot safety standard listing.
- RoboDK ISO 9283 documentation: https://www.robodk.com/doc/en/Robot-Validation-ISO9283.html — practical explanation of ISO 9283-style validation.
- Universal Robots safety FAQ: https://www.universal-robots.com/articles/ur/safety/safety-faq/ — vendor safety reference mentioning ISO 10218-1:2025 context.
- Kollmorgen manual tuning: https://webhelp.kollmorgen.com/akd2g/english/Content/Tuning/Manually-Tuning/Manually-Tuning-A-System.htm — official servo tuning and plant understanding reference.
- NI voltage/current/power measurement: https://www.ni.com/en/shop/data-acquisition/how-to-measure-voltage--current--and-power.html — official measurement reference.
- "Fault Types and Diagnostic Methods of Manipulator Robots: A Review": https://www.mdpi.com/1424-8220/25/6/1716 — open-access review of robot faults and diagnosis.
- "A survey on control of humanoid fall over", DOI: https://doi.org/10.1016/j.robot.2023.104443 — humanoid fall prediction/recovery survey.
- "System-Level Fault Diagnosis for an Industrial Wafer Transfer Robot with Multi-Component Failure Modes", DOI: https://doi.org/10.3390/app131810243 — system-level multi-component robot fault diagnosis.
- "Fault accommodation in compliant quadruped robot through a moving appendage mechanism", DOI: https://doi.org/10.1016/j.mechmachtheory.2017.10.011 — legged robot joint/sensor fault accommodation reference.
