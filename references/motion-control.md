# Motion, Dynamics, WBC, and Gait

## Capability Boundaries

- Humanlike motion must be translated into feasible robot motion through joint limits, torque-speed envelopes, contact limits, and stability criteria.
- Human ROM data is a starting point, not a robot requirement; robot morphology, packaging, cable routing, collision, and load cases can narrow or widen ranges.
- Floating-base dynamics and contact constraints dominate humanoid motion; fixed-base manipulator intuition often fails.

## Key Models and Criteria

- Floating-base dynamics: `M(q) qdd + h = S^T tau + J_c^T f_c`.
- Contact consistency: `J_c(q) nudot + Jdot_c(q,nu) nu = 0` for rigid non-slipping contacts.
- CoM/ZMP planning often starts from LIPM assumptions: constant CoM height, massless legs, flat contacts. Mark those assumptions.
- LIPM sagittal relation: `xdd = omega0^2 * (x - p_x)`, `omega0 = sqrt(g / z_c)`.
- DCM/capture-point methods are better for dynamic balance reasoning than static ZMP alone.
- WBC commonly solves prioritized tasks or a QP with equality constraints for dynamics/contacts and inequalities for friction cones, joint limits, torque limits, and collision margins.
- MPC provides receding-horizon correction but depends on model quality, horizon, constraints, and computation budget.
- RL locomotion needs sim-to-real strategy: domain randomization, safety filters, fallback controller, reward audit, and hardware envelope checks.

## Modeling Boundaries

- Human motion capture and skeletal reconstruction can contain marker swap, soft-tissue artifact, scale mismatch, and calibration errors.
- IK can answer reachability but cannot prove dynamic feasibility, contact stability, or actuator feasibility.
- ZMP/LIPM preview control is strongest under foot-contact, near-flat-ground, and approximate constant-CoM-height assumptions. It is not a universal proof for jumping, flight, multi-contact, soft ground, or strong angular-momentum motions.
- RL simulation success is not hardware evidence unless actuator delay, saturation, sensor noise, contact variation, and safety fallback are tested.

## Diagnosis Clues

- Reference ZMP/CoP outside support polygon: planning infeasibility.
- Estimated base pose or velocity oscillates before body motion: estimator/sensor issue.
- Torque command saturates and actual motion clips: actuator or control saturation.
- Error grows with gain and has phase lag: control instability or delay.
- Real robot fails while simulation succeeds: model mismatch in contact, friction, compliance, actuator dynamics, latency, or sensor noise.
