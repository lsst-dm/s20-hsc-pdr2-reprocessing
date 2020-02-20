#!/bin/bash -l

#SBATCH -p normal
#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#SBATCH -t 6-14:00:00
#SBATCH -J fgcm 
#SBATCH --reservation=pdr2


srun fgcmOutputProducts.py /datasets/hsc/repo --rerun DM-23243/FGCM/fit
# --config cycleNumber=5
