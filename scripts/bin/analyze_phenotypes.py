#!/usr/bin/env python3
import sys
import pandas as pd

input_file, output_file = sys.argv[1], sys.argv[2]

df = pd.read_csv(input_file)
total = df['patient_id'].nunique()
prev = df[df['case'] == 1].groupby(['phecode', 'Phenotype'])['patient_id'].nunique().reset_index()
prev.columns = ['phecode', 'Phenotype', 'case_count']
prev['prevalence'] = prev['case_count'] / total
prev = prev.sort_values('prevalence', ascending=False)
prev.to_csv(output_file, index=False)
print(f"Analyzed {len(prev)} phenotypes -> {output_file}")