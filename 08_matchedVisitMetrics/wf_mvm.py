#!/usr/bin/env python
import argparse
import logging
import os
import re
import Pegasus.DAX3 as peg


rootRepo = "/datasets/hsc/repo/"
inputRepo = "/datasets/hsc/repo/rerun/DM-23243/JOINTCAL/DEEP"
#calibRepo = "/datasets/hsc/calib/20200115/"

outPath = "/datasets/hsc/repo/rerun/DM-23243/validateDrp/matchedVisitMetrics/DEEP"

ch = logging.StreamHandler()
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(ch)


def generateDax(name="mvm", inputData=None):
    """Generate a Pegasus DAX abstract workflow"""
    dax = peg.ADAG(name)
    taskname = "matchedVisitMetrics"
    arguments = " --doraise --config instrumentName='HSC' datasetName='HSC-PDR2' " \
                "doApplyExternalPhotoCalib=True doApplyExternalSkyWcs=True externalPhotoCalibName=fgcm "

    with open(inputData, 'r') as f:
        for line in f:
            filt, tract, visits = line.strip().split(' ')
            outNonRepoPath = os.path.join(outPath, tract, filt)

            logger.debug("add job of dataId: %s %s %s to %s", filt, tract, visits, outNonRepoPath)
            task = peg.Job(name=taskname)
            task.addArguments(inputRepo,
                              "--output", outNonRepoPath, arguments,
                              "--id ccd=0..8^10..103 tract=%s visit=%s" % (tract, visits))
            dax.addJob(task)

            logfile = peg.File("%s-%s-%s.log" % (taskname, tract, filt))
            dax.addFile(logfile)
            task.setStdout(logfile)
            task.setStderr(logfile)
            task.uses(logfile, link=peg.Link.OUTPUT)

    return dax


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a DAX")
    parser.add_argument("-i", "--inputData", default="FilterTractVisits_example",
                        help="a file including input data information")
    parser.add_argument("-o", "--outputFile", type=str, default="va.dax",
                        help="file name for the output dax xml")
    args = parser.parse_args()

    dax = generateDax("matchedVisitMetricsS20pdr2", inputData=args.inputData)
    with open(args.outputFile, "w") as f:
        dax.writeXML(f)
