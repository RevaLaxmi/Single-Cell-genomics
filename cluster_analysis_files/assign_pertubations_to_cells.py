#we need perturbation information linked to the corresponding cells in the scRNA-seq data.
#we need this to analyze the gene expression changes associated with different perturbations or perform downstream analyses.

import pandas as pd
scRNAseq_file_path = "C:/Users/Reva Laxmi Chauhan/Desktop/RINTU/project/SCP24/expression/dc_both_filt_fix_tp10k.txt"
scRNAseq_data = pd.read_csv(scRNAseq_file_path, sep="\t", index_col=0)
print("scRNA-seq data:")
print(scRNAseq_data.head())

CRISPR_perturbation_file_path = "C:/Users/Reva Laxmi Chauhan/Desktop/RINTU/project/SCP24/metadata/cluster_assignment_bmdc.txt" #CRISPR perturbation data into a pandas DataFrame
CRISPR_data = pd.read_csv(CRISPR_perturbation_file_path, sep="\t")
print("\nCRISPR perturbation data:")
print(CRISPR_data.head())

merged_data = pd.merge(scRNAseq_data, CRISPR_data, left_index=True, right_on='NAME') #merging the scRNA-seq data with the CRISPR perturbation data based on the common identifier 'NAME'
print("\nMerged data:")
print(merged_data.head())