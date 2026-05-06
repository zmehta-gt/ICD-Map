process ANALYZE_PHENOTYPES {
    input:
    path phenotypes_csv

    output:
    path "prevalence.csv"

    script:
    """
    analyze_phenotypes.py ${phenotypes_csv} prevalence.csv
    """
}