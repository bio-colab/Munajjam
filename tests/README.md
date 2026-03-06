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
```

## Running tests

```bash
PYTHONPATH=munajjam pytest
```

### Coverage target

Track coverage in CI and keep total coverage at or above **85%**:

```bash
PYTHONPATH=munajjam pytest --cov=munajjam --cov-report=term-missing
```
