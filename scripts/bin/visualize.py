#!/usr/bin/env python3
import sys
import pandas as pd
import matplotlib.pyplot as plt

input_file, output_file = sys.argv[1], sys.argv[2]

df = pd.read_csv(input_file).head(15)

fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(df['Phenotype'], df['prevalence'], color='steelblue')
ax.set_xlabel('Prevalence')
ax.set_title('Top 15 Phenotype Prevalences')
ax.invert_yaxis()
plt.tight_layout()
plt.savefig(output_file, dpi=150)
print(f"Saved plot -> {output_file}")