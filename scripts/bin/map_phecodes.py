#!/usr/bin/env python3
import sys
import pandas as pd

input_file, output_file = sys.argv[1], sys.argv[2]

df = pd.read_csv(input_file)

phecode_stub = {
    # ICD-10
    'E11.9':   ('250.2',  'Type 2 diabetes'),
    'I10':     ('401.1',  'Hypertension'),
    'J45.901': ('495',    'Asthma'),
    'F32.1':   ('296.22', 'Depression'),
    # ICD-9
    '780.2':   ('345.1',  'Epilepsy'),
    '428.0':   ('428',    'Heart failure'),
    '401.9':   ('401.1',  'Hypertension'),
    '250.00':  ('250.1',  'Diabetes'),
    '272.0':   ('272.1',  'Hyperlipidemia'),
    '780.39':  ('345.1',  'Epilepsy'),
    '458.0':   ('458',    'Hypotension'),
    '296.23':  ('296.22', 'Depression'),
}

df['phecode']   = df['icd_code'].map(lambda x: phecode_stub.get(x, (None, None))[0])
df['Phenotype'] = df['icd_code'].map(lambda x: phecode_stub.get(x, (None, None))[1])
df = df.dropna(subset=['phecode'])
df.to_csv(output_file, index=False)
print(f"Mapped {len(df)} records -> {output_file}")