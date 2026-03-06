# Adversarial Review Report (Red-Team Style)

## Scope

This report audits the latest test/doc scaffolding PR from the perspective of a skeptical attacker trying to undermine trust in the project quality.

Audited areas:
- Newly added tests and test expectations
- Consistency between claims and implementation
- Benchmark/dataset/paper scaffolding maturity

---

## Executive Summary

The previous PR improved structure, but several changes are **easy to challenge publicly** because assertions were relaxed and reproducibility claims remain mostly non-executable.

The key risk is **perception risk**: the project appears robust on paper, while important guarantees are not yet strictly enforced by tests/CI.

---

## Findings

### F1 — Weakened test guarantees (High)

Several new tests allow broad passing conditions such as `len(results) >= 3` instead of enforcing deterministic expected behavior per fixture.

Why this is attackable:
- A future regression can drop outputs silently yet still pass.
- Critics can claim "tests are green but quality gates are soft."

Evidence:
- `tests/unit/test_alignment_dp.py`: only checks length >= 3 and score range. No strict ayah coverage mapping assertion.
- `tests/unit/test_drift_correction.py`: same weakened cardinality check.
- `tests/integration/test_full_pipeline.py`: same weakened cardinality check.

Recommended fix:
1. Introduce fixture-specific expected ayah-number sequence checks.
2. Assert monotonic non-overlap and bounded timing drift relative to baseline.
3. Keep a strict regression fixture that fails on missing ayah outputs.

---

### F2 — Regression test is too narrow for its stated purpose (Medium)

`test_known_timestamps` validates only a short start-time list and does not protect end times, similarity deltas, or strategy-specific differences.

Why this is attackable:
- Regressions in boundaries/confidence may slip through while the single check remains green.

Recommended fix:
1. Validate both start/end arrays with a clear tolerance policy.
2. Add at least one per-strategy regression snapshot (`greedy`, `dp`, `hybrid/auto`).
3. Store expected outputs in versioned JSON under fixtures.

---

### F3 — Coverage target is documented but not enforced in CI (High)

`tests/README.md` states 85% coverage target, but no guaranteed execution path is provided when `pytest-cov` is unavailable.

Why this is attackable:
- Public claim without automated gate appears aspirational, not enforceable.

Recommended fix:
1. Add `pytest-cov` to test dependencies and CI workflow.
2. Enforce `--cov-fail-under=85` in CI.
3. Fail PR checks when coverage cannot be computed.

---

### F4 — Benchmark plan is descriptive, not runnable (Medium)

`benchmarks/README.md` defines metrics and targets but there is no executable benchmark runner or saved machine-readable results.

Why this is attackable:
- Anyone can ask for proof and no reproducible script exists yet.

Recommended fix:
1. Add `benchmarks/run.py` that outputs JSON/CSV.
2. Add a baseline artifact and comparison command.
3. Publish benchmark table in root `README.md` from generated artifacts.

---

### F5 — Dataset is layout-only, not benchmark-ready (Medium)

`dataset/` is currently scaffold documentation; ground-truth content is not yet a validated benchmark slice.

Why this is attackable:
- Claims of benchmarking readiness can be challenged as "no real corpus committed."

Recommended fix:
1. Provide a minimal verified subset (e.g., Al-Fatiha across a few reciters).
2. Add metadata fields: source URL, license, annotator IDs, review status.
3. Add validation script for schema and timestamp continuity.

---

### F6 — Scientific paper folder is outline-level only (Low)

`docs/paper/README.md` is useful but still a plan; no experimental section, reproducibility appendix, or result tables yet.

Recommended fix:
1. Add draft manuscript skeleton with numbered sections and TODOs.
2. Link experiments directly to benchmark scripts and dataset versions.

---

## Prioritized Remediation Plan

1. **Immediate (this sprint)**
   - Harden weakened assertions (F1).
   - Enforce coverage in CI (F3).
   - Expand regression baseline outputs (F2).

2. **Short term (next sprint)**
   - Implement runnable benchmark pipeline (F4).
   - Add minimal validated dataset subset and schema checks (F5).

3. **Medium term**
   - Convert paper outline to reproducible manuscript draft (F6).

---

## "Attacker questions" to preempt in future PR reviews

- "Can a missing ayah still pass tests?"
- "Where is the CI gate proving 85% coverage?"
- "Show me one command that reproduces benchmark numbers."
- "What dataset slice is truly ground-truth reviewed and versioned?"

If these are answered with code + artifacts (not prose), trust in the project rises significantly.
