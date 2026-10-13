# AWS S3 execution profile

This document describes the cloud-storage integration added to the
bioinformatics workflow.

## Objective

Demonstrate a secure and reproducible hybrid execution pattern:

- Nextflow orchestrates the workflow.
- Docker provides the reproducible runtime.
- Amazon S3 stores the input and published result.
- Compute runs locally during this validation stage.

```text
Private S3 input
       │
       ▼
Nextflow + Docker (local execution)
       │
       ▼
Private S3 results
```

The workflow can later be extended to AWS Batch for managed cloud compute
without changing the pipeline logic.

## AWS resources

| Resource | Purpose |
|---|---|
| S3 bucket | `lartieda-nextflow-portfolio-2026` |
| `input/` prefix | Source input data |
| `results/` prefix | Published workflow outputs |
| `logs/` prefix | Operational logs and connection checks |
| IAM user | `nextflow-portfolio-runner` |
| IAM policy | Least-privilege access restricted to this bucket |

The bucket is private and public access is blocked.

## Credential handling

No AWS credentials are stored in this repository.

The workflow uses a local AWS CLI profile named `nextflow-portfolio`.
The IAM policy allows object access only within the `input/`, `results/`, and
`logs/` prefixes of the portfolio bucket.

## Nextflow profile

The `aws_s3` profile in `nextflow.config` configures:

- `nf-amazon` for S3 support.
- `us-east-1` as the AWS region.
- Server-side S3 encryption using AES-256.
- S3 input and output locations.

## Run the workflow

```bash
AWS_PROFILE=nextflow-portfolio 
nextflow run main.nf -profile aws_s3 -resume
```

The workflow reads:

```text
s3://lartieda-nextflow-portfolio-2026/input/expression.csv
```

and publishes:

```text
s3://lartieda-nextflow-portfolio-2026/results/fold_change_results.csv
```

## Validation

The cloud-storage profile was validated with a successful two-process
Nextflow execution:

```text
PREPROCESS  ✔
ANALYZE     ✔
```

## Scope and next step

This stage validates cloud object storage, IAM least privilege, and
reproducible local container execution. It does not claim that the workflow
has been executed on AWS Batch yet.

The next extension is to configure AWS Batch and run the same workflow with
the `awsbatch` executor.