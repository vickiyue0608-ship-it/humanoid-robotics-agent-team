# Testing and Diagnosis

## Four-Layer Symptom Diagnosis

| Layer | Evidence | Typical Root Causes |
|---|---|---|
| Safety isolation | Emergency stop, soft limits, low-speed mode, fixture/hoist, load limits | Test may amplify damage or create fall/collision risk |
| Sensing/state estimation | Raw IMU/encoder/force data, timestamps, residuals, covariance, estimator output leads body motion | bias, scale, extrinsic/time offset, vibration, timestamp mismatch, bad initialization |
| Planning/reference | reference trajectory, ZMP/CoP, footstep plan, jerk, contact schedule | infeasible reference, bad contact transition, discontinuity, wrong state machine |
| Control | tracking error, command, saturation, gain, phase, frequency response | too high gain, delay, poor bandwidth separation, anti-windup missing, impedance too stiff |
| Mechanical/electrical hardware | current, voltage, temperature, backlash, friction, stiffness, limit, noise | actuator undersized, stiction, backlash, compliance, overheating, bus/power issue |

## Oscillation Triage

- 1-2 Hz whole-body same-phase standing oscillation: often balance/state-estimation/control loop or nonlinear limit cycle. Verify by disabling WBC/balance, supporting the robot, and logging phase.
- Higher-frequency local joint oscillation: check joint servo gains, current loop, encoder noise, structural mode, backlash/compliance.
- Saturated torque/current waveform: hardware envelope or controller saturation, not a pure planning problem.

## Test Plan Template

`Objective | Metric | Requirement | Fixture | Equipment accuracy | Conditions | Procedure | Sampling | Processing | Pass/fail | Safety | Report fields`

## Motor/Joint Tests

- Torque-speed curve: dynamometer or calibrated load, voltage/current/temperature conditions, peak duration and continuous thermal equilibrium separated.
- Efficiency: mechanical output power divided by electrical input or motor input, with losses and conditions stated.
- Backlash/hysteresis: bidirectional load/position sweep around torque reversals.
- Torsional stiffness: known torque vs angular deflection with fixture compliance subtracted.
- Thermal: duty cycle, ambient, mounting, cooling, winding/case/sensor locations, steady-state or transient criterion.
- Lifetime/fatigue: load spectrum, cycles, environment, failure definition, inspection interval.

## Report Rules

- No measured number without condition and equipment accuracy.
- No pass/fail without a requirement.
- No extrapolated continuous rating from short peak tests.
- Always list limitations and next verification.

## Minimum Report Structure

`Version | firmware | parameters | calibration state | load | environment | fixture | equipment accuracy | procedure | raw data links | plots | decision | limitations | regression result`

For repair work, include before/after comparison and the exact configuration version used for the passing run.
