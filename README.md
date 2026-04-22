# Gene Expression Analysis of Linker Histones in Cancer vs Healthy Tissue

**Author:** Yousra Farrukh  
**Degree:** BSc Artificial Intelligence, COMSATS University Islamabad  
---

## What This Project Does

This project builds a computational pipeline to analyse **linker histone gene expression** in cancer vs healthy tissue using public data from NCBI GEO. The goal is to identify which histone genes are significantly over- or under-expressed in disease contexts, cluster patient samples by expression profile, and scan for recurrent mutations.

This is directly relevant to Fischle's lab, which studies how linker histones regulate chromatin organisation and how changes in their expression or mutation are linked to diseases including cancer, diabetes, and neurodevelopmental disorders.

---

## Background

**What are linker histones?**  
DNA is packaged into a structure called chromatin. Histones are proteins that DNA wraps around to form the basic unit of chromatin (the nucleosome). Linker histones sit between these units and control how tightly the chromatin is packaged — affecting which genes can be accessed and expressed. When linker histone genes are mutated or their expression changes, normal gene regulation breaks down.

**Why catch expression data?**  
Direct measurement of protein levels across thousands of patient samples is expensive. Gene expression microarray and RNA-seq data — widely available in GEO — provides a good proxy. Persistently lower or higher expression of a histone gene across cancer samples compared to healthy tissue is a biologically meaningful signal.

---

## Project Structure

```
gene_expression_analysis/
│
│
├── data/
│   ├── download_geo.py             
│   └── preprocess.py               
│
├── analysis/
│   ├── differential_expression.py  
│   ├── clustering.py               
│   └── mutation_scan.py            
│
├── visualisation/
│   └── plots.py                    
│
├── results/                        
├── pipeline.py                     
└── README.md
```

---

## Installation

```bash
pip install GEOparse pandas numpy scipy scikit-learn matplotlib seaborn
```

---

## Usage

**Run the full pipeline:**
```bash
python pipeline.py
```
The pipeline downloads data automatically on first run (~few minutes for large datasets). All outputs are saved to `results/`.

**To use real mutation data from cBioPortal:**
1. Go to https://www.cbioportal.org/
2. Select a cancer study
3. Click Mutations tab → Download TSV
4. Run: `python -c "from analysis.mutation_scan import run_mutation_scan; run_mutation_scan('your_file.tsv')"`

---

## Methods

### Linker Histone Genes Studied
```
H1F0, HIST1H1A, HIST1H1B, HIST1H1C, HIST1H1D, HIST1H1E, H1FX, H1FOO
```

### Data Source
**GSE2109** from NCBI GEO — a large multi-cancer expression dataset with 6,000+ samples across multiple cancer types. Downloaded automatically via GEOparse.

### Preprocessing
- **Log2(x+1) normalisation** — standard in gene expression analysis. Compresses the dynamic range and produces more symmetric distributions better suited to statistical testing.
- **Variance filtering** — removes genes with near-zero variance across samples (uninformative).
- **Automatic sample labelling** — classifies samples as Cancer/Healthy/Unknown based on metadata keyword matching.

### Differential Expression
For each gene:
1. Split samples into Cancer vs Healthy groups
2. Apply Welch's t-test (handles unequal group sizes and variances)
3. Calculate Log2 Fold Change = mean(Cancer) − mean(Healthy)
4. Apply Benjamini-Hochberg FDR correction (implemented from scratch)
5. Call significant if: adjusted p < 0.05 AND |Log2FC| > 1

### Dimensionality Reduction and Clustering
- **PCA:** Reduces expression matrix to 2 components for visualisation
- **K-Means:** Groups samples by expression profile (elbow method for optimal k)

### Mutation Analysis
- Mutation frequency per gene across cancer samples
- Mutation type breakdown (missense, nonsense, frameshift, etc.)
- Hotspot identification — positions mutated in ≥3 patients
- Cancer-type stratification — which cancers mutate which histones

---

## Outputs

```
results/
├── expression_distribution.png   — Before/after log normalisation
├── expression_boxplots.png       — Cancer vs Healthy expression per gene
├── volcano_plot.png              — Fold change vs significance
├── pca_plot.png                  — Sample separation by condition
├── elbow_plot.png                — Optimal cluster number
├── kmeans_pca.png                — K-Means clusters in PCA space
├── mutation_frequency.png        — Most frequently mutated histone genes
├── mutation_types.png            — Mutation type breakdown
├── hotspot_lollipop_*.png        — Protein-level mutation maps
├── cancer_type_heatmap.png       — Mutations by cancer type
├── de_results.csv                — Full differential expression results
└── mutation_frequency.csv        — Mutation counts per gene
```

---

## Limitations and Next Steps

**Current limitations:**
- Sample labelling is automated from metadata text — manual curation would improve accuracy
- Analysis treats all cancer types together — stratifying by cancer type would give more specific results
- Probe-to-gene mapping depends on probe ID format, which varies across platforms
- Mutation analysis currently uses simulated data — real MAF files from cBioPortal are needed

**Natural extensions:**
- Separate analysis by cancer type (breast, lung, colorectal, etc.)
- Integration of expression and mutation data — do samples with histone mutations also show expression changes?
- Correlation with clinical outcomes (survival data available in some GEO studies)
- Expand to neurodevelopmental disease datasets (autism, schizophrenia) as described in the VSRP project

---

## Connection to Fischle Lab Research

This project directly mirrors the computational work described in the VSRP project:

| VSRP Deliverable | This Project |
|---|---|
| Interface with different databases | GEO download via GEOparse |
| Execute datamining pipelines | DE analysis + mutation scan |
| Expression analysis | Welch's t-test, BH correction, volcano plot |
| Mutant analysis | Frequency, hotspot, cancer-type breakdown |
| Debugging of code | Pipeline structured for modularity and debugging |
| GitHub documentation | This README + inline code comments |

---

## References

1. Barrett et al. (2013) — NCBI GEO: archive for functional genomics data sets. *Nucleic Acids Research.*
2. Benjamini & Hochberg (1995) — Controlling the false discovery rate. *Journal of the Royal Statistical Society.*
3. Irizarry et al. (2003) — Exploration, normalisation, and summaries of high density oligonucleotide array probe level data. *Biostatistics.*
4. Talbert & Henikoff (2021) — Histone variants at a glance. *Journal of Cell Science.*
5. Fyodorov et al. (2018) — Emerging roles of linker histones in regulating chromatin structure and function. *Nature Reviews Molecular Cell Biology.*
