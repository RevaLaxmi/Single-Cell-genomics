# Perturb-seq: Understanding Transcriptional Complexity in Dendritic Cells using Single-Cell Genomics and CRISPR-based Perturbations

## Project Summary
The project aims to investigate gene functions in mammalian cells, particularly focusing on dendritic cells' response to lipopolysaccharide (LPS). To achieve this, the study utilizes Perturb-seq which combines single-cell RNA sequencing (scRNA-seq) and CRISPR-based perturbations. This approach helps in understanding immune cell activation and the genes that regulate these processes.

## Aim of the Project
The aim of the project is to uncover the functional roles of genes in mammalian cells, specifically in the context of dendritic cell responses to LPS, using the Perturb-seq approach. By integrating scRNA-seq and CRISPR data, the project seeks to provide a comprehensive understanding of immune activation processes and potential therapeutic targets.

## Coding Aspect and Benefits
The computational steps implemented are crucial for uncovering functional insights from vast amounts of single-cell genomic data. These steps enable researchers to analyze and visualize gene expression landscapes, identify marker genes, and gain valuable knowledge about immune activation and cellular functions.

## Key Features
- **Data Collection and Preprocessing**: Download and preprocess scRNA-seq and CRISPR data.
- **Quality Control**: Perform quality control and filter out low-quality cells.
- **Cell Clustering**: Identify and visualize cell clusters.
- **CRISPR Perturbation Assignment**: Link CRISPR perturbations to corresponding cells.
- **Integration and Analysis**: Integrate scRNA-seq and CRISPR data for comprehensive analysis.
- **Visualization**: Create visualizations to represent data and findings.

## Special Terms and Definitions
- **Perturb-seq**: A technique that combines single-cell RNA sequencing (scRNA-seq) with CRISPR-based perturbations to study gene function and cellular responses at a large scale.
- **Transcriptional Profiles**: The collection of all the genes expressed and their respective expression levels in a given cell or tissue type.
- **CRISPR**: Clustered Regularly Interspaced Short Palindromic Repeats, a powerful gene editing tool used to introduce specific changes in the genome.
- **Dendritic Cells (DCs)**: Immune cells that play a crucial role in recognizing and presenting antigens to activate the immune response.
- **Lipopolysaccharide (LPS)**: A component found in the cell walls of certain bacteria, used in experiments to stimulate the immune response.
- **Gene Regulatory Networks**: Complex interactions between genes and their products that control gene expression and cellular processes.
- **Dimensionality Reduction Techniques**: Computational methods used to reduce the number of variables in high-dimensional datasets, aiding in data visualization and analysis.
- **UMAP (Uniform Manifold Approximation and Projection)**: A dimensionality reduction algorithm used to visualize high-dimensional data in lower-dimensional spaces.

## Project Documentation
### Data Sources
- Downloaded from: [Single Cell Portal - Perturb-seq Study](https://singlecell.broadinstitute.org/single_cell/study/SCP24/perturb-seq)

### Data Files
- `cluster/pc_coords_fix.txt`
- `expression/dc_both_filt_fix_tp10k.txt`
- `metadata/cluster_assignment_bmdc.txt`
- `file_supplemental_info.tsv`

### Steps
1. **Exploring Data**: Understand the format and contents of each file.
2. **Quality Control**: Preprocess scRNA-seq and CRISPR data to filter out low-quality cells.
3. **Identifying Cell Clusters**: Use cluster assignment data to identify and visualize cell clusters.
4. **Assigning Perturbations**: Link CRISPR perturbations to the corresponding cells.
5. **Gene Expression Data**: Analyze gene expression levels in dendritic cells.
6. **CRISPR Perturbation Data**: Integrate CRISPR perturbation data with scRNA-seq data.
7. **Integration of Data**: Perform statistical analysis to identify the effects of perturbations on gene expression.
8. **Visualization and Analysis**: Use tools like scatter plots, heatmaps, UMAP to visualize data.
9. **Interpretation and Conclusion**: Draw conclusions about the effects of CRISPR perturbations on gene expression and cellular functions.

### Conclusion
By focusing on dendritic cells' response to LPS, the study offers novel insights into gene regulatory networks, differentiation, antiviral responses, and mitochondrial functions during immune activation.

## Usage
To use the scripts and data processing steps outlined in this project, follow these general steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/perturb-seq.git
   cd perturb-seq
   pip install -r requirements.txt
   python preprocess_data.py
   python quality_control.py
   python clustering.py
   python analysis.py
   python visualize.py




