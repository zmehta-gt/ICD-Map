process CONSTRUCT_PHENOTYPES {
    input:
    path mapped_csv

    output:
    path "phenotypes.csv"

    script:
    """
    construct_phenotypes.py ${mapped_csv} phenotypes.csv ${params.min_count}
    """
}