include { CLEAN_ICD_CODES      } from './modules/clean'
include { MAP_TO_PHECODES      } from './modules/map'
include { CONSTRUCT_PHENOTYPES } from './modules/construct'
include { ANALYZE_PHENOTYPES   } from './modules/analyze'
include { VISUALIZE            } from './modules/visualize'

workflow {
    raw_data   = Channel.fromPath(params.input)

    cleaned    = CLEAN_ICD_CODES(raw_data)
    mapped     = MAP_TO_PHECODES(cleaned)
    phenotypes = CONSTRUCT_PHENOTYPES(mapped)

    // Collect both files' phenotypes, combine into one, then analyze
    combined   = phenotypes.collectFile(
                     name: 'combined_phenotypes.csv',
                     keepHeader: true,
                     skip: 1
                 )

    prevalence = ANALYZE_PHENOTYPES(combined)
                 VISUALIZE(prevalence)
}
