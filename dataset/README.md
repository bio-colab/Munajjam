# munajjam-benchmark-dataset (starter layout)

This directory is a starter layout for building a benchmark dataset for ayah timestamp alignment.

## Layout

```
dataset/
├── README.md
├── metadata.json
├── audio/
│   ├── 001_husary/
│   ├── 001_sudais/
│   ├── 001_minshawi/
│   └── 001_alafasy/
├── ground_truth/
│   └── 001_husary.json
└── annotations/
    └── annotation_guide.md
```

## Initial scope

- Start with Surah Al-Fatiha from 20 reciters.
- Prefer openly licensed recitations and document source per file.
- Ground truth should include manual start/end timestamps per ayah.
