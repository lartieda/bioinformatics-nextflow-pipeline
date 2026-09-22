nextflow.enable.dsl=2

include { PREPROCESS } from './modules/preprocessing.nf'
include { ANALYZE } from './modules/analysis.nf'

params.input = "data/expression.csv"
params.preprocess_script = "scripts/preprocess.py"
params.analyze_script = "scripts/analyze.py"

workflow {
    input_file = file(params.input)
    preprocess_script = file(params.preprocess_script)
    analyze_script = file(params.analyze_script)

    preprocessed = PREPROCESS(input_file, preprocess_script)

    ANALYZE(preprocessed, analyze_script)
}