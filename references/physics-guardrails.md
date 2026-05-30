# Physics Guardrails

## Non-Negotiable Laws

- Energy, linear momentum, and angular momentum cannot appear from nowhere.
- A humanoid is a floating-base multibody system unless the base is physically fixed.
- Joint torque, speed, power, current, voltage, temperature, and duty cycle are coupled constraints.
- Efficiency below 100% means losses become heat.
- A controller cannot recover information absent from sensors or delayed beyond usable phase margin.
- A simulation is a model prediction until anchored by mesh convergence, boundary conditions, material data, and experimental validation.

## Balance

- Static/quasi-static: CoP/ZMP must remain inside the support polygon for balance under the model assumptions.
- Dynamic: use capture point, divergent component of motion, centroidal momentum, contact wrench cone, or full-order dynamics.
- Flight phase: do not use ZMP as a ground-contact balance criterion.

## Dynamics

Use the floating-base form:

`M(q) qdd + h(q, qd) = S^T tau + J_c(q)^T f_c`

Where `S` selects actuated joints and the floating base is unactuated. Any inverse dynamics answer must state masses, inertias, contact assumptions, and motion profiles.

## Control

- Closed-loop bandwidth must sit below sampling/Nyquist, actuator bandwidth, structural modes, and delay-limited phase margin.
- Integral action plus stiction/backlash can create low-frequency limit cycles.
- Saturation invalidates linear controller assumptions; check anti-windup, current limits, voltage limits, thermal limits.

## Materials and Structures

- Check stress against allowable stress with safety factor, not just yield strength.
- Fatigue depends on load spectrum, surface finish, mean stress, stress concentration, and manufacturing process.
- Topology optimization is a design concept generator; it requires manufacturable reconstruction and re-analysis.

