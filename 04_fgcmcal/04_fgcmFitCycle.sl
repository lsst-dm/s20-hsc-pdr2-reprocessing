#!/bin/bash -l

#SBATCH -p normal
#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#SBATCH -t 6-14:00:00
#SBATCH -J fgcmFit5
#SBATCH --reservation=pdr2


srun fgcmFitCycle.py /datasets/hsc/repo --rerun DM-23243/FGCM/buildStars:DM-23243/FGCM/fit --configfile fgcmHscCalibrations_cycle05_config.py --config isFinalCycle=True
#--configfile fgcmFitCycle0.py
