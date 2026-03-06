# Munajjam Paper Draft (docs/paper)

This folder contains the scientific write-up plan for publishing Munajjam as a reproducible Islamic NLP / speech-alignment project.

## Proposed structure

1. **Problem formulation**
   - Define alignment as an ordered mapping function:
     - `f: Segments -> Ayahs`
   - Objective: maximize textual/phonetic similarity while preserving recitation order.

2. **Algorithms and complexity**

| Strategy | Time complexity | Recommended usage |
|---|---:|---|
| Greedy | O(n) | Clean recitations, low latency |
| DP | O(n×m) | Highest matching quality |
| Hybrid | O(n log n) (practical) | Balanced robustness/performance |
| Auto | Adaptive | Default for production |

3. **Arabic text normalization**
   - Hamza forms and alif variants.
   - Diacritics/tashkeel handling.
   - Ta marbuta and alef maqsura normalization.

4. **Quality and confidence**
   - Similarity score definition and calibration.
   - High-confidence threshold rationale.

5. **Reproducibility package**
   - Reference fixtures.
   - Benchmark scripts + expected outputs.
   - Versioned metrics table in README.

6. **Publication plan**
   - Target: arXiv preprint in Islamic NLP / Speech Processing.
   - Include ethics statement and dataset licensing notes.
