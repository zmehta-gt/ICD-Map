process VISUALIZE {
    publishDir "${params.outdir}", mode: 'copy'

    input:
    path prevalence_csv

    output:
    path "phenotype_prevalence.png"

    script:
    """
    visualize.py ${prevalence_csv} phenotype_prevalence.png
    """
}