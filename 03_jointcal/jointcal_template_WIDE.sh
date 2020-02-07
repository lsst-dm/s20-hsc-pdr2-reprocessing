#!/bin/bash -l
 
#SBATCH -p normal
#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#SBATCH --time=48:00:00
#SBATCH -J jc@TRACT@-@FILTER@
#SBATCH --output=/datasets/hsc/repo/rerun/DM-23243/logs/jointcal/WIDE/jointcal-@TRACT@-@FILTER@-%j.log
#SBATCH --error=/datasets/hsc/repo/rerun/DM-23243/logs/jointcal/WIDE/jointcal-@TRACT@-@FILTER@-%j.log
#SBATCH --reservation=pdr2


srun jointcal.py /datasets/hsc/repo --calib /datasets/hsc/calib/20200115 --rerun DM-23243/SFM/WIDE:DM-23243/JOINTCAL/WIDE --id ccd=0..8^10..103 visit=@VISIT@ filter=@FILTER@ tract=@TRACT@
