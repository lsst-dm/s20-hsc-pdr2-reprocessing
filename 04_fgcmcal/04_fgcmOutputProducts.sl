#!/bin/bash -l

#SBATCH -p normal
#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#SBATCH -t 24:00:00
#SBATCH -J fgcm 
#SBATCH --reservation=tempnodes


srun fgcmOutputProducts.py /datasets/hsc/repo --calib /datasets/hsc/calib/20200115 --rerun DM-23243/FGCM/fit
# --config cycleNumber=4
