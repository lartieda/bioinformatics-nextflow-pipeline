# AWS Batch Fargate execution

This document describes the cloud-compute execution profile added to the
bioinformatics workflow.

## Objective

Demonstrate that the Nextflow pipeline can execute reproducibly on managed AWS
compute, using private cloud storage and a private container image.

## Architecture

```text
Private S3 input
       │
       ▼
Nextflow orchestrator
       │
       ▼
AWS Batch queue
       │
       ▼
AWS Fargate tasks using a private ECR image
       │
       ▼
Private S3 work directory and published results
```

## AWS resources

| Resource | Purpose |
|---|---|
| S3 bucket | `lartieda-nextflow-portfolio-2026` |
| ECR repository | `nextflow-portfolio-pipeline` |
| ECR image | `352285845344.dkr.ecr.us-east-1.amazonaws.com/nextflow-portfolio-pipeline:v1.0.1` |
| Batch compute environment | `nextflow-portfolio-fargate` |
| Batch job queue | `nextflow-portfolio-queue` |
| Task role | `NextflowPortfolioBatchTaskRole` |
| Execution role | `NextflowPortfolioBatchExecutionRole` |

The ECR image is versioned with an immutable tag. Version `v1.0.1` includes
the `procps` package, which provides the `ps` command required by Nextflow to
collect task metrics.

## Nextflow configuration

The `aws_batch` profile configures:

- The `awsbatch` executor.
- AWS Batch Fargate through `nextflow-portfolio-queue`.
- A private S3 work directory.
- A private ECR image through the `container_image` parameter.
- Separate ECS task and execution IAM roles.
- Wave support for resolving the private ECR image for Fargate execution.

The workflow inputs and outputs are configured as:

```text
Input:
s3://lartieda-nextflow-portfolio-2026/input/expression.csv

Work directory:
s3://lartieda-nextflow-portfolio-2026/work

Published results:
s3://lartieda-nextflow-portfolio-2026/results/batch/
```

## Run the workflow

AWS credentials are supplied through a local AWS CLI profile. No credentials
are stored in this repository.

```bash
export AWS_PROFILE=nextflow-portfolio

nextflow run main.nf -profile aws_batch -with-tower -resume
```

## Validation

The workflow was successfully executed on AWS Batch Fargate on 14 October
2026.

```text
executor > awsbatch (2)
PREPROCESS  ✔
ANALYZE     ✔

Succeeded   : 2
Duration    : 2m 41s
```

The generated `fold_change_results.csv` file was published to the private S3
results prefix.

## Security and reproducibility

- The S3 bucket is private and blocks public access.
- The ECR repository is private and uses immutable image tags.
- IAM permissions are separated between workflow submission, task execution,
  and ECR image retrieval.
- The task role is scoped to the portfolio S3 bucket prefixes.
- The ECR registry credential is stored in Seqera Platform and is not committed
  to this repository.
- Docker provides a consistent Python runtime for both local and cloud runs.

## Scope

This implementation validates a hybrid cloud workflow: Nextflow runs from a
local environment, while pipeline processes execute as managed AWS Batch
Fargate tasks. The same pipeline logic is retained across local, S3, and AWS
Batch execution profiles.
