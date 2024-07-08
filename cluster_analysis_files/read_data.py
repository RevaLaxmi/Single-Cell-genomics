#Load the scRNA-seq data from the "dc_both_filt_fix_tp10k.txt" file into our analysis environment. This data contains gene expression values for each cell.
import pandas as pd
file_path = "C:/Users/Reva Laxmi Chauhan/Desktop/RINTU/project/SCP24/expression/dc_both_filt_fix_tp10k.txt"
scRNAseq_data = pd.read_csv(file_path, sep="\t", index_col=0) #loading data into pandas DF
print(scRNAseq_data.head()) #just printing the first few rows because the file is very large 