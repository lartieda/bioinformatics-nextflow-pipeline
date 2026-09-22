nextflow.enable.dsl=2

include { PREPROCESS } from './modules/qc.nf'
include { ANALYZE } from './modules/analysis.nf'

workflow {
    input_file = file("data/expression.csv")
    preprocess_script = file("scripts/preprocess.py")
    analyze_script = file("scripts/analyze.py")

    preprocessed = PREPROCESS(input_file, preprocess_script)

    ANALYZE(preprocessed, analyze_script)
}
