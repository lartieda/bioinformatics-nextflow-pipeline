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

