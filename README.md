# Humanoid Robotics Agent Team

Codex skill for humanoid robotics R&D work: specialist routing, physics guardrails, deep-research discipline, paper/library references, tests, and a local practical article corpus.

## Contents

- `SKILL.md` — skill entrypoint and operating contract.
- `agents/openai.yaml` — UI metadata.
- `references/` — physics guardrails, domain references, paper library, source map, and Zane Hub article index.
- `tests/` and `scripts/validate_skill.py` — deterministic skill contract checks.
- `knowledge/hub_articles_227/` — full exported Hub article corpus: 227 articles with Markdown, HTML, JSON metadata, and `index.jsonl`.

## Validation

```powershell
C:\Users\yueqi\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe scripts\validate_skill.py
```

## Evidence Boundary

The  Hub corpus is included as practical engineering commentary and industry-observation material. Treat it as `S4/S5` evidence unless a claim is independently confirmed by papers, standards, datasheets, simulations, or measured tests.
