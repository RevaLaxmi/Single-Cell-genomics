#we're going to remove cells with extremely low counts, as they may represent dead cells or technical artifacts.
'''
Applies quality control on the entire dataset.
The filtered data is subsampled to a specific number of cells 
Temporary columns 'TotalExpressedGenes' and 'TotalUMIs' are added to calculate and store metrics, which are later dropped after filtering.
The filtered results are printed, showing the number of cells before and after filtering.
'''

import pandas as pd
file_path = "C:/Users/Reva Laxmi Chauhan/Desktop/RINTU/project/SCP24/expression/dc_both_filt_fix_tp10k.txt" #loading the data
scRNAseq_data = pd.read_csv(file_path, sep="\t", index_col=0)

def filter_low_quality_cells(data, expressed_genes_threshold, UMI_threshold): #the function to perform quality control and filter low-quality cells
    data['TotalExpressedGenes'] = (data > 0).sum(axis=1) #calculate the total no. of expressed genes for each cell
    data['TotalUMIs'] = data.sum(axis=1)  #calculate the total count of UMIs for each cell

    #filtering the low-quality cells
    high_quality_cells = data[(data['TotalExpressedGenes'] >= expressed_genes_threshold) & (data['TotalUMIs'] >= UMI_threshold)]

    #but we might not need these metrics
    high_quality_cells = high_quality_cells.drop(columns=['TotalExpressedGenes', 'TotalUMIs'])
    return high_quality_cells

'''
The reason for adding the columns 'TotalExpressedGenes' and 'TotalUMIs' is to calculate and store the total number of expressed genes and total UMIs for each cell in the dataset.
These columns are temporary and serve the purpose of calculating these metrics.
After filtering out the low-quality cells based on the given thresholds, we no longer need those temporary columns
'''

expressed_genes_threshold = 200  #min no. of expressed genes to consider a cell high-quality
UMI_threshold = 1000  #min total UMI count to consider a cell high-quality

num_cells_to_subsample = 1000
subsampled_data = scRNAseq_data.sample(n=num_cells_to_subsample, random_state=42) #for random sampling

#we have to perform quality control and filtering on the subsampled data
high_quality_cells = filter_low_quality_cells(subsampled_data, expressed_genes_threshold, UMI_threshold)

#print the before and after
print("Number of cells before filtering:", len(subsampled_data))
print("Number of cells after filtering:", len(high_quality_cells))