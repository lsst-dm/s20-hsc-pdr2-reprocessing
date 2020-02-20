import lsst.fgcmcal.fgcmFitCycle
assert type(config)==lsst.fgcmcal.fgcmFitCycle.FgcmFitCycleConfig, 'config is of type %s.%s instead of lsst.fgcmcal.fgcmFitCycle.FgcmFitCycleConfig' % (type(config).__module__, type(config).__name__)
import lsst.fgcmcal.sedterms
# Bands to run calibration (in wavelength order)
config.bands=['N387', 'g', 'r', 'i', 'N816', 'z', 'N921', 'y']

# Flag for which bands are directly constrained in the FGCM fit. Bands set to 0 will have the atmosphere constrained from observations in other bands on the same night.  Must be same length as config.bands, and matched band-by-band.
config.fitFlag=[1, 1, 1, 1, 1, 1, 1, 1]

# Flag for which bands are required for a star to be considered a calibration star in the FGCM fit.  Typically this should be the same as fitFlag.  Must be same length as config.bands, and matched band-by-band.
config.requiredFlag=[0, 0, 0, 0, 0, 0, 0, 0]

# Mapping from 'filterName' to band.
config.filterMap={'g': 'g', 'r': 'r', 'r2': 'r', 'i': 'i', 'i2': 'i', 'z': 'z', 'y': 'y', 'N387': 'N387', 'N816': 'N816', 'N921': 'N921'}

# Use reference catalog as additional constraint on calibration
config.doReferenceCalibration=True

# Reference star signal-to-noise minimum to use in calibration.  Set to <=0 for no cut.
config.refStarSnMin=50.0

# Number of sigma compared to average mag for reference star to be considered an outlier. Computed per-band, and if it is an outlier in any band it is rejected from fits.
config.refStarOutlierNSig=4.0

# Apply color cuts to reference stars?
config.applyRefStarColorCuts=True

# Number of cores to use
config.nCore=12

# Number of stars to run in each chunk
config.nStarPerRun=200000

# Number of exposures to run in each chunk
config.nExpPerRun=1000

# Fraction of stars to reserve for testing
config.reserveFraction=0.1

# Freeze atmosphere parameters to standard (for testing)
config.freezeStdAtmosphere=False

# Precompute superstar flat for initial cycle
config.precomputeSuperStarInitialCycle=False

# Compute superstar flat on sub-ccd scale
config.superStarSubCcd=True

# Order of the 2D chebyshev polynomials for sub-ccd superstar fit. Global default is first-order polynomials, and should be overridden on a camera-by-camera basis depending on the ISR.
config.superStarSubCcdChebyshevOrder=2

# Should the sub-ccd superstar chebyshev matrix be triangular to suppress high-order cross terms?
config.superStarSubCcdTriangular=False

# Number of sigma to clip outliers when selecting for superstar flats
config.superStarSigmaClip=5.0

# Compute CCD gray terms on sub-ccd scale
config.ccdGraySubCcd=True

# Order of the 2D chebyshev polynomials for sub-ccd gray fit.
config.ccdGraySubCcdChebyshevOrder=1

# Should the sub-ccd gray chebyshev matrix be triangular to suppress high-order cross terms?
config.ccdGraySubCcdTriangular=True

# FGCM fit cycle number.  This is automatically incremented after each run and stage of outlier rejection.  See cookbook for details.
config.cycleNumber=4

# Is this the final cycle of the fitting?  Will automatically compute final selection of stars and photometric exposures, and will output zeropoints and standard stars for use in fgcmOutputProducts
config.isFinalCycle=False

# Maximum fit iterations, prior to final cycle.  The number of iterations will always be 0 in the final cycle for cleanup and final selection.
config.maxIterBeforeFinalCycle=75

# Boundary (in UTC) from day-to-day
config.utBoundary=0.0

# Mirror wash MJDs
config.washMjds=[56650.0, 57500.0, 57700.0, 58050.0]

# Epoch boundaries in MJD
config.epochMjds=[56650.0, 57420.0, 57606.0, 59000.0]

# Minimum good observations per band
config.minObsPerBand=2

# Observatory latitude
config.latitude=19.8256

# Maximum gray extinction to be considered bright observation
config.brightObsGrayMax=0.15

# Minimum number of good stars per CCD to be used in calibration fit. CCDs with fewer stars will have their calibration estimated from other CCDs in the same visit, with zeropoint error increased accordingly.
config.minStarPerCcd=5

# Minimum number of good CCDs per exposure/visit to be used in calibration fit. Visits with fewer good CCDs will have CCD zeropoints estimated where possible.
config.minCcdPerExp=5

# Maximum error on CCD gray offset to be considered photometric
config.maxCcdGrayErr=0.05

# Minimum number of good stars per exposure/visit to be used in calibration fit. Visits with fewer good stars will have CCD zeropoints estimated where possible.
config.minStarPerExp=100

# Minimum number of good exposures/visits to consider a partly photometric night
config.minExpPerNight=3

# Maximum exposure/visit gray value for initial selection of possible photometric observations.
config.expGrayInitialCut=-0.25

# Maximum (negative) exposure gray for a visit to be considered photometric. Must be same length as config.bands, and matched band-by-band.
config.expGrayPhotometricCut=[-0.03, -0.0125, -0.0125, -0.015, -0.0075, -0.0225, -0.025, -0.0225]

# Maximum (positive) exposure gray for a visit to be considered photometric. Must be same length as config.bands, and matched band-by-band.
config.expGrayHighCut=[0.0375, 0.0175, 0.0175, 0.0225, 0.015, 0.03, 0.0325, 0.03]

# Maximum (negative) exposure gray to be able to recover bad ccds via interpolation. Visits with more gray extinction will only get CCD zeropoints if there are sufficient star observations (minStarPerCcd) on that CCD.
config.expGrayRecoverCut=-1.0

# Maximum exposure variance to be considered possibly photometric
config.expVarGrayPhotometricCut=0.0025

# Maximum exposure gray error to be able to recover bad ccds via interpolation. Visits with more gray variance will only get CCD zeropoints if there are sufficient star observations (minStarPerCcd) on that CCD.
config.expGrayErrRecoverCut=0.05

# Number of aperture bins used in aperture correction fit.  When set to 0no fit will be performed, and the config.aperCorrInputSlopes will be used if available.
config.aperCorrFitNBins=10

# Aperture correction input slope parameters.  These are used on the first fit iteration, and aperture correction parameters will be updated from the data if config.aperCorrFitNBins > 0.  It is recommended to set thiswhen there is insufficient data to fit the parameters (e.g. tract mode). If set, must be same length as config.bands, and matched band-by-band.
config.aperCorrInputSlopes=[-1.0, -1.1579, -1.3908, -1.1436, -1.8149, -1.6974, -1.331, -1.2057]

config.sedboundaryterms.data={}
config.sedboundaryterms.data['gr']=lsst.fgcmcal.sedterms.Sedboundaryterm()
# name of primary band
config.sedboundaryterms.data['gr'].primary='g'

# name of secondary band
config.sedboundaryterms.data['gr'].secondary='r'

config.sedboundaryterms.data['ri']=lsst.fgcmcal.sedterms.Sedboundaryterm()
# name of primary band
config.sedboundaryterms.data['ri'].primary='r'

# name of secondary band
config.sedboundaryterms.data['ri'].secondary='i'

config.sedboundaryterms.data['iz']=lsst.fgcmcal.sedterms.Sedboundaryterm()
# name of primary band
config.sedboundaryterms.data['iz'].primary='i'

# name of secondary band
config.sedboundaryterms.data['iz'].secondary='z'

config.sedboundaryterms.data['zy']=lsst.fgcmcal.sedterms.Sedboundaryterm()
# name of primary band
config.sedboundaryterms.data['zy'].primary='z'

# name of secondary band
config.sedboundaryterms.data['zy'].secondary='y'

config.sedboundaryterms.data['N387g']=lsst.fgcmcal.sedterms.Sedboundaryterm()
# name of primary band
config.sedboundaryterms.data['N387g'].primary='N387'

# name of secondary band
config.sedboundaryterms.data['N387g'].secondary='g'

config.sedboundaryterms.data['N816i']=lsst.fgcmcal.sedterms.Sedboundaryterm()
# name of primary band
config.sedboundaryterms.data['N816i'].primary='N816'

# name of secondary band
config.sedboundaryterms.data['N816i'].secondary='i'

config.sedboundaryterms.data['N921z']=lsst.fgcmcal.sedterms.Sedboundaryterm()
# name of primary band
config.sedboundaryterms.data['N921z'].primary='N921'

# name of secondary band
config.sedboundaryterms.data['N921z'].secondary='z'

config.sedterms.data={}
config.sedterms.data['g']=lsst.fgcmcal.sedterms.Sedterm()
# Name of primary Sedboundaryterm
config.sedterms.data['g'].primaryTerm='gr'

# Name of secondary Sedboundaryterm
config.sedterms.data['g'].secondaryTerm='ri'

# Extrapolate to compute SED slope
config.sedterms.data['g'].extrapolated=False

# Adjustment constant for SED slope
config.sedterms.data['g'].constant=1.6

# Primary band name for extrapolation
config.sedterms.data['g'].primaryBand=None

# Secondary band name for extrapolation
config.sedterms.data['g'].secondaryBand=None

# Tertiary band name for extrapolation
config.sedterms.data['g'].tertiaryBand=None

config.sedterms.data['r']=lsst.fgcmcal.sedterms.Sedterm()
# Name of primary Sedboundaryterm
config.sedterms.data['r'].primaryTerm='gr'

# Name of secondary Sedboundaryterm
config.sedterms.data['r'].secondaryTerm='ri'

# Extrapolate to compute SED slope
config.sedterms.data['r'].extrapolated=False

# Adjustment constant for SED slope
config.sedterms.data['r'].constant=0.9

# Primary band name for extrapolation
config.sedterms.data['r'].primaryBand=None

# Secondary band name for extrapolation
config.sedterms.data['r'].secondaryBand=None

# Tertiary band name for extrapolation
config.sedterms.data['r'].tertiaryBand=None

config.sedterms.data['i']=lsst.fgcmcal.sedterms.Sedterm()
# Name of primary Sedboundaryterm
config.sedterms.data['i'].primaryTerm='ri'

# Name of secondary Sedboundaryterm
config.sedterms.data['i'].secondaryTerm='iz'

# Extrapolate to compute SED slope
config.sedterms.data['i'].extrapolated=False

# Adjustment constant for SED slope
config.sedterms.data['i'].constant=1.0

# Primary band name for extrapolation
config.sedterms.data['i'].primaryBand=None

# Secondary band name for extrapolation
config.sedterms.data['i'].secondaryBand=None

# Tertiary band name for extrapolation
config.sedterms.data['i'].tertiaryBand=None

config.sedterms.data['z']=lsst.fgcmcal.sedterms.Sedterm()
# Name of primary Sedboundaryterm
config.sedterms.data['z'].primaryTerm='iz'

# Name of secondary Sedboundaryterm
config.sedterms.data['z'].secondaryTerm='zy'

# Extrapolate to compute SED slope
config.sedterms.data['z'].extrapolated=False

# Adjustment constant for SED slope
config.sedterms.data['z'].constant=1.0

# Primary band name for extrapolation
config.sedterms.data['z'].primaryBand=None

# Secondary band name for extrapolation
config.sedterms.data['z'].secondaryBand=None

# Tertiary band name for extrapolation
config.sedterms.data['z'].tertiaryBand=None

config.sedterms.data['y']=lsst.fgcmcal.sedterms.Sedterm()
# Name of primary Sedboundaryterm
config.sedterms.data['y'].primaryTerm='zy'

# Name of secondary Sedboundaryterm
config.sedterms.data['y'].secondaryTerm='iz'

# Extrapolate to compute SED slope
config.sedterms.data['y'].extrapolated=True

# Adjustment constant for SED slope
config.sedterms.data['y'].constant=0.25

# Primary band name for extrapolation
config.sedterms.data['y'].primaryBand='y'

# Secondary band name for extrapolation
config.sedterms.data['y'].secondaryBand='z'

# Tertiary band name for extrapolation
config.sedterms.data['y'].tertiaryBand='i'

config.sedterms.data['N387']=lsst.fgcmcal.sedterms.Sedterm()
# Name of primary Sedboundaryterm
config.sedterms.data['N387'].primaryTerm='N387g'

# Name of secondary Sedboundaryterm
config.sedterms.data['N387'].secondaryTerm=None

# Extrapolate to compute SED slope
config.sedterms.data['N387'].extrapolated=False

# Adjustment constant for SED slope
config.sedterms.data['N387'].constant=1.0

# Primary band name for extrapolation
config.sedterms.data['N387'].primaryBand=None

# Secondary band name for extrapolation
config.sedterms.data['N387'].secondaryBand=None

# Tertiary band name for extrapolation
config.sedterms.data['N387'].tertiaryBand=None

config.sedterms.data['N816']=lsst.fgcmcal.sedterms.Sedterm()
# Name of primary Sedboundaryterm
config.sedterms.data['N816'].primaryTerm='N816i'

# Name of secondary Sedboundaryterm
config.sedterms.data['N816'].secondaryTerm=None

# Extrapolate to compute SED slope
config.sedterms.data['N816'].extrapolated=False

# Adjustment constant for SED slope
config.sedterms.data['N816'].constant=1.0

# Primary band name for extrapolation
config.sedterms.data['N816'].primaryBand=None

# Secondary band name for extrapolation
config.sedterms.data['N816'].secondaryBand=None

# Tertiary band name for extrapolation
config.sedterms.data['N816'].tertiaryBand=None

config.sedterms.data['N921']=lsst.fgcmcal.sedterms.Sedterm()
# Name of primary Sedboundaryterm
config.sedterms.data['N921'].primaryTerm='N921z'

# Name of secondary Sedboundaryterm
config.sedterms.data['N921'].secondaryTerm=None

# Extrapolate to compute SED slope
config.sedterms.data['N921'].extrapolated=False

# Adjustment constant for SED slope
config.sedterms.data['N921'].constant=1.0

# Primary band name for extrapolation
config.sedterms.data['N921'].primaryBand=None

# Secondary band name for extrapolation
config.sedterms.data['N921'].secondaryBand=None

# Tertiary band name for extrapolation
config.sedterms.data['N921'].tertiaryBand=None

# Maximum mag error for fitting sigma_FGCM
config.sigFgcmMaxErr=0.01

# Maximum (absolute) gray value for observation in sigma_FGCM. May be 1 element (same for all bands) or the same length as config.bands.
config.sigFgcmMaxEGray=[0.05, 0.05, 0.05, 0.05, 0.05, 0.15, 0.15, 0.15]

# Maximum error on a star observation to use in ccd gray computation
config.ccdGrayMaxStarErr=0.1

# Approximate overall throughput at start of calibration observations. May be 1 element (same for all bands) or the same length as config.bands.
config.approxThroughput=[1.0]

# Allowed range for systematic error floor estimation
config.sigmaCalRange=[0.001, 0.003]

# Magnitude percentile range to fit systematic error floor
config.sigmaCalFitPercentile=[0.05, 0.15]

# Magnitude percentile range to plot systematic error floor
config.sigmaCalPlotPercentile=[0.05, 0.95]

# Systematic error floor for all zeropoints
config.sigma0Phot=0.003

# Reference longitude for plotting maps
config.mapLongitudeRef=0.0

# Healpix nside for plotting maps
config.mapNSide=256

# Filename start for plot output files
config.outfileBase='fgcmHscCalibrations'

# Encoded star-color cuts (to be cleaned up)
config.starColorCuts=['g,r,-0.25,2.25', 'r,i,-0.50,2.25', 'i,z,-0.50,1.00', 'g,i,0.0,3.5']

# Band indices to use to split stars by color
config.colorSplitIndices=[1, 3]

# Should FGCM model the magnitude errors from sky/fwhm? (False means trust inputs)
config.modelMagErrors=True

# Model PWV with a quadratic term for variation through the night?
config.useQuadraticPwv=False

# Model instrumental parameters per band? Otherwise, instrumental parameters (QE changes with time) are shared among all bands.
config.instrumentParsPerBand=True

# Minimum time change (in days) between observations to use in constraining instrument slope.
config.instrumentSlopeMinDeltaT=20.0

# Fit (intraband) mirror chromatic term?
config.fitMirrorChromaticity=False

# Mirror coating dates in MJD
config.coatingMjds=[56650.0, 58050.0]

# Output standard stars prior to final cycle?  Used in debugging.
config.outputStandardsBeforeFinalCycle=False

# Output standard stars prior to final cycle?  Used in debugging.
config.outputZeropointsBeforeFinalCycle=False

# Use star repeatability (instead of exposures) for computing photometric cuts? Recommended for tract mode or bands with few exposures. May be 1 element (same for all bands) or the same length as config.bands.
config.useRepeatabilityForExpGrayCuts=[False, False, False, False, False, True, True, True]

# Number of sigma for automatic computation of (low) photometric cut. Cut is based on exposure gray width (per band), unless useRepeatabilityForExpGrayCuts is set, in which case the star repeatability is used (also per band).
config.autoPhotometricCutNSig=3.0

# Number of sigma for automatic computation of (high) outlier cut. Cut is based on exposure gray width (per band), unless useRepeatabilityForExpGrayCuts is set, in which case the star repeatability is used (also per band).
config.autoHighCutNSig=4.0

# Be less verbose with logging.
config.quietMode=False

