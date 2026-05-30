# Electrical and Sensing

## Sensor/Signal Chain Boundaries

- Resolution is the smallest representable increment; accuracy is closeness to truth; precision/repeatability is scatter; bandwidth and latency define dynamic usefulness.
- Noise and delay reduce state-estimator and controller performance even when static accuracy is good.
- Time synchronization is a system requirement, not a software afterthought.

## Common Sensors

- Encoders: absolute/incremental, optical/magnetic/inductive; check resolution, accuracy, latency, update rate, interface, temperature drift, mounting eccentricity.
- IMU: gyroscope/accelerometer noise density, bias instability, scale factor, axis misalignment, vibration sensitivity, bandwidth, timestamping.
- Force/torque: range, overload, stiffness, cross-axis coupling, hysteresis, calibration matrix, thermal drift.
- Current: shunt/Hall/fluxgate; check bandwidth, offset, gain error, isolation, thermal drift, ADC timing.
- Temperature: placement, response time, calibration, thermal path.
- Vision/depth: intrinsics, rolling shutter, exposure latency, synchronization, extrinsics, environmental robustness.

## Calibration Rules

- Camera-IMU fusion requires camera intrinsics, IMU intrinsics/noise, camera-IMU spatial extrinsic, and camera-IMU temporal offset.
- A calibrated camera+IMU pair can be moved only if it remains a rigid subassembly.
- Sensors on different moving links need sensor-to-link extrinsics plus robot kinematics and joint zero calibration. A fixed head-IMU to torso-IMU transform does not exist if the neck moves.
- Static gravity alignment cannot determine yaw by itself.

## Electrical Checks

- Power electronics must stay within safe operating area, voltage/current margins, thermal limits, and EMI/EMC constraints.
- PWM, ADC sampling, current loop timing, encoder sampling, IMU timestamps, and communication bus cycles must be aligned or explicitly modeled.
- For EtherCAT/CAN-FD/other buses, log cycle time, jitter, dropped frames, and timestamp origin before blaming control gains.

## Motor Drive and Timing Checks

- PMSM FOC depends on rotor electrical angle plus phase-current measurement. Without reliable angle feedback, low-speed and zero-speed torque control become fragile.
- PMSM torque model: `T_e = (3*p/2) * (psi_m*i_q + (L_d - L_q)*i_d*i_q)`. For surface PMSM, `T_e` is often approximated as proportional to `i_q`; cite the motor model before using this simplification.
- Center-aligned PWM, dead time, propagation delay, bus ripple, current-sense offset, and ADC sampling instant can all change actual torque.
- Current sensing with shunt: `V_shunt = I * R_shunt`; include shunt tolerance, temperature coefficient, amplifier offset, common-mode rejection, layout parasitics, and PWM rejection.
- Time synchronization metrics: offset, jitter, drift, path-delay asymmetry, trigger latency, and timestamp origin.
- IEEE 1588/PTP and EtherCAT Distributed Clocks are relevant synchronization mechanisms; CAN FD is useful for robust distributed communication but should not be assumed to provide tight synchronized servo sampling by itself.
