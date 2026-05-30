#!/usr/bin/env python3
"""Validate the humanoid robotics agent-team skill package."""

from __future__ import annotations

import re
import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
    "references/research-method.md",
    "references/agent-team.md",
    "references/core-knowledge.md",
    "references/paper-library.md",
    "references/zane-hub-articles.md",
    "references/zane-hub-index.jsonl",
    "references/physics-guardrails.md",
    "references/motion-control.md",
    "references/simulation-cae.md",
    "references/joint-actuation.md",
    "references/electrical-sensing.md",
    "references/testing-diagnosis.md",
    "references/source-map.md",
    "tests/test_cases.json",
]

REQUIRED_SKILL_TERMS = [
    "deep-research",
    "fault-diagnosis",
    "motion-dynamics",
    "control-gait",
    "cae-simulation",
    "joint-actuator",
    "electrical-sensing",
    "test-validation",
    "物理学铁律",
    "不得编造",
    "core-knowledge",
    "zane-hub-articles",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def fail(message: str) -> None:
    if os.name == "nt":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except AttributeError:
            pass
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> int:
    if os.name == "nt":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except AttributeError:
            pass
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).exists()]
    if missing:
        fail("missing required files: " + ", ".join(missing))

    skill_text = read_text(ROOT / "SKILL.md")
    for term in REQUIRED_SKILL_TERMS:
        if term not in skill_text:
            fail(f"SKILL.md missing required term: {term}")

    if len(re.findall(r"https?://|doi\.org|DOI:", read_text(ROOT / "references/source-map.md"))) < 20:
        fail("source-map.md must include at least 20 source locators")

    tests_text = read_text(ROOT / "tests/test_cases.json")
    case_count = tests_text.count('"id"')
    if case_count < 8:
        fail(f"expected at least 8 test cases, found {case_count}")

    zane_index = read_text(ROOT / "references/zane-hub-index.jsonl")
    zane_count = sum(1 for line in zane_index.splitlines() if line.strip())
    if zane_count < 200:
        fail(f"expected at least 200 Zane Hub index entries, found {zane_count}")

    print("PASS: humanoid robotics agent-team skill contract is satisfied")
    return 0


if __name__ == "__main__":
    sys.exit(main())
