# Reproducible Bioinformatics Pipeline

[![CI](https://github.com/lartieda/bioinformatics-nextflow-pipeline/actions/workflows/ci.yml/badge.svg)](https://github.com/lartieda/bioinformatics-nextflow-pipeline/actions/workflows/ci.yml)

A small, reproducible bioinformatics workflow built with **Nextflow, Python, Docker, and pytest**.

The pipeline processes a gene expression dataset, performs basic preprocessing, and calculates fold changes between control and treated samples.

## Workflow

```text
Raw expression data
        │
        ▼
   Preprocessing
        │
        ▼
Fold-change analysis
        │
        ▼
     Results
```

### Pipeline steps

1. **Preprocessing**

   * Validates the expected input columns.
   * Checks for missing values.
   * Calculates mean expression for control and treated samples.

2. **Fold-change analysis**

   * Calculates the treated/control expression ratio for each gene.
   * Sorts genes by fold change.
   * Writes the results to `fold_change_results.csv`.

## Project structure

```text
bioinformatics-nextflow-pipeline/
├── data/
│   └── expression.csv
├── modules/
│   ├── analysis.nf
│   └── preprocessing.nf
├── scripts/
│   ├── analyze.py
│   ├── explore_data.py
│   └── preprocess.py
├── tests/
│   └── test_analysis.py
├── results/
├── Dockerfile
├── main.nf
├── nextflow.config
└── requirements.txt
```

## Technologies

* **Nextflow** — workflow orchestration and reproducibility
* **Python** — data processing and analysis
* **pandas** — tabular data manipulation
* **Docker** — reproducible execution environment
* **pytest** — unit testing
* **Git/GitHub** — version control

## Running the pipeline

Build the Docker image:

```bash
docker build -t bioinformatics-pipeline:latest .
```

Run the Nextflow workflow:

```bash
./nextflow run main.nf
```

The input file can also be specified explicitly:

```bash
./nextflow run main.nf --input data/expression.csv
```

The generated results are published to:

```text
results/
```

## Testing

The analysis logic includes a unit test for the fold-change calculation.

Run the test inside the Docker environment:

```bash
docker run --rm \
  -v "$(pwd):/pipeline" \
  -w /pipeline \
  bioinformatics-pipeline:latest \
  pytest tests/test_analysis.py
```

## Scope

This project is intentionally small and focuses on demonstrating **reproducible workflow design, data processing, containerization, and testing**.

The analysis calculates fold changes only; it is **not a statistical differential-expression analysis**.

## Reproducibility

The workflow separates:

* input data
* analysis scripts
* workflow orchestration
* dependencies
* tests
* generated results

Docker provides a consistent Python environment, while Nextflow manages the execution of the workflow steps.
