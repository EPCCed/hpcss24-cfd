#!/bin/bash

# Slurm job options (name, compute nodes, job time)
#SBATCH --job-name=cfd
#SBATCH --time=0:05:0
#SBATCH --partition=gpu
#SBATCH --qos=gpu
#SBATCH --gres=gpu:1

# Load the required modules 
module load nvidia/nvhpc

srun --unbuffered ./cfd 20 10000
