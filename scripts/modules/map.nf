process MAP_TO_PHECODES {
    input:
    path cleaned_csv

    output:
    path "phecode_mapped.csv"

    script:
    """
    map_phecodes.py ${cleaned_csv} phecode_mapped.csv
    """
}