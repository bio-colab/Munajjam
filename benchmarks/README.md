# Benchmarks

Benchmarking goals for alignment quality:

## Metrics

1. **Timestamp Accuracy (MAE)**

```python
MAE = mean(abs(predicted_start - true_start))
```

Target: `< 0.5s` for the default `auto` strategy on clean recitations.

2. **Ayah Accuracy**

```python
accuracy = matched_ayahs / total_ayahs
```

Target: `> 95%` on clean recitations.

## Runnable baseline

Generate reproducible fixture benchmark output:

```bash
PYTHONPATH=munajjam python benchmarks/run.py --output benchmarks/results/latest.json
```

The command writes machine-readable results JSON for all strategies.

## Planned public table

| Reciter | Auto | DP | Greedy | Hybrid |
|---|---:|---:|---:|---:|
| Husary | TBD | TBD | TBD | TBD |
| Sudais | TBD | TBD | TBD | TBD |

## CI recommendation

Run benchmark checks on release tags and publish results artifact.
