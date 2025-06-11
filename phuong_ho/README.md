# Applying MENDER and MISO on Multi-modal Spatial Omics Data

Student name: Ho Thi Ngoc Phuong
Student ID: 6172970

## Installation

Clone this repository and enter the project folder:

```bash
git clone https://github.com/feenix-ho/dsait4045-group-5-mender.git
cd dsait4045-group-5-mender/phuong_ho
```

Create and activate the Conda environment, then install dependencies:

```bash
conda create -n momender python=3.12
conda activate momender
pip install -r requirements.txt
```

## Usage

### Running on MERFISH Aging Data

Open and execute [MERFISH Aging Data](run_allen_aging.ipynb) in Jupyter Notebook or JupyterLab.

### Running on Human Heart Atlas Data

Open and execute [Human Heart Atlas Data](run_human_heart.ipynb)

### Result Analysis and Hypothesis Testing

Review findings and visualizations in [Result Analysis](result_analysis.ipynb)

## Acknowledgements

This project integrates several external libraries by cloning their repos as local modules due to version conflicts:

-   [miso](https://github.com/kpcoleman/miso/tree/main)
-   [MENDER](https://github.com/yuanzhiyuan/MENDER/tree/master)
-   [pysodb](https://github.com/TencentAILabHealthcare/pysodb)

OME-TIFF -> TIFF conversion uses [bftools](https://docs.openmicroscopy.org/bio-formats/5.7.3/users/comlinetools/index.html) (requires [Java](https://www.java.com/en/download/)).
