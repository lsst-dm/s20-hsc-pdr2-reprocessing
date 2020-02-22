source scl_source enable devtoolset-8 rh-git29
. /software/lsstsw/stack_20191101/loadLSST.bash

setup git_lfs
export OMP_NUM_THREADS=1

setup lsst_distrib -t w_2020_07
