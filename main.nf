nextflow.enable.dsl=2

process PREPROCESS {
    container 'bioinformatics-pipeline:latest'

    input:
    path input_file
    path script_file

    output:
    path "preprocessed_expression.csv"

    script:
    """
    python ${script_file}
    """
}

workflow {
    input_file = file("data/expression.csv")
    script_file = file("scripts/preprocess.py")

    PREPROCESS(input_file, script_file)
}
