source scl_source enable devtoolset-8 rh-git29
.  /software/lsstsw/stack/loadLSST.bash

setup git_lfs
export OMP_NUM_THREADS=1

setup lsst_distrib -t w_2020_06

# Re-start from fit cycle 0 
setup -j -r /home/hchiang2/PDR2/fgcm-DM-23526/fgcm
setup -j -r /home/hchiang2/PDR2/fgcm-DM-23526/fgcmcal 
setup -j -r /home/hchiang2/PDR2/fgcm-DM-23526/obs_subaru

