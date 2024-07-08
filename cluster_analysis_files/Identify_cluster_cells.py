#we need this to explore the clusters and perform downstream analyses
#example, the merged data can be grouped by cluster in order to calculate cluster-specific statistics, visualize the clusters, or identify marker genes for each cluster.

import pandas as pd
scRNAseq_file_path = "C:/Users/Reva Laxmi Chauhan/Desktop/RINTU/project/SCP24/expression/dc_both_filt_fix_tp10k.txt"
cluster_assignment_file_path = "C:/Users/Reva Laxmi Chauhan/Desktop/RINTU/project/SCP24/metadata/cluster_assignment_bmdc.txt"
scRNAseq_data = pd.read_csv(scRNAseq_file_path, sep="\t", index_col=0)
print("Original scRNA-seq data:")
print(scRNAseq_data.head())

cluster_assignment_data = pd.read_csv(cluster_assignment_file_path, sep="\t") #the cluster assignment data into a pandas DataFrame
print("Cluster assignment data:")
print(cluster_assignment_data.head())

merged_data = pd.merge(scRNAseq_data, cluster_assignment_data, left_index=True, right_on='NAME') #we are merging the cluster assignment with scRNA-seq data using 'NAME' column as the common identifier


# Print the first few rows of the merged data to check if the merge is successful
print("Merged data:")
print(merged_data.head())

'''
the kind of data we are working with
NAME	CLUSTER	SUB-CLUSTER
TYPE	group	group
CCTTCACTAAACAG_dc0h_F9	0hr	0hr_m_Nfkb1_3
GTCGAATGACCACA_dc0h_F8	0hr	0hr_multi
CAGTTGGACAGATC_dc0h_F9	0hr	0hr_m_Rel_2

from my understanding: the pc_coords_fix.txt files are ref to the websites cluster visual models which have been designed?
'''
