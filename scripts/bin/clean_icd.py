#!/usr/bin/env python3
import sys
import pandas as pd
import os

input_file = sys.argv[1]
output_file = sys.argv[2]

filename = os.path.basename(input_file)
ext = filename.lower()

# ── Detect format ──────────────────────────────────────────
if ext.endswith('.tsv') or 'ukb' in filename.lower():
    fmt = 'ukb'
elif ext.endswith('.csv'):
    fmt = 'cms'
else:
    raise ValueError(f"Unrecognized file format: {filename}")

print(f"Detected format: {fmt} for file: {filename}")

# ── Parse UKB format ───────────────────────────────────────
# uuid | ICD10_codes (comma-separated in one cell)
if fmt == 'ukb':
    df = pd.read_csv(input_file, sep='\t')
    df = df.rename(columns={df.columns[0]: 'patient_id', df.columns[1]: 'ICD10_codes'})
    df = df.dropna(subset=['ICD10_codes'])

    rows = []
    for _, row in df.iterrows():
        codes = [c.strip() for c in str(row['ICD10_codes']).split(',') if c.strip()]
        for code in codes:
            rows.append({
                'patient_id': row['patient_id'],
                'icd_code':   code,
                'icd_version': 'ICD10CM',
                'date':        None
            })
    result = pd.DataFrame(rows)

# ── Parse CMS format ───────────────────────────────────────
# Wide format: ICD9_DGNS_CD_1 through ICD9_DGNS_CD_10
elif fmt == 'cms':
    df = pd.read_csv(input_file, dtype=str)

    icd_cols = [c for c in df.columns if c.startswith('ICD9_DGNS_CD_')]
    date_col = 'CLM_FROM_DT' if 'CLM_FROM_DT' in df.columns else None

    rows = []
    for _, row in df.iterrows():
        for col in icd_cols:
            code = str(row[col]).strip()
            if code and code.lower() not in ('nan', ''):
                rows.append({
                    'patient_id':  row['DESYNPUF_ID'],
                    'icd_code':    code,
                    'icd_version': 'ICD9',
                    'date':        row[date_col] if date_col else None
                })
    result = pd.DataFrame(rows)

# ── Shared cleaning ────────────────────────────────────────
result = result.dropna(subset=['patient_id', 'icd_code'])
result['icd_code'] = result['icd_code'].str.strip().str.upper()

# Normalize ICD-9: insert decimal after 3rd char if missing
def normalize_icd9(code):
    if '.' not in code and len(code) > 3:
        return code[:3] + '.' + code[3:]
    return code

result.loc[result['icd_version'] == 'ICD9', 'icd_code'] = \
    result.loc[result['icd_version'] == 'ICD9', 'icd_code'].apply(normalize_icd9)

result = result.drop_duplicates()
result.to_csv(output_file, index=False)
print(f"Output: {len(result)} rows -> {output_file}")