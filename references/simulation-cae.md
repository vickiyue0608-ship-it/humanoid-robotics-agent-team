# Simulation and CAE

## Required Setup Checklist

For any CAE claim, state:

- Geometry version and simplifications.
- Material model, source, temperature assumptions, and manufacturing state.
- Loads and boundary conditions, including contact and preload.
- Mesh type, mesh convergence strategy, and element quality.
- Solver type: linear static, nonlinear contact, modal, harmonic, explicit dynamics, thermal, electromagnetic, multibody, or co-simulation.
- Validation plan and acceptance criterion.

## Analysis Types

- Static strength/stiffness: check peak stress, stress concentration, displacement, stiffness, safety factor, and load path.
- Modal/vibration: compare natural frequencies and mode shapes to step frequency, motor electrical/mechanical orders, gear mesh, controller bandwidth, and impact excitations.
- Fatigue: require load spectrum, material fatigue curve, mean stress correction, stress concentration, surface/process data, and survival target.
- Drop/impact: use explicit dynamics or equivalent energy methods; check contact stiffness, damping, energy absorption, peak acceleration, and residual deformation.
- Thermal: convert copper loss, iron loss, driver loss, friction, reducer/screw losses into heat sources; include convection/conduction paths and duty cycle.
- Electromagnetic: check flux density, saturation, cogging torque, torque constant, back EMF, iron/copper losses, and thermal coupling.
- Topology optimization: define design/non-design space, load cases, volume fraction, manufacturing constraints, stress/displacement/frequency constraints.
- Multibody/control co-simulation: include actuator dynamics, controller delay, contact model, compliance/backlash, sensor noise, and realistic solver step.

## Hallucination Defenses

- Do not infer stress from a red contour without legend, units, mesh, loads, and material.
- Do not claim fatigue life without a load spectrum and material fatigue data.
- Do not claim topology optimization preserves strength unless re-analysis verifies it.
- Do not compare solvers or software by reputation; compare setup, assumptions, and validation.

## 3D Result Image Reading

Before interpreting any 3D cloud plot, identify:

- Result type: nodal value, element value, averaged/extrapolated contour, slice, isosurface, vector field, deformation, or animation frame.
- Units, coordinate system, color-bar fixed range, deformed-scale factor, and hidden/blanked regions.
- Whether the maximum is a physical hotspot or a singularity from point constraint, sharp corner, contact edge, or load application artifact.
- Whether the conclusion needs mesh convergence, time-step convergence, frequency resolution, or experimental correlation.

For fatigue, modal, thermal, and impact claims, a single static contour is insufficient evidence.
