# Core Humanoid Robotics Knowledge

This file is the minimum stable knowledge base for the humanoid robotics agent team. It is not a complete handbook. Use it to start reasoning correctly before running deeper paper/GitHub research.

## System View

A humanoid robot is a floating-base, multi-contact, high-DoF, actuator-limited, sensor-limited, thermally constrained electromechanical system.

Do not solve any serious humanoid problem from only one layer. Always check:

- task and motion requirement,
- body/limb kinematics,
- floating-base dynamics and contact,
- actuator/transmission envelope,
- sensing/timing/estimation quality,
- structural stiffness, strength, thermal and fatigue,
- controller bandwidth and stability,
- test evidence.

## Coordinate Frames and Kinematics

- Use clear frames: world, base/torso, link, joint, sensor, camera, IMU, foot/contact.
- A rigid transform is `T_AB`, mapping coordinates from frame B to frame A. Do not mix direction silently.
- Rotation matrices must remain orthonormal; quaternions must be normalized.
- Forward kinematics gives pose from joint states. It does not prove dynamic feasibility.
- Inverse kinematics can have multiple solutions, no solution, or singular solutions.
- Jacobian relation: `V = J(q) * qdot`.
- Near singularity, small task-space motion can require large joint velocity/torque.
- For sensors mounted on moving links, use sensor-to-link extrinsic plus robot kinematics. Do not invent a fixed transform between two sensors on different moving links.

## Floating-Base Dynamics

Use the floating-base dynamics form:

`M(q) * nudot + h(q, nu) = S^T * tau + J_c(q)^T * lambda`

Where:

- `q`: floating-base pose plus joint positions.
- `nu`: floating-base spatial velocity plus joint velocities.
- `S`: actuator selection matrix; the 6-DoF floating base is unactuated.
- `tau`: joint torques.
- `J_c`: contact Jacobian.
- `lambda`: contact wrench/force.

For rigid sticking contact:

`J_c(q) * nudot + Jdot_c(q, nu) * nu = 0`

Any load extraction or actuator sizing must state:

- robot mass distribution, CoM, inertia,
- motion trajectory and speed,
- contact state,
- payload,
- gravity direction,
- safety factor,
- whether loads are peak, RMS, or continuous.

## Balance and Locomotion

- Static/quasi-static balance: CoP/ZMP inside support polygon under model assumptions.
- Dynamic balance: use capture point, DCM, centroidal momentum, contact wrench cone, or full-body dynamics.
- Flight phase has no ground-contact ZMP.
- LIPM approximation: `xdd = omega0^2 * (x - p_x)`, `omega0 = sqrt(g / z_c)`. It assumes constant CoM height and simplified contact.
- MPC is useful for online constrained correction but depends on model fidelity, horizon, constraints, and solve time.
- WBC coordinates many tasks under constraints; it is not magic. A credible WBC formulation must include dynamics/contact constraints and inequality limits such as friction cone, torque, velocity, joint, and contact-force limits.
- RL policies must be checked for sim-to-real gaps: actuator delay, saturation, contact friction, compliance, sensor noise, dropped frames, terrain variation, and reward hacking.

## Human Motion and Joint Requirements

Human ROM and motion data are references, not direct robot requirements.

Use human data to infer task classes:

- walking, turning, stair climbing,
- squatting, kneeling, lifting,
- reaching, pushing, pulling,
- recovery stepping,
- fall protection.

Then convert to robot requirements:

- joint DoF allocation,
- ROM with collision/cable/package margins,
- peak and continuous joint torque,
- peak speed and acceleration,
- mechanical stops,
- stiffness/backlash limits,
- sensing needs.

Do not state a universal ROM or torque requirement without task set and morphology.

## Actuator and Transmission Basics

For rotary transmission:

- `tau_out = eta * i * tau_motor`
- `omega_out = omega_motor / i`
- `J_ref_to_motor = J_load / i^2`
- `P = tau * omega`

Check together:

- peak torque versus continuous torque,
- torque-speed curve,
- voltage/current limit,
- thermal limit and duty cycle,
- reflected inertia and control stability,
- backlash, compliance, friction, efficiency,
- shock load, lifetime, lubrication,
- mass and packaging.

Peak torque is not continuous torque. Continuous torque is usually thermal. Peak torque has duration/current/voltage/demagnetization constraints.

For screw transmission:

- `T = F * p / (2*pi*eta)`
- `v = n * p / 60`

Use `行星滚柱丝杠 / planetary roller screw` for high-load roller-screw discussions. `行星滚珠丝杠` is often a mistaken phrase; clarify whether the intended device is ball screw or planetary roller screw.

## Electrical, Sensor, and Timing Basics

- Resolution is not accuracy.
- Accuracy is not bandwidth.
- Static accuracy is not dynamic accuracy.
- Low noise does not remove delay.
- A sensor without a trustworthy timestamp can harm fusion.

Critical quantities:

- encoder resolution, accuracy, cyclic error, latency,
- IMU noise density, bias instability, scale factor, axis misalignment, vibration sensitivity,
- force/torque sensor range, stiffness, cross-axis coupling, overload protection,
- current sensor bandwidth, offset, gain error, common-mode rejection,
- camera intrinsics, shutter type, exposure time, timestamp, extrinsics,
- bus cycle time, jitter, dropped frames, clock source.

Camera-IMU fusion requires:

- camera intrinsics,
- IMU intrinsics/noise,
- camera-IMU spatial extrinsic,
- camera-IMU temporal offset.

If camera and IMU are calibrated off-body, the calibration remains valid only if they are installed as an unchanged rigid subassembly.

## Control and Stability Basics

Closed-loop performance is limited by:

- sampling rate,
- computation delay,
- communication delay,
- sensor delay/noise,
- actuator bandwidth,
- structural modes,
- backlash/compliance,
- saturation,
- thermal derating.

Typical diagnosis:

- oscillation changes with gain: control loop issue likely.
- oscillation frequency matches structural mode: mechanical resonance likely.
- output saturates/clips: actuator or command envelope issue.
- estimator moves before body: sensing/estimation issue likely.
- reference itself oscillates: planning/state-machine issue likely.
- low-frequency whole-body rocking during standing: balance/estimation/control interaction likely.

## CAE and Simulation Basics

A simulation claim is not credible unless it states:

- geometry and simplification,
- material and source,
- boundary conditions,
- loads and contacts,
- mesh/time-step/frequency strategy,
- solver type,
- convergence or validation path,
- decision criterion.

Use the right analysis:

- static strength/stiffness for quasi-static loads,
- modal/frequency response for vibration,
- fatigue for cyclic lifetime,
- explicit dynamics for drop/impact,
- thermal transient/steady-state for temperature,
- electromagnetic for motors/fields/loss,
- multibody/control co-simulation for coupled motion/control.

Do not infer lifetime, impact safety, or fatigue from one static stress plot.

## Test and Evidence Basics

A test result must include:

- sample/version,
- firmware/control parameters,
- calibration state,
- fixture,
- environment,
- equipment accuracy,
- procedure,
- raw data,
- pass/fail requirement,
- uncertainty or limitation.

No measured number is meaningful without units and conditions.

For fault diagnosis, prefer discriminating experiments:

- disable or reduce one loop,
- support or suspend robot,
- test one joint at a time,
- compare no-load/load/hot/cold,
- log reference/state/command/current/voltage/temperature/timestamps together,
- replay the same trajectory before and after a change.

