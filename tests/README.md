# Munajjam Test Suite

This directory contains unit, integration, and regression tests for Munajjam.

## Test Structure

```
tests/
├── conftest.py
├── unit/
│   ├── test_text_normalization.py
│   ├── test_alignment_greedy.py
│   ├── test_alignment_dp.py
│   ├── test_alignment_hybrid.py
│   ├── test_confidence_scores.py
│   ├── test_drift_correction.py
│   └── ...
├── integration/
│   ├── test_full_pipeline.py
│   ├── test_batch_processing.py
│   └── ...
├── regression/
│   └── test_known_timestamps.py
└── fixtures/
    └── expected_outputs/
        └── fatiha_fixture_alignment.json
```

## Running tests

```bash
PYTHONPATH=munajjam pytest
```

## Coverage gate

CI enforces total coverage at or above **85%**.

```bash
PYTHONPATH=munajjam pytest --cov=munajjam --cov-report=term-missing --cov-fail-under=85
```

## Regression policy

Regression tests use versioned expected outputs under `tests/fixtures/expected_outputs/`.
If output changes intentionally, update fixtures in the same PR and explain why.
