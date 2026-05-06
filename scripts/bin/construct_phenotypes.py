#!/usr/bin/env python3
import sys
import pandas as pd

input_file, output_file, min_count = sys.argv[1], sys.argv[2], int(sys.argv[3])

df = pd.read_csv(input_file)
grouped = df.groupby(['patient_id', 'phecode', 'Phenotype']).size().reset_index(name='count')
grouped['case'] = (grouped['count'] >= min_count).astype(int)
grouped.to_csv(output_file, index=False)
print(f"Constructed phenotypes for {grouped['patient_id'].nunique()} patients -> {output_file}")