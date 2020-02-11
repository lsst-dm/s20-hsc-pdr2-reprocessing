#!/bin/bash -l

#SBATCH -p normal
#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#SBATCH -t 24:00:00
#SBATCH -J fgcm 
#SBATCH --reservation=tempnodes


srun fgcmBuildStars.py /datasets/hsc/repo --calib /datasets/hsc/calib/20200115 --rerun DM-23243/FGCM --id ccd=13 filter=HSC-G^HSC-I^HSC-I2^HSC-R^HSC-R2^HSC-Y^HSC-Z^NB0387^NB0816^NB0921
