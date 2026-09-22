nextflow.enable.dsl=2

process HELLO {
    output:
    path "hello.txt"

    script:
    """
    echo "Hello from Nextflow" > hello.txt
    """
}

workflow {
    HELLO()
}