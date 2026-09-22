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

process ANALYZE {
    container 'bioinformatics-pipeline:latest'

    input:
    path input_file
    path script_file

    output:
    path "differential_expression.csv"

    script:
    """
    mkdir -p results
    cp ${input_file} results/preprocessed_expression.csv
    python ${script_file}
    """
}

workflow {
    input_file = file("data/expression.csv")
    preprocess_script = file("scripts/preprocess.py")
    analyze_script = file("scripts/analyze.py")

    preprocessed = PREPROCESS(input_file, preprocess_script)

    ANALYZE(preprocessed, analyze_script)
}
