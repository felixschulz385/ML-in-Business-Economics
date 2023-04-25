#!/bin/bash

#SBATCH --job-name=data_handling.job
#SBATCH --output=data_handling.out
#SBATCH --export=ALL

#SBATCH --partition=single
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16 
#SBATCH --mem-per-cpu=4000
#SBATCH --time=12:00:00

#SBATCH --mail-user=f.schulz@student.uni-tuebingen.de
#SBATCH --mail-type=START,END,FAIL

# Load conda
source /pfs/work7/workspace/scratch/tu_zxobe27-ds_project/conda/bin/activate
conda activate nlp_cuda

# run pipeline
python /pfs/work7/workspace/scratch/tu_zxobe27-hiwi_project/ML-in-Business-Economics/data_handling.py

