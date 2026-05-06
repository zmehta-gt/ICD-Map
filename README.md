# ICD-Map

BIOL 8802: Spring 2026
Zeel H. Mehta

# Description

A reproducible Nextflow pipeline for harmonizing ICD codes for cohesive phenotype generation

---

# Environment and Version Information

| Software | Version | Notes |
|----------|---------|-------|
| Nextflow | 26.04.0 | Workflow system & DSL |
| Podman | 4.9.3 | Containerization |
| Python | 3.3.12 | Environment and package manager |
| conda | 26.3.2 | Environment and package manager |
| pandas | 3.0.2 | Data analysis package |
| matplotlib | 3.10.9 | Visualization package |

# System Compatability

All tools run on:
- **Linux (Ubuntu)**
- **macOS (Intel)**

# Pipeline Overview

```
TSV or CSV files containing patient identifiers and ICD-9 or ICD-10 codes
        |
        |-- Step 1: Pre-processing
        |
        |-- Step 2: Phecode Mapping
        |
        |-- Step 3: Phenotype Construction
        |        |-- File merge
        |
        |-- Step 4: Phenotype Analysis
        |
        |-- Step 5: Visualization
```

---

# Quickstart: Running the Pipeline

## Prerequisites

Install **Nextflow**.

Verify installation:

```bash
nextflow -version
```

Install **Miniconda or Anaconda**.

Verify installation:

```bash
conda --version
```

## Usage

Clone the repository:

```bash
git clone https://github.com/zmehta-gt/RB-pipeline.git
cd RB-pipeline/scripts
```

Run the pipeline:

```bash
nextflow run main.nf
```

---

# Tool References

Nextflow
https://www.nextflow.io/

Podman
https://podman.io/

Python
https://www.python.org/

conda
https://anaconda.org/channels/anaconda/packages/conda/overview

pandas
https://pandas.pydata.org/

matplotlib
https://matplotlib.org/
