
import lsst.daf.persistence as dafPersistence
butler = dafPersistence.Butler(inputs=[{'root': '/datasets/hsc/repo/rerun/DM-23243/SFM/DEEP/'},
                                       {'root': '/datasets/hsc/repo/rerun/DM-23243/SFM/WIDE/'}],
                               outputs={'root': '/datasets/hsc/repo/rerun/DM-23243/FGCM/buildStars',
                                        'mode': 'rw'})
