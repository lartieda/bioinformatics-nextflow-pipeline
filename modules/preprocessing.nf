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
