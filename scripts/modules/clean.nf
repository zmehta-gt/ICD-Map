process CLEAN_ICD_CODES {
    input:
    path raw_csv

    output:
    path "cleaned_icd.csv"

    script:
    """
    clean_icd.py ${raw_csv} cleaned_icd.csv
    """
}