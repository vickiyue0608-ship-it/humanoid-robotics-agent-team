# Deep Research Method

Use the installed `deep-research` skill for any answer that depends on current industry state, product/vendor claims, safety standards, novel papers, open-source implementations, or disputed design trade-offs.

Default strategy: paper-first, implementation-second. Start from papers, standards, and textbooks to establish what is physically and mathematically valid. Then search GitHub for similar implementations, reproduction code, benchmarks, issues, and engineering constraints. Treat papers and code as complementary evidence: papers clarify theory and claims; code reveals what actually had to be simplified, tuned, patched, or left unsupported.

## Research Discipline

1. Define scope and audience. For this skill, the default audience is a humanoid robotics R&D engineer.
2. Decompose into independent questions: physics model, implementation method, hardware constraints, validation, and failure modes.
3. Prefer source tiers in this order:
   - Peer-reviewed papers, review articles, textbooks, and university course material for theories, algorithms, control laws, simulation methods, and experimental findings.
   - Standards bodies, official software documentation, datasheets, and vendor application notes for product-specific claims and compliance/test details.
   - GitHub repositories tied to papers, labs, robot companies, official toolchains, or widely used research groups for implementation details and reproduction evidence.
   - Company engineering blogs and technical briefs for industry implementations.
   - Forums and social posts only as anecdotal leads, never as final evidence.
4. Record every factual claim with a source. For numerical values, keep units and test conditions.
5. Triangulate major claims using at least three independent sources when the claim affects design, safety, sizing, or procurement.
6. Surface conflicts instead of hiding them.
7. End with: what is known, what is estimated, what is unknown, and what test or source would close the gap.

## Paper-First Workflow

1. Search for review papers and canonical papers first; use recent papers only after the foundations are clear.
2. Extract: problem statement, assumptions, equations, constraints, experiment platform, metrics, failure cases, and stated limitations.
3. Mark source type:
   - `peer-reviewed`: journal/conference with DOI or proceedings page.
   - `preprint`: arXiv or similar; useful but not final proof.
   - `thesis/book`: strong for method depth; check date and scope.
4. For every paper-backed method, ask:
   - What assumptions must be true on the robot?
   - What sensors/actuators/control rate did the paper need?
   - What was tested on real hardware versus simulation only?
   - What failure modes were excluded?

## GitHub Implementation Search

Use GitHub as an execution and reality-check layer, not as a substitute for papers.

1. Search with combinations of method + robot + artifact:
   - `humanoid whole body control github`
   - `humanoid MPC locomotion github`
   - `ZMP preview control humanoid github`
   - `legged robot reinforcement learning humanoid gym github`
   - `camera IMU calibration kalibr OpenVINS github`
   - `topology optimization FEA python github`
2. Prefer repositories that have at least one of:
   - linked paper/preprint/DOI,
   - active commits or recent releases,
   - runnable examples, datasets, Docker/conda setup, CI, or tests,
   - clear license and hardware/simulator target,
   - issues/discussions showing real users and limitations.
3. When reporting a GitHub implementation, include:
   - repo URL, owner, license if visible, language/toolchain,
   - claimed robot/simulator/hardware target,
   - whether it is paper code, demo code, production code, or unverified sample,
   - installation/running burden,
   - what can be reused directly and what must be treated only as reference.
4. Never infer correctness from stars alone. Stars are popularity signals, not validation.
5. If a repo is stale, unlicensed, simulation-only, or lacks tests, say so explicitly.

## Anti-Hallucination Rules

- Do not fabricate model numbers, datasheet values, company rankings, market share, or unpublished test results.
- Do not fabricate paper titles, authors, DOI values, GitHub stars, licenses, commit recency, benchmark results, or repository capabilities.
- If the source is paywalled or only a snippet is visible, say so and treat it as weaker evidence.
- If a formula is standard but an input value is unknown, provide the formula and a sensitivity range, not a fake result.
- If a tool or simulator was not actually run, describe setup and expected outputs only.

## Evidence Tags

- `S1 primary`: standards, official docs, datasheets, source code from official project.
- `S2 scholarly`: peer-reviewed journal/conference, thesis, textbook.
- `S3 open implementation`: GitHub repo, paper code, official demo, benchmark suite, or reproducible toolchain.
- `S4 reputable engineering`: company technical brief, application note, engineering blog.
- `S5 anecdotal`: forums, social media, unverified marketplace pages.

Local Zane Hub articles in `references/zane-hub-articles.md` and `references/zane-hub-index.jsonl` are a practical engineering corpus. Use them for design heuristics, industry leads, teardown questions, and Chinese-domain terminology. They must not be used as sole evidence for safety, sizing, procurement, or design-freeze claims; cross-check critical statements against papers, standards, datasheets, simulations, or tests.
