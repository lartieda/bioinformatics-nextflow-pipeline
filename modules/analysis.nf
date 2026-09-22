process ANALYZE {

    publishDir 'results', mode: 'copy'

    container 'bioinformatics-pipeline:latest'

    input:
    path input_file
    path script_file

    output:
    path "fold_change_results.csv"

    script:
    """
    mkdir -p results
    cp ${input_file} results/preprocessed_expression.csv
    python ${script_file}
    """
}

