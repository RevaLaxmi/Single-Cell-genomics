'''
similar to our filter_data but im making some changes here
directly works on a small subsample of the data 
The metrics 'TotalExpressedGenes' and 'TotalUMIs' are calculated without creating temporary columns.
the threshold vlaues for filtering are different
'''

import pandas as pd
file_path = "C:/Users/Reva Laxmi Chauhan/Desktop/RINTU/project/SCP24/expression/dc_both_filt_fix_tp10k.txt"
scRNAseq_data = pd.read_csv(file_path, sep="\t", index_col=0)
print("Original data:")
print(scRNAseq_data.head())

num_cells_to_subsample = 5 #subsample the data to a smaller size.
subsampled_data = scRNAseq_data.sample(n=num_cells_to_subsample, random_state=42) #for random sampling - just as we did in the previous code

subsampled_data['TotalExpressedGenes'] = (subsampled_data > 0).sum(axis=1) #we calculate the total number of expressed genes for each cell 
subsampled_data['TotalUMIs'] = subsampled_data.sum(axis=1) #we calculate the total count of UMIs for each cell 

expressed_genes_threshold = 10  #min no. of expressed genes to consider a cell as non-low count.
UMIs_threshold = 100  #min total UMI count to consider a cell as non-low count.

#fltering out whatever doesn't meet the requirement
high_quality_cells = subsampled_data[(subsampled_data['TotalExpressedGenes'] >= expressed_genes_threshold) & (subsampled_data['TotalUMIs'] >= UMIs_threshold)]

print("Subsampled data with metrics after filtering:")
print(high_quality_cells)