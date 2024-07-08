'''
we directly apply quality control to the entire dataset
calculates the metrics 'TotalExpressedGenes' and 'TotalUMIs' without temporary columns
the we are printing the number of cells before and after filtering, along with the data after filtering.
'''

import pandas as pd
file_path = "C:/Users/Reva Laxmi Chauhan/Desktop/RINTU/project/SCP24/expression/dc_both_filt_fix_tp10k.txt"
scRNAseq_data = pd.read_csv(file_path, sep="\t", index_col=0)
print("Original data:")
print(scRNAseq_data.head())

scRNAseq_data['TotalExpressedGenes'] = (scRNAseq_data > 0).sum(axis=1) #the total number of expressed genes for each cell.
scRNAseq_data['TotalUMIs'] = scRNAseq_data.sum(axis=1) #the total count of UMIs for each cell.

expressed_genes_threshold = 10  #can consider a cell as non-low count if it has at least 10 expressed genes
UMIs_threshold = 100  #and a cell is non-low count if its total UMI count is at least 100.

#filter whatever doesn't meet the threshold 
high_quality_cells = scRNAseq_data[(scRNAseq_data['TotalExpressedGenes'] >= expressed_genes_threshold) & (scRNAseq_data['TotalUMIs'] >= UMIs_threshold)]

print("no. of cells before filtering:", len(scRNAseq_data))
print("no. of cells after filtering:", len(high_quality_cells))

print("Data with metrics after filtering:") #and the data metrics after filtering 
print(high_quality_cells)