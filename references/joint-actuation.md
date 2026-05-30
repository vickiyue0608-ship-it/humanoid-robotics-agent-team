# Joint Actuation and Transmission

Terminology note: the high-load screw used in many humanoid linear-actuator discussions is normally `planetary roller screw`, in Chinese `行星滚柱丝杠`. The user's phrase `行星滚珠丝杠` should still trigger this section, but answers should use the correct term and mention the correction.

## Design Flow

1. Input joint load spectrum: peak torque, continuous torque, peak speed, RMS speed, duty cycle, impact load, required backdrivability, stiffness, backlash, mass, and packaging.
2. Select architecture: quasi-direct drive, strain-wave/harmonic reducer, planetary/cycloidal/RV reducer, series elastic actuator, ball screw, planetary roller screw, linkage, or hybrid.
3. Choose transmission ratio `i` and efficiency `eta`.
4. Reflect load inertia: `J_reflected = J_load / i^2`.
5. Check motor-side speed: `omega_motor = i * omega_joint`.
6. Check motor torque: `tau_motor = tau_joint / (i * eta)` plus acceleration/friction terms.
7. Check power, voltage/current, thermal continuous rating, peak duration, reducer/screw lifetime, backlash, stiffness, and sensing strategy.

## Key Judgments

- Higher ratio increases output torque but reduces output speed and reflected load inertia; it also increases reflected motor inertia at the output and can reduce transparency.
- Peak torque and continuous torque are different promises. Continuous is normally thermal; peak is time/current/voltage/demagnetization limited.
- Low ratio/high torque-density QDD can improve force transparency but needs larger motors and careful thermal design.
- Strain-wave reducers offer compact high reduction but can bring torsional compliance, friction, efficiency, and fatigue constraints.
- Planetary roller screws can provide high axial force density for linear joints, but require careful lifetime, lubrication, efficiency, packaging, backlash/preload, and manufacturability checks.

## Ball Screw and Planetary Roller Screw Checks

- Screw torque-force: `T = F * p / (2*pi*eta)` where `p` is lead and `eta` is efficiency.
- Linear speed: `v = n * p / 60` with `n` in rpm.
- Ball-screw life and rigidity must be checked against ISO 3408 and the vendor catalog. Do not reuse a generic life number across load spectra.
- Allowable speed must satisfy both critical speed and DN limits; use the lower limit.
- Preload can reduce backlash and raise stiffness, but increases friction, heat, and life consumption.
- Planetary roller screws are usually considered when axial force density, shock load, stiffness, and life dominate; ball screws remain strong for precision linear motion where load density is moderate and cost/maturity matter.

## Output Indicators

Produce a table:

`Joint | architecture | i | peak torque | continuous torque | peak speed | peak power | reflected inertia ratio | stiffness | backlash | efficiency | mass | thermal limit | sensor set | verification`

Use datasheets or vendor confirmation for product-specific numbers.
