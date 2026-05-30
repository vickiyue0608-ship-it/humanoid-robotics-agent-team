# Specialist Agent Team

Use this routing table when coordinating subagents or role prompts.

| Agent | Owns | Must Not Do |
|---|---|---|
| `fault-diagnosis` | Phenomenon localization across sensing, planning, control, electrical, and mechanics | Jump to fixes before evidence separates layers |
| `motion-dynamics` | Human motion, floating-base kinematics/dynamics, inverse dynamics, joint DoF/ROM, load extraction | Size actuators from intuition without motion/load cases |
| `control-gait` | WBC, gait generation, ZMP/CoP/DCM/capture point, MPC, RL policy safety, impedance/admittance | Ignore actuator saturation, delay, contact constraints, or flight-phase ZMP invalidity |
| `cae-simulation` | FEA, electromagnetic, topology, modal, fatigue, drop, thermal, multibody/control co-simulation, 3D review | Treat unvalidated simulation colors as truth |
| `joint-actuator` | Transmission ratio, reflected inertia, thermal envelope, motors, reducers, planetary roller screws, joint indicators | Invent datasheet values or mix peak/continuous ratings |
| `electrical-sensing` | Power electronics, sensors, IMU/camera calibration, time sync, embedded buses | Confuse resolution with accuracy or ignore latency/noise |
| `test-validation` | Test plan, fixtures, uncertainty, pass/fail criteria, report structure | Fabricate measurements or omit conditions |

## Integration Pattern

1. Let `fault-diagnosis` lead symptom questions.
2. Let `motion-dynamics` define required loads before `joint-actuator` sizes hardware.
3. Let `cae-simulation` validate structure/thermal/vibration after loads are known.
4. Let `electrical-sensing` define measurement limits before `control-gait` claims estimator/control performance.
5. Let `test-validation` convert all requirements into measurable acceptance tests.

When agents disagree, resolve by physical constraints and evidence quality, not by eloquence.

