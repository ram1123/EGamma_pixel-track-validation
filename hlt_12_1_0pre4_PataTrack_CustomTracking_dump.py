import FWCore.ParameterSet.Config as cms
from HeterogeneousCore.CUDACore.SwitchProducerCUDA import SwitchProducerCUDA

process = cms.Process("MYHLT")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('root://cms-xrd-global.cern.ch///store/mc/Run3Winter21DRMiniAOD/DYToLL_M-50_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/270024/a5adba3d-a6b2-46c0-b690-04e9462fad11.root'),
    inputCommands = cms.untracked.vstring('keep *')
)
process.HLTConfigVersion = cms.PSet(
    tableName = cms.string('/users/swmukher/egm_ele5_open/V16')
)

process.HLTIter0GroupedCkfTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    cleanTrajectoryAfterInOut = cms.bool(False),
    doSeedingRegionRebuilding = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0PSetTrajectoryFilterIT')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useHitsSplitting = cms.bool(False),
    useSameTrajFilter = cms.bool(True)
)

process.HLTIter0HighPtTkMuPSetTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(4),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0HighPtTkMuPSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTIter0HighPtTkMuPSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter0IterL3FromL1MuonGroupedCkfTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(10.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter0IterL3FromL1MuonPSetGroupedCkfTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(1000.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0IterL3FromL1MuonGroupedCkfTrajectoryFilterIT')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(True),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(1.0),
    maxCand = cms.int32(5),
    minNrOfHitsForRebuild = cms.int32(2),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0IterL3FromL1MuonGroupedCkfTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTIter0IterL3MuonGroupedCkfTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(10.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter0IterL3MuonPSetGroupedCkfTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(1000.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0IterL3MuonGroupedCkfTrajectoryFilterIT')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(True),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(1.0),
    maxCand = cms.int32(5),
    minNrOfHitsForRebuild = cms.int32(2),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0IterL3MuonGroupedCkfTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTIter0PSetTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator9'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTIter0PSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter1GroupedCkfTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltIter1ESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    foundHitBonus = cms.double(5.0),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter1PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTIter1PSetTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltIter1ESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter1PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTIter1PSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.2),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter2GroupedCkfTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    cleanTrajectoryAfterInOut = cms.bool(False),
    doSeedingRegionRebuilding = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter2PSetTrajectoryFilterIT')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter2PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useHitsSplitting = cms.bool(False),
    useSameTrajFilter = cms.bool(True)
)

process.HLTIter2HighPtTkMuPSetTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltIter2HighPtTkMuESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter2HighPtTkMuPSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTIter2HighPtTkMuPSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(3),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter2IterL3FromL1MuonPSetGroupedCkfTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltIter2HighPtTkMuESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(1000.0),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(False),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter2IterL3FromL1MuonPSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTIter2IterL3FromL1MuonPSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(3),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter2IterL3MuonPSetGroupedCkfTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltIter2HighPtTkMuESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(1000.0),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(False),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter2IterL3MuonPSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTIter2IterL3MuonPSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(3),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter2PSetTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltIter2ESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter2PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTIter2PSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(1),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter3PSetTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltIter3ESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(1),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter3PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTIter3PSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter4PSetTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltIter4ESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(1),
    minNrOfHitsForRebuild = cms.untracked.int32(4),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter4PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTIter4PSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(6),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetCkf3HitTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(-1),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetCkfBaseTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetCkfTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(-1),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetCkfTrajectoryFilterIterL3OI = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(10.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(-1),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(3.0),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetDetachedCkfTrajectoryBuilderForHI = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2MeasurementEstimator9'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedCkfTrajectoryFilterForHI')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(0.0),
    maxPtForLooperReconstruction = cms.double(0.0),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialForHI'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOppositeForHI'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedCkfTrajectoryFilterForHI')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetDetachedCkfTrajectoryBuilderForHIGlobalPt8 = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2MeasurementEstimator9'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedCkfTrajectoryFilterForHIGlobalPt8')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(0.0),
    maxPtForLooperReconstruction = cms.double(0.0),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialForHI'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOppositeForHI'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedCkfTrajectoryFilterForHIGlobalPt8')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetDetachedCkfTrajectoryFilterForHI = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(0.701),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(6),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetDetachedCkfTrajectoryFilterForHIGlobalPt8 = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(0.701),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(8.0),
    minimumNumberOfHits = cms.int32(6),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetDetachedQuadStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPDetachedQuadStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedQuadStepTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedQuadStepTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetDetachedQuadStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPDetachedQuadStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedQuadStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetDetachedQuadStepTrajectoryBuilderPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPDetachedQuadStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedQuadStepTrajectoryFilterPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetDetachedQuadStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.075),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetDetachedQuadStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetDetachedQuadStepTrajectoryFilterPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetDetachedStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedStepTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedStepTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetDetachedStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CompositeTrajectoryFilter'),
    filters = cms.VPSet(cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedStepTrajectoryFilterBase')
    ))
)

process.HLTPSetDetachedStepTrajectoryFilterBase = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(2),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.075),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetDetachedTripletStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPDetachedTripletStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedTripletStepTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedTripletStepTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetDetachedTripletStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPDetachedTripletStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedTripletStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetDetachedTripletStepTrajectoryBuilderPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPDetachedTripletStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedTripletStepTrajectoryFilterPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetDetachedTripletStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.075),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetDetachedTripletStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetDetachedTripletStepTrajectoryFilterPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetGroupedCkfTrajectoryBuilderIterL3ForOI = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltSiStripClusters'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    deltaEta = cms.double(-1.0),
    deltaPhi = cms.double(-1.0),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(1000.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfTrajectoryFilterIterL3OI')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(5),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    propagatorProximity = cms.string('SteppingHelixPropagatorAny'),
    requireSeedHitsInRebuild = cms.bool(False),
    rescaleErrorIfFail = cms.double(1.0),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfTrajectoryFilterIterL3OI')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True),
    useSeedLayer = cms.bool(False)
)

process.HLTPSetHighPtTripletStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPHighPtTripletStepChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetHighPtTripletStepTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetHighPtTripletStepTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetHighPtTripletStepTrajectoryBuilderForDmesonPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPHighPtTripletStepChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetHighPtTripletStepTrajectoryFilterForDmesonPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetHighPtTripletStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPHighPtTripletStepChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetHighPtTripletStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetHighPtTripletStepTrajectoryBuilderPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPHighPtTripletStepChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetHighPtTripletStepTrajectoryFilterPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetHighPtTripletStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.2),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(5),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetHighPtTripletStepTrajectoryFilterForDmesonPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(3.5),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetHighPtTripletStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(1.0),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetHighPtTripletStepTrajectoryFilterPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.7),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetInitialCkfTrajectoryBuilderForHI = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    intermediateCleaning = cms.bool(False),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialForHI'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOppositeForHI'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetInitialCkfTrajectoryFilterForHI')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTPSetInitialCkfTrajectoryFilterForHI = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(6),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetInitialStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPInitialStepChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(True),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(1),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetInitialStepTrajectoryBuilderForDmesonPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPInitialStepChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(True),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(1),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilterForDmesonPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetInitialStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPInitialStepChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(True),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(1),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetInitialStepTrajectoryBuilderPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPInitialStepChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(True),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(1),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilterPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetInitialStepTrajectoryBuilderPreSplittingForDmesonPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPInitialStepChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilterPreSplittingForDmesonPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetInitialStepTrajectoryBuilderPreSplittingForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPInitialStepChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilterPreSplittingForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetInitialStepTrajectoryBuilderPreSplittingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPInitialStepChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilterPreSplittingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetInitialStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.2),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetInitialStepTrajectoryFilterBase = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(2),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.2),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetInitialStepTrajectoryFilterBasePreSplittingForDmesonPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(3.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetInitialStepTrajectoryFilterBasePreSplittingForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(1.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetInitialStepTrajectoryFilterBasePreSplittingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.2),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetInitialStepTrajectoryFilterForDmesonPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(3.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetInitialStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(1.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetInitialStepTrajectoryFilterPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.6),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetInitialStepTrajectoryFilterPreSplittingForDmesonPPOnAA = cms.PSet(
    ComponentType = cms.string('CompositeTrajectoryFilter'),
    filters = cms.VPSet(
        cms.PSet(
            refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilterBasePreSplittingForDmesonPPOnAA')
        ),
        cms.PSet(
            refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilterShapePreSplittingPPOnAA')
        )
    )
)

process.HLTPSetInitialStepTrajectoryFilterPreSplittingForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CompositeTrajectoryFilter'),
    filters = cms.VPSet(
        cms.PSet(
            refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilterBasePreSplittingForFullTrackingPPOnAA')
        ),
        cms.PSet(
            refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilterShapePreSplittingPPOnAA')
        )
    )
)

process.HLTPSetInitialStepTrajectoryFilterPreSplittingPPOnAA = cms.PSet(
    ComponentType = cms.string('CompositeTrajectoryFilter'),
    filters = cms.VPSet(
        cms.PSet(
            refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilterBasePreSplittingPPOnAA')
        ),
        cms.PSet(
            refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilterShapePreSplittingPPOnAA')
        )
    )
)

process.HLTPSetInitialStepTrajectoryFilterShapePreSplittingPPOnAA = cms.PSet(
    ComponentType = cms.string('StripSubClusterShapeTrajectoryFilter'),
    layerMask = cms.PSet(
        TEC = cms.bool(False),
        TIB = cms.vuint32(1, 2),
        TID = cms.vuint32(1, 2),
        TOB = cms.bool(False)
    ),
    maxNSat = cms.uint32(3),
    maxTrimmedSizeDiffNeg = cms.double(1.0),
    maxTrimmedSizeDiffPos = cms.double(0.7),
    seedCutMIPs = cms.double(0.35),
    seedCutSN = cms.double(7.0),
    subclusterCutMIPs = cms.double(0.45),
    subclusterCutSN = cms.double(12.0),
    subclusterWindow = cms.double(0.7),
    trimMaxADC = cms.double(30.0),
    trimMaxFracNeigh = cms.double(0.25),
    trimMaxFracTotal = cms.double(0.15)
)

process.HLTPSetJetCoreStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetJetCoreStepTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(50),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetJetCoreStepTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetJetCoreStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(50),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetJetCoreStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetJetCoreStepTrajectoryBuilderPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(50),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetJetCoreStepTrajectoryFilterPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetJetCoreStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetJetCoreStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetJetCoreStepTrajectoryFilterPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetLowPtQuadStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPLowPtQuadStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetLowPtQuadStepTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(4),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetLowPtQuadStepTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetLowPtQuadStepTrajectoryBuilderForDmesonPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPLowPtQuadStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(4),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetLowPtQuadStepTrajectoryFilterForDmesonPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetLowPtQuadStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPLowPtQuadStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(4),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetLowPtQuadStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetLowPtQuadStepTrajectoryBuilderPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPLowPtQuadStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(4),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetLowPtQuadStepTrajectoryFilterPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetLowPtQuadStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.075),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetLowPtQuadStepTrajectoryFilterForDmesonPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(2.8),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetLowPtQuadStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(1.0),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetLowPtQuadStepTrajectoryFilterPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.49),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetLowPtStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetLowPtStepTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(4),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetLowPtStepTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetLowPtStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(1),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.075),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetLowPtTripletStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPLowPtTripletStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetLowPtTripletStepTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(4),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetLowPtTripletStepTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetLowPtTripletStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPLowPtTripletStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(4),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetLowPtTripletStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetLowPtTripletStepTrajectoryBuilderPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPLowPtTripletStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(4),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetLowPtTripletStepTrajectoryFilterPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetLowPtTripletStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.075),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetLowPtTripletStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(2.8),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetLowPtTripletStepTrajectoryFilterPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.49),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetMixedStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeTightMeasurementEstimator16'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMixedStepTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialForMixedStep'),
    propagatorOpposite = cms.string('PropagatorWithMaterialForMixedStepOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMixedStepTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetMixedStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.4),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetMixedStepTrajectoryFilterBase = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.05),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetMixedTripletStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPMixedTripletStepChi2ChargeMeasurementEstimator16'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMixedTripletStepTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialForMixedStep'),
    propagatorOpposite = cms.string('PropagatorWithMaterialForMixedStepOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMixedTripletStepTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetMixedTripletStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPMixedTripletStepChi2ChargeMeasurementEstimator16'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialForMixedStep'),
    propagatorOpposite = cms.string('PropagatorWithMaterialForMixedStepOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMixedTripletStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetMixedTripletStepTrajectoryBuilderPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPMixedTripletStepChi2ChargeMeasurementEstimator16'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialForMixedStep'),
    propagatorOpposite = cms.string('PropagatorWithMaterialForMixedStepOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMixedTripletStepTrajectoryFilterPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetMixedTripletStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.4),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetMixedTripletStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.4),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetMixedTripletStepTrajectoryFilterPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.4),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.4),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetMuTrackJpsiEffTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(1),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMuTrackJpsiEffTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTPSetMuTrackJpsiEffTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(9),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(1.0),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetMuTrackJpsiTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(1),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMuTrackJpsiTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTPSetMuTrackJpsiTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(8),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(10.0),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetMuonCkfTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('MuonCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    deltaEta = cms.double(-1.0),
    deltaPhi = cms.double(-1.0),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    intermediateCleaning = cms.bool(False),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    propagatorProximity = cms.string('SteppingHelixPropagatorAny'),
    rescaleErrorIfFail = cms.double(1.0),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMuonCkfTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSeedLayer = cms.bool(False)
)

process.HLTPSetMuonCkfTrajectoryBuilderSeedHit = cms.PSet(
    ComponentType = cms.string('MuonCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    deltaEta = cms.double(-1.0),
    deltaPhi = cms.double(-1.0),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    intermediateCleaning = cms.bool(False),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    propagatorProximity = cms.string('SteppingHelixPropagatorAny'),
    rescaleErrorIfFail = cms.double(1.0),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMuonCkfTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSeedLayer = cms.bool(True)
)

process.HLTPSetMuonCkfTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(-1),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetMuonTrackingRegionBuilder8356 = cms.PSet(
    DeltaEta = cms.double(0.2),
    DeltaPhi = cms.double(0.2),
    DeltaR = cms.double(0.2),
    DeltaZ = cms.double(15.9),
    EtaR_UpperLimit_Par1 = cms.double(0.25),
    EtaR_UpperLimit_Par2 = cms.double(0.15),
    Eta_fixed = cms.bool(False),
    Eta_min = cms.double(0.1),
    MeasurementTrackerName = cms.InputTag("hltESPMeasurementTracker"),
    OnDemand = cms.int32(-1),
    PhiR_UpperLimit_Par1 = cms.double(0.6),
    PhiR_UpperLimit_Par2 = cms.double(0.2),
    Phi_fixed = cms.bool(False),
    Phi_min = cms.double(0.1),
    Pt_fixed = cms.bool(False),
    Pt_min = cms.double(1.5),
    Rescale_Dz = cms.double(3.0),
    Rescale_eta = cms.double(3.0),
    Rescale_phi = cms.double(3.0),
    UseVertex = cms.bool(False),
    Z_fixed = cms.bool(True),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    input = cms.InputTag("hltL2Muons","UpdatedAtVtx"),
    maxRegions = cms.int32(2),
    precise = cms.bool(True),
    vertexCollection = cms.InputTag("pixelVertices")
)

process.HLTPSetPixelLessStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPPixelLessStepChi2ChargeMeasurementEstimator16'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelLessStepTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(4),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelLessStepTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetPixelLessStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPPixelLessStepChi2ChargeMeasurementEstimator16'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(4),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelLessStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetPixelLessStepTrajectoryBuilderPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPPixelLessStepChi2ChargeMeasurementEstimator16'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(4),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelLessStepTrajectoryFilterPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetPixelLessStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(1),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetPixelLessStepTrajectoryFilterBase = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.05),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetPixelLessStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(1),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetPixelLessStepTrajectoryFilterPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(2.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(1),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetPixelPairCkfTrajectoryBuilderForHI = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator9ForHI'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelPairCkfTrajectoryFilterForHI')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialForHI'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOppositeForHI'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelPairCkfTrajectoryFilterForHI')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetPixelPairCkfTrajectoryBuilderForHIGlobalPt8 = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator9ForHI'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelPairCkfTrajectoryFilterForHIGlobalPt8')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialForHI'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOppositeForHI'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelPairCkfTrajectoryFilterForHIGlobalPt8')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetPixelPairCkfTrajectoryFilterForHI = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(100),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(1.0),
    minimumNumberOfHits = cms.int32(6),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetPixelPairCkfTrajectoryFilterForHIGlobalPt8 = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(100),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(8.0),
    minimumNumberOfHits = cms.int32(6),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetPixelPairStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPPixelPairStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelPairStepTrajectoryFilterInOut')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelPairStepTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(False)
)

process.HLTPSetPixelPairStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPPixelPairStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelPairStepTrajectoryFilterInOutForFullTrackingPPOnAA')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelPairStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(False)
)

process.HLTPSetPixelPairStepTrajectoryBuilderPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPPixelPairStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelPairStepTrajectoryFilterInOutPPOnAA')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelPairStepTrajectoryFilterPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(False)
)

process.HLTPSetPixelPairStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetPixelPairStepTrajectoryFilterBase = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(2),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetPixelPairStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetPixelPairStepTrajectoryFilterInOut = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(1),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetPixelPairStepTrajectoryFilterInOutForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(1),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetPixelPairStepTrajectoryFilterInOutPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(1),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetPixelPairStepTrajectoryFilterPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetPvClusterComparer = cms.PSet(
    track_chi2_max = cms.double(9999999.0),
    track_prob_min = cms.double(-1.0),
    track_pt_max = cms.double(10.0),
    track_pt_min = cms.double(2.5)
)

process.HLTPSetPvClusterComparerForBTag = cms.PSet(
    track_chi2_max = cms.double(20.0),
    track_prob_min = cms.double(-1.0),
    track_pt_max = cms.double(20.0),
    track_pt_min = cms.double(0.1)
)

process.HLTPSetPvClusterComparerForIT = cms.PSet(
    track_chi2_max = cms.double(20.0),
    track_prob_min = cms.double(-1.0),
    track_pt_max = cms.double(20.0),
    track_pt_min = cms.double(1.0)
)

process.HLTPSetTobTecStepInOutTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(1),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetTobTecStepInOutTrajectoryFilterBase = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(1),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetTobTecStepInOutTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(1),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetTobTecStepInOutTrajectoryFilterPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(2.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(1),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetTobTecStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPTobTecStepChi2ChargeMeasurementEstimator16'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetTobTecStepInOutTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(4),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetTobTecStepTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(False)
)

process.HLTPSetTobTecStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPTobTecStepChi2ChargeMeasurementEstimator16'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetTobTecStepInOutTrajectoryFilterForFullTrackingPPOnAA')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(4),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetTobTecStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(False)
)

process.HLTPSetTobTecStepTrajectoryBuilderPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPTobTecStepChi2ChargeMeasurementEstimator16'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetTobTecStepInOutTrajectoryFilterPPOnAA')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(4),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetTobTecStepTrajectoryFilterPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(False)
)

process.HLTPSetTobTecStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(1),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetTobTecStepTrajectoryFilterBase = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(1),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetTobTecStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(1),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetTobTecStepTrajectoryFilterPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(2.0),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(1),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetTrajectoryBuilderForElectrons = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    intermediateCleaning = cms.bool(False),
    lostHitPenalty = cms.double(90.0),
    maxCand = cms.int32(5),
    propagatorAlong = cms.string('hltESPFwdElectronPropagator'),
    propagatorOpposite = cms.string('hltESPBwdElectronPropagator'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetTrajectoryFilterForElectrons')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTPSetTrajectoryBuilderForGsfElectrons = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('hltESPMeasurementTracker'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator2000'),
    intermediateCleaning = cms.bool(False),
    lostHitPenalty = cms.double(90.0),
    maxCand = cms.int32(5),
    propagatorAlong = cms.string('hltESPFwdElectronPropagator'),
    propagatorOpposite = cms.string('hltESPBwdElectronPropagator'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetTrajectoryFilterForElectrons')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTPSetTrajectoryFilterForElectrons = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(-1),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(-1),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(2.0),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetTrajectoryFilterL3 = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(1000000000),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.5),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetbJetRegionalTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(8),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(1.0),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTSeedFromConsecutiveHitsCreator = cms.PSet(
    ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
    MinOneOverPtError = cms.double(1.0),
    OriginTransverseErrorMultiplier = cms.double(1.0),
    SeedMomentumForBOFF = cms.double(5.0),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string(''),
    propagator = cms.string('PropagatorWithMaterial')
)

process.HLTSeedFromConsecutiveHitsCreatorIT = cms.PSet(
    ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
    MinOneOverPtError = cms.double(1.0),
    OriginTransverseErrorMultiplier = cms.double(1.0),
    SeedMomentumForBOFF = cms.double(5.0),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf')
)

process.HLTSeedFromConsecutiveHitsTripletOnlyCreator = cms.PSet(
    ComponentName = cms.string('SeedFromConsecutiveHitsTripletOnlyCreator'),
    MinOneOverPtError = cms.double(1.0),
    OriginTransverseErrorMultiplier = cms.double(1.0),
    SeedMomentumForBOFF = cms.double(5.0),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf')
)

process.HLTSeedFromProtoTracks = cms.PSet(
    ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
    MinOneOverPtError = cms.double(1.0),
    OriginTransverseErrorMultiplier = cms.double(1.0),
    SeedMomentumForBOFF = cms.double(5.0),
    TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf')
)

process.HLTSiStripClusterChargeCutForHI = cms.PSet(
    value = cms.double(2069.0)
)

process.HLTSiStripClusterChargeCutLoose = cms.PSet(
    value = cms.double(1620.0)
)

process.HLTSiStripClusterChargeCutNone = cms.PSet(
    value = cms.double(-1.0)
)

process.HLTSiStripClusterChargeCutTight = cms.PSet(
    value = cms.double(1945.0)
)

process.HLTSiStripClusterChargeCutTiny = cms.PSet(
    value = cms.double(800.0)
)

process.datasets = cms.PSet(
    AlCaLumiPixelCountsExpress = cms.vstring('AlCa_LumiPixelsCounts_Random_v1'),
    AlCaLumiPixelCountsPrompt = cms.vstring('AlCa_LumiPixelsCounts_ZeroBias_v1'),
    AlCaP0 = cms.vstring(
        'AlCa_EcalEtaEBonly_v13',
        'AlCa_EcalEtaEEonly_v13',
        'AlCa_EcalPi0EBonly_v13',
        'AlCa_EcalPi0EEonly_v13'
    ),
    AlCaPhiSym = cms.vstring('AlCa_EcalPhiSym_v9'),
    BTagMu = cms.vstring(
        'HLT_BTagMu_AK4DiJet110_Mu5_noalgo_v13',
        'HLT_BTagMu_AK4DiJet110_Mu5_v13',
        'HLT_BTagMu_AK4DiJet170_Mu5_noalgo_v12',
        'HLT_BTagMu_AK4DiJet170_Mu5_v12',
        'HLT_BTagMu_AK4DiJet20_Mu5_noalgo_v13',
        'HLT_BTagMu_AK4DiJet20_Mu5_v13',
        'HLT_BTagMu_AK4DiJet40_Mu5_noalgo_v13',
        'HLT_BTagMu_AK4DiJet40_Mu5_v13',
        'HLT_BTagMu_AK4DiJet70_Mu5_noalgo_v13',
        'HLT_BTagMu_AK4DiJet70_Mu5_v13',
        'HLT_BTagMu_AK4Jet300_Mu5_noalgo_v12',
        'HLT_BTagMu_AK4Jet300_Mu5_v12',
        'HLT_BTagMu_AK8DiJet170_Mu5_noalgo_v9',
        'HLT_BTagMu_AK8DiJet170_Mu5_v9',
        'HLT_BTagMu_AK8Jet170_DoubleMu5_noalgo_v2',
        'HLT_BTagMu_AK8Jet170_DoubleMu5_v2',
        'HLT_BTagMu_AK8Jet300_Mu5_noalgo_v12',
        'HLT_BTagMu_AK8Jet300_Mu5_v12'
    ),
    Charmonium = cms.vstring(
        'HLT_Dimuon0_Jpsi3p5_Muon2_v5',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v7',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v7',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v7',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v7',
        'HLT_Dimuon0_Jpsi_NoVertexing_v8',
        'HLT_Dimuon0_Jpsi_v8',
        'HLT_Dimuon0_LowMass_L1_0er1p5R_v7',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v8',
        'HLT_Dimuon0_LowMass_L1_4R_v7',
        'HLT_Dimuon0_LowMass_L1_4_v8',
        'HLT_Dimuon0_LowMass_v8',
        'HLT_Dimuon10_PsiPrime_Barrel_Seagulls_v7',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v6',
        'HLT_Dimuon18_PsiPrime_v14',
        'HLT_Dimuon20_Jpsi_Barrel_Seagulls_v7',
        'HLT_Dimuon25_Jpsi_noCorrL1_v6',
        'HLT_Dimuon25_Jpsi_v14',
        'HLT_DoubleMu2_Jpsi_DoubleTkMu0_Phi_v5',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v6',
        'HLT_DoubleMu4_3_Bs_v14',
        'HLT_DoubleMu4_3_Jpsi_v2',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v7',
        'HLT_DoubleMu4_JpsiTrk_Displaced_v15',
        'HLT_DoubleMu4_Jpsi_Displaced_v7',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v7',
        'HLT_DoubleMu4_PsiPrimeTrk_Displaced_v15',
        'HLT_Mu30_TkMu0_Psi_v1',
        'HLT_Mu7p5_L2Mu2_Jpsi_v10',
        'HLT_Mu7p5_Track2_Jpsi_v11',
        'HLT_Mu7p5_Track3p5_Jpsi_v11',
        'HLT_Mu7p5_Track7_Jpsi_v11'
    ),
    Commissioning = cms.vstring(
        'HLT_IsoTrackHB_v4',
        'HLT_IsoTrackHE_v4',
        'HLT_L1_CDC_SingleMu_3_er1p2_TOP120_DPHI2p618_3p142_v2'
    ),
    Cosmics = cms.vstring('HLT_L1SingleMuCosmics_v1'),
    DQMOnlineBeamspot = cms.vstring(
        'HLT_HT300_Beamspot_v11',
        'HLT_HT450_Beamspot_v11',
        'HLT_ZeroBias_Beamspot_v4'
    ),
    DisplacedJet = cms.vstring(
        'HLT_HT400_DisplacedDijet40_DisplacedTrack_v13',
        'HLT_HT425_v9',
        'HLT_HT430_DisplacedDijet40_DisplacedTrack_v13',
        'HLT_HT430_DisplacedDijet60_DisplacedTrack_v13',
        'HLT_HT500_DisplacedDijet40_DisplacedTrack_v13',
        'HLT_HT550_DisplacedDijet60_Inclusive_v13',
        'HLT_HT650_DisplacedDijet60_Inclusive_v13'
    ),
    DoubleMuon = cms.vstring(
        'HLT_DoubleL2Mu23NoVtx_2Cha_CosmicSeed_NoL2Matched_v2',
        'HLT_DoubleL2Mu23NoVtx_2Cha_CosmicSeed_v2',
        'HLT_DoubleL2Mu23NoVtx_2Cha_NoL2Matched_v2',
        'HLT_DoubleL2Mu23NoVtx_2Cha_v2',
        'HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_Eta2p4_v2',
        'HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_NoL2Matched_v2',
        'HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_v2',
        'HLT_DoubleL2Mu25NoVtx_2Cha_Eta2p4_v2',
        'HLT_DoubleL2Mu25NoVtx_2Cha_NoL2Matched_v2',
        'HLT_DoubleL2Mu25NoVtx_2Cha_v2',
        'HLT_DoubleL2Mu30NoVtx_2Cha_CosmicSeed_Eta2p4_v2',
        'HLT_DoubleL2Mu30NoVtx_2Cha_Eta2p4_v2',
        'HLT_DoubleL2Mu50_v2',
        'HLT_DoubleMu33NoFiltersNoVtxDisplaced_v1',
        'HLT_DoubleMu3_DCA_PFMET50_PFMHT60_v10',
        'HLT_DoubleMu3_DZ_PFMET50_PFMHT60_v10',
        'HLT_DoubleMu3_DZ_PFMET70_PFMHT70_v10',
        'HLT_DoubleMu3_DZ_PFMET90_PFMHT90_v10',
        'HLT_DoubleMu40NoFiltersNoVtxDisplaced_v1',
        'HLT_DoubleMu43NoFiltersNoVtx_v4',
        'HLT_DoubleMu48NoFiltersNoVtx_v4',
        'HLT_DoubleMu4_Mass3p8_DZ_PFHT350_v8',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v5',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v5',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v15',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v14',
        'HLT_Mu17_TrkIsoVVL_v13',
        'HLT_Mu17_v13',
        'HLT_Mu18_Mu9_DZ_v4',
        'HLT_Mu18_Mu9_SameSign_DZ_v4',
        'HLT_Mu18_Mu9_SameSign_v4',
        'HLT_Mu18_Mu9_v4',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass3p8_v3',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass8_v3',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_v3',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_v3',
        'HLT_Mu19_TrkIsoVVL_v4',
        'HLT_Mu19_v4',
        'HLT_Mu20_Mu10_DZ_v4',
        'HLT_Mu20_Mu10_SameSign_DZ_v4',
        'HLT_Mu20_Mu10_SameSign_v4',
        'HLT_Mu20_Mu10_v4',
        'HLT_Mu23_Mu12_DZ_v4',
        'HLT_Mu23_Mu12_SameSign_DZ_v4',
        'HLT_Mu23_Mu12_SameSign_v4',
        'HLT_Mu23_Mu12_v4',
        'HLT_Mu37_TkMu27_v5',
        'HLT_Mu8_TrkIsoVVL_v12',
        'HLT_Mu8_v12',
        'HLT_TripleMu_10_5_5_DZ_v10',
        'HLT_TripleMu_12_10_5_v10',
        'HLT_TripleMu_5_3_3_Mass3p8_DCA_v3',
        'HLT_TripleMu_5_3_3_Mass3p8_DZ_v8',
        'HLT_TrkMu12_DoubleTrkMu5NoFiltersNoVtx_v6',
        'HLT_TrkMu16_DoubleTrkMu6NoFiltersNoVtx_v12',
        'HLT_TrkMu17_DoubleTrkMu8NoFiltersNoVtx_v13'
    ),
    DoubleMuonLowMass = cms.vstring(
        'HLT_Dimuon0_LowMass_L1_TM530_v6',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v4',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v6',
        'HLT_DoubleMu3_Trk_Tau3mu_v12',
        'HLT_DoubleMu4_LowMassNonResonantTrk_Displaced_v15',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v4',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v4',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v4',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v4'
    ),
    EGamma = cms.vstring(
        'HLT_DiEle27_WPTightCaloOnly_L1DoubleEG_v4',
        'HLT_DiSC30_18_EIso_AND_HE_Mass70_v13',
        'HLT_Diphoton30PV_18PV_R9Id_AND_IsoCaloId_AND_HE_R9Id_NoPixelVeto_Mass55_v13',
        'HLT_Diphoton30PV_18PV_R9Id_AND_IsoCaloId_AND_HE_R9Id_PixelVeto_Mass55_v15',
        'HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_NoPixelVeto_Mass55_v2',
        'HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_NoPixelVeto_v2',
        'HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90_v13',
        'HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass95_v13',
        'HLT_DoubleEle25_CaloIdL_MW_v4',
        'HLT_DoubleEle27_CaloIdL_MW_v4',
        'HLT_DoubleEle33_CaloIdL_MW_v17',
        'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_DZ_PFHT350_v20',
        'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT350_v20',
        'HLT_DoublePhoton33_CaloIdL_v6',
        'HLT_DoublePhoton70_v6',
        'HLT_DoublePhoton85_v14',
        'HLT_ECALHT800_v10',
        'HLT_Ele115_CaloIdVT_GsfTrkIdT_v14',
        'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30_v18',
        'HLT_Ele135_CaloIdVT_GsfTrkIdT_v7',
        'HLT_Ele145_CaloIdVT_GsfTrkIdT_v8',
        'HLT_Ele15_CaloIdL_TrackIdL_IsoVL_PFJet30_v3',
        'HLT_Ele15_Ele8_CaloIdL_TrackIdL_IsoVL_v3',
        'HLT_Ele15_IsoVVVL_PFHT450_CaloBTagDeepCSV_4p5_v8',
        'HLT_Ele15_IsoVVVL_PFHT450_PFMET50_v16',
        'HLT_Ele15_IsoVVVL_PFHT450_v16',
        'HLT_Ele15_IsoVVVL_PFHT600_v20',
        'HLT_Ele15_WPLoose_Gsf_v3',
        'HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v9',
        'HLT_Ele17_CaloIdM_TrackIdM_PFJet30_v16',
        'HLT_Ele17_WPLoose_Gsf_v3',
        'HLT_Ele200_CaloIdVT_GsfTrkIdT_v8',
        'HLT_Ele20_WPLoose_Gsf_v6',
        'HLT_Ele20_WPTight_Gsf_v6',
        'HLT_Ele20_eta2p1_WPLoose_Gsf_v6',
        'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30_v18',
        'HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v18',
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v19',
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v19',
        'HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1_v13',
        'HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTauHPS30_eta2p1_CrossL1_v1',
        'HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTauHPS30_eta2p1_TightID_CrossL1_v1',
        'HLT_Ele24_eta2p1_WPTight_Gsf_MediumChargedIsoPFTauHPS30_eta2p1_CrossL1_v1',
        'HLT_Ele24_eta2p1_WPTight_Gsf_MediumChargedIsoPFTauHPS30_eta2p1_TightID_CrossL1_v1',
        'HLT_Ele24_eta2p1_WPTight_Gsf_TightChargedIsoPFTauHPS30_eta2p1_CrossL1_v1',
        'HLT_Ele24_eta2p1_WPTight_Gsf_TightChargedIsoPFTauHPS30_eta2p1_TightID_CrossL1_v1',
        'HLT_Ele250_CaloIdVT_GsfTrkIdT_v13',
        'HLT_Ele27_Ele37_CaloIdL_MW_v4',
        'HLT_Ele27_WPTight_Gsf_v16',
        'HLT_Ele28_HighEta_SC20_Mass55_v13',
        'HLT_Ele28_WPTight_Gsf_v1',
        'HLT_Ele28_eta2p1_WPTight_Gsf_HT150_v13',
        'HLT_Ele300_CaloIdVT_GsfTrkIdT_v13',
        'HLT_Ele30_WPTight_Gsf_v1',
        'HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned_v13',
        'HLT_Ele32_WPTight_Gsf_L1DoubleEG_v9',
        'HLT_Ele32_WPTight_Gsf_v15',
        'HLT_Ele35_WPTight_Gsf_L1EGMT_v5',
        'HLT_Ele35_WPTight_Gsf_v9',
        'HLT_Ele38_WPTight_Gsf_v9',
        'HLT_Ele40_WPTight_Gsf_v9',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v18',
        'HLT_Ele50_IsoVVVL_PFHT450_v16',
        'HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30_v16',
        'HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v18',
        'HLT_Photon100EBHE10_v2',
        'HLT_Photon100EB_TightID_TightIso_v2',
        'HLT_Photon100EEHE10_v2',
        'HLT_Photon100EE_TightID_TightIso_v2',
        'HLT_Photon110EB_TightID_TightIso_v2',
        'HLT_Photon120EB_TightID_TightIso_v2',
        'HLT_Photon120_R9Id90_HE10_IsoM_v14',
        'HLT_Photon120_v13',
        'HLT_Photon150_v6',
        'HLT_Photon165_R9Id90_HE10_IsoM_v15',
        'HLT_Photon175_v14',
        'HLT_Photon200_v13',
        'HLT_Photon20_HoverELoose_v10',
        'HLT_Photon20_v2',
        'HLT_Photon300_NoHE_v12',
        'HLT_Photon30_HoverELoose_v10',
        'HLT_Photon33_v5',
        'HLT_Photon50_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3_PFMET50_v5',
        'HLT_Photon50_R9Id90_HE10_IsoM_v14',
        'HLT_Photon50_v13',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT350MinPFJet15_v11',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_v5',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_v5',
        'HLT_Photon75_R9Id90_HE10_IsoM_EBOnly_CaloMJJ300_PFJetsMJJ400DEta3_v5',
        'HLT_Photon75_R9Id90_HE10_IsoM_EBOnly_CaloMJJ400_PFJetsMJJ600DEta3_v5',
        'HLT_Photon75_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3_v5',
        'HLT_Photon75_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ600DEta3_v5',
        'HLT_Photon75_R9Id90_HE10_IsoM_v14',
        'HLT_Photon75_v13',
        'HLT_Photon90_CaloIdL_PFHT700_v16',
        'HLT_Photon90_R9Id90_HE10_IsoM_v14',
        'HLT_Photon90_v13',
        'HLT_TriplePhoton_20_20_20_CaloIdLV2_R9IdVL_v3',
        'HLT_TriplePhoton_20_20_20_CaloIdLV2_v3',
        'HLT_TriplePhoton_30_30_10_CaloIdLV2_R9IdVL_v4',
        'HLT_TriplePhoton_30_30_10_CaloIdLV2_v4',
        'HLT_TriplePhoton_35_35_5_CaloIdLV2_R9IdVL_v4'
    ),
    EcalLaser = cms.vstring('HLT_EcalCalibration_v4'),
    EmptyBX = cms.vstring(
        'HLT_L1NotBptxOR_v3',
        'HLT_L1UnpairedBunchBptxMinus_v2',
        'HLT_L1UnpairedBunchBptxPlus_v2'
    ),
    EphemeralHLTPhysics1 = cms.vstring('HLT_Physics_part0_v7'),
    EphemeralHLTPhysics2 = cms.vstring('HLT_Physics_part1_v7'),
    EphemeralHLTPhysics3 = cms.vstring('HLT_Physics_part2_v7'),
    EphemeralHLTPhysics4 = cms.vstring('HLT_Physics_part3_v7'),
    EphemeralHLTPhysics5 = cms.vstring('HLT_Physics_part4_v7'),
    EphemeralHLTPhysics6 = cms.vstring('HLT_Physics_part5_v7'),
    EphemeralHLTPhysics7 = cms.vstring('HLT_Physics_part6_v7'),
    EphemeralHLTPhysics8 = cms.vstring('HLT_Physics_part7_v7'),
    EphemeralZeroBias1 = cms.vstring('HLT_ZeroBias_part0_v6'),
    EphemeralZeroBias2 = cms.vstring('HLT_ZeroBias_part1_v6'),
    EphemeralZeroBias3 = cms.vstring('HLT_ZeroBias_part2_v6'),
    EphemeralZeroBias4 = cms.vstring('HLT_ZeroBias_part3_v6'),
    EphemeralZeroBias5 = cms.vstring('HLT_ZeroBias_part4_v6'),
    EphemeralZeroBias6 = cms.vstring('HLT_ZeroBias_part5_v6'),
    EphemeralZeroBias7 = cms.vstring('HLT_ZeroBias_part6_v6'),
    EphemeralZeroBias8 = cms.vstring('HLT_ZeroBias_part7_v6'),
    EventDisplay = cms.vstring(
        'HLT_AK4PFJet100_v19',
        'HLT_DoublePhoton85_v14',
        'HLT_PFJet500_v21'
    ),
    ExpressAlignment = cms.vstring(
        'HLT_HT300_Beamspot_v11',
        'HLT_HT450_Beamspot_v11',
        'HLT_ZeroBias_Beamspot_v4'
    ),
    ExpressPhysics = cms.vstring(
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v19',
        'HLT_IsoMu20_v15',
        'HLT_IsoMu24_v13',
        'HLT_IsoMu27_v16',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v15',
        'HLT_Physics_v7',
        'HLT_Random_v3',
        'HLT_ZeroBias_Alignment_v1',
        'HLT_ZeroBias_FirstCollisionAfterAbortGap_v5',
        'HLT_ZeroBias_IsolatedBunches_v5',
        'HLT_ZeroBias_v6'
    ),
    FSQJet1 = cms.vstring(
        'HLT_DiPFJet15_NoCaloMatched_v16',
        'HLT_DiPFJet25_NoCaloMatched_v16'
    ),
    FSQJet2 = cms.vstring(
        'HLT_DiPFJet15_FBEta3_NoCaloMatched_v17',
        'HLT_DiPFJet25_FBEta3_NoCaloMatched_v17',
        'HLT_DiPFJetAve15_HFJEC_v17',
        'HLT_DiPFJetAve25_HFJEC_v17',
        'HLT_DiPFJetAve35_HFJEC_v17'
    ),
    HINCaloJets = cms.vstring(
        'HLT_AK4CaloJet100_v10',
        'HLT_AK4CaloJet120_v9',
        'HLT_AK4CaloJet30_v11',
        'HLT_AK4CaloJet40_v10',
        'HLT_AK4CaloJet50_v10',
        'HLT_AK4CaloJet80_v10'
    ),
    HINPFJets = cms.vstring(
        'HLT_AK4PFJet100_v19',
        'HLT_AK4PFJet120_v18',
        'HLT_AK4PFJet30_v19',
        'HLT_AK4PFJet50_v19',
        'HLT_AK4PFJet80_v19'
    ),
    HLTMonitor = cms.vstring(
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v19',
        'HLT_Ele32_WPTight_Gsf_v15',
        'HLT_HT400_DisplacedDijet40_DisplacedTrack_v13',
        'HLT_HT550_DisplacedDijet60_Inclusive_v13',
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v15',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_CaloDiJet30_CaloBtagDeepCSV_1p5_v1',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PFBtagDeepCSV_1p5_v1',
        'HLT_PFHT400_SixPFJet32_DoublePFBTagDeepCSV_2p94_v8',
        'HLT_PFHT510_v17',
        'HLT_PFJet260_v20',
        'HLT_PFJet320_v20',
        'HLT_PFMET130_PFMHT130_IDTight_v20',
        'HLT_PFMET140_PFMHT140_IDTight_v20'
    ),
    HLTPhysics = cms.vstring('HLT_Physics_v7'),
    HcalNZS = cms.vstring(
        'HLT_HcalNZS_v13',
        'HLT_HcalPhiSym_v15'
    ),
    HighPtLowerPhotons = cms.vstring(
        'HLT_SinglePhoton10_Eta3p1ForPPRef_v8',
        'HLT_SinglePhoton20_Eta3p1ForPPRef_v9'
    ),
    HighPtPhoton30AndZ = cms.vstring('HLT_SinglePhoton30_Eta3p1ForPPRef_v9'),
    IsolatedBunch = cms.vstring('HLT_HcalIsolatedbunch_v5'),
    JetHT = cms.vstring(
        'HLT_AK8PFHT750_TrimMass50_v12',
        'HLT_AK8PFHT800_TrimMass50_v12',
        'HLT_AK8PFHT850_TrimMass50_v11',
        'HLT_AK8PFHT900_TrimMass50_v11',
        'HLT_AK8PFJet140_v15',
        'HLT_AK8PFJet15_v3',
        'HLT_AK8PFJet200_v15',
        'HLT_AK8PFJet25_v3',
        'HLT_AK8PFJet260_v16',
        'HLT_AK8PFJet320_v16',
        'HLT_AK8PFJet330_TrimMass30_PFAK8BTagDeepCSV_p17_v2',
        'HLT_AK8PFJet330_TrimMass30_PFAK8BTagDeepCSV_p1_v2',
        'HLT_AK8PFJet330_TrimMass30_PFAK8BoostedDoubleB_np2_v2',
        'HLT_AK8PFJet330_TrimMass30_PFAK8BoostedDoubleB_np4_v2',
        'HLT_AK8PFJet330_TrimMass30_PFAK8BoostedDoubleB_p02_v3',
        'HLT_AK8PFJet360_TrimMass30_v18',
        'HLT_AK8PFJet380_TrimMass30_v11',
        'HLT_AK8PFJet400_TrimMass30_v12',
        'HLT_AK8PFJet400_v16',
        'HLT_AK8PFJet40_v16',
        'HLT_AK8PFJet420_TrimMass30_v11',
        'HLT_AK8PFJet450_v16',
        'HLT_AK8PFJet500_v16',
        'HLT_AK8PFJet550_v11',
        'HLT_AK8PFJet60_v15',
        'HLT_AK8PFJet80_v15',
        'HLT_AK8PFJetFwd140_v14',
        'HLT_AK8PFJetFwd15_v3',
        'HLT_AK8PFJetFwd200_v14',
        'HLT_AK8PFJetFwd25_v3',
        'HLT_AK8PFJetFwd260_v15',
        'HLT_AK8PFJetFwd320_v15',
        'HLT_AK8PFJetFwd400_v15',
        'HLT_AK8PFJetFwd40_v15',
        'HLT_AK8PFJetFwd450_v15',
        'HLT_AK8PFJetFwd500_v15',
        'HLT_AK8PFJetFwd60_v14',
        'HLT_AK8PFJetFwd80_v14',
        'HLT_CaloJet500_NoJetID_v12',
        'HLT_CaloJet550_NoJetID_v7',
        'HLT_DiPFJetAve100_HFJEC_v16',
        'HLT_DiPFJetAve140_v13',
        'HLT_DiPFJetAve160_HFJEC_v16',
        'HLT_DiPFJetAve200_v13',
        'HLT_DiPFJetAve220_HFJEC_v16',
        'HLT_DiPFJetAve260_v14',
        'HLT_DiPFJetAve300_HFJEC_v16',
        'HLT_DiPFJetAve320_v14',
        'HLT_DiPFJetAve400_v14',
        'HLT_DiPFJetAve40_v14',
        'HLT_DiPFJetAve500_v14',
        'HLT_DiPFJetAve60_HFJEC_v15',
        'HLT_DiPFJetAve60_v14',
        'HLT_DiPFJetAve80_HFJEC_v16',
        'HLT_DiPFJetAve80_v13',
        'HLT_DoublePFJets100_CaloBTagDeepCSV_p71_v2',
        'HLT_DoublePFJets116MaxDeta1p6_DoubleCaloBTagDeepCSV_p71_v2',
        'HLT_DoublePFJets128MaxDeta1p6_DoubleCaloBTagDeepCSV_p71_v2',
        'HLT_DoublePFJets200_CaloBTagDeepCSV_p71_v2',
        'HLT_DoublePFJets350_CaloBTagDeepCSV_p71_v2',
        'HLT_DoublePFJets40_CaloBTagDeepCSV_p71_v2',
        'HLT_Mu12_DoublePFJets100_CaloBTagDeepCSV_p71_v2',
        'HLT_Mu12_DoublePFJets200_CaloBTagDeepCSV_p71_v2',
        'HLT_Mu12_DoublePFJets350_CaloBTagDeepCSV_p71_v2',
        'HLT_Mu12_DoublePFJets40MaxDeta1p6_DoubleCaloBTagDeepCSV_p71_v2',
        'HLT_Mu12_DoublePFJets40_CaloBTagDeepCSV_p71_v2',
        'HLT_Mu12_DoublePFJets54MaxDeta1p6_DoubleCaloBTagDeepCSV_p71_v2',
        'HLT_Mu12_DoublePFJets62MaxDeta1p6_DoubleCaloBTagDeepCSV_p71_v2',
        'HLT_PFHT1050_v18',
        'HLT_PFHT180_v17',
        'HLT_PFHT250_v17',
        'HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_4p5_v3',
        'HLT_PFHT330PT30_QuadPFJet_75_60_45_40_v9',
        'HLT_PFHT350MinPFJet15_v9',
        'HLT_PFHT350_v19',
        'HLT_PFHT370_v17',
        'HLT_PFHT400_FivePFJet_100_100_60_30_30_DoublePFBTagDeepCSV_4p5_v8',
        'HLT_PFHT400_FivePFJet_100_100_60_30_30_v8',
        'HLT_PFHT400_FivePFJet_120_120_60_30_30_DoublePFBTagDeepCSV_4p5_v8',
        'HLT_PFHT400_SixPFJet32_DoublePFBTagDeepCSV_2p94_v8',
        'HLT_PFHT400_SixPFJet32_v8',
        'HLT_PFHT430_v17',
        'HLT_PFHT450_SixPFJet36_PFBTagDeepCSV_1p59_v7',
        'HLT_PFHT450_SixPFJet36_v7',
        'HLT_PFHT500_PFMET100_PFMHT100_IDTight_v12',
        'HLT_PFHT500_PFMET110_PFMHT110_IDTight_v12',
        'HLT_PFHT510_v17',
        'HLT_PFHT590_v17',
        'HLT_PFHT680_v17',
        'HLT_PFHT700_PFMET85_PFMHT85_IDTight_v12',
        'HLT_PFHT700_PFMET95_PFMHT95_IDTight_v12',
        'HLT_PFHT780_v17',
        'HLT_PFHT800_PFMET75_PFMHT75_IDTight_v12',
        'HLT_PFHT800_PFMET85_PFMHT85_IDTight_v12',
        'HLT_PFHT890_v17',
        'HLT_PFJet140_v19',
        'HLT_PFJet15_v3',
        'HLT_PFJet200_v19',
        'HLT_PFJet25_v3',
        'HLT_PFJet260_v20',
        'HLT_PFJet320_v20',
        'HLT_PFJet400_v20',
        'HLT_PFJet40_v21',
        'HLT_PFJet450_v21',
        'HLT_PFJet500_v21',
        'HLT_PFJet550_v11',
        'HLT_PFJet60_v21',
        'HLT_PFJet80_v20',
        'HLT_PFJetFwd140_v18',
        'HLT_PFJetFwd15_v3',
        'HLT_PFJetFwd200_v18',
        'HLT_PFJetFwd25_v3',
        'HLT_PFJetFwd260_v19',
        'HLT_PFJetFwd320_v19',
        'HLT_PFJetFwd400_v19',
        'HLT_PFJetFwd40_v19',
        'HLT_PFJetFwd450_v19',
        'HLT_PFJetFwd500_v19',
        'HLT_PFJetFwd60_v19',
        'HLT_PFJetFwd80_v18',
        'HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1_v8',
        'HLT_QuadPFJet103_88_75_15_PFBTagDeepCSV_1p3_VBF2_v8',
        'HLT_QuadPFJet103_88_75_15_v5',
        'HLT_QuadPFJet105_88_76_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1_v8',
        'HLT_QuadPFJet105_88_76_15_PFBTagDeepCSV_1p3_VBF2_v8',
        'HLT_QuadPFJet105_88_76_15_v5',
        'HLT_QuadPFJet111_90_80_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1_v8',
        'HLT_QuadPFJet111_90_80_15_PFBTagDeepCSV_1p3_VBF2_v8',
        'HLT_QuadPFJet111_90_80_15_v5',
        'HLT_QuadPFJet98_83_71_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1_v8',
        'HLT_QuadPFJet98_83_71_15_PFBTagDeepCSV_1p3_VBF2_v8',
        'HLT_QuadPFJet98_83_71_15_v5',
        'HLT_Rsq0p35_v15',
        'HLT_Rsq0p40_v15',
        'HLT_RsqMR300_Rsq0p09_MR200_4jet_v15',
        'HLT_RsqMR300_Rsq0p09_MR200_v15',
        'HLT_RsqMR320_Rsq0p09_MR200_4jet_v15',
        'HLT_RsqMR320_Rsq0p09_MR200_v15',
        'HLT_SingleJet30_Mu12_SinglePFJet40_v11'
    ),
    L1Accept = cms.vstring(
        'DST_Physics_v7',
        'DST_ZeroBias_v2'
    ),
    MET = cms.vstring(
        'HLT_CaloMET100_NotCleaned_v4',
        'HLT_CaloMET110_NotCleaned_v4',
        'HLT_CaloMET250_NotCleaned_v4',
        'HLT_CaloMET300_NotCleaned_v4',
        'HLT_CaloMET350_NotCleaned_v4',
        'HLT_CaloMET80_NotCleaned_v4',
        'HLT_CaloMET90_NotCleaned_v4',
        'HLT_CaloMHT90_v4',
        'HLT_DiJet110_35_Mjj650_PFMET110_v9',
        'HLT_DiJet110_35_Mjj650_PFMET120_v9',
        'HLT_DiJet110_35_Mjj650_PFMET130_v9',
        'HLT_L1ETMHadSeeds_v2',
        'HLT_MET105_IsoTrk50_v9',
        'HLT_MET120_IsoTrk50_v9',
        'HLT_MonoCentralPFJet80_PFMETNoMu110_PFMHTNoMu110_IDTight_v20',
        'HLT_MonoCentralPFJet80_PFMETNoMu120_PFMHTNoMu120_IDTight_v20',
        'HLT_MonoCentralPFJet80_PFMETNoMu130_PFMHTNoMu130_IDTight_v19',
        'HLT_MonoCentralPFJet80_PFMETNoMu140_PFMHTNoMu140_IDTight_v19',
        'HLT_PFMET100_PFMHT100_IDTight_CaloBTagDeepCSV_3p1_v8',
        'HLT_PFMET100_PFMHT100_IDTight_PFHT60_v9',
        'HLT_PFMET110_PFMHT110_IDTight_CaloBTagDeepCSV_3p1_v8',
        'HLT_PFMET110_PFMHT110_IDTight_v20',
        'HLT_PFMET120_PFMHT120_IDTight_CaloBTagDeepCSV_3p1_v8',
        'HLT_PFMET120_PFMHT120_IDTight_PFHT60_v9',
        'HLT_PFMET120_PFMHT120_IDTight_v20',
        'HLT_PFMET130_PFMHT130_IDTight_CaloBTagDeepCSV_3p1_v8',
        'HLT_PFMET130_PFMHT130_IDTight_v20',
        'HLT_PFMET140_PFMHT140_IDTight_CaloBTagDeepCSV_3p1_v8',
        'HLT_PFMET140_PFMHT140_IDTight_v20',
        'HLT_PFMET200_BeamHaloCleaned_v9',
        'HLT_PFMET200_NotCleaned_v9',
        'HLT_PFMET250_NotCleaned_v9',
        'HLT_PFMET300_NotCleaned_v9',
        'HLT_PFMETNoMu100_PFMHTNoMu100_IDTight_PFHT60_v9',
        'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_v20',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v9',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v20',
        'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v19',
        'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v19',
        'HLT_PFMETTypeOne100_PFMHT100_IDTight_PFHT60_v9',
        'HLT_PFMETTypeOne110_PFMHT110_IDTight_v12',
        'HLT_PFMETTypeOne120_PFMHT120_IDTight_PFHT60_v9',
        'HLT_PFMETTypeOne120_PFMHT120_IDTight_v12',
        'HLT_PFMETTypeOne130_PFMHT130_IDTight_v12',
        'HLT_PFMETTypeOne140_PFMHT140_IDTight_v11',
        'HLT_PFMETTypeOne200_BeamHaloCleaned_v9',
        'HLT_TripleJet110_35_35_Mjj650_PFMET110_v9',
        'HLT_TripleJet110_35_35_Mjj650_PFMET120_v9',
        'HLT_TripleJet110_35_35_Mjj650_PFMET130_v9'
    ),
    MonteCarlo = cms.vstring(
        'MC_AK4CaloJetsFromPV_v8',
        'MC_AK4CaloJets_v9',
        'MC_AK4PFJets_v17',
        'MC_AK8CaloHT_v8',
        'MC_AK8PFHT_v16',
        'MC_AK8PFJets_v17',
        'MC_AK8TrimPFJets_v17',
        'MC_CaloBTagDeepCSV_v8',
        'MC_CaloHT_v8',
        'MC_CaloMET_JetIdCleaned_v9',
        'MC_CaloMET_v8',
        'MC_CaloMHT_v8',
        'MC_Diphoton10_10_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass10_v13',
        'MC_DoubleEle5_CaloIdL_MW_v15',
        'MC_DoubleMuNoFiltersNoVtx_v7',
        'MC_DoubleMu_TrkIsoVVL_DZ_v11',
        'MC_Ele15_Ele10_CaloIdL_TrackIdL_IsoVL_DZ_v15',
        'MC_Ele5_WPTight_Gsf_v8',
        'MC_IsoMu_v15',
        'MC_PFBTagDeepCSV_v10',
        'MC_PFHT_v16',
        'MC_PFMET_v17',
        'MC_PFMHT_v16',
        'MC_ReducedIterativeTracking_v12'
    ),
    MuOnia = cms.vstring(
        'HLT_Dimuon0_Upsilon_L1_4p5NoOS_v8',
        'HLT_Dimuon0_Upsilon_L1_4p5_v9',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v7',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v9',
        'HLT_Dimuon0_Upsilon_L1_5M_v8',
        'HLT_Dimuon0_Upsilon_L1_5_v9',
        'HLT_Dimuon0_Upsilon_Muon_L1_TM0_v6',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v6',
        'HLT_Dimuon0_Upsilon_NoVertexing_v7',
        'HLT_Dimuon12_Upsilon_y1p4_v2',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v7',
        'HLT_Dimuon24_Phi_noCorrL1_v6',
        'HLT_Dimuon24_Upsilon_noCorrL1_v6',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v4',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v4',
        'HLT_Mu20_TkMu0_Phi_v8',
        'HLT_Mu25_TkMu0_Onia_v8',
        'HLT_Mu25_TkMu0_Phi_v8',
        'HLT_Mu30_TkMu0_Upsilon_v1',
        'HLT_Mu7p5_L2Mu2_Upsilon_v10',
        'HLT_Mu7p5_Track2_Upsilon_v11',
        'HLT_Mu7p5_Track3p5_Upsilon_v11',
        'HLT_Mu7p5_Track7_Upsilon_v11',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v5',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v3'
    ),
    MuonEG = cms.vstring(
        'HLT_DiMu4_Ele9_CaloIdL_TrackIdL_DZ_Mass3p8_v17',
        'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_DZ_v17',
        'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v17',
        'HLT_DoubleMu20_7_Mass0to30_L1_DM4EG_v8',
        'HLT_DoubleMu20_7_Mass0to30_L1_DM4_v7',
        'HLT_DoubleMu20_7_Mass0to30_Photon23_v8',
        'HLT_Mu12_DoublePhoton20_v5',
        'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v15',
        'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v7',
        'HLT_Mu17_Photon30_IsoCaloId_v6',
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v15',
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v7',
        'HLT_Mu27_Ele37_CaloIdL_MW_v5',
        'HLT_Mu37_Ele27_CaloIdL_MW_v5',
        'HLT_Mu38NoFiltersNoVtxDisplaced_Photon38_CaloIdL_v1',
        'HLT_Mu43NoFiltersNoVtxDisplaced_Photon43_CaloIdL_v1',
        'HLT_Mu43NoFiltersNoVtx_Photon43_CaloIdL_v5',
        'HLT_Mu48NoFiltersNoVtx_Photon48_CaloIdL_v5',
        'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_DZ_v18',
        'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v18',
        'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350_DZ_v19',
        'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350_v19',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_CaloDiJet30_CaloBtagDeepCSV_1p5_v1',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_CaloDiJet30_v1',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PFBtagDeepCSV_1p5_v1',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_v1',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v13',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v11'
    ),
    NoBPTX = cms.vstring(
        'HLT_CDC_L2cosmic_10_er1p0_v1',
        'HLT_CDC_L2cosmic_5p5_er1p0_v1',
        'HLT_L2Mu10_NoVertex_NoBPTX3BX_v5',
        'HLT_L2Mu10_NoVertex_NoBPTX_v6',
        'HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_v5',
        'HLT_L2Mu45_NoVertex_3Sta_NoBPTX3BX_v4',
        'HLT_UncorrectedJetE30_NoBPTX3BX_v6',
        'HLT_UncorrectedJetE30_NoBPTX_v6',
        'HLT_UncorrectedJetE60_NoBPTX3BX_v6',
        'HLT_UncorrectedJetE70_NoBPTX3BX_v6'
    ),
    OnlineMonitor = cms.vstring( (
        'HLT_AK4CaloJet100_v10',
        'HLT_AK4CaloJet120_v9',
        'HLT_AK4CaloJet30_v11',
        'HLT_AK4CaloJet40_v10',
        'HLT_AK4CaloJet50_v10',
        'HLT_AK4CaloJet80_v10',
        'HLT_AK4PFJet100_v19',
        'HLT_AK4PFJet120_v18',
        'HLT_AK4PFJet30_v19',
        'HLT_AK4PFJet50_v19',
        'HLT_AK4PFJet80_v19',
        'HLT_AK8PFHT750_TrimMass50_v12',
        'HLT_AK8PFHT800_TrimMass50_v12',
        'HLT_AK8PFHT850_TrimMass50_v11',
        'HLT_AK8PFHT900_TrimMass50_v11',
        'HLT_AK8PFJet140_v15',
        'HLT_AK8PFJet15_v3',
        'HLT_AK8PFJet200_v15',
        'HLT_AK8PFJet25_v3',
        'HLT_AK8PFJet260_v16',
        'HLT_AK8PFJet320_v16',
        'HLT_AK8PFJet330_TrimMass30_PFAK8BTagDeepCSV_p17_v2',
        'HLT_AK8PFJet330_TrimMass30_PFAK8BTagDeepCSV_p1_v2',
        'HLT_AK8PFJet330_TrimMass30_PFAK8BoostedDoubleB_np2_v2',
        'HLT_AK8PFJet330_TrimMass30_PFAK8BoostedDoubleB_np4_v2',
        'HLT_AK8PFJet330_TrimMass30_PFAK8BoostedDoubleB_p02_v3',
        'HLT_AK8PFJet360_TrimMass30_v18',
        'HLT_AK8PFJet380_TrimMass30_v11',
        'HLT_AK8PFJet400_TrimMass30_v12',
        'HLT_AK8PFJet400_v16',
        'HLT_AK8PFJet40_v16',
        'HLT_AK8PFJet420_TrimMass30_v11',
        'HLT_AK8PFJet450_v16',
        'HLT_AK8PFJet500_v16',
        'HLT_AK8PFJet550_v11',
        'HLT_AK8PFJet60_v15',
        'HLT_AK8PFJet80_v15',
        'HLT_AK8PFJetFwd140_v14',
        'HLT_AK8PFJetFwd15_v3',
        'HLT_AK8PFJetFwd200_v14',
        'HLT_AK8PFJetFwd25_v3',
        'HLT_AK8PFJetFwd260_v15',
        'HLT_AK8PFJetFwd320_v15',
        'HLT_AK8PFJetFwd400_v15',
        'HLT_AK8PFJetFwd40_v15',
        'HLT_AK8PFJetFwd450_v15',
        'HLT_AK8PFJetFwd500_v15',
        'HLT_AK8PFJetFwd60_v14',
        'HLT_AK8PFJetFwd80_v14',
        'HLT_BTagMu_AK4DiJet110_Mu5_noalgo_v13',
        'HLT_BTagMu_AK4DiJet110_Mu5_v13',
        'HLT_BTagMu_AK4DiJet170_Mu5_noalgo_v12',
        'HLT_BTagMu_AK4DiJet170_Mu5_v12',
        'HLT_BTagMu_AK4DiJet20_Mu5_noalgo_v13',
        'HLT_BTagMu_AK4DiJet20_Mu5_v13',
        'HLT_BTagMu_AK4DiJet40_Mu5_noalgo_v13',
        'HLT_BTagMu_AK4DiJet40_Mu5_v13',
        'HLT_BTagMu_AK4DiJet70_Mu5_noalgo_v13',
        'HLT_BTagMu_AK4DiJet70_Mu5_v13',
        'HLT_BTagMu_AK4Jet300_Mu5_noalgo_v12',
        'HLT_BTagMu_AK4Jet300_Mu5_v12',
        'HLT_BTagMu_AK8DiJet170_Mu5_noalgo_v9',
        'HLT_BTagMu_AK8DiJet170_Mu5_v9',
        'HLT_BTagMu_AK8Jet170_DoubleMu5_noalgo_v2',
        'HLT_BTagMu_AK8Jet170_DoubleMu5_v2',
        'HLT_BTagMu_AK8Jet300_Mu5_noalgo_v12',
        'HLT_BTagMu_AK8Jet300_Mu5_v12',
        'HLT_CDC_L2cosmic_10_er1p0_v1',
        'HLT_CDC_L2cosmic_5p5_er1p0_v1',
        'HLT_CaloJet500_NoJetID_v12',
        'HLT_CaloJet550_NoJetID_v7',
        'HLT_CaloMET100_NotCleaned_v4',
        'HLT_CaloMET110_NotCleaned_v4',
        'HLT_CaloMET250_NotCleaned_v4',
        'HLT_CaloMET300_NotCleaned_v4',
        'HLT_CaloMET350_NotCleaned_v4',
        'HLT_CaloMET80_NotCleaned_v4',
        'HLT_CaloMET90_NotCleaned_v4',
        'HLT_CaloMHT90_v4',
        'HLT_DiEle27_WPTightCaloOnly_L1DoubleEG_v4',
        'HLT_DiJet110_35_Mjj650_PFMET110_v9',
        'HLT_DiJet110_35_Mjj650_PFMET120_v9',
        'HLT_DiJet110_35_Mjj650_PFMET130_v9',
        'HLT_DiMu4_Ele9_CaloIdL_TrackIdL_DZ_Mass3p8_v17',
        'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_DZ_v17',
        'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v17',
        'HLT_DiPFJet15_FBEta3_NoCaloMatched_v17',
        'HLT_DiPFJet15_NoCaloMatched_v16',
        'HLT_DiPFJet25_FBEta3_NoCaloMatched_v17',
        'HLT_DiPFJet25_NoCaloMatched_v16',
        'HLT_DiPFJetAve100_HFJEC_v16',
        'HLT_DiPFJetAve140_v13',
        'HLT_DiPFJetAve15_HFJEC_v17',
        'HLT_DiPFJetAve160_HFJEC_v16',
        'HLT_DiPFJetAve200_v13',
        'HLT_DiPFJetAve220_HFJEC_v16',
        'HLT_DiPFJetAve25_HFJEC_v17',
        'HLT_DiPFJetAve260_v14',
        'HLT_DiPFJetAve300_HFJEC_v16',
        'HLT_DiPFJetAve320_v14',
        'HLT_DiPFJetAve35_HFJEC_v17',
        'HLT_DiPFJetAve400_v14',
        'HLT_DiPFJetAve40_v14',
        'HLT_DiPFJetAve500_v14',
        'HLT_DiPFJetAve60_HFJEC_v15',
        'HLT_DiPFJetAve60_v14',
        'HLT_DiPFJetAve80_HFJEC_v16',
        'HLT_DiPFJetAve80_v13',
        'HLT_DiSC30_18_EIso_AND_HE_Mass70_v13',
        'HLT_Dimuon0_Jpsi3p5_Muon2_v5',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v7',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v7',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v7',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v7',
        'HLT_Dimuon0_Jpsi_NoVertexing_v8',
        'HLT_Dimuon0_Jpsi_v8',
        'HLT_Dimuon0_LowMass_L1_0er1p5R_v7',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v8',
        'HLT_Dimuon0_LowMass_L1_4R_v7',
        'HLT_Dimuon0_LowMass_L1_4_v8',
        'HLT_Dimuon0_LowMass_L1_TM530_v6',
        'HLT_Dimuon0_LowMass_v8',
        'HLT_Dimuon0_Upsilon_L1_4p5NoOS_v8',
        'HLT_Dimuon0_Upsilon_L1_4p5_v9',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v7',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v9',
        'HLT_Dimuon0_Upsilon_L1_5M_v8',
        'HLT_Dimuon0_Upsilon_L1_5_v9',
        'HLT_Dimuon0_Upsilon_Muon_L1_TM0_v6',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v6',
        'HLT_Dimuon0_Upsilon_NoVertexing_v7',
        'HLT_Dimuon10_PsiPrime_Barrel_Seagulls_v7',
        'HLT_Dimuon12_Upsilon_y1p4_v2',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v7',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v6',
        'HLT_Dimuon18_PsiPrime_v14',
        'HLT_Dimuon20_Jpsi_Barrel_Seagulls_v7',
        'HLT_Dimuon24_Phi_noCorrL1_v6',
        'HLT_Dimuon24_Upsilon_noCorrL1_v6',
        'HLT_Dimuon25_Jpsi_noCorrL1_v6',
        'HLT_Dimuon25_Jpsi_v14',
        'HLT_Diphoton30PV_18PV_R9Id_AND_IsoCaloId_AND_HE_R9Id_NoPixelVeto_Mass55_v13',
        'HLT_Diphoton30PV_18PV_R9Id_AND_IsoCaloId_AND_HE_R9Id_PixelVeto_Mass55_v15',
        'HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_NoPixelVeto_Mass55_v2',
        'HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_NoPixelVeto_v2',
        'HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90_v13',
        'HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass95_v13',
        'HLT_DoubleEle25_CaloIdL_MW_v4',
        'HLT_DoubleEle27_CaloIdL_MW_v4',
        'HLT_DoubleEle33_CaloIdL_MW_v17',
        'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_DZ_PFHT350_v20',
        'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT350_v20',
        'HLT_DoubleL2Mu23NoVtx_2Cha_CosmicSeed_NoL2Matched_v2',
        'HLT_DoubleL2Mu23NoVtx_2Cha_CosmicSeed_v2',
        'HLT_DoubleL2Mu23NoVtx_2Cha_NoL2Matched_v2',
        'HLT_DoubleL2Mu23NoVtx_2Cha_v2',
        'HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_Eta2p4_v2',
        'HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_NoL2Matched_v2',
        'HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_v2',
        'HLT_DoubleL2Mu25NoVtx_2Cha_Eta2p4_v2',
        'HLT_DoubleL2Mu25NoVtx_2Cha_NoL2Matched_v2',
        'HLT_DoubleL2Mu25NoVtx_2Cha_v2',
        'HLT_DoubleL2Mu30NoVtx_2Cha_CosmicSeed_Eta2p4_v2',
        'HLT_DoubleL2Mu30NoVtx_2Cha_Eta2p4_v2',
        'HLT_DoubleL2Mu50_v2',
        'HLT_DoubleMediumChargedIsoPFTauHPS30_L1MaxMass_Trk1_eta2p1_Reg_v1',
        'HLT_DoubleMediumChargedIsoPFTauHPS35_Trk1_TightID_eta2p1_Reg_v1',
        'HLT_DoubleMediumChargedIsoPFTauHPS35_Trk1_eta2p1_Reg_v4',
        'HLT_DoubleMediumChargedIsoPFTauHPS40_Trk1_TightID_eta2p1_Reg_v1',
        'HLT_DoubleMediumChargedIsoPFTauHPS40_Trk1_eta2p1_Reg_v1',
        'HLT_DoubleMu20_7_Mass0to30_L1_DM4EG_v8',
        'HLT_DoubleMu20_7_Mass0to30_L1_DM4_v7',
        'HLT_DoubleMu20_7_Mass0to30_Photon23_v8',
        'HLT_DoubleMu2_Jpsi_DoubleTkMu0_Phi_v5',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v6',
        'HLT_DoubleMu33NoFiltersNoVtxDisplaced_v1',
        'HLT_DoubleMu3_DCA_PFMET50_PFMHT60_v10',
        'HLT_DoubleMu3_DZ_PFMET50_PFMHT60_v10',
        'HLT_DoubleMu3_DZ_PFMET70_PFMHT70_v10',
        'HLT_DoubleMu3_DZ_PFMET90_PFMHT90_v10',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v4',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v4',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v6',
        'HLT_DoubleMu3_Trk_Tau3mu_v12',
        'HLT_DoubleMu40NoFiltersNoVtxDisplaced_v1',
        'HLT_DoubleMu43NoFiltersNoVtx_v4',
        'HLT_DoubleMu48NoFiltersNoVtx_v4',
        'HLT_DoubleMu4_3_Bs_v14',
        'HLT_DoubleMu4_3_Jpsi_v2',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v7',
        'HLT_DoubleMu4_JpsiTrk_Displaced_v15',
        'HLT_DoubleMu4_Jpsi_Displaced_v7',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v7',
        'HLT_DoubleMu4_LowMassNonResonantTrk_Displaced_v15',
        'HLT_DoubleMu4_Mass3p8_DZ_PFHT350_v8',
        'HLT_DoubleMu4_PsiPrimeTrk_Displaced_v15',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v4',
        'HLT_DoublePFJets100_CaloBTagDeepCSV_p71_v2',
        'HLT_DoublePFJets116MaxDeta1p6_DoubleCaloBTagDeepCSV_p71_v2',
        'HLT_DoublePFJets128MaxDeta1p6_DoubleCaloBTagDeepCSV_p71_v2',
        'HLT_DoublePFJets200_CaloBTagDeepCSV_p71_v2',
        'HLT_DoublePFJets350_CaloBTagDeepCSV_p71_v2',
        'HLT_DoublePFJets40_CaloBTagDeepCSV_p71_v2',
        'HLT_DoublePhoton33_CaloIdL_v6',
        'HLT_DoublePhoton70_v6',
        'HLT_DoublePhoton85_v14',
        'HLT_DoubleTightChargedIsoPFTauHPS35_Trk1_TightID_eta2p1_Reg_v1',
        'HLT_DoubleTightChargedIsoPFTauHPS35_Trk1_eta2p1_Reg_v1',
        'HLT_DoubleTightChargedIsoPFTauHPS40_Trk1_TightID_eta2p1_Reg_v1',
        'HLT_DoubleTightChargedIsoPFTauHPS40_Trk1_eta2p1_Reg_v1',
        'HLT_ECALHT800_v10',
        'HLT_Ele115_CaloIdVT_GsfTrkIdT_v14',
        'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30_v18',
        'HLT_Ele135_CaloIdVT_GsfTrkIdT_v7',
        'HLT_Ele145_CaloIdVT_GsfTrkIdT_v8',
        'HLT_Ele15_CaloIdL_TrackIdL_IsoVL_PFJet30_v3',
        'HLT_Ele15_Ele8_CaloIdL_TrackIdL_IsoVL_v3',
        'HLT_Ele15_IsoVVVL_PFHT450_CaloBTagDeepCSV_4p5_v8',
        'HLT_Ele15_IsoVVVL_PFHT450_PFMET50_v16',
        'HLT_Ele15_IsoVVVL_PFHT450_v16',
        'HLT_Ele15_IsoVVVL_PFHT600_v20',
        'HLT_Ele15_WPLoose_Gsf_v3',
        'HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v9',
        'HLT_Ele17_CaloIdM_TrackIdM_PFJet30_v16',
        'HLT_Ele17_WPLoose_Gsf_v3',
        'HLT_Ele200_CaloIdVT_GsfTrkIdT_v8',
        'HLT_Ele20_WPLoose_Gsf_v6',
        'HLT_Ele20_WPTight_Gsf_v6',
        'HLT_Ele20_eta2p1_WPLoose_Gsf_v6',
        'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30_v18',
        'HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v18',
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v19',
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v19',
        'HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTauHPS30_eta2p1_CrossL1_v1',
        'HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTauHPS30_eta2p1_TightID_CrossL1_v1',
        'HLT_Ele24_eta2p1_WPTight_Gsf_MediumChargedIsoPFTauHPS30_eta2p1_CrossL1_v1',
        'HLT_Ele24_eta2p1_WPTight_Gsf_MediumChargedIsoPFTauHPS30_eta2p1_TightID_CrossL1_v1',
        'HLT_Ele24_eta2p1_WPTight_Gsf_TightChargedIsoPFTauHPS30_eta2p1_CrossL1_v1',
        'HLT_Ele24_eta2p1_WPTight_Gsf_TightChargedIsoPFTauHPS30_eta2p1_TightID_CrossL1_v1',
        'HLT_Ele250_CaloIdVT_GsfTrkIdT_v13',
        'HLT_Ele27_Ele37_CaloIdL_MW_v4',
        'HLT_Ele27_WPTight_Gsf_v16',
        'HLT_Ele28_HighEta_SC20_Mass55_v13',
        'HLT_Ele28_WPTight_Gsf_v1',
        'HLT_Ele28_eta2p1_WPTight_Gsf_HT150_v13',
        'HLT_Ele300_CaloIdVT_GsfTrkIdT_v13',
        'HLT_Ele30_WPTight_Gsf_v1',
        'HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned_v13',
        'HLT_Ele32_WPTight_Gsf_L1DoubleEG_v9',
        'HLT_Ele32_WPTight_Gsf_v15',
        'HLT_Ele35_WPTight_Gsf_L1EGMT_v5',
        'HLT_Ele35_WPTight_Gsf_v9',
        'HLT_Ele38_WPTight_Gsf_v9',
        'HLT_Ele40_WPTight_Gsf_v9',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v18',
        'HLT_Ele50_IsoVVVL_PFHT450_v16',
        'HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30_v16',
        'HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v18',
        'HLT_HT400_DisplacedDijet40_DisplacedTrack_v13',
        'HLT_HT425_v9',
        'HLT_HT430_DisplacedDijet40_DisplacedTrack_v13',
        'HLT_HT430_DisplacedDijet60_DisplacedTrack_v13',
        'HLT_HT500_DisplacedDijet40_DisplacedTrack_v13',
        'HLT_HT550_DisplacedDijet60_Inclusive_v13',
        'HLT_HT650_DisplacedDijet60_Inclusive_v13',
        'HLT_HcalIsolatedbunch_v5',
        'HLT_HcalNZS_v13',
        'HLT_HcalPhiSym_v15',
        'HLT_IsoMu20_eta2p1_LooseChargedIsoPFTauHPS27_eta2p1_CrossL1_v4',
        'HLT_IsoMu20_eta2p1_LooseChargedIsoPFTauHPS27_eta2p1_TightID_CrossL1_v1',
        'HLT_IsoMu20_eta2p1_MediumChargedIsoPFTauHPS27_eta2p1_CrossL1_v1',
        'HLT_IsoMu20_eta2p1_MediumChargedIsoPFTauHPS27_eta2p1_TightID_CrossL1_v1',
        'HLT_IsoMu20_eta2p1_TightChargedIsoPFTauHPS27_eta2p1_CrossL1_v1',
        'HLT_IsoMu20_eta2p1_TightChargedIsoPFTauHPS27_eta2p1_TightID_CrossL1_v1',
        'HLT_IsoMu20_v15',
        'HLT_IsoMu24_TwoProngs35_v1',
        'HLT_IsoMu24_eta2p1_v15',
        'HLT_IsoMu24_v13',
        'HLT_IsoMu27_v16',
        'HLT_IsoMu30_v4',
        'HLT_IsoTrackHB_v4',
        'HLT_IsoTrackHE_v4',
        'HLT_L1ETMHadSeeds_v2',
        'HLT_L1NotBptxOR_v3',
        'HLT_L1SingleMu18_v3',
        'HLT_L1SingleMu25_v2',
        'HLT_L1SingleMuCosmics_v1',
        'HLT_L1UnpairedBunchBptxMinus_v2',
        'HLT_L1UnpairedBunchBptxPlus_v2',
        'HLT_L1_CDC_SingleMu_3_er1p2_TOP120_DPHI2p618_3p142_v2',
        'HLT_L2Mu10_NoVertex_NoBPTX3BX_v5',
        'HLT_L2Mu10_NoVertex_NoBPTX_v6',
        'HLT_L2Mu10_v7',
        'HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_v5',
        'HLT_L2Mu45_NoVertex_3Sta_NoBPTX3BX_v4',
        'HLT_L2Mu50_v2',
        'HLT_MET105_IsoTrk50_v9',
        'HLT_MET120_IsoTrk50_v9',
        'HLT_MediumChargedIsoPFTau180HighPtRelaxedIso_Trk50_eta2p1_1pr_v11',
        'HLT_MediumChargedIsoPFTau180HighPtRelaxedIso_Trk50_eta2p1_v12',
        'HLT_MediumChargedIsoPFTau200HighPtRelaxedIso_Trk50_eta2p1_v12',
        'HLT_MediumChargedIsoPFTau220HighPtRelaxedIso_Trk50_eta2p1_v12',
        'HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_MET100_v12',
        'HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_MET110_v8',
        'HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_MET120_v8',
        'HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_MET130_v8',
        'HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_MET140_v3',
        'HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_MET90_v12',
        'HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_v12',
        'HLT_MonoCentralPFJet80_PFMETNoMu110_PFMHTNoMu110_IDTight_v20',
        'HLT_MonoCentralPFJet80_PFMETNoMu120_PFMHTNoMu120_IDTight_v20',
        'HLT_MonoCentralPFJet80_PFMETNoMu130_PFMHTNoMu130_IDTight_v19',
        'HLT_MonoCentralPFJet80_PFMETNoMu140_PFMHTNoMu140_IDTight_v19',
        'HLT_Mu10_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT350_PFMETNoMu60_v15',
        'HLT_Mu12_DoublePFJets100_CaloBTagDeepCSV_p71_v2',
        'HLT_Mu12_DoublePFJets200_CaloBTagDeepCSV_p71_v2',
        'HLT_Mu12_DoublePFJets350_CaloBTagDeepCSV_p71_v2',
        'HLT_Mu12_DoublePFJets40MaxDeta1p6_DoubleCaloBTagDeepCSV_p71_v2',
        'HLT_Mu12_DoublePFJets40_CaloBTagDeepCSV_p71_v2',
        'HLT_Mu12_DoublePFJets54MaxDeta1p6_DoubleCaloBTagDeepCSV_p71_v2',
        'HLT_Mu12_DoublePFJets62MaxDeta1p6_DoubleCaloBTagDeepCSV_p71_v2',
        'HLT_Mu12_DoublePhoton20_v5',
        'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v15',
        'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v7',
        'HLT_Mu12_v3',
        'HLT_Mu15_IsoVVVL_PFHT450_CaloBTagDeepCSV_4p5_v8',
        'HLT_Mu15_IsoVVVL_PFHT450_PFMET50_v15',
        'HLT_Mu15_IsoVVVL_PFHT450_v15',
        'HLT_Mu15_IsoVVVL_PFHT600_v19',
        'HLT_Mu15_v3',
        'HLT_Mu17_Photon30_IsoCaloId_v6',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v5',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v5',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v15',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v14',
        'HLT_Mu17_TrkIsoVVL_v13',
        'HLT_Mu17_v13',
        'HLT_Mu18_Mu9_DZ_v4',
        'HLT_Mu18_Mu9_SameSign_DZ_v4',
        'HLT_Mu18_Mu9_SameSign_v4',
        'HLT_Mu18_Mu9_v4',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass3p8_v3',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass8_v3',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_v3',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_v3',
        'HLT_Mu19_TrkIsoVVL_v4',
        'HLT_Mu19_v4',
        'HLT_Mu20_Mu10_DZ_v4',
        'HLT_Mu20_Mu10_SameSign_DZ_v4',
        'HLT_Mu20_Mu10_SameSign_v4',
        'HLT_Mu20_Mu10_v4',
        'HLT_Mu20_TkMu0_Phi_v8',
        'HLT_Mu20_v12',
        'HLT_Mu23_Mu12_DZ_v4',
        'HLT_Mu23_Mu12_SameSign_DZ_v4',
        'HLT_Mu23_Mu12_SameSign_v4',
        'HLT_Mu23_Mu12_v4',
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v15',
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v7',
        'HLT_Mu25_TkMu0_Onia_v8',
        'HLT_Mu25_TkMu0_Phi_v8',
        'HLT_Mu27_Ele37_CaloIdL_MW_v5',
        'HLT_Mu27_v13',
        'HLT_Mu30_TkMu0_Psi_v1',
        'HLT_Mu30_TkMu0_Upsilon_v1',
        'HLT_Mu37_Ele27_CaloIdL_MW_v5',
        'HLT_Mu37_TkMu27_v5',
        'HLT_Mu38NoFiltersNoVtxDisplaced_Photon38_CaloIdL_v1',
        'HLT_Mu3_PFJet40_v16',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET100_PFMHT100_IDTight_v2',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET70_PFMHT70_IDTight_v2',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET80_PFMHT80_IDTight_v2',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET90_PFMHT90_IDTight_v2',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu100_PFMHTNoMu100_IDTight_v2',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu70_PFMHTNoMu70_IDTight_v2',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu80_PFMHTNoMu80_IDTight_v2',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu90_PFMHTNoMu90_IDTight_v2',
        'HLT_Mu43NoFiltersNoVtxDisplaced_Photon43_CaloIdL_v1',
        'HLT_Mu43NoFiltersNoVtx_Photon43_CaloIdL_v5',
        'HLT_Mu48NoFiltersNoVtx_Photon48_CaloIdL_v5',
        'HLT_Mu4_TrkIsoVVL_DiPFJet90_40_DEta3p5_MJJ750_HTT300_PFMETNoMu60_v15',
        'HLT_Mu50_IsoVVVL_PFHT450_v15',
        'HLT_Mu50_v13',
        'HLT_Mu55_v3',
        'HLT_Mu7p5_L2Mu2_Jpsi_v10',
        'HLT_Mu7p5_L2Mu2_Upsilon_v10',
        'HLT_Mu7p5_Track2_Jpsi_v11',
        'HLT_Mu7p5_Track2_Upsilon_v11',
        'HLT_Mu7p5_Track3p5_Jpsi_v11',
        'HLT_Mu7p5_Track3p5_Upsilon_v11',
        'HLT_Mu7p5_Track7_Jpsi_v11',
        'HLT_Mu7p5_Track7_Upsilon_v11',
        'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_DZ_v18',
        'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v18',
        'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350_DZ_v19',
        'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350_v19',
        'HLT_Mu8_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT300_PFMETNoMu60_v16',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_CaloDiJet30_CaloBtagDeepCSV_1p5_v1',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_CaloDiJet30_v1',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PFBtagDeepCSV_1p5_v1',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_v1',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v13',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v11',
        'HLT_Mu8_TrkIsoVVL_v12',
        'HLT_Mu8_v12',
        'HLT_OldMu100_v3',
        'HLT_PFHT1050_v18',
        'HLT_PFHT180_v17',
        'HLT_PFHT250_v17',
        'HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_4p5_v3',
        'HLT_PFHT330PT30_QuadPFJet_75_60_45_40_v9',
        'HLT_PFHT350MinPFJet15_v9',
        'HLT_PFHT350_v19',
        'HLT_PFHT370_v17',
        'HLT_PFHT400_FivePFJet_100_100_60_30_30_DoublePFBTagDeepCSV_4p5_v8',
        'HLT_PFHT400_FivePFJet_100_100_60_30_30_v8',
        'HLT_PFHT400_FivePFJet_120_120_60_30_30_DoublePFBTagDeepCSV_4p5_v8',
        'HLT_PFHT400_SixPFJet32_DoublePFBTagDeepCSV_2p94_v8',
        'HLT_PFHT400_SixPFJet32_v8',
        'HLT_PFHT430_v17',
        'HLT_PFHT450_SixPFJet36_PFBTagDeepCSV_1p59_v7',
        'HLT_PFHT450_SixPFJet36_v7',
        'HLT_PFHT500_PFMET100_PFMHT100_IDTight_v12',
        'HLT_PFHT500_PFMET110_PFMHT110_IDTight_v12',
        'HLT_PFHT510_v17',
        'HLT_PFHT590_v17',
        'HLT_PFHT680_v17',
        'HLT_PFHT700_PFMET85_PFMHT85_IDTight_v12',
        'HLT_PFHT700_PFMET95_PFMHT95_IDTight_v12',
        'HLT_PFHT780_v17',
        'HLT_PFHT800_PFMET75_PFMHT75_IDTight_v12',
        'HLT_PFHT800_PFMET85_PFMHT85_IDTight_v12',
        'HLT_PFHT890_v17',
        'HLT_PFJet140_v19',
        'HLT_PFJet15_v3',
        'HLT_PFJet200_v19',
        'HLT_PFJet25_v3',
        'HLT_PFJet260_v20',
        'HLT_PFJet320_v20',
        'HLT_PFJet400_v20',
        'HLT_PFJet40_v21',
        'HLT_PFJet450_v21',
        'HLT_PFJet500_v21',
        'HLT_PFJet550_v11',
        'HLT_PFJet60_v21',
        'HLT_PFJet80_v20',
        'HLT_PFJetFwd140_v18',
        'HLT_PFJetFwd15_v3',
        'HLT_PFJetFwd200_v18',
        'HLT_PFJetFwd25_v3',
        'HLT_PFJetFwd260_v19',
        'HLT_PFJetFwd320_v19',
        'HLT_PFJetFwd400_v19',
        'HLT_PFJetFwd40_v19',
        'HLT_PFJetFwd450_v19',
        'HLT_PFJetFwd500_v19',
        'HLT_PFJetFwd60_v19',
        'HLT_PFJetFwd80_v18',
        'HLT_PFMET100_PFMHT100_IDTight_CaloBTagDeepCSV_3p1_v8',
        'HLT_PFMET100_PFMHT100_IDTight_PFHT60_v9',
        'HLT_PFMET110_PFMHT110_IDTight_CaloBTagDeepCSV_3p1_v8',
        'HLT_PFMET110_PFMHT110_IDTight_v20',
        'HLT_PFMET120_PFMHT120_IDTight_CaloBTagDeepCSV_3p1_v8',
        'HLT_PFMET120_PFMHT120_IDTight_PFHT60_v9',
        'HLT_PFMET120_PFMHT120_IDTight_v20',
        'HLT_PFMET130_PFMHT130_IDTight_CaloBTagDeepCSV_3p1_v8',
        'HLT_PFMET130_PFMHT130_IDTight_v20',
        'HLT_PFMET140_PFMHT140_IDTight_CaloBTagDeepCSV_3p1_v8',
        'HLT_PFMET140_PFMHT140_IDTight_v20',
        'HLT_PFMET200_BeamHaloCleaned_v9',
        'HLT_PFMET200_NotCleaned_v9',
        'HLT_PFMET250_NotCleaned_v9',
        'HLT_PFMET300_NotCleaned_v9',
        'HLT_PFMETNoMu100_PFMHTNoMu100_IDTight_PFHT60_v9',
        'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_v20',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v9',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v20',
        'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v19',
        'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v19',
        'HLT_PFMETTypeOne100_PFMHT100_IDTight_PFHT60_v9',
        'HLT_PFMETTypeOne110_PFMHT110_IDTight_v12',
        'HLT_PFMETTypeOne120_PFMHT120_IDTight_PFHT60_v9',
        'HLT_PFMETTypeOne120_PFMHT120_IDTight_v12',
        'HLT_PFMETTypeOne130_PFMHT130_IDTight_v12',
        'HLT_PFMETTypeOne140_PFMHT140_IDTight_v11',
        'HLT_PFMETTypeOne200_BeamHaloCleaned_v9',
        'HLT_Photon100EBHE10_v2',
        'HLT_Photon100EB_TightID_TightIso_v2',
        'HLT_Photon100EEHE10_v2',
        'HLT_Photon100EE_TightID_TightIso_v2',
        'HLT_Photon110EB_TightID_TightIso_v2',
        'HLT_Photon120EB_TightID_TightIso_v2',
        'HLT_Photon120_R9Id90_HE10_IsoM_v14',
        'HLT_Photon120_v13',
        'HLT_Photon150_v6',
        'HLT_Photon165_R9Id90_HE10_IsoM_v15',
        'HLT_Photon175_v14',
        'HLT_Photon200_v13',
        'HLT_Photon20_HoverELoose_v10',
        'HLT_Photon20_v2',
        'HLT_Photon300_NoHE_v12',
        'HLT_Photon30_HoverELoose_v10',
        'HLT_Photon33_v5',
        'HLT_Photon35_TwoProngs35_v1',
        'HLT_Photon50_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3_PFMET50_v5',
        'HLT_Photon50_R9Id90_HE10_IsoM_v14',
        'HLT_Photon50_v13',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT350MinPFJet15_v11',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_v5',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_v5',
        'HLT_Photon75_R9Id90_HE10_IsoM_EBOnly_CaloMJJ300_PFJetsMJJ400DEta3_v5',
        'HLT_Photon75_R9Id90_HE10_IsoM_EBOnly_CaloMJJ400_PFJetsMJJ600DEta3_v5',
        'HLT_Photon75_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3_v5',
        'HLT_Photon75_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ600DEta3_v5',
        'HLT_Photon75_R9Id90_HE10_IsoM_v14',
        'HLT_Photon75_v13',
        'HLT_Photon90_CaloIdL_PFHT700_v16',
        'HLT_Photon90_R9Id90_HE10_IsoM_v14',
        'HLT_Photon90_v13',
        'HLT_Physics_v7',
        'HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1_v8',
        'HLT_QuadPFJet103_88_75_15_PFBTagDeepCSV_1p3_VBF2_v8',
        'HLT_QuadPFJet103_88_75_15_v5',
        'HLT_QuadPFJet105_88_76_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1_v8',
        'HLT_QuadPFJet105_88_76_15_PFBTagDeepCSV_1p3_VBF2_v8',
        'HLT_QuadPFJet105_88_76_15_v5',
        'HLT_QuadPFJet111_90_80_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1_v8',
        'HLT_QuadPFJet111_90_80_15_PFBTagDeepCSV_1p3_VBF2_v8',
        'HLT_QuadPFJet111_90_80_15_v5',
        'HLT_QuadPFJet98_83_71_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1_v8',
        'HLT_QuadPFJet98_83_71_15_PFBTagDeepCSV_1p3_VBF2_v8',
        'HLT_QuadPFJet98_83_71_15_v5',
        'HLT_Random_v3',
        'HLT_Rsq0p35_v15',
        'HLT_Rsq0p40_v15',
        'HLT_RsqMR300_Rsq0p09_MR200_4jet_v15',
        'HLT_RsqMR300_Rsq0p09_MR200_v15',
        'HLT_RsqMR320_Rsq0p09_MR200_4jet_v15',
        'HLT_RsqMR320_Rsq0p09_MR200_v15',
        'HLT_SingleJet30_Mu12_SinglePFJet40_v11',
        'HLT_SinglePhoton10_Eta3p1ForPPRef_v8',
        'HLT_SinglePhoton20_Eta3p1ForPPRef_v9',
        'HLT_SinglePhoton30_Eta3p1ForPPRef_v9',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v4',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v4',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v4',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v4',
        'HLT_TkMu100_v2',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v5',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v3',
        'HLT_TripleJet110_35_35_Mjj650_PFMET110_v9',
        'HLT_TripleJet110_35_35_Mjj650_PFMET120_v9',
        'HLT_TripleJet110_35_35_Mjj650_PFMET130_v9',
        'HLT_TripleMu_10_5_5_DZ_v10',
        'HLT_TripleMu_12_10_5_v10',
        'HLT_TripleMu_5_3_3_Mass3p8_DCA_v3',
        'HLT_TripleMu_5_3_3_Mass3p8_DZ_v8',
        'HLT_TriplePhoton_20_20_20_CaloIdLV2_R9IdVL_v3',
        'HLT_TriplePhoton_20_20_20_CaloIdLV2_v3',
        'HLT_TriplePhoton_30_30_10_CaloIdLV2_R9IdVL_v4',
        'HLT_TriplePhoton_30_30_10_CaloIdLV2_v4',
        'HLT_TriplePhoton_35_35_5_CaloIdLV2_R9IdVL_v4',
        'HLT_TrkMu12_DoubleTrkMu5NoFiltersNoVtx_v6',
        'HLT_TrkMu16_DoubleTrkMu6NoFiltersNoVtx_v12',
        'HLT_TrkMu17_DoubleTrkMu8NoFiltersNoVtx_v13',
        'HLT_UncorrectedJetE30_NoBPTX3BX_v6',
        'HLT_UncorrectedJetE30_NoBPTX_v6',
        'HLT_UncorrectedJetE60_NoBPTX3BX_v6',
        'HLT_UncorrectedJetE70_NoBPTX3BX_v6',
        'HLT_VBF_DoubleLooseChargedIsoPFTauHPS20_Trk1_eta2p1_v1',
        'HLT_VBF_DoubleMediumChargedIsoPFTauHPS20_Trk1_eta2p1_v1',
        'HLT_VBF_DoubleTightChargedIsoPFTauHPS20_Trk1_eta2p1_v1',
        'HLT_ZeroBias_Alignment_v1',
        'HLT_ZeroBias_FirstBXAfterTrain_v3',
        'HLT_ZeroBias_FirstCollisionAfterAbortGap_v5',
        'HLT_ZeroBias_FirstCollisionInTrain_v4',
        'HLT_ZeroBias_IsolatedBunches_v5',
        'HLT_ZeroBias_LastCollisionInTrain_v3',
        'HLT_ZeroBias_v6'
     ) ),
    ParkingBPH1 = cms.vstring(
        'HLT_Mu12_IP6_part0_v2',
        'HLT_Mu7_IP4_part0_v2',
        'HLT_Mu8_IP3_part0_v3',
        'HLT_Mu8_IP5_part0_v2',
        'HLT_Mu8_IP6_part0_v2',
        'HLT_Mu9_IP0_part0_v2',
        'HLT_Mu9_IP3_part0_v2',
        'HLT_Mu9_IP4_part0_v2',
        'HLT_Mu9_IP5_part0_v2',
        'HLT_Mu9_IP6_part0_v3'
    ),
    ParkingBPH2 = cms.vstring(
        'HLT_Mu12_IP6_part1_v2',
        'HLT_Mu7_IP4_part1_v2',
        'HLT_Mu8_IP3_part1_v3',
        'HLT_Mu8_IP5_part1_v2',
        'HLT_Mu8_IP6_part1_v2',
        'HLT_Mu9_IP4_part1_v2',
        'HLT_Mu9_IP5_part1_v2',
        'HLT_Mu9_IP6_part1_v3'
    ),
    ParkingBPH3 = cms.vstring(
        'HLT_Mu12_IP6_part2_v2',
        'HLT_Mu7_IP4_part2_v2',
        'HLT_Mu8_IP3_part2_v3',
        'HLT_Mu8_IP5_part2_v2',
        'HLT_Mu8_IP6_part2_v2',
        'HLT_Mu9_IP4_part2_v2',
        'HLT_Mu9_IP5_part2_v2',
        'HLT_Mu9_IP6_part2_v3'
    ),
    ParkingBPH4 = cms.vstring(
        'HLT_Mu12_IP6_part3_v2',
        'HLT_Mu7_IP4_part3_v2',
        'HLT_Mu8_IP3_part3_v3',
        'HLT_Mu8_IP5_part3_v2',
        'HLT_Mu8_IP6_part3_v2',
        'HLT_Mu9_IP4_part3_v2',
        'HLT_Mu9_IP5_part3_v2',
        'HLT_Mu9_IP6_part3_v3'
    ),
    ParkingBPH5 = cms.vstring(
        'HLT_Mu12_IP6_part4_v2',
        'HLT_Mu7_IP4_part4_v2',
        'HLT_Mu8_IP3_part4_v3',
        'HLT_Mu8_IP5_part4_v2',
        'HLT_Mu8_IP6_part4_v2',
        'HLT_Mu9_IP4_part4_v2',
        'HLT_Mu9_IP5_part4_v2',
        'HLT_Mu9_IP6_part4_v3'
    ),
    ParkingBPHPromptCSCS = cms.vstring(
        'HLT_Mu12_IP6_ToCSCS_v1',
        'HLT_Mu7_IP4_ToCSCS_v1',
        'HLT_Mu8_IP3_ToCSCS_v1',
        'HLT_Mu8_IP5_ToCSCS_v1',
        'HLT_Mu8_IP6_ToCSCS_v1',
        'HLT_Mu9_IP4_ToCSCS_v1',
        'HLT_Mu9_IP5_ToCSCS_v1',
        'HLT_Mu9_IP6_ToCSCS_v1'
    ),
    RPCMonitor = cms.vstring('AlCa_RPCMuonNormalisation_v13'),
    ScoutingMonitor = cms.vstring(
        'DST_Run3_PFScoutingPixelTracking_v16',
        'HLT_Ele115_CaloIdVT_GsfTrkIdT_v14',
        'HLT_Ele35_WPTight_Gsf_v9',
        'HLT_IsoMu27_v16',
        'HLT_Mu50_v13',
        'HLT_PFHT1050_v18',
        'HLT_Photon200_v13'
    ),
    ScoutingPFRun3 = cms.vstring('DST_Run3_PFScoutingPixelTracking_v16'),
    SingleMuon = cms.vstring(
        'HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1_v12',
        'HLT_IsoMu20_eta2p1_LooseChargedIsoPFTauHPS27_eta2p1_CrossL1_v4',
        'HLT_IsoMu20_eta2p1_LooseChargedIsoPFTauHPS27_eta2p1_TightID_CrossL1_v1',
        'HLT_IsoMu20_eta2p1_MediumChargedIsoPFTauHPS27_eta2p1_CrossL1_v1',
        'HLT_IsoMu20_eta2p1_MediumChargedIsoPFTauHPS27_eta2p1_TightID_CrossL1_v1',
        'HLT_IsoMu20_eta2p1_TightChargedIsoPFTauHPS27_eta2p1_CrossL1_v1',
        'HLT_IsoMu20_eta2p1_TightChargedIsoPFTauHPS27_eta2p1_TightID_CrossL1_v1',
        'HLT_IsoMu20_v15',
        'HLT_IsoMu24_TwoProngs35_v1',
        'HLT_IsoMu24_eta2p1_v15',
        'HLT_IsoMu24_v13',
        'HLT_IsoMu27_v16',
        'HLT_IsoMu30_v4',
        'HLT_L1SingleMu18_v3',
        'HLT_L1SingleMu25_v2',
        'HLT_L2Mu10_v7',
        'HLT_L2Mu50_v2',
        'HLT_Mu10_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT350_PFMETNoMu60_v15',
        'HLT_Mu12_v3',
        'HLT_Mu15_IsoVVVL_PFHT450_CaloBTagDeepCSV_4p5_v8',
        'HLT_Mu15_IsoVVVL_PFHT450_PFMET50_v15',
        'HLT_Mu15_IsoVVVL_PFHT450_v15',
        'HLT_Mu15_IsoVVVL_PFHT600_v19',
        'HLT_Mu15_v3',
        'HLT_Mu20_v12',
        'HLT_Mu27_v13',
        'HLT_Mu3_PFJet40_v16',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET100_PFMHT100_IDTight_v2',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET70_PFMHT70_IDTight_v2',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET80_PFMHT80_IDTight_v2',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET90_PFMHT90_IDTight_v2',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu100_PFMHTNoMu100_IDTight_v2',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu70_PFMHTNoMu70_IDTight_v2',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu80_PFMHTNoMu80_IDTight_v2',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu90_PFMHTNoMu90_IDTight_v2',
        'HLT_Mu4_TrkIsoVVL_DiPFJet90_40_DEta3p5_MJJ750_HTT300_PFMETNoMu60_v15',
        'HLT_Mu50_IsoVVVL_PFHT450_v15',
        'HLT_Mu50_v13',
        'HLT_Mu55_v3',
        'HLT_Mu8_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT300_PFMETNoMu60_v16',
        'HLT_OldMu100_v3',
        'HLT_TkMu100_v2'
    ),
    Tau = cms.vstring(
        'HLT_DoubleMediumChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v12',
        'HLT_DoubleMediumChargedIsoPFTau35_Trk1_eta2p1_Reg_v12',
        'HLT_DoubleMediumChargedIsoPFTauHPS30_L1MaxMass_Trk1_eta2p1_Reg_v1',
        'HLT_DoubleMediumChargedIsoPFTauHPS35_Trk1_TightID_eta2p1_Reg_v1',
        'HLT_DoubleMediumChargedIsoPFTauHPS35_Trk1_eta2p1_Reg_v4',
        'HLT_DoubleMediumChargedIsoPFTauHPS40_Trk1_TightID_eta2p1_Reg_v1',
        'HLT_DoubleMediumChargedIsoPFTauHPS40_Trk1_eta2p1_Reg_v1',
        'HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v12',
        'HLT_DoubleTightChargedIsoPFTau35_Trk1_eta2p1_Reg_v12',
        'HLT_DoubleTightChargedIsoPFTauHPS35_Trk1_TightID_eta2p1_Reg_v1',
        'HLT_DoubleTightChargedIsoPFTauHPS35_Trk1_eta2p1_Reg_v1',
        'HLT_DoubleTightChargedIsoPFTauHPS40_Trk1_TightID_eta2p1_Reg_v1',
        'HLT_DoubleTightChargedIsoPFTauHPS40_Trk1_eta2p1_Reg_v1',
        'HLT_MediumChargedIsoPFTau180HighPtRelaxedIso_Trk50_eta2p1_1pr_v11',
        'HLT_MediumChargedIsoPFTau180HighPtRelaxedIso_Trk50_eta2p1_v12',
        'HLT_MediumChargedIsoPFTau200HighPtRelaxedIso_Trk50_eta2p1_v12',
        'HLT_MediumChargedIsoPFTau220HighPtRelaxedIso_Trk50_eta2p1_v12',
        'HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_MET100_v12',
        'HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_MET110_v8',
        'HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_MET120_v8',
        'HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_MET130_v8',
        'HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_MET140_v3',
        'HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_MET90_v12',
        'HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_v12',
        'HLT_Photon35_TwoProngs35_v1',
        'HLT_VBF_DoubleLooseChargedIsoPFTau20_Trk1_eta2p1_v3',
        'HLT_VBF_DoubleLooseChargedIsoPFTauHPS20_Trk1_eta2p1_v1',
        'HLT_VBF_DoubleMediumChargedIsoPFTauHPS20_Trk1_eta2p1_v1',
        'HLT_VBF_DoubleTightChargedIsoPFTauHPS20_Trk1_eta2p1_v1'
    ),
    TestEnablesEcalHcal = cms.vstring(
        'HLT_EcalCalibration_v4',
        'HLT_HcalCalibration_v5'
    ),
    TestEnablesEcalHcalDQM = cms.vstring(
        'HLT_EcalCalibration_v4',
        'HLT_HcalCalibration_v5'
    ),
    ZeroBias = cms.vstring(
        'HLT_Random_v3',
        'HLT_ZeroBias_Alignment_v1',
        'HLT_ZeroBias_FirstBXAfterTrain_v3',
        'HLT_ZeroBias_FirstCollisionAfterAbortGap_v5',
        'HLT_ZeroBias_FirstCollisionInTrain_v4',
        'HLT_ZeroBias_IsolatedBunches_v5',
        'HLT_ZeroBias_LastCollisionInTrain_v3',
        'HLT_ZeroBias_v6'
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(50),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

process.maxLuminosityBlocks = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.nanoDQMIO_perLSoutput = cms.PSet(
    MEsToSave = cms.untracked.vstring(
        'Muons/MuonRecoAnalyzer/',
        'Muons/MuonIdDQM/GlobalMuons/hDT1Pullx'
    )
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(4),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(True)
)

process.streams = cms.PSet(
    ALCALumiPixelCountsExpress = cms.vstring('AlCaLumiPixelCountsExpress'),
    ALCALumiPixelCountsPrompt = cms.vstring('AlCaLumiPixelCountsPrompt'),
    ALCAP0 = cms.vstring('AlCaP0'),
    ALCAPHISYM = cms.vstring('AlCaPhiSym'),
    Calibration = cms.vstring('TestEnablesEcalHcal'),
    DQM = cms.vstring('OnlineMonitor'),
    DQMCalibration = cms.vstring('TestEnablesEcalHcalDQM'),
    DQMEventDisplay = cms.vstring('EventDisplay'),
    DQMOnlineBeamspot = cms.vstring('DQMOnlineBeamspot'),
    EcalCalibration = cms.vstring('EcalLaser'),
    Express = cms.vstring('ExpressPhysics'),
    ExpressAlignment = cms.vstring('ExpressAlignment'),
    HLTMonitor = cms.vstring('HLTMonitor'),
    NanoDST = cms.vstring('L1Accept'),
    ParkingBPH1 = cms.vstring(
        'ParkingBPH1',
        'ParkingBPHPromptCSCS'
    ),
    ParkingBPH2 = cms.vstring('ParkingBPH2'),
    ParkingBPH3 = cms.vstring('ParkingBPH3'),
    ParkingBPH4 = cms.vstring('ParkingBPH4'),
    ParkingBPH5 = cms.vstring('ParkingBPH5'),
    PhysicsCommissioning = cms.vstring(
        'Commissioning',
        'Cosmics',
        'HLTPhysics',
        'HcalNZS',
        'HighPtLowerPhotons',
        'HighPtPhoton30AndZ',
        'IsolatedBunch',
        'MonteCarlo',
        'NoBPTX',
        'ZeroBias'
    ),
    PhysicsEGamma = cms.vstring('EGamma'),
    PhysicsEndOfFill = cms.vstring(
        'EmptyBX',
        'FSQJet1',
        'FSQJet2',
        'HINCaloJets',
        'HINPFJets'
    ),
    PhysicsHLTPhysics1 = cms.vstring(
        'EphemeralHLTPhysics1',
        'EphemeralHLTPhysics2'
    ),
    PhysicsHLTPhysics2 = cms.vstring(
        'EphemeralHLTPhysics3',
        'EphemeralHLTPhysics4'
    ),
    PhysicsHLTPhysics3 = cms.vstring(
        'EphemeralHLTPhysics5',
        'EphemeralHLTPhysics6'
    ),
    PhysicsHLTPhysics4 = cms.vstring(
        'EphemeralHLTPhysics7',
        'EphemeralHLTPhysics8'
    ),
    PhysicsHadronsTaus = cms.vstring(
        'BTagMu',
        'DisplacedJet',
        'JetHT',
        'MET',
        'Tau'
    ),
    PhysicsMuons = cms.vstring(
        'Charmonium',
        'DoubleMuon',
        'DoubleMuonLowMass',
        'MuOnia',
        'MuonEG',
        'SingleMuon'
    ),
    PhysicsScoutingMonitor = cms.vstring('ScoutingMonitor'),
    PhysicsZeroBias1 = cms.vstring(
        'EphemeralZeroBias1',
        'EphemeralZeroBias2'
    ),
    PhysicsZeroBias2 = cms.vstring(
        'EphemeralZeroBias3',
        'EphemeralZeroBias4'
    ),
    PhysicsZeroBias3 = cms.vstring(
        'EphemeralZeroBias5',
        'EphemeralZeroBias6'
    ),
    PhysicsZeroBias4 = cms.vstring(
        'EphemeralZeroBias7',
        'EphemeralZeroBias8'
    ),
    RPCMON = cms.vstring('RPCMonitor'),
    ScoutingPF = cms.vstring('ScoutingPFRun3')
)

process.transferSystem = cms.PSet(
    default = cms.PSet(
        default = cms.vstring('Tier0'),
        emulator = cms.vstring('Lustre'),
        streamLookArea = cms.PSet(

        ),
        test = cms.vstring('Lustre')
    ),
    destinations = cms.vstring(
        'Tier0',
        'DQM',
        'ECAL',
        'EventDisplay',
        'Lustre',
        'None'
    ),
    streamA = cms.PSet(
        default = cms.vstring('Tier0'),
        emulator = cms.vstring('Lustre'),
        test = cms.vstring('Lustre')
    ),
    streamCalibration = cms.PSet(
        default = cms.vstring('Tier0'),
        emulator = cms.vstring('None'),
        test = cms.vstring('Lustre')
    ),
    streamDQM = cms.PSet(
        default = cms.vstring('DQM'),
        emulator = cms.vstring('None'),
        test = cms.vstring(
            'DQM',
            'Lustre'
        )
    ),
    streamDQMCalibration = cms.PSet(
        default = cms.vstring('DQM'),
        emulator = cms.vstring('None'),
        test = cms.vstring(
            'DQM',
            'Lustre'
        )
    ),
    streamEcalCalibration = cms.PSet(
        default = cms.vstring('ECAL'),
        emulator = cms.vstring('None'),
        test = cms.vstring('ECAL')
    ),
    streamEventDisplay = cms.PSet(
        default = cms.vstring(
            'EventDisplay',
            'Tier0'
        ),
        emulator = cms.vstring('None'),
        test = cms.vstring(
            'EventDisplay',
            'Lustre'
        )
    ),
    streamExpressCosmics = cms.PSet(
        default = cms.vstring('Tier0'),
        emulator = cms.vstring('Lustre'),
        test = cms.vstring('Lustre')
    ),
    streamLookArea = cms.PSet(
        default = cms.vstring('DQM'),
        emulator = cms.vstring('None'),
        test = cms.vstring(
            'DQM',
            'Lustre'
        )
    ),
    streamNanoDST = cms.PSet(
        default = cms.vstring('Tier0'),
        emulator = cms.vstring('None'),
        test = cms.vstring('Lustre')
    ),
    streamRPCMON = cms.PSet(
        default = cms.vstring('Tier0'),
        emulator = cms.vstring('None'),
        test = cms.vstring('Lustre')
    ),
    streamTrackerCalibration = cms.PSet(
        default = cms.vstring('Tier0'),
        emulator = cms.vstring('None'),
        test = cms.vstring('Lustre')
    ),
    transferModes = cms.vstring(
        'default',
        'test',
        'emulator'
    )
)

process.hltAK4CaloJetsPF = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(5),
    DxyTrVtxMax = cms.double(0.0),
    DzTrVtxMax = cms.double(0.0),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.0),
    MaxVtxZ = cms.double(15.0),
    MinVtxNdof = cms.int32(5),
    R0 = cms.double(-1.0),
    Rho_EtaMax = cms.double(4.4),
    UseOnlyOnePV = cms.bool(False),
    UseOnlyVertexTracks = cms.bool(False),
    applyWeight = cms.bool(False),
    beta = cms.double(-1.0),
    correctShape = cms.bool(False),
    csRParam = cms.double(-1.0),
    csRho_EtaMax = cms.double(-1.0),
    dRMax = cms.double(-1.0),
    dRMin = cms.double(-1.0),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doFastJetNonUniform = cms.bool(False),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    gridMaxRapidity = cms.double(-1.0),
    gridSpacing = cms.double(-1.0),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetCollInstanceName = cms.string(''),
    jetPtMin = cms.double(1.0),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxDepth = cms.int32(-1),
    maxInputs = cms.uint32(1),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(0),
    minimumTowersFraction = cms.double(0.0),
    muCut = cms.double(-1.0),
    muMax = cms.double(-1.0),
    muMin = cms.double(-1.0),
    nExclude = cms.uint32(0),
    nFilt = cms.int32(-1),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(),
    puPtMin = cms.double(10.0),
    puWidth = cms.double(0.0),
    rFilt = cms.double(-1.0),
    rFiltFactor = cms.double(-1.0),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.4),
    rcut_factor = cms.double(-1.0),
    restrictInputs = cms.bool(False),
    src = cms.InputTag("hltTowerMakerForAll"),
    srcPVs = cms.InputTag("NotUsed"),
    srcWeights = cms.InputTag(""),
    subjetPtMin = cms.double(-1.0),
    subtractorName = cms.string(''),
    sumRecHits = cms.bool(False),
    trimPtFracMin = cms.double(-1.0),
    useCMSBoostedTauSeedingAlgorithm = cms.bool(False),
    useConstituentSubtraction = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    useDynamicFiltering = cms.bool(False),
    useExplicitGhosts = cms.bool(False),
    useFiltering = cms.bool(False),
    useKtPruning = cms.bool(False),
    useMassDropTagger = cms.bool(False),
    usePruning = cms.bool(False),
    useSoftDrop = cms.bool(False),
    useTrimming = cms.bool(False),
    verbosity = cms.int32(0),
    voronoiRfact = cms.double(-9.0),
    writeCompound = cms.bool(False),
    writeJetsWithConst = cms.bool(False),
    yCut = cms.double(-1.0),
    yMax = cms.double(-1.0),
    yMin = cms.double(-1.0),
    zcut = cms.double(-1.0)
)


process.hltEcalDetIdToBeRecovered = cms.EDProducer("EcalDetIdToBeRecoveredProducer",
    ebDetIdToBeRecovered = cms.string('ebDetId'),
    ebFEToBeRecovered = cms.string('ebFE'),
    ebIntegrityChIdErrors = cms.InputTag("hltEcalDigis","EcalIntegrityChIdErrors"),
    ebIntegrityGainErrors = cms.InputTag("hltEcalDigis","EcalIntegrityGainErrors"),
    ebIntegrityGainSwitchErrors = cms.InputTag("hltEcalDigis","EcalIntegrityGainSwitchErrors"),
    ebSrFlagCollection = cms.InputTag("hltEcalDigis"),
    eeDetIdToBeRecovered = cms.string('eeDetId'),
    eeFEToBeRecovered = cms.string('eeFE'),
    eeIntegrityChIdErrors = cms.InputTag("hltEcalDigis","EcalIntegrityChIdErrors"),
    eeIntegrityGainErrors = cms.InputTag("hltEcalDigis","EcalIntegrityGainErrors"),
    eeIntegrityGainSwitchErrors = cms.InputTag("hltEcalDigis","EcalIntegrityGainSwitchErrors"),
    eeSrFlagCollection = cms.InputTag("hltEcalDigis"),
    integrityBlockSizeErrors = cms.InputTag("hltEcalDigis","EcalIntegrityBlockSizeErrors"),
    integrityTTIdErrors = cms.InputTag("hltEcalDigis","EcalIntegrityTTIdErrors")
)


process.hltEcalDigisGPU = cms.EDProducer("EcalRawToDigiGPU",
    FEDs = cms.vint32(
        601, 602, 603, 604, 605,
        606, 607, 608, 609, 610,
        611, 612, 613, 614, 615,
        616, 617, 618, 619, 620,
        621, 622, 623, 624, 625,
        626, 627, 628, 629, 630,
        631, 632, 633, 634, 635,
        636, 637, 638, 639, 640,
        641, 642, 643, 644, 645,
        646, 647, 648, 649, 650,
        651, 652, 653, 654
    ),
    InputLabel = cms.InputTag("rawDataCollector"),
    digisLabelEB = cms.string('ebDigis'),
    digisLabelEE = cms.string('eeDigis'),
    maxChannelsEB = cms.uint32(61200),
    maxChannelsEE = cms.uint32(14648),
    maxFedSize = cms.uint32(10240),
    mightGet = cms.optional.untracked.vstring
)


process.hltEcalDigisLegacy = cms.EDProducer("EcalRawToDigi",
    DoRegional = cms.bool(False),
    FEDs = cms.vint32(
        601, 602, 603, 604, 605,
        606, 607, 608, 609, 610,
        611, 612, 613, 614, 615,
        616, 617, 618, 619, 620,
        621, 622, 623, 624, 625,
        626, 627, 628, 629, 630,
        631, 632, 633, 634, 635,
        636, 637, 638, 639, 640,
        641, 642, 643, 644, 645,
        646, 647, 648, 649, 650,
        651, 652, 653, 654
    ),
    FedLabel = cms.InputTag("listfeds"),
    InputLabel = cms.InputTag("rawDataCollector"),
    eventPut = cms.bool(True),
    feIdCheck = cms.bool(True),
    feUnpacking = cms.bool(True),
    forceToKeepFRData = cms.bool(False),
    headerUnpacking = cms.bool(True),
    memUnpacking = cms.bool(True),
    numbTriggerTSamples = cms.int32(1),
    numbXtalTSamples = cms.int32(10),
    orderedDCCIdList = cms.vint32(
        1, 2, 3, 4, 5,
        6, 7, 8, 9, 10,
        11, 12, 13, 14, 15,
        16, 17, 18, 19, 20,
        21, 22, 23, 24, 25,
        26, 27, 28, 29, 30,
        31, 32, 33, 34, 35,
        36, 37, 38, 39, 40,
        41, 42, 43, 44, 45,
        46, 47, 48, 49, 50,
        51, 52, 53, 54
    ),
    orderedFedList = cms.vint32(
        601, 602, 603, 604, 605,
        606, 607, 608, 609, 610,
        611, 612, 613, 614, 615,
        616, 617, 618, 619, 620,
        621, 622, 623, 624, 625,
        626, 627, 628, 629, 630,
        631, 632, 633, 634, 635,
        636, 637, 638, 639, 640,
        641, 642, 643, 644, 645,
        646, 647, 648, 649, 650,
        651, 652, 653, 654
    ),
    silentMode = cms.untracked.bool(True),
    srpUnpacking = cms.bool(True),
    syncCheck = cms.bool(True),
    tccUnpacking = cms.bool(True)
)


process.hltEcalPreshowerDigis = cms.EDProducer("ESRawToDigi",
    ESdigiCollection = cms.string(''),
    InstanceES = cms.string(''),
    LookupTable = cms.FileInPath('EventFilter/ESDigiToRaw/data/ES_lookup_table.dat'),
    debugMode = cms.untracked.bool(False),
    sourceTag = cms.InputTag("rawDataCollector")
)


process.hltEcalPreshowerRecHit = cms.EDProducer("ESRecHitProducer",
    ESRecoAlgo = cms.int32(0),
    ESdigiCollection = cms.InputTag("hltEcalPreshowerDigis"),
    ESrechitCollection = cms.string('EcalRecHitsES'),
    algo = cms.string('ESRecHitWorker')
)


process.hltEcalUncalibRecHitGPU = cms.EDProducer("EcalUncalibRecHitProducerGPU",
    EBtimeConstantTerm = cms.double(0.6),
    EBtimeFitLimits_Lower = cms.double(0.2),
    EBtimeFitLimits_Upper = cms.double(1.4),
    EBtimeNconst = cms.double(28.5),
    EEtimeConstantTerm = cms.double(1),
    EEtimeFitLimits_Lower = cms.double(0.2),
    EEtimeFitLimits_Upper = cms.double(1.4),
    EEtimeNconst = cms.double(31.8),
    amplitudeThresholdEB = cms.double(10),
    amplitudeThresholdEE = cms.double(10),
    digisLabelEB = cms.InputTag("hltEcalDigisGPU","ebDigis"),
    digisLabelEE = cms.InputTag("hltEcalDigisGPU","eeDigis"),
    kernelMinimizeThreads = cms.untracked.vuint32(32, 1, 1),
    maxNumberHitsEB = cms.uint32(61200),
    maxNumberHitsEE = cms.uint32(14648),
    mightGet = cms.optional.untracked.vstring,
    outOfTimeThresholdGain12mEB = cms.double(5),
    outOfTimeThresholdGain12mEE = cms.double(1000),
    outOfTimeThresholdGain12pEB = cms.double(5),
    outOfTimeThresholdGain12pEE = cms.double(1000),
    outOfTimeThresholdGain61mEB = cms.double(5),
    outOfTimeThresholdGain61mEE = cms.double(1000),
    outOfTimeThresholdGain61pEB = cms.double(5),
    outOfTimeThresholdGain61pEE = cms.double(1000),
    recHitsLabelEB = cms.string('EcalUncalibRecHitsEB'),
    recHitsLabelEE = cms.string('EcalUncalibRecHitsEE'),
    shouldRunTimingComputation = cms.bool(False)
)


process.hltEcalUncalibRecHitSoA = cms.EDProducer("EcalCPUUncalibRecHitProducer",
    containsTimingInformation = cms.bool(False),
    mightGet = cms.optional.untracked.vstring,
    recHitsInLabelEB = cms.InputTag("hltEcalUncalibRecHitGPU","EcalUncalibRecHitsEB"),
    recHitsInLabelEE = cms.InputTag("hltEcalUncalibRecHitGPU","EcalUncalibRecHitsEE"),
    recHitsOutLabelEB = cms.string('EcalUncalibRecHitsEB'),
    recHitsOutLabelEE = cms.string('EcalUncalibRecHitsEE')
)


process.hltEgammaCandidates = cms.EDProducer("EgammaHLTRecoEcalCandidateProducers",
    recoEcalCandidateCollection = cms.string(''),
    scHybridBarrelProducer = cms.InputTag("hltParticleFlowSuperClusterECALL1Seeded","hltParticleFlowSuperClusterECALBarrel"),
    scIslandEndcapProducer = cms.InputTag("hltParticleFlowSuperClusterECALL1Seeded","hltParticleFlowSuperClusterECALEndcapWithPreshower")
)


process.hltEgammaCkfTrackCandidatesForGSF = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string(''),
    TrajectoryBuilder = cms.string(''),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('HLTPSetTrajectoryBuilderForGsfElectrons')
    ),
    TrajectoryCleaner = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(1000000),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("hltEgammaElectronPixelSeeds"),
    useHitsSplitting = cms.bool(True)
)


process.hltEgammaClusterShape = cms.EDProducer("EgammaHLTClusterShapeProducer",
    ecalRechitEB = cms.InputTag("hltRechitInRegionsECAL","EcalRecHitsEB"),
    ecalRechitEE = cms.InputTag("hltRechitInRegionsECAL","EcalRecHitsEE"),
    isIeta = cms.bool(True),
    multThresEB = cms.double(1.0),
    multThresEE = cms.double(1.25),
    recoEcalCandidateProducer = cms.InputTag("hltEgammaCandidates")
)


process.hltEgammaEcalPFClusterIso = cms.EDProducer("EgammaHLTEcalPFClusterIsolationProducer",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    doRhoCorrection = cms.bool(False),
    drMax = cms.double(0.3),
    drVetoBarrel = cms.double(0.0),
    drVetoEndcap = cms.double(0.0),
    effectiveAreas = cms.vdouble(0.29, 0.21),
    energyBarrel = cms.double(0.0),
    energyEndcap = cms.double(0.0),
    etaStripBarrel = cms.double(0.0),
    etaStripEndcap = cms.double(0.0),
    pfClusterProducer = cms.InputTag("hltParticleFlowClusterECALL1Seeded"),
    recoEcalCandidateProducer = cms.InputTag("hltEgammaCandidates"),
    rhoMax = cms.double(99999999.0),
    rhoProducer = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
    rhoScale = cms.double(1.0)
)


process.hltEgammaEleGsfTrackIso = cms.EDProducer("EgammaHLTElectronTrackIsolationProducers",
    beamSpotProducer = cms.InputTag("hltOnlineBeamSpot"),
    egTrkIsoConeSize = cms.double(0.2),
    egTrkIsoPtMin = cms.double(1.0),
    egTrkIsoRSpan = cms.double(999999.0),
    egTrkIsoStripBarrel = cms.double(0.01),
    egTrkIsoStripEndcap = cms.double(0.01),
    egTrkIsoVetoConeSizeBarrel = cms.double(0.03),
    egTrkIsoVetoConeSizeEndcap = cms.double(0.03),
    egTrkIsoZSpan = cms.double(0.15),
    electronProducer = cms.InputTag("hltEgammaGsfElectrons"),
    recoEcalCandidateProducer = cms.InputTag("hltEgammaCandidates"),
    trackProducer = cms.InputTag("hltMergedTracks"),
    useGsfTrack = cms.bool(True),
    useSCRefs = cms.bool(True)
)


process.hltEgammaElectronPixelSeeds = cms.EDProducer("ElectronNHitSeedProducer",
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    initialSeeds = cms.InputTag("hltElePixelSeedsCombined"),
    matcherConfig = cms.PSet(
        detLayerGeom = cms.ESInputTag("","hltESPGlobalDetLayerGeometry"),
        matchingCuts = cms.VPSet(
            cms.PSet(
                dPhiMaxHighEt = cms.vdouble(0.05),
                dPhiMaxHighEtThres = cms.vdouble(20.0),
                dPhiMaxLowEtGrad = cms.vdouble(-0.002),
                dRZMaxHighEt = cms.vdouble(9999.0),
                dRZMaxHighEtThres = cms.vdouble(0.0),
                dRZMaxLowEtGrad = cms.vdouble(0.0),
                version = cms.int32(2)
            ),
            cms.PSet(
                dPhiMaxHighEt = cms.vdouble(0.003),
                dPhiMaxHighEtThres = cms.vdouble(0.0),
                dPhiMaxLowEtGrad = cms.vdouble(0.0),
                dRZMaxHighEt = cms.vdouble(0.05),
                dRZMaxHighEtThres = cms.vdouble(30.0),
                dRZMaxLowEtGrad = cms.vdouble(-0.002),
                etaBins = cms.vdouble(),
                version = cms.int32(2)
            ),
            cms.PSet(
                dPhiMaxHighEt = cms.vdouble(0.003),
                dPhiMaxHighEtThres = cms.vdouble(0.0),
                dPhiMaxLowEtGrad = cms.vdouble(0.0),
                dRZMaxHighEt = cms.vdouble(0.05),
                dRZMaxHighEtThres = cms.vdouble(30.0),
                dRZMaxLowEtGrad = cms.vdouble(-0.002),
                etaBins = cms.vdouble(),
                version = cms.int32(2)
            )
        ),
        minNrHits = cms.vuint32(2, 3),
        minNrHitsValidLayerBins = cms.vint32(4),
        navSchool = cms.ESInputTag("","SimpleNavigationSchool"),
        paramMagField = cms.ESInputTag("","ParabolicMf"),
        useRecoVertex = cms.bool(False)
    ),
    measTkEvt = cms.InputTag("hltSiStripClusters"),
    superClusters = cms.VInputTag("hltEgammaSuperClustersToPixelMatch"),
    vertices = cms.InputTag("")
)


process.hltEgammaGsfElectrons = cms.EDProducer("EgammaHLTPixelMatchElectronProducers",
    BSProducer = cms.InputTag("hltOnlineBeamSpot"),
    GsfTrackProducer = cms.InputTag("hltEgammaGsfTracks"),
    TrackProducer = cms.InputTag(""),
    UseGsfTracks = cms.bool(True)
)


process.hltEgammaGsfTrackVars = cms.EDProducer("EgammaHLTGsfTrackVarProducer",
    beamSpotProducer = cms.InputTag("hltOnlineBeamSpot"),
    inputCollection = cms.InputTag("hltEgammaGsfTracks"),
    lowerTrackNrToRemoveCut = cms.int32(-1),
    recoEcalCandidateProducer = cms.InputTag("hltEgammaCandidates"),
    upperTrackNrToRemoveCut = cms.int32(9999),
    useDefaultValuesForBarrel = cms.bool(False),
    useDefaultValuesForEndcap = cms.bool(False)
)


process.hltEgammaGsfTracks = cms.EDProducer("GsfTrackProducer",
    AlgorithmName = cms.string('gsf'),
    Fitter = cms.string('hltESPGsfElectronFittingSmoother'),
    GeometricInnerState = cms.bool(True),
    MeasurementTracker = cms.string('hltESPMeasurementTracker'),
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('hltESPFwdElectronPropagator'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    TrajectoryInEvent = cms.bool(True),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    producer = cms.string(''),
    src = cms.InputTag("hltEgammaCkfTrackCandidatesForGSF"),
    useHitsSplitting = cms.bool(False)
)


process.hltEgammaHLTExtra = cms.EDProducer("EgammaHLTExtraProducer",
    ecal = cms.VPSet(
        cms.PSet(
            label = cms.string('EcalRecHitsEB'),
            src = cms.InputTag("hltEcalRecHit","EcalRecHitsEB")
        ),
        cms.PSet(
            label = cms.string('EcalRecHitsEE'),
            src = cms.InputTag("hltEcalRecHit","EcalRecHitsEE")
        )
    ),
    egCands = cms.VPSet(
        cms.PSet(
            ecalCands = cms.InputTag("hltEgammaCandidates"),
            gsfTracks = cms.InputTag("hltEgammaGsfTracks"),
            label = cms.string(''),
            pixelSeeds = cms.InputTag("hltEgammaElectronPixelSeeds")
        ),
        cms.PSet(
            ecalCands = cms.InputTag("hltEgammaCandidatesUnseeded"),
            gsfTracks = cms.InputTag("hltEgammaGsfTracksUnseeded"),
            label = cms.string('Unseeded'),
            pixelSeeds = cms.InputTag("hltEgammaElectronPixelSeedsUnseeded")
        )
    ),
    hcal = cms.VPSet(cms.PSet(
        label = cms.string(''),
        src = cms.InputTag("hltHbhereco")
    )),
    minPtToSaveHits = cms.double(8.0),
    pfClusIso = cms.VPSet(
        cms.PSet(
            label = cms.string('Ecal'),
            src = cms.InputTag("hltParticleFlowClusterECALL1Seeded")
        ),
        cms.PSet(
            label = cms.string('EcalUnseeded'),
            src = cms.InputTag("hltParticleFlowClusterECALUnseeded")
        ),
        cms.PSet(
            label = cms.string('Hcal'),
            src = cms.InputTag("hltParticleFlowClusterHCAL")
        )
    ),
    saveHitsPlusHalfPi = cms.bool(True),
    saveHitsPlusPi = cms.bool(False),
    trks = cms.VPSet(cms.PSet(
        label = cms.string(''),
        src = cms.InputTag("hltMergedTracks")
    ))
)


process.hltEgammaHcalPFClusterIso = cms.EDProducer("EgammaHLTHcalPFClusterIsolationProducer",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    doRhoCorrection = cms.bool(False),
    drMax = cms.double(0.3),
    drVetoBarrel = cms.double(0.0),
    drVetoEndcap = cms.double(0.0),
    effectiveAreas = cms.vdouble(0.2, 0.25),
    energyBarrel = cms.double(0.0),
    energyEndcap = cms.double(0.0),
    etaStripBarrel = cms.double(0.0),
    etaStripEndcap = cms.double(0.0),
    pfClusterProducerHCAL = cms.InputTag("hltParticleFlowClusterHCAL"),
    pfClusterProducerHFEM = cms.InputTag(""),
    pfClusterProducerHFHAD = cms.InputTag(""),
    recoEcalCandidateProducer = cms.InputTag("hltEgammaCandidates"),
    rhoMax = cms.double(99999999.0),
    rhoProducer = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
    rhoScale = cms.double(1.0),
    useEt = cms.bool(True),
    useHF = cms.bool(False)
)


process.hltEgammaHoverE = cms.EDProducer("EgammaHLTBcHcalIsolationProducersRegional",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    caloTowerProducer = cms.InputTag("hltTowerMakerForAll"),
    depth = cms.int32(-1),
    doEtSum = cms.bool(False),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.105, 0.17),
    etMin = cms.double(0.0),
    innerCone = cms.double(0.0),
    outerCone = cms.double(0.14),
    recoEcalCandidateProducer = cms.InputTag("hltEgammaCandidates"),
    rhoMax = cms.double(99999999.0),
    rhoProducer = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
    rhoScale = cms.double(1.0),
    useSingleTower = cms.bool(False)
)


process.hltEgammaPixelMatchVars = cms.EDProducer("EgammaHLTPixelMatchVarProducer",
    dPhi1SParams = cms.PSet(
        bins = cms.VPSet(
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.00112, 0.000752, -0.00122, 0.00109),
                funcType = cms.string('TF1:=pol3'),
                xMax = cms.double(1.5),
                xMin = cms.double(0.0),
                yMax = cms.int32(1),
                yMin = cms.int32(1)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.00222, 0.000196, -0.000203, 0.000447),
                funcType = cms.string('TF1:=pol3'),
                xMax = cms.double(1.5),
                xMin = cms.double(0.0),
                yMax = cms.int32(2),
                yMin = cms.int32(2)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.00236, 0.000691, 0.000199, 0.000416),
                funcType = cms.string('TF1:=pol3'),
                xMax = cms.double(1.5),
                xMin = cms.double(0.0),
                yMax = cms.int32(99999),
                yMin = cms.int32(3)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.00823, -0.0029),
                funcType = cms.string('TF1:=pol1'),
                xMax = cms.double(2.0),
                xMin = cms.double(1.5),
                yMax = cms.int32(1),
                yMin = cms.int32(1)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.00282),
                funcType = cms.string('TF1:=pol0'),
                xMax = cms.double(3.0),
                xMin = cms.double(2.0),
                yMax = cms.int32(1),
                yMin = cms.int32(1)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.010838, -0.00345),
                funcType = cms.string('TF1:=pol1'),
                xMax = cms.double(2.0),
                xMin = cms.double(1.5),
                yMax = cms.int32(2),
                yMin = cms.int32(2)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.0043),
                funcType = cms.string('TF1:=pol0'),
                xMax = cms.double(3.0),
                xMin = cms.double(2.0),
                yMax = cms.int32(2),
                yMin = cms.int32(2)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.0208, -0.0125, 0.00231),
                funcType = cms.string('TF1:=pol2'),
                xMax = cms.double(3.0),
                xMin = cms.double(1.5),
                yMax = cms.int32(99999),
                yMin = cms.int32(3)
            )
        )
    ),
    dPhi2SParams = cms.PSet(
        bins = cms.VPSet(
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.00013),
                funcType = cms.string('TF1:=pol0'),
                xMax = cms.double(1.6),
                xMin = cms.double(0.0),
                yMax = cms.int32(99999),
                yMin = cms.int32(1)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.00045, -0.000199),
                funcType = cms.string('TF1:=pol1'),
                xMax = cms.double(1.9),
                xMin = cms.double(1.5),
                yMax = cms.int32(99999),
                yMin = cms.int32(1)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(7.94e-05),
                funcType = cms.string('TF1:=pol0'),
                xMax = cms.double(3.0),
                xMin = cms.double(1.9),
                yMax = cms.int32(99999),
                yMin = cms.int32(1)
            )
        )
    ),
    dRZ2SParams = cms.PSet(
        bins = cms.VPSet(
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.00299, 0.000299, -4.13e-06, 0.00191),
                funcType = cms.string('TF1:=pol3'),
                xMax = cms.double(1.5),
                xMin = cms.double(0.0),
                yMax = cms.int32(99999),
                yMin = cms.int32(1)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.248, -0.329, 0.148, -0.0222),
                funcType = cms.string('TF1:=pol3'),
                xMax = cms.double(3.0),
                xMin = cms.double(1.5),
                yMax = cms.int32(99999),
                yMin = cms.int32(1)
            )
        )
    ),
    pixelSeedsProducer = cms.InputTag("hltEgammaElectronPixelSeeds"),
    productsToWrite = cms.int32(0),
    recoEcalCandidateProducer = cms.InputTag("hltEgammaCandidates")
)


process.hltEgammaSuperClustersToPixelMatch = cms.EDProducer("EgammaHLTFilteredSuperClusterProducer",
    cands = cms.InputTag("hltEgammaCandidates"),
    cuts = cms.VPSet(cms.PSet(
        barrelCut = cms.PSet(
            cutOverE = cms.double(0.2),
            useEt = cms.bool(False)
        ),
        endcapCut = cms.PSet(
            cutOverE = cms.double(0.2),
            useEt = cms.bool(False)
        ),
        var = cms.InputTag("hltEgammaHoverE")
    )),
    minEtCutEB = cms.double(0.0),
    minEtCutEE = cms.double(0.0)
)


process.hltElePixelHitDoublets = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag(""),
    layerPairs = cms.vuint32(0),
    maxElement = cms.uint32(0),
    maxElementTotal = cms.uint32(50000000),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(True),
    seedingLayers = cms.InputTag("hltPixelLayerPairs"),
    trackingRegions = cms.InputTag("hltEleSeedsTrackingRegions"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


process.hltElePixelHitDoubletsForTriplets = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag(""),
    layerPairs = cms.vuint32(0, 1),
    maxElement = cms.uint32(0),
    maxElementTotal = cms.uint32(50000000),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(True),
    seedingLayers = cms.InputTag("hltPixelLayerTriplets"),
    trackingRegions = cms.InputTag("hltEleSeedsTrackingRegions"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


process.hltElePixelHitTriplets = cms.EDProducer("CAHitTripletEDProducer",
    CAHardPtCut = cms.double(0.3),
    CAPhiCut = cms.double(0.1),
    CAPhiCut_byTriplets = cms.VPSet(cms.PSet(
        cut = cms.double(-1.0),
        seedingLayers = cms.string('')
    )),
    CAThetaCut = cms.double(0.004),
    CAThetaCut_byTriplets = cms.VPSet(cms.PSet(
        cut = cms.double(-1.0),
        seedingLayers = cms.string('')
    )),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    doublets = cms.InputTag("hltElePixelHitDoubletsForTriplets"),
    extraHitRPhitolerance = cms.double(0.032),
    maxChi2 = cms.PSet(
        enabled = cms.bool(True),
        pt1 = cms.double(0.8),
        pt2 = cms.double(8.0),
        value1 = cms.double(100.0),
        value2 = cms.double(6.0)
    ),
    useBendingCorrection = cms.bool(True)
)


process.hltElePixelSeedsCombined = cms.EDProducer("SeedCombiner",
    seedCollections = cms.VInputTag("hltElePixelSeedsDoublets", "hltElePixelSeedsTriplets")
)


process.hltElePixelSeedsDoublets = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsEDProducer",
    MinOneOverPtError = cms.double(1.0),
    OriginTransverseErrorMultiplier = cms.double(1.0),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    SeedMomentumForBOFF = cms.double(5.0),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("hltElePixelHitDoublets")
)


process.hltElePixelSeedsTriplets = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsEDProducer",
    MinOneOverPtError = cms.double(1.0),
    OriginTransverseErrorMultiplier = cms.double(1.0),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    SeedMomentumForBOFF = cms.double(5.0),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("hltElePixelHitTriplets")
)


process.hltEleSeedsTrackingRegions = cms.EDProducer("TrackingRegionsFromSuperClustersEDProducer",
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("hltOnlineBeamSpot"),
        defaultZ = cms.double(0.0),
        deltaEtaRegion = cms.double(0.1),
        deltaPhiRegion = cms.double(0.4),
        measurementTrackerEvent = cms.InputTag(""),
        minBSDeltaZ = cms.double(0.0),
        nrSigmaForBSDeltaZ = cms.double(4.0),
        originHalfLength = cms.double(12.5),
        originRadius = cms.double(0.2),
        precise = cms.bool(True),
        ptMin = cms.double(1.5),
        superClusters = cms.VInputTag("hltEgammaSuperClustersToPixelMatch"),
        useZInBeamspot = cms.bool(False),
        useZInVertex = cms.bool(False),
        vertices = cms.InputTag(""),
        whereToUseMeasTracker = cms.string('kNever')
    )
)


process.hltFEDSelector = cms.EDProducer("EvFFEDSelector",
    fedList = cms.vuint32(1023, 1024),
    inputTag = cms.InputTag("rawDataCollector")
)


process.hltFixedGridRhoFastjetAllCaloForMuons = cms.EDProducer("FixedGridRhoProducerFastjet",
    gridSpacing = cms.double(0.55),
    maxRapidity = cms.double(2.5),
    pfCandidatesTag = cms.InputTag("hltTowerMakerForAll")
)


process.hltGtStage2Digis = cms.EDProducer("L1TRawToDigi",
    CTP7 = cms.untracked.bool(False),
    DmxFWId = cms.uint32(0),
    FWId = cms.uint32(0),
    FWOverride = cms.bool(False),
    FedIds = cms.vint32(1404),
    InputLabel = cms.InputTag("rawDataCollector"),
    MTF7 = cms.untracked.bool(False),
    MinFeds = cms.uint32(0),
    Setup = cms.string('stage2::GTSetup'),
    TMTCheck = cms.bool(True),
    debug = cms.untracked.bool(False),
    lenAMC13Header = cms.untracked.int32(8),
    lenAMC13Trailer = cms.untracked.int32(8),
    lenAMCHeader = cms.untracked.int32(8),
    lenAMCTrailer = cms.untracked.int32(0),
    lenSlinkHeader = cms.untracked.int32(8),
    lenSlinkTrailer = cms.untracked.int32(8)
)


process.hltGtStage2ObjectMap = cms.EDProducer("L1TGlobalProducer",
    AlgoBlkInputTag = cms.InputTag("hltGtStage2Digis"),
    AlgorithmTriggersUnmasked = cms.bool(True),
    AlgorithmTriggersUnprescaled = cms.bool(True),
    AlternativeNrBxBoardDaq = cms.uint32(0),
    BstLengthBytes = cms.int32(-1),
    EGammaInputTag = cms.InputTag("hltGtStage2Digis","EGamma"),
    EmulateBxInEvent = cms.int32(1),
    EtSumInputTag = cms.InputTag("hltGtStage2Digis","EtSum"),
    ExtInputTag = cms.InputTag("hltGtStage2Digis"),
    GetPrescaleColumnFromData = cms.bool(False),
    JetInputTag = cms.InputTag("hltGtStage2Digis","Jet"),
    L1DataBxInEvent = cms.int32(5),
    MuonInputTag = cms.InputTag("hltGtStage2Digis","Muon"),
    PrescaleCSVFile = cms.string('prescale_L1TGlobal.csv'),
    PrescaleSet = cms.uint32(1),
    PrintL1Menu = cms.untracked.bool(False),
    ProduceL1GtDaqRecord = cms.bool(True),
    ProduceL1GtObjectMapRecord = cms.bool(True),
    RequireMenuToMatchAlgoBlkInput = cms.bool(True),
    TauInputTag = cms.InputTag("hltGtStage2Digis","Tau"),
    TriggerMenuLuminosity = cms.string('startup'),
    Verbosity = cms.untracked.int32(0)
)


process.hltHbherecoFromGPU = cms.EDProducer("HcalCPURecHitsProducer",
    mightGet = cms.optional.untracked.vstring,
    produceLegacy = cms.bool(True),
    produceSoA = cms.bool(True),
    recHitsLegacyLabelOut = cms.string(''),
    recHitsM0LabelIn = cms.InputTag("hltHbherecoGPU"),
    recHitsM0LabelOut = cms.string('')
)


process.hltHbherecoGPU = cms.EDProducer("HBHERecHitProducerGPU",
    applyTimeSlew = cms.bool(True),
    digisLabelF01HE = cms.InputTag("hltHcalDigisGPU"),
    digisLabelF3HB = cms.InputTag("hltHcalDigisGPU"),
    digisLabelF5HB = cms.InputTag("hltHcalDigisGPU"),
    firstSampleShift = cms.int32(0),
    kernelMinimizeThreads = cms.vuint32(16, 1, 1),
    kprep1dChannelsPerBlock = cms.uint32(32),
    maxChannels = cms.uint32(10000),
    maxTimeSamples = cms.uint32(10),
    meanTime = cms.double(0),
    mightGet = cms.optional.untracked.vstring,
    recHitsLabelM0HBHE = cms.string(''),
    sipmQNTStoSum = cms.int32(3),
    sipmQTSShift = cms.int32(0),
    slopeTimeSlewParameters = cms.vdouble(-3.178648, -1.5610227, -1.075824),
    timeSigmaHPD = cms.double(5),
    timeSigmaSiPM = cms.double(2.5),
    tmaxTimeSlewParameters = cms.vdouble(16, 10, 6.25),
    ts4Thresh = cms.double(0),
    tzeroTimeSlewParameters = cms.vdouble(23.960177, 11.977461, 9.109694),
    useEffectivePedestals = cms.bool(True)
)


process.hltHcalDigis = cms.EDProducer("HcalRawToDigi",
    ComplainEmptyData = cms.untracked.bool(False),
    ElectronicsMap = cms.string(''),
    ExpectedOrbitMessageTime = cms.untracked.int32(-1),
    FEDs = cms.untracked.vint32(),
    FilterDataQuality = cms.bool(True),
    HcalFirstFED = cms.untracked.int32(700),
    InputLabel = cms.InputTag("rawDataCollector"),
    UnpackCalib = cms.untracked.bool(True),
    UnpackTTP = cms.untracked.bool(False),
    UnpackUMNio = cms.untracked.bool(True),
    UnpackZDC = cms.untracked.bool(True),
    UnpackerMode = cms.untracked.int32(0),
    firstSample = cms.int32(0),
    lastSample = cms.int32(9),
    saveQIE10DataNSamples = cms.untracked.vint32(),
    saveQIE10DataTags = cms.untracked.vstring(),
    saveQIE11DataNSamples = cms.untracked.vint32(),
    saveQIE11DataTags = cms.untracked.vstring(),
    silent = cms.untracked.bool(True)
)


process.hltHcalDigisGPU = cms.EDProducer("HcalDigisProducerGPU",
    digisLabelF01HE = cms.string(''),
    digisLabelF3HB = cms.string(''),
    digisLabelF5HB = cms.string(''),
    hbheDigisLabel = cms.InputTag("hltHcalDigis"),
    maxChannelsF01HE = cms.uint32(10000),
    maxChannelsF3HB = cms.uint32(10000),
    maxChannelsF5HB = cms.uint32(10000),
    mightGet = cms.optional.untracked.vstring,
    qie11DigiLabel = cms.InputTag("hltHcalDigis")
)


process.hltHfprereco = cms.EDProducer("HFPreReconstructor",
    digiLabel = cms.InputTag("hltHcalDigis"),
    dropZSmarkedPassed = cms.bool(True),
    forceSOI = cms.int32(-1),
    soiShift = cms.int32(0),
    sumAllTimeSlices = cms.bool(False),
    tsFromDB = cms.bool(False)
)


process.hltHfreco = cms.EDProducer("HFPhase1Reconstructor",
    HFStripFilter = cms.PSet(
        gap = cms.int32(2),
        lstrips = cms.int32(2),
        maxStripTime = cms.double(10.0),
        maxThreshold = cms.double(100.0),
        seedHitIetaMax = cms.int32(35),
        stripThreshold = cms.double(40.0),
        timeMax = cms.double(6.0),
        verboseLevel = cms.untracked.int32(10),
        wedgeCut = cms.double(0.05)
    ),
    PETstat = cms.PSet(
        HcalAcceptSeverityLevel = cms.int32(9),
        longETParams = cms.vdouble(
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0
        ),
        longEnergyParams = cms.vdouble(
            43.5, 45.7, 48.32, 51.36, 54.82,
            58.7, 63.0, 67.72, 72.86, 78.42,
            84.4, 90.8, 97.62
        ),
        long_R = cms.vdouble(0.98),
        long_R_29 = cms.vdouble(0.8),
        shortETParams = cms.vdouble(
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0
        ),
        shortEnergyParams = cms.vdouble(
            35.1773, 35.37, 35.7933, 36.4472, 37.3317,
            38.4468, 39.7925, 41.3688, 43.1757, 45.2132,
            47.4813, 49.98, 52.7093
        ),
        short_R = cms.vdouble(0.8),
        short_R_29 = cms.vdouble(0.8)
    ),
    S8S1stat = cms.PSet(
        HcalAcceptSeverityLevel = cms.int32(9),
        isS8S1 = cms.bool(True),
        longETParams = cms.vdouble(
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0
        ),
        longEnergyParams = cms.vdouble(
            40.0, 100.0, 100.0, 100.0, 100.0,
            100.0, 100.0, 100.0, 100.0, 100.0,
            100.0, 100.0, 100.0
        ),
        long_optimumSlope = cms.vdouble(
            0.3, 0.1, 0.1, 0.1, 0.1,
            0.1, 0.1, 0.1, 0.1, 0.1,
            0.1, 0.1, 0.1
        ),
        shortETParams = cms.vdouble(
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0
        ),
        shortEnergyParams = cms.vdouble(
            40.0, 100.0, 100.0, 100.0, 100.0,
            100.0, 100.0, 100.0, 100.0, 100.0,
            100.0, 100.0, 100.0
        ),
        short_optimumSlope = cms.vdouble(
            0.3, 0.1, 0.1, 0.1, 0.1,
            0.1, 0.1, 0.1, 0.1, 0.1,
            0.1, 0.1, 0.1
        )
    ),
    S9S1stat = cms.PSet(
        HcalAcceptSeverityLevel = cms.int32(9),
        isS8S1 = cms.bool(False),
        longETParams = cms.vdouble(
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0
        ),
        longEnergyParams = cms.vdouble(
            43.5, 45.7, 48.32, 51.36, 54.82,
            58.7, 63.0, 67.72, 72.86, 78.42,
            84.4, 90.8, 97.62
        ),
        long_optimumSlope = cms.vdouble(
            -99999.0, 0.0164905, 0.0238698, 0.0321383, 0.041296,
            0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422,
            0.135313, 0.136289, 0.0589927
        ),
        shortETParams = cms.vdouble(
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0
        ),
        shortEnergyParams = cms.vdouble(
            35.1773, 35.37, 35.7933, 36.4472, 37.3317,
            38.4468, 39.7925, 41.3688, 43.1757, 45.2132,
            47.4813, 49.98, 52.7093
        ),
        short_optimumSlope = cms.vdouble(
            -99999.0, 0.0164905, 0.0238698, 0.0321383, 0.041296,
            0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422,
            0.135313, 0.136289, 0.0589927
        )
    ),
    algoConfigClass = cms.string('HFPhase1PMTParams'),
    algorithm = cms.PSet(
        Class = cms.string('HFFlexibleTimeCheck'),
        energyWeights = cms.vdouble(
            1.0, 1.0, 1.0, 0.0, 1.0,
            0.0, 2.0, 0.0, 2.0, 0.0,
            2.0, 0.0, 1.0, 0.0, 0.0,
            1.0, 0.0, 1.0, 0.0, 2.0,
            0.0, 2.0, 0.0, 2.0, 0.0,
            1.0
        ),
        rejectAllFailures = cms.bool(True),
        soiPhase = cms.uint32(1),
        tfallIfNoTDC = cms.double(-101.0),
        timeShift = cms.double(0.0),
        tlimits = cms.vdouble(-1000.0, 1000.0, -1000.0, 1000.0),
        triseIfNoTDC = cms.double(-100.0)
    ),
    checkChannelQualityForDepth3and4 = cms.bool(False),
    inputLabel = cms.InputTag("hltHfprereco"),
    runHFStripFilter = cms.bool(False),
    setNoiseFlags = cms.bool(True),
    useChannelQualityFromDB = cms.bool(False)
)


process.hltHoreco = cms.EDProducer("HcalHitReconstructor",
    HFInWindowStat = cms.PSet(

    ),
    PETstat = cms.PSet(

    ),
    S8S1stat = cms.PSet(

    ),
    S9S1stat = cms.PSet(

    ),
    Subdetector = cms.string('HO'),
    correctForPhaseContainment = cms.bool(True),
    correctForTimeslew = cms.bool(True),
    correctTiming = cms.bool(False),
    correctionPhaseNS = cms.double(13.0),
    dataOOTCorrectionCategory = cms.string('Data'),
    dataOOTCorrectionName = cms.string(''),
    digiLabel = cms.InputTag("hltHcalDigis"),
    digiTimeFromDB = cms.bool(True),
    digistat = cms.PSet(

    ),
    dropZSmarkedPassed = cms.bool(True),
    firstAuxTS = cms.int32(4),
    firstSample = cms.int32(4),
    hfTimingTrustParameters = cms.PSet(

    ),
    mcOOTCorrectionCategory = cms.string('MC'),
    mcOOTCorrectionName = cms.string(''),
    recoParamsFromDB = cms.bool(True),
    samplesToAdd = cms.int32(4),
    saturationParameters = cms.PSet(
        maxADCvalue = cms.int32(127)
    ),
    setHSCPFlags = cms.bool(False),
    setNegativeFlags = cms.bool(False),
    setNoiseFlags = cms.bool(False),
    setPulseShapeFlags = cms.bool(False),
    setSaturationFlags = cms.bool(False),
    setTimingTrustFlags = cms.bool(False),
    tsFromDB = cms.bool(True),
    useLeakCorrection = cms.bool(False)
)


process.hltIter0PFLowPixelSeedsFromPixelTracks = cms.EDProducer("SeedGeneratorFromProtoTracksEDProducer",
    InputCollection = cms.InputTag("hltPixelTracks"),
    InputVertexCollection = cms.InputTag("hltTrimmedPixelVertices"),
    SeedCreatorPSet = cms.PSet(
        refToPSet_ = cms.string('HLTSeedFromProtoTracks')
    ),
    TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
    includeFourthHit = cms.bool(True),
    originHalfLength = cms.double(0.3),
    originRadius = cms.double(0.1),
    useEventsWithNoVertex = cms.bool(True),
    usePV = cms.bool(False),
    useProtoTrackKinematics = cms.bool(False)
)


process.hltIter0PFlowCkfTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    TrajectoryBuilder = cms.string(''),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('HLTIter0GroupedCkfTrajectoryBuilderIT')
    ),
    TrajectoryCleaner = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterialParabolicMf'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialParabolicMfOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(False),
    doSeedingRegionRebuilding = cms.bool(False),
    maxNSeeds = cms.uint32(100000),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("hltIter0PFLowPixelSeedsFromPixelTracks"),
    useHitsSplitting = cms.bool(False)
)


process.hltIter0PFlowCtfWithMaterialTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('hltIter0'),
    Fitter = cms.string('hltESPFittingSmootherIT'),
    GeometricInnerState = cms.bool(True),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    NavigationSchool = cms.string(''),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("hltIter0PFlowCkfTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(True)
)


process.hltIter0PFlowTrackCutClassifier = cms.EDProducer("TrackCutClassifier",
    beamspot = cms.InputTag("hltOnlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        dr_par = cms.PSet(
            d0err = cms.vdouble(0.003, 0.003, 0.003),
            d0err_par = cms.vdouble(0.001, 0.001, 0.001),
            dr_exp = cms.vint32(4, 4, 4),
            dr_par1 = cms.vdouble(3.40282346639e+38, 0.8, 0.8),
            dr_par2 = cms.vdouble(3.40282346639e+38, 0.6, 0.6)
        ),
        dz_par = cms.PSet(
            dz_exp = cms.vint32(4, 4, 4),
            dz_par1 = cms.vdouble(3.40282346639e+38, 0.75, 0.75),
            dz_par2 = cms.vdouble(3.40282346639e+38, 0.5, 0.5)
        ),
        maxChi2 = cms.vdouble(9999.0, 25.0, 16.0),
        maxChi2n = cms.vdouble(1.2, 1.0, 0.7),
        maxDr = cms.vdouble(0.5, 0.03, 3.40282346639e+38),
        maxDz = cms.vdouble(0.5, 0.2, 3.40282346639e+38),
        maxDzWrtBS = cms.vdouble(3.40282346639e+38, 24.0, 15.0),
        maxLostLayers = cms.vint32(1, 1, 1),
        min3DLayers = cms.vint32(0, 0, 0),
        minLayers = cms.vint32(3, 3, 3),
        minNVtxTrk = cms.int32(3),
        minNdof = cms.vdouble(1e-05, 1e-05, 1e-05),
        minPixelHits = cms.vint32(0, 0, 0)
    ),
    qualityCuts = cms.vdouble(-0.7, 0.1, 0.7),
    src = cms.InputTag("hltIter0PFlowCtfWithMaterialTracks"),
    vertices = cms.InputTag("hltTrimmedPixelVertices")
)


process.hltMergedTracks = cms.EDProducer("TrackCollectionFilterCloner",
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    minQuality = cms.string('highPurity'),
    originalMVAVals = cms.InputTag("hltIter0PFlowTrackCutClassifier","MVAValues"),
    originalQualVals = cms.InputTag("hltIter0PFlowTrackCutClassifier","QualityMasks"),
    originalSource = cms.InputTag("hltIter0PFlowCtfWithMaterialTracks")
)


process.hltOnlineBeamSpot = cms.EDProducer("BeamSpotOnlineProducer",
    beamMode = cms.untracked.uint32(11),
    changeToCMSCoordinates = cms.bool(False),
    gtEvmLabel = cms.InputTag(""),
    maxRadius = cms.double(2.0),
    maxZ = cms.double(40.0),
    setSigmaZ = cms.double(0.0),
    src = cms.InputTag("hltScalersRawToDigi"),
    useTransientRecord = cms.bool(False)
)


process.hltOnlineBeamSpotToCUDA = cms.EDProducer("BeamSpotToCUDA",
    mightGet = cms.optional.untracked.vstring,
    src = cms.InputTag("hltOnlineBeamSpot")
)


process.hltPSetMap = cms.EDProducer("ParameterSetBlobProducer")


process.hltParticleFlowClusterECALL1Seeded = cms.EDProducer("CorrectedECALPFClusterProducer",
    energyCorrector = cms.PSet(
        applyCrackCorrections = cms.bool(False)
    ),
    inputECAL = cms.InputTag("hltParticleFlowClusterECALUncorrectedL1Seeded"),
    inputPS = cms.InputTag("hltParticleFlowClusterPSL1Seeded"),
    minimumPSEnergy = cms.double(0.0),
    skipPS = cms.bool(False)
)


process.hltParticleFlowClusterECALUncorrectedL1Seeded = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('ECAL_BARREL'),
                gatheringThreshold = cms.double(0.08),
                gatheringThresholdPt = cms.double(0.0)
            ),
            cms.PSet(
                detector = cms.string('ECAL_ENDCAP'),
                gatheringThreshold = cms.double(0.3),
                gatheringThresholdPt = cms.double(0.0)
            )
        ),
        useCornerCells = cms.bool(True)
    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        allCellsPositionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.08),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1),
            timeResolutionCalcBarrel = cms.PSet(
                constantTerm = cms.double(0.428192),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0510871),
                noiseTerm = cms.double(1.10889),
                noiseTermLowE = cms.double(1.31883),
                threshHighE = cms.double(5.0),
                threshLowE = cms.double(0.5)
            ),
            timeResolutionCalcEndcap = cms.PSet(
                constantTerm = cms.double(0.0),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0),
                noiseTerm = cms.double(5.72489999999),
                noiseTermLowE = cms.double(6.92683000001),
                threshHighE = cms.double(10.0),
                threshLowE = cms.double(1.0)
            )
        ),
        excludeOtherSeeds = cms.bool(True),
        maxIterations = cms.uint32(50),
        minFracTot = cms.double(1e-20),
        minFractionToKeep = cms.double(1e-07),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.08),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(9),
            timeResolutionCalcBarrel = cms.PSet(
                constantTerm = cms.double(0.428192),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0510871),
                noiseTerm = cms.double(1.10889),
                noiseTermLowE = cms.double(1.31883),
                threshHighE = cms.double(5.0),
                threshLowE = cms.double(0.5)
            ),
            timeResolutionCalcEndcap = cms.PSet(
                constantTerm = cms.double(0.0),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0),
                noiseTerm = cms.double(5.72489999999),
                noiseTermLowE = cms.double(6.92683000001),
                threshHighE = cms.double(10.0),
                threshLowE = cms.double(1.0)
            )
        ),
        positionCalcForConvergence = cms.PSet(
            T0_EB = cms.double(7.4),
            T0_EE = cms.double(3.1),
            T0_ES = cms.double(1.2),
            W0 = cms.double(4.2),
            X0 = cms.double(0.89),
            algoName = cms.string('ECAL2DPositionCalcWithDepthCorr'),
            minAllowedNormalization = cms.double(0.0),
            minFractionInCalc = cms.double(0.0)
        ),
        recHitEnergyNorms = cms.VPSet(
            cms.PSet(
                detector = cms.string('ECAL_BARREL'),
                recHitEnergyNorm = cms.double(0.08)
            ),
            cms.PSet(
                detector = cms.string('ECAL_ENDCAP'),
                recHitEnergyNorm = cms.double(0.3)
            )
        ),
        showerSigma = cms.double(1.5),
        stoppingTolerance = cms.double(1e-08)
    ),
    positionReCalc = cms.PSet(
        T0_EB = cms.double(7.4),
        T0_EE = cms.double(3.1),
        T0_ES = cms.double(1.2),
        W0 = cms.double(4.2),
        X0 = cms.double(0.89),
        algoName = cms.string('ECAL2DPositionCalcWithDepthCorr'),
        minAllowedNormalization = cms.double(0.0),
        minFractionInCalc = cms.double(0.0)
    ),
    recHitCleaners = cms.VPSet(),
    recHitsSource = cms.InputTag("hltParticleFlowRecHitECALL1Seeded"),
    seedCleaners = cms.VPSet(),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        nNeighbours = cms.int32(8),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('ECAL_ENDCAP'),
                seedingThreshold = cms.double(0.6),
                seedingThresholdPt = cms.double(0.15)
            ),
            cms.PSet(
                detector = cms.string('ECAL_BARREL'),
                seedingThreshold = cms.double(0.23),
                seedingThresholdPt = cms.double(0.0)
            )
        )
    )
)


process.hltParticleFlowClusterHBHE = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                depths = cms.vint32(1, 2, 3, 4),
                detector = cms.string('HCAL_BARREL1'),
                gatheringThreshold = cms.vdouble(0.1, 0.2, 0.3, 0.3),
                gatheringThresholdPt = cms.vdouble(0.0, 0.0, 0.0, 0.0)
            ),
            cms.PSet(
                depths = cms.vint32(
                    1, 2, 3, 4, 5,
                    6, 7
                ),
                detector = cms.string('HCAL_ENDCAP'),
                gatheringThreshold = cms.vdouble(
                    0.1, 0.2, 0.2, 0.2, 0.2,
                    0.2, 0.2
                ),
                gatheringThresholdPt = cms.vdouble(
                    0.0, 0.0, 0.0, 0.0, 0.0,
                    0.0, 0.0
                )
            )
        ),
        useCornerCells = cms.bool(True)
    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        allCellsPositionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominatorByDetector = cms.VPSet(
                cms.PSet(
                    depths = cms.vint32(1, 2, 3, 4),
                    detector = cms.string('HCAL_BARREL1'),
                    logWeightDenominator = cms.vdouble(0.1, 0.2, 0.3, 0.3)
                ),
                cms.PSet(
                    depths = cms.vint32(
                        1, 2, 3, 4, 5,
                        6, 7
                    ),
                    detector = cms.string('HCAL_ENDCAP'),
                    logWeightDenominator = cms.vdouble(
                        0.1, 0.2, 0.2, 0.2, 0.2,
                        0.2, 0.2
                    )
                )
            ),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1)
        ),
        clusterTimeResFromSeed = cms.bool(False),
        excludeOtherSeeds = cms.bool(True),
        maxIterations = cms.uint32(50),
        maxNSigmaTime = cms.double(10.0),
        minChi2Prob = cms.double(0.0),
        minFracTot = cms.double(1e-20),
        minFractionToKeep = cms.double(1e-07),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominatorByDetector = cms.VPSet(
                cms.PSet(
                    depths = cms.vint32(1, 2, 3, 4),
                    detector = cms.string('HCAL_BARREL1'),
                    logWeightDenominator = cms.vdouble(0.1, 0.2, 0.3, 0.3)
                ),
                cms.PSet(
                    depths = cms.vint32(
                        1, 2, 3, 4, 5,
                        6, 7
                    ),
                    detector = cms.string('HCAL_ENDCAP'),
                    logWeightDenominator = cms.vdouble(
                        0.1, 0.2, 0.2, 0.2, 0.2,
                        0.2, 0.2
                    )
                )
            ),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(5)
        ),
        recHitEnergyNorms = cms.VPSet(
            cms.PSet(
                depths = cms.vint32(1, 2, 3, 4),
                detector = cms.string('HCAL_BARREL1'),
                recHitEnergyNorm = cms.vdouble(0.1, 0.2, 0.3, 0.3)
            ),
            cms.PSet(
                depths = cms.vint32(
                    1, 2, 3, 4, 5,
                    6, 7
                ),
                detector = cms.string('HCAL_ENDCAP'),
                recHitEnergyNorm = cms.vdouble(
                    0.1, 0.2, 0.2, 0.2, 0.2,
                    0.2, 0.2
                )
            )
        ),
        showerSigma = cms.double(10.0),
        stoppingTolerance = cms.double(1e-08),
        timeResolutionCalcBarrel = cms.PSet(
            constantTerm = cms.double(2.82),
            constantTermLowE = cms.double(4.24),
            corrTermLowE = cms.double(0.0),
            noiseTerm = cms.double(21.86),
            noiseTermLowE = cms.double(8.0),
            threshHighE = cms.double(15.0),
            threshLowE = cms.double(6.0)
        ),
        timeResolutionCalcEndcap = cms.PSet(
            constantTerm = cms.double(2.82),
            constantTermLowE = cms.double(4.24),
            corrTermLowE = cms.double(0.0),
            noiseTerm = cms.double(21.86),
            noiseTermLowE = cms.double(8.0),
            threshHighE = cms.double(15.0),
            threshLowE = cms.double(6.0)
        ),
        timeSigmaEB = cms.double(10.0),
        timeSigmaEE = cms.double(10.0)
    ),
    positionReCalc = cms.PSet(

    ),
    recHitCleaners = cms.VPSet(),
    recHitsSource = cms.InputTag("hltParticleFlowRecHitHBHE"),
    seedCleaners = cms.VPSet(),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        nNeighbours = cms.int32(4),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                depths = cms.vint32(1, 2, 3, 4),
                detector = cms.string('HCAL_BARREL1'),
                seedingThreshold = cms.vdouble(0.125, 0.25, 0.35, 0.35),
                seedingThresholdPt = cms.vdouble(0.0, 0.0, 0.0, 0.0)
            ),
            cms.PSet(
                depths = cms.vint32(
                    1, 2, 3, 4, 5,
                    6, 7
                ),
                detector = cms.string('HCAL_ENDCAP'),
                seedingThreshold = cms.vdouble(
                    0.1375, 0.275, 0.275, 0.275, 0.275,
                    0.275, 0.275
                ),
                seedingThresholdPt = cms.vdouble(
                    0.0, 0.0, 0.0, 0.0, 0.0,
                    0.0, 0.0
                )
            )
        )
    )
)


process.hltParticleFlowClusterHCAL = cms.EDProducer("PFMultiDepthClusterProducer",
    clustersSource = cms.InputTag("hltParticleFlowClusterHBHE"),
    energyCorrector = cms.PSet(

    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('PFMultiDepthClusterizer'),
        allCellsPositionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominatorByDetector = cms.VPSet(
                cms.PSet(
                    depths = cms.vint32(1, 2, 3, 4),
                    detector = cms.string('HCAL_BARREL1'),
                    logWeightDenominator = cms.vdouble(0.1, 0.2, 0.3, 0.3)
                ),
                cms.PSet(
                    depths = cms.vint32(
                        1, 2, 3, 4, 5,
                        6, 7
                    ),
                    detector = cms.string('HCAL_ENDCAP'),
                    logWeightDenominator = cms.vdouble(
                        0.1, 0.2, 0.2, 0.2, 0.2,
                        0.2, 0.2
                    )
                )
            ),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1)
        ),
        minFractionToKeep = cms.double(1e-07),
        nSigmaEta = cms.double(2.0),
        nSigmaPhi = cms.double(2.0)
    ),
    positionReCalc = cms.PSet(

    )
)


process.hltParticleFlowClusterPSL1Seeded = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('PS1'),
                gatheringThreshold = cms.double(6e-05),
                gatheringThresholdPt = cms.double(0.0)
            ),
            cms.PSet(
                detector = cms.string('PS2'),
                gatheringThreshold = cms.double(6e-05),
                gatheringThresholdPt = cms.double(0.0)
            )
        ),
        useCornerCells = cms.bool(False)
    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        excludeOtherSeeds = cms.bool(True),
        maxIterations = cms.uint32(50),
        minFracTot = cms.double(1e-20),
        minFractionToKeep = cms.double(1e-07),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(6e-05),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1)
        ),
        recHitEnergyNorms = cms.VPSet(
            cms.PSet(
                detector = cms.string('PS1'),
                recHitEnergyNorm = cms.double(6e-05)
            ),
            cms.PSet(
                detector = cms.string('PS2'),
                recHitEnergyNorm = cms.double(6e-05)
            )
        ),
        showerSigma = cms.double(0.3),
        stoppingTolerance = cms.double(1e-08)
    ),
    positionReCalc = cms.PSet(

    ),
    recHitCleaners = cms.VPSet(),
    recHitsSource = cms.InputTag("hltParticleFlowRecHitPSL1Seeded"),
    seedCleaners = cms.VPSet(),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        nNeighbours = cms.int32(4),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('PS1'),
                seedingThreshold = cms.double(0.00012),
                seedingThresholdPt = cms.double(0.0)
            ),
            cms.PSet(
                detector = cms.string('PS2'),
                seedingThreshold = cms.double(0.00012),
                seedingThresholdPt = cms.double(0.0)
            )
        )
    )
)


process.hltParticleFlowRecHitECALL1Seeded = cms.EDProducer("PFRecHitProducer",
    navigator = cms.PSet(
        barrel = cms.PSet(

        ),
        endcap = cms.PSet(

        ),
        name = cms.string('PFRecHitECALNavigator')
    ),
    producers = cms.VPSet(
        cms.PSet(
            name = cms.string('PFEBRecHitCreator'),
            qualityTests = cms.VPSet(
                cms.PSet(
                    applySelectionsToAllCrystals = cms.bool(True),
                    name = cms.string('PFRecHitQTestDBThreshold')
                ),
                cms.PSet(
                    cleaningThreshold = cms.double(2.0),
                    name = cms.string('PFRecHitQTestECAL'),
                    skipTTRecoveredHits = cms.bool(True),
                    timingCleaning = cms.bool(True),
                    topologicalCleaning = cms.bool(True)
                )
            ),
            srFlags = cms.InputTag(""),
            src = cms.InputTag("hltRechitInRegionsECAL","EcalRecHitsEB")
        ),
        cms.PSet(
            name = cms.string('PFEERecHitCreator'),
            qualityTests = cms.VPSet(
                cms.PSet(
                    applySelectionsToAllCrystals = cms.bool(True),
                    name = cms.string('PFRecHitQTestDBThreshold')
                ),
                cms.PSet(
                    cleaningThreshold = cms.double(2.0),
                    name = cms.string('PFRecHitQTestECAL'),
                    skipTTRecoveredHits = cms.bool(True),
                    timingCleaning = cms.bool(True),
                    topologicalCleaning = cms.bool(True)
                )
            ),
            srFlags = cms.InputTag(""),
            src = cms.InputTag("hltRechitInRegionsECAL","EcalRecHitsEE")
        )
    )
)


process.hltParticleFlowRecHitHBHE = cms.EDProducer("PFRecHitProducer",
    navigator = cms.PSet(
        hcalEnums = cms.vint32(1, 2),
        name = cms.string('PFRecHitHCALDenseIdNavigator')
    ),
    producers = cms.VPSet(cms.PSet(
        name = cms.string('PFHBHERecHitCreator'),
        qualityTests = cms.VPSet(
            cms.PSet(
                cuts = cms.VPSet(
                    cms.PSet(
                        depth = cms.vint32(1, 2, 3, 4),
                        detectorEnum = cms.int32(1),
                        threshold = cms.vdouble(0.1, 0.2, 0.3, 0.3)
                    ),
                    cms.PSet(
                        depth = cms.vint32(
                            1, 2, 3, 4, 5,
                            6, 7
                        ),
                        detectorEnum = cms.int32(2),
                        threshold = cms.vdouble(
                            0.1, 0.2, 0.2, 0.2, 0.2,
                            0.2, 0.2
                        )
                    )
                ),
                name = cms.string('PFRecHitQTestThreshold'),
                threshold = cms.double(0.8)
            ),
            cms.PSet(
                cleaningThresholds = cms.vdouble(0.0),
                flags = cms.vstring('Standard'),
                maxSeverities = cms.vint32(11),
                name = cms.string('PFRecHitQTestHCALChannel')
            )
        ),
        src = cms.InputTag("hltHbhereco")
    ))
)


process.hltParticleFlowRecHitPSL1Seeded = cms.EDProducer("PFRecHitProducer",
    navigator = cms.PSet(
        name = cms.string('PFRecHitPreshowerNavigator')
    ),
    producers = cms.VPSet(cms.PSet(
        name = cms.string('PFPSRecHitCreator'),
        qualityTests = cms.VPSet(cms.PSet(
            name = cms.string('PFRecHitQTestThreshold'),
            threshold = cms.double(7e-06)
        )),
        src = cms.InputTag("hltRechitInRegionsES","EcalRecHitsES")
    ))
)


process.hltParticleFlowSuperClusterECALL1Seeded = cms.EDProducer("PFECALSuperClusterProducer",
    BeamSpot = cms.InputTag("hltOnlineBeamSpot"),
    ClusteringType = cms.string('Mustache'),
    ESAssociation = cms.InputTag("hltParticleFlowClusterECALL1Seeded"),
    EnergyWeight = cms.string('Raw'),
    PFBasicClusterCollectionBarrel = cms.string('hltParticleFlowBasicClusterECALBarrel'),
    PFBasicClusterCollectionEndcap = cms.string('hltParticleFlowBasicClusterECALEndcap'),
    PFBasicClusterCollectionPreshower = cms.string('hltParticleFlowBasicClusterECALPreshower'),
    PFClusters = cms.InputTag("hltParticleFlowClusterECALL1Seeded"),
    PFSuperClusterCollectionBarrel = cms.string('hltParticleFlowSuperClusterECALBarrel'),
    PFSuperClusterCollectionEndcap = cms.string('hltParticleFlowSuperClusterECALEndcap'),
    PFSuperClusterCollectionEndcapWithPreshower = cms.string('hltParticleFlowSuperClusterECALEndcapWithPreshower'),
    applyCrackCorrections = cms.bool(False),
    barrelRecHits = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    doSatelliteClusterMerge = cms.bool(False),
    dropUnseedable = cms.bool(False),
    endcapRecHits = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    etawidth_SuperClusterBarrel = cms.double(0.04),
    etawidth_SuperClusterEndcap = cms.double(0.04),
    isOOTCollection = cms.bool(False),
    phiwidth_SuperClusterBarrel = cms.double(0.6),
    phiwidth_SuperClusterEndcap = cms.double(0.6),
    regressionConfig = cms.PSet(
        ecalRecHitsEB = cms.InputTag("hltEcalRecHit","EcalRecHitsEB"),
        ecalRecHitsEE = cms.InputTag("hltEcalRecHit","EcalRecHitsEE"),
        isHLT = cms.bool(True),
        regressionKeyEB = cms.string('pfscecal_EBCorrection_online'),
        regressionKeyEE = cms.string('pfscecal_EECorrection_online'),
        uncertaintyKeyEB = cms.string('pfscecal_EBUncertainty_online'),
        uncertaintyKeyEE = cms.string('pfscecal_EEUncertainty_online')
    ),
    satelliteClusterSeedThreshold = cms.double(50.0),
    satelliteMajorityFraction = cms.double(0.5),
    seedThresholdIsET = cms.bool(True),
    thresh_PFClusterBarrel = cms.double(0.5),
    thresh_PFClusterES = cms.double(0.5),
    thresh_PFClusterEndcap = cms.double(0.5),
    thresh_PFClusterSeedBarrel = cms.double(1.0),
    thresh_PFClusterSeedEndcap = cms.double(1.0),
    thresh_SCEt = cms.double(4.0),
    useDynamicDPhiWindow = cms.bool(True),
    useRegression = cms.bool(True),
    use_preshower = cms.bool(True),
    verbose = cms.untracked.bool(False)
)


process.hltPixelLayerPairs = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        hitErrorRPhi = cms.double(0.0027),
        hitErrorRZ = cms.double(0.006),
        useErrorsFromParam = cms.bool(True)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        hitErrorRPhi = cms.double(0.0051),
        hitErrorRZ = cms.double(0.0036),
        useErrorsFromParam = cms.bool(True)
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(

    ),
    TIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
    layerList = cms.vstring(
        'BPix1+BPix2',
        'BPix1+BPix3',
        'BPix1+BPix4',
        'BPix2+BPix3',
        'BPix2+BPix4',
        'BPix3+BPix4',
        'FPix1_pos+FPix2_pos',
        'FPix1_pos+FPix3_pos',
        'FPix2_pos+FPix3_pos',
        'BPix1+FPix1_pos',
        'BPix1+FPix2_pos',
        'BPix1+FPix3_pos',
        'BPix2+FPix1_pos',
        'BPix2+FPix2_pos',
        'BPix2+FPix3_pos',
        'BPix3+FPix1_pos',
        'BPix3+FPix2_pos',
        'BPix3+FPix3_pos',
        'BPix4+FPix1_pos',
        'BPix4+FPix2_pos',
        'BPix4+FPix3_pos',
        'FPix1_neg+FPix2_neg',
        'FPix1_neg+FPix3_neg',
        'FPix2_neg+FPix3_neg',
        'BPix1+FPix1_neg',
        'BPix1+FPix2_neg',
        'BPix1+FPix3_neg',
        'BPix2+FPix1_neg',
        'BPix2+FPix2_neg',
        'BPix2+FPix3_neg',
        'BPix3+FPix1_neg',
        'BPix3+FPix2_neg',
        'BPix3+FPix3_neg',
        'BPix4+FPix1_neg',
        'BPix4+FPix2_neg',
        'BPix4+FPix3_neg'
    )
)


process.hltPixelLayerTriplets = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        hitErrorRPhi = cms.double(0.0027),
        hitErrorRZ = cms.double(0.006),
        useErrorsFromParam = cms.bool(True)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        hitErrorRPhi = cms.double(0.0051),
        hitErrorRZ = cms.double(0.0036),
        useErrorsFromParam = cms.bool(True)
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(

    ),
    TIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
    layerList = cms.vstring(
        'BPix1+BPix2+BPix3',
        'BPix2+BPix3+BPix4',
        'BPix1+BPix3+BPix4',
        'BPix1+BPix2+BPix4',
        'BPix2+BPix3+FPix1_pos',
        'BPix2+BPix3+FPix1_neg',
        'BPix1+BPix2+FPix1_pos',
        'BPix1+BPix2+FPix1_neg',
        'BPix2+FPix1_pos+FPix2_pos',
        'BPix2+FPix1_neg+FPix2_neg',
        'BPix1+FPix1_pos+FPix2_pos',
        'BPix1+FPix1_neg+FPix2_neg',
        'FPix1_pos+FPix2_pos+FPix3_pos',
        'FPix1_neg+FPix2_neg+FPix3_neg',
        'BPix1+BPix3+FPix1_pos',
        'BPix1+BPix2+FPix2_pos',
        'BPix1+BPix3+FPix1_neg',
        'BPix1+BPix2+FPix2_neg',
        'BPix1+FPix2_neg+FPix3_neg',
        'BPix1+FPix1_neg+FPix3_neg',
        'BPix1+FPix2_pos+FPix3_pos',
        'BPix1+FPix1_pos+FPix3_pos'
    )
)


process.hltPixelTracks = cms.EDProducer("PixelTrackProducerFromSoA",
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    mightGet = cms.optional.untracked.vstring,
    minNumberOfHits = cms.int32(0),
    minQuality = cms.string('loose'),
    pixelRecHitLegacySrc = cms.InputTag("hltSiPixelRecHits"),
    trackSrc = cms.InputTag("hltPixelTracksSoA")
)


process.hltPixelTracksCUDA = cms.EDProducer("CAHitNtupletCUDA",
    CAThetaCutBarrel = cms.double(0.0020000000949949026),
    CAThetaCutForward = cms.double(0.003000000026077032),
    dcaCutInnerTriplet = cms.double(0.15000000596046448),
    dcaCutOuterTriplet = cms.double(0.25),
    doClusterCut = cms.bool(True),
    doPtCut = cms.bool(True),
    doSharedHitCut = cms.bool(True),
    doZ0Cut = cms.bool(True),
    dupPassThrough = cms.bool(False),
    earlyFishbone = cms.bool(True),
    fillStatistics = cms.bool(True),
    fit5as4 = cms.bool(True),
    hardCurvCut = cms.double(0.03284072249589491),
    idealConditions = cms.bool(False),
    includeJumpingForwardDoublets = cms.bool(True),
    lateFishbone = cms.bool(False),
    maxNumberOfDoublets = cms.uint32(524288),
    mightGet = cms.optional.untracked.vstring,
    minHitsForSharingCut = cms.uint32(5),
    minHitsPerNtuplet = cms.uint32(3),
    onGPU = cms.bool(True),
    pixelRecHitSrc = cms.InputTag("hltSiPixelRecHitsCUDA"),
    ptmin = cms.double(0.8999999761581421),
    trackQualityCuts = cms.PSet(
        chi2Coeff = cms.vdouble(0.9, 1.8),
        chi2MaxPt = cms.double(10),
        chi2Scale = cms.double(8),
        quadrupletMaxTip = cms.double(0.5),
        quadrupletMaxZip = cms.double(12),
        quadrupletMinPt = cms.double(0.3),
        tripletMaxTip = cms.double(0.3),
        tripletMaxZip = cms.double(12),
        tripletMinPt = cms.double(0.5)
    ),
    useRiemannFit = cms.bool(False),
    useSimpleTripletCleaner = cms.bool(False)
)


process.hltPixelTracksFilter = cms.EDProducer("PixelTrackFilterByKinematicsProducer",
    chi2 = cms.double(1000.0),
    nSigmaInvPtTolerance = cms.double(0.0),
    nSigmaTipMaxTolerance = cms.double(0.0),
    ptMin = cms.double(0.1),
    tipMax = cms.double(1.0)
)


process.hltPixelTracksFitter = cms.EDProducer("PixelFitterByHelixProjectionsProducer",
    scaleErrorsForBPix1 = cms.bool(False),
    scaleFactor = cms.double(0.65)
)


process.hltPixelTracksTrackingRegions = cms.EDProducer("GlobalTrackingRegionFromBeamSpotEDProducer",
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("hltOnlineBeamSpot"),
        nSigmaZ = cms.double(4.0),
        originRadius = cms.double(0.02),
        precise = cms.bool(True),
        ptMin = cms.double(0.8)
    )
)


process.hltPixelVertices = cms.EDProducer("PixelVertexProducerFromSoA",
    TrackCollection = cms.InputTag("hltPixelTracks"),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    mightGet = cms.optional.untracked.vstring,
    src = cms.InputTag("hltPixelVerticesSoA")
)


process.hltPixelVerticesCUDA = cms.EDProducer("PixelVertexProducerCUDA",
    PtMin = cms.double(0.5),
    chi2max = cms.double(9),
    eps = cms.double(0.07),
    errmax = cms.double(0.01),
    mightGet = cms.optional.untracked.vstring,
    minT = cms.int32(2),
    onGPU = cms.bool(True),
    oneKernel = cms.bool(True),
    pixelTrackSrc = cms.InputTag("hltPixelTracksCUDA"),
    useDBSCAN = cms.bool(False),
    useDensity = cms.bool(True),
    useIterative = cms.bool(False)
)


process.hltRechitInRegionsECAL = cms.EDProducer("HLTEcalRecHitInAllL1RegionsProducer",
    l1InputRegions = cms.VPSet(
        cms.PSet(
            inputColl = cms.InputTag("hltGtStage2Digis","EGamma"),
            maxEt = cms.double(999999.0),
            minEt = cms.double(5.0),
            regionEtaMargin = cms.double(0.9),
            regionPhiMargin = cms.double(1.2),
            type = cms.string('EGamma')
        ),
        cms.PSet(
            inputColl = cms.InputTag("hltGtStage2Digis","Jet"),
            maxEt = cms.double(999999.0),
            minEt = cms.double(170.0),
            regionEtaMargin = cms.double(0.9),
            regionPhiMargin = cms.double(1.2),
            type = cms.string('Jet')
        ),
        cms.PSet(
            inputColl = cms.InputTag("hltGtStage2Digis","Tau"),
            maxEt = cms.double(999999.0),
            minEt = cms.double(100.0),
            regionEtaMargin = cms.double(0.9),
            regionPhiMargin = cms.double(1.2),
            type = cms.string('Tau')
        )
    ),
    productLabels = cms.vstring(
        'EcalRecHitsEB',
        'EcalRecHitsEE'
    ),
    recHitLabels = cms.VInputTag("hltEcalRecHit:EcalRecHitsEB", "hltEcalRecHit:EcalRecHitsEE")
)


process.hltRechitInRegionsES = cms.EDProducer("HLTEcalRecHitInAllL1RegionsProducer",
    l1InputRegions = cms.VPSet(
        cms.PSet(
            inputColl = cms.InputTag("hltGtStage2Digis","EGamma"),
            maxEt = cms.double(999999.0),
            minEt = cms.double(5.0),
            regionEtaMargin = cms.double(0.9),
            regionPhiMargin = cms.double(1.2),
            type = cms.string('EGamma')
        ),
        cms.PSet(
            inputColl = cms.InputTag("hltGtStage2Digis","Jet"),
            maxEt = cms.double(999999.0),
            minEt = cms.double(170.0),
            regionEtaMargin = cms.double(0.9),
            regionPhiMargin = cms.double(1.2),
            type = cms.string('Jet')
        ),
        cms.PSet(
            inputColl = cms.InputTag("hltGtStage2Digis","Tau"),
            maxEt = cms.double(999999.0),
            minEt = cms.double(100.0),
            regionEtaMargin = cms.double(0.9),
            regionPhiMargin = cms.double(1.2),
            type = cms.string('Tau')
        )
    ),
    productLabels = cms.vstring('EcalRecHitsES'),
    recHitLabels = cms.VInputTag("hltEcalPreshowerRecHit:EcalRecHitsES")
)


process.hltScalersRawToDigi = cms.EDProducer("ScalersRawToDigi",
    scalersInputTag = cms.InputTag("rawDataCollector")
)


process.hltSiPixelClustersCUDA = cms.EDProducer("SiPixelRawToClusterCUDA",
    CablingMapLabel = cms.string(''),
    IncludeErrors = cms.bool(True),
    InputLabel = cms.InputTag("rawDataCollector"),
    MaxFEDWords = cms.uint32(300000),
    Regions = cms.PSet(
        beamSpot = cms.optional.InputTag,
        deltaPhi = cms.optional.vdouble,
        inputs = cms.optional.VInputTag,
        maxZ = cms.optional.vdouble
    ),
    UseQualityInfo = cms.bool(False),
    clusterThreshold_layer1 = cms.int32(2000),
    clusterThreshold_otherLayers = cms.int32(4000),
    isRun2 = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
)


process.hltSiPixelClustersCache = cms.EDProducer("SiPixelClusterShapeCacheProducer",
    onDemand = cms.bool(False),
    src = cms.InputTag("hltSiPixelClusters")
)


process.hltSiPixelClustersLegacy = cms.EDProducer("SiPixelClusterProducer",
    ChannelThreshold = cms.int32(1000),
    ClusterMode = cms.string('PixelThresholdClusterizer'),
    ClusterThreshold = cms.int32(4000),
    ClusterThreshold_L1 = cms.int32(2000),
    ElectronPerADCGain = cms.double(135.0),
    MissCalibrate = cms.bool(True),
    Phase2Calibration = cms.bool(False),
    Phase2DigiBaseline = cms.double(1200.0),
    Phase2KinkADC = cms.int32(8),
    Phase2ReadoutMode = cms.int32(-1),
    SeedThreshold = cms.int32(1000),
    SplitClusters = cms.bool(False),
    VCaltoElectronGain = cms.int32(1),
    VCaltoElectronGain_L1 = cms.int32(1),
    VCaltoElectronOffset = cms.int32(0),
    VCaltoElectronOffset_L1 = cms.int32(0),
    maxNumberOfClusters = cms.int32(40000),
    payloadType = cms.string('HLT'),
    src = cms.InputTag("hltSiPixelDigisLegacy")
)


process.hltSiPixelDigiErrorsSoA = cms.EDProducer("SiPixelDigiErrorsSoAFromCUDA",
    mightGet = cms.optional.untracked.vstring,
    src = cms.InputTag("hltSiPixelClustersCUDA")
)


process.hltSiPixelDigisLegacy = cms.EDProducer("SiPixelRawToDigi",
    CablingMapLabel = cms.string(''),
    ErrorList = cms.vint32(29),
    IncludeErrors = cms.bool(True),
    InputLabel = cms.InputTag("rawDataCollector"),
    Regions = cms.PSet(

    ),
    UsePhase1 = cms.bool(True),
    UsePilotBlade = cms.bool(False),
    UseQualityInfo = cms.bool(False),
    UserErrorList = cms.vint32()
)


process.hltSiPixelDigisSoA = cms.EDProducer("SiPixelDigisSoAFromCUDA",
    mightGet = cms.optional.untracked.vstring,
    src = cms.InputTag("hltSiPixelClustersCUDA")
)


process.hltSiPixelRecHitSoA = cms.EDProducer("SiPixelRecHitSoAFromLegacy",
    CPE = cms.string('PixelCPEFast'),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    convertToLegacy = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    src = cms.InputTag("hltSiPixelClusters")
)


process.hltSiPixelRecHitsCUDA = cms.EDProducer("SiPixelRecHitCUDA",
    CPE = cms.string('PixelCPEFast'),
    beamSpot = cms.InputTag("hltOnlineBeamSpotToCUDA"),
    mightGet = cms.optional.untracked.vstring,
    src = cms.InputTag("hltSiPixelClustersCUDA")
)


process.hltSiStripClusters = cms.EDProducer("MeasurementTrackerEventProducer",
    Phase2TrackerCluster1DProducer = cms.string(''),
    badPixelFEDChannelCollectionLabels = cms.VInputTag("hltSiPixelDigis"),
    inactivePixelDetectorLabels = cms.VInputTag("hltSiPixelDigis"),
    inactiveStripDetectorLabels = cms.VInputTag("hltSiStripExcludedFEDListProducer"),
    measurementTracker = cms.string('hltESPMeasurementTracker'),
    pixelCablingMapLabel = cms.string(''),
    pixelClusterProducer = cms.string('hltSiPixelClusters'),
    skipClusters = cms.InputTag(""),
    stripClusterProducer = cms.string('hltSiStripRawToClustersFacility'),
    switchOffPixelsIfEmpty = cms.bool(True),
    vectorHits = cms.InputTag(""),
    vectorHitsRej = cms.InputTag("")
)


process.hltSiStripExcludedFEDListProducer = cms.EDProducer("SiStripExcludedFEDListProducer",
    ProductLabel = cms.InputTag("rawDataCollector")
)


process.hltSiStripRawToClustersFacility = cms.EDProducer("SiStripClusterizerFromRaw",
    Algorithms = cms.PSet(
        CommonModeNoiseSubtractionMode = cms.string('Median'),
        PedestalSubtractionFedMode = cms.bool(True),
        SiStripFedZeroSuppressionMode = cms.uint32(4),
        TruncateInSuppressor = cms.bool(True),
        Use10bitsTruncation = cms.bool(False),
        doAPVRestore = cms.bool(False),
        useCMMeanMap = cms.bool(False)
    ),
    Clusterizer = cms.PSet(
        Algorithm = cms.string('ThreeThresholdAlgorithm'),
        ChannelThreshold = cms.double(2.0),
        ClusterThreshold = cms.double(5.0),
        ConditionsLabel = cms.string(''),
        MaxAdjacentBad = cms.uint32(0),
        MaxSequentialBad = cms.uint32(1),
        MaxSequentialHoles = cms.uint32(0),
        RemoveApvShots = cms.bool(True),
        SeedThreshold = cms.double(3.0),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
        ),
        setDetId = cms.bool(True)
    ),
    DoAPVEmulatorCheck = cms.bool(False),
    HybridZeroSuppressed = cms.bool(False),
    ProductLabel = cms.InputTag("rawDataCollector"),
    onDemand = cms.bool(False)
)


process.hltTowerMakerForAll = cms.EDProducer("CaloTowersCreator",
    AllowMissingInputs = cms.bool(False),
    EBGrid = cms.vdouble(),
    EBSumThreshold = cms.double(0.2),
    EBThreshold = cms.double(0.07),
    EBWeight = cms.double(1.0),
    EBWeights = cms.vdouble(),
    EEGrid = cms.vdouble(),
    EESumThreshold = cms.double(0.45),
    EEThreshold = cms.double(0.3),
    EEWeight = cms.double(1.0),
    EEWeights = cms.vdouble(),
    EcalRecHitSeveritiesToBeExcluded = cms.vstring(
        'kTime',
        'kWeird',
        'kBad'
    ),
    EcalSeveritiesToBeUsedInBadTowers = cms.vstring(),
    EcutTower = cms.double(-1000.0),
    HBGrid = cms.vdouble(),
    HBThreshold = cms.double(0.3),
    HBThreshold1 = cms.double(0.1),
    HBThreshold2 = cms.double(0.2),
    HBWeight = cms.double(1.0),
    HBWeights = cms.vdouble(),
    HEDGrid = cms.vdouble(),
    HEDThreshold = cms.double(0.2),
    HEDThreshold1 = cms.double(0.1),
    HEDWeight = cms.double(1.0),
    HEDWeights = cms.vdouble(),
    HESGrid = cms.vdouble(),
    HESThreshold = cms.double(0.2),
    HESThreshold1 = cms.double(0.1),
    HESWeight = cms.double(1.0),
    HESWeights = cms.vdouble(),
    HF1Grid = cms.vdouble(),
    HF1Threshold = cms.double(0.5),
    HF1Weight = cms.double(1.0),
    HF1Weights = cms.vdouble(),
    HF2Grid = cms.vdouble(),
    HF2Threshold = cms.double(0.85),
    HF2Weight = cms.double(1.0),
    HF2Weights = cms.vdouble(),
    HOGrid = cms.vdouble(),
    HOThreshold0 = cms.double(3.5),
    HOThresholdMinus1 = cms.double(3.5),
    HOThresholdMinus2 = cms.double(3.5),
    HOThresholdPlus1 = cms.double(3.5),
    HOThresholdPlus2 = cms.double(3.5),
    HOWeight = cms.double(1e-99),
    HOWeights = cms.vdouble(),
    HcalAcceptSeverityLevel = cms.uint32(9),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32(9999),
    HcalPhase = cms.int32(1),
    HcalThreshold = cms.double(-1000.0),
    MomConstrMethod = cms.int32(1),
    MomEBDepth = cms.double(0.3),
    MomEEDepth = cms.double(0.0),
    MomHBDepth = cms.double(0.2),
    MomHEDepth = cms.double(0.4),
    UseEcalRecoveredHits = cms.bool(False),
    UseEtEBTreshold = cms.bool(False),
    UseEtEETreshold = cms.bool(False),
    UseHO = cms.bool(False),
    UseHcalRecoveredHits = cms.bool(False),
    UseRejectedHitsOnly = cms.bool(False),
    UseRejectedRecoveredEcalHits = cms.bool(False),
    UseRejectedRecoveredHcalHits = cms.bool(False),
    UseSymEBTreshold = cms.bool(False),
    UseSymEETreshold = cms.bool(False),
    ecalInputs = cms.VInputTag("hltEcalRecHit:EcalRecHitsEB", "hltEcalRecHit:EcalRecHitsEE"),
    hbheInput = cms.InputTag("hltHbhereco"),
    hfInput = cms.InputTag("hltHfreco"),
    hoInput = cms.InputTag("hltHoreco"),
    missingHcalRescaleFactorForEcal = cms.double(0.0)
)


process.hltTriggerSummaryAOD = cms.EDProducer("TriggerSummaryProducerAOD",
    moduleLabelPatternsToMatch = cms.vstring('hlt*'),
    moduleLabelPatternsToSkip = cms.vstring(),
    processName = cms.string('@'),
    throw = cms.bool(False)
)


process.hltTriggerSummaryRAW = cms.EDProducer("TriggerSummaryProducerRAW",
    processName = cms.string('@')
)


process.hltTrimmedPixelVertices = cms.EDProducer("PixelVertexCollectionTrimmer",
    PVcomparer = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPvClusterComparerForIT')
    ),
    fractionSumPt2 = cms.double(0.3),
    maxVtx = cms.uint32(100),
    minSumPt2 = cms.double(0.0),
    src = cms.InputTag("hltPixelVertices")
)


process.hltEcalDigis = SwitchProducerCUDA(
    cpu = cms.EDAlias(
        hltEcalDigisLegacy = cms.VPSet(
            cms.PSet(
                type = cms.string('EBDigiCollection')
            ),
            cms.PSet(
                type = cms.string('EEDigiCollection')
            ),
            cms.PSet(
                type = cms.string('EBDetIdedmEDCollection')
            ),
            cms.PSet(
                type = cms.string('EEDetIdedmEDCollection')
            ),
            cms.PSet(
                type = cms.string('EBSrFlagsSorted')
            ),
            cms.PSet(
                type = cms.string('EESrFlagsSorted')
            ),
            cms.PSet(
                fromProductInstance = cms.string('EcalIntegrityBlockSizeErrors'),
                type = cms.string('EcalElectronicsIdedmEDCollection')
            ),
            cms.PSet(
                fromProductInstance = cms.string('EcalIntegrityTTIdErrors'),
                type = cms.string('EcalElectronicsIdedmEDCollection')
            ),
            cms.PSet(
                fromProductInstance = cms.string('EcalIntegrityZSXtalIdErrors'),
                type = cms.string('EcalElectronicsIdedmEDCollection')
            ),
            cms.PSet(
                type = cms.string('EcalPnDiodeDigisSorted')
            ),
            cms.PSet(
                fromProductInstance = cms.string('EcalPseudoStripInputs'),
                type = cms.string('EcalPseudoStripInputDigisSorted')
            ),
            cms.PSet(
                fromProductInstance = cms.string('EcalTriggerPrimitives'),
                type = cms.string('EcalTriggerPrimitiveDigisSorted')
            )
        )
    ),
    cuda = cms.EDProducer("EcalCPUDigisProducer",
        digisInLabelEB = cms.InputTag("hltEcalDigisGPU","ebDigis"),
        digisInLabelEE = cms.InputTag("hltEcalDigisGPU","eeDigis"),
        digisOutLabelEB = cms.string('ebDigis'),
        digisOutLabelEE = cms.string('eeDigis'),
        mightGet = cms.optional.untracked.vstring,
        produceDummyIntegrityCollections = cms.bool(True)
    )
)


process.hltEcalRecHit = SwitchProducerCUDA(
    cpu = cms.EDProducer("EcalRecHitProducer",
        ChannelStatusToBeExcluded = cms.vstring(),
        EBLaserMAX = cms.double(3.0),
        EBLaserMIN = cms.double(0.5),
        EBrechitCollection = cms.string('EcalRecHitsEB'),
        EBuncalibRecHitCollection = cms.InputTag("hltEcalUncalibRecHit","EcalUncalibRecHitsEB"),
        EELaserMAX = cms.double(8.0),
        EELaserMIN = cms.double(0.5),
        EErechitCollection = cms.string('EcalRecHitsEE'),
        EEuncalibRecHitCollection = cms.InputTag("hltEcalUncalibRecHit","EcalUncalibRecHitsEE"),
        algo = cms.string('EcalRecHitWorkerSimple'),
        algoRecover = cms.string('EcalRecHitWorkerRecover'),
        bdtWeightFileCracks = cms.FileInPath('RecoLocalCalo/EcalDeadChannelRecoveryAlgos/data/BDTWeights/bdtgAllRH_8GT700MeV_onlyCracks_ZskimData2017_v1.xml'),
        bdtWeightFileNoCracks = cms.FileInPath('RecoLocalCalo/EcalDeadChannelRecoveryAlgos/data/BDTWeights/bdtgAllRH_8GT700MeV_noCracks_ZskimData2017_v1.xml'),
        cleaningConfig = cms.PSet(
            cThreshold_barrel = cms.double(4.0),
            cThreshold_double = cms.double(10.0),
            cThreshold_endcap = cms.double(15.0),
            e4e1Threshold_barrel = cms.double(0.08),
            e4e1Threshold_endcap = cms.double(0.3),
            e4e1_a_barrel = cms.double(0.04),
            e4e1_a_endcap = cms.double(0.02),
            e4e1_b_barrel = cms.double(-0.024),
            e4e1_b_endcap = cms.double(-0.0125),
            e6e2thresh = cms.double(0.04),
            ignoreOutOfTimeThresh = cms.double(1000000000.0),
            tightenCrack_e1_double = cms.double(2.0),
            tightenCrack_e1_single = cms.double(2.0),
            tightenCrack_e4e1_single = cms.double(3.0),
            tightenCrack_e6e2_double = cms.double(3.0)
        ),
        dbStatusToBeExcludedEB = cms.vint32(14, 78, 142),
        dbStatusToBeExcludedEE = cms.vint32(14, 78, 142),
        ebDetIdToBeRecovered = cms.InputTag("hltEcalDetIdToBeRecovered","ebDetId"),
        ebFEToBeRecovered = cms.InputTag("hltEcalDetIdToBeRecovered","ebFE"),
        eeDetIdToBeRecovered = cms.InputTag("hltEcalDetIdToBeRecovered","eeDetId"),
        eeFEToBeRecovered = cms.InputTag("hltEcalDetIdToBeRecovered","eeFE"),
        flagsMapDBReco = cms.PSet(
            kDead = cms.vstring('kNoDataNoTP'),
            kGood = cms.vstring(
                'kOk',
                'kDAC',
                'kNoLaser',
                'kNoisy'
            ),
            kNeighboursRecovered = cms.vstring(
                'kFixedG0',
                'kNonRespondingIsolated',
                'kDeadVFE'
            ),
            kNoisy = cms.vstring(
                'kNNoisy',
                'kFixedG6',
                'kFixedG1'
            ),
            kTowerRecovered = cms.vstring('kDeadFE')
        ),
        killDeadChannels = cms.bool(True),
        laserCorrection = cms.bool(True),
        logWarningEtThreshold_EB_FE = cms.double(50.0),
        logWarningEtThreshold_EE_FE = cms.double(50.0),
        recoverEBFE = cms.bool(True),
        recoverEBIsolatedChannels = cms.bool(False),
        recoverEBVFE = cms.bool(False),
        recoverEEFE = cms.bool(True),
        recoverEEIsolatedChannels = cms.bool(False),
        recoverEEVFE = cms.bool(False),
        singleChannelRecoveryMethod = cms.string('NeuralNetworks'),
        singleChannelRecoveryThreshold = cms.double(8.0),
        skipTimeCalib = cms.bool(True),
        sum8ChannelRecoveryThreshold = cms.double(0.0),
        triggerPrimitiveDigiCollection = cms.InputTag("hltEcalDigisLegacy","EcalTriggerPrimitives")
    ),
    cuda = cms.EDProducer("EcalRecHitProducer",
        ChannelStatusToBeExcluded = cms.vstring(),
        EBLaserMAX = cms.double(3.0),
        EBLaserMIN = cms.double(0.5),
        EBrechitCollection = cms.string('EcalRecHitsEB'),
        EBuncalibRecHitCollection = cms.InputTag("hltEcalUncalibRecHit","EcalUncalibRecHitsEB"),
        EELaserMAX = cms.double(8.0),
        EELaserMIN = cms.double(0.5),
        EErechitCollection = cms.string('EcalRecHitsEE'),
        EEuncalibRecHitCollection = cms.InputTag("hltEcalUncalibRecHit","EcalUncalibRecHitsEE"),
        algo = cms.string('EcalRecHitWorkerSimple'),
        algoRecover = cms.string('EcalRecHitWorkerRecover'),
        bdtWeightFileCracks = cms.FileInPath('RecoLocalCalo/EcalDeadChannelRecoveryAlgos/data/BDTWeights/bdtgAllRH_8GT700MeV_onlyCracks_ZskimData2017_v1.xml'),
        bdtWeightFileNoCracks = cms.FileInPath('RecoLocalCalo/EcalDeadChannelRecoveryAlgos/data/BDTWeights/bdtgAllRH_8GT700MeV_noCracks_ZskimData2017_v1.xml'),
        cleaningConfig = cms.PSet(
            cThreshold_barrel = cms.double(4.0),
            cThreshold_double = cms.double(10.0),
            cThreshold_endcap = cms.double(15.0),
            e4e1Threshold_barrel = cms.double(0.08),
            e4e1Threshold_endcap = cms.double(0.3),
            e4e1_a_barrel = cms.double(0.04),
            e4e1_a_endcap = cms.double(0.02),
            e4e1_b_barrel = cms.double(-0.024),
            e4e1_b_endcap = cms.double(-0.0125),
            e6e2thresh = cms.double(0.04),
            ignoreOutOfTimeThresh = cms.double(1000000000.0),
            tightenCrack_e1_double = cms.double(2.0),
            tightenCrack_e1_single = cms.double(2.0),
            tightenCrack_e4e1_single = cms.double(3.0),
            tightenCrack_e6e2_double = cms.double(3.0)
        ),
        dbStatusToBeExcludedEB = cms.vint32(14, 78, 142),
        dbStatusToBeExcludedEE = cms.vint32(14, 78, 142),
        ebDetIdToBeRecovered = cms.InputTag("hltEcalDetIdToBeRecovered","ebDetId"),
        ebFEToBeRecovered = cms.InputTag("hltEcalDetIdToBeRecovered","ebFE"),
        eeDetIdToBeRecovered = cms.InputTag("hltEcalDetIdToBeRecovered","eeDetId"),
        eeFEToBeRecovered = cms.InputTag("hltEcalDetIdToBeRecovered","eeFE"),
        flagsMapDBReco = cms.PSet(
            kDead = cms.vstring('kNoDataNoTP'),
            kGood = cms.vstring(
                'kOk',
                'kDAC',
                'kNoLaser',
                'kNoisy'
            ),
            kNeighboursRecovered = cms.vstring(
                'kFixedG0',
                'kNonRespondingIsolated',
                'kDeadVFE'
            ),
            kNoisy = cms.vstring(
                'kNNoisy',
                'kFixedG6',
                'kFixedG1'
            ),
            kTowerRecovered = cms.vstring('kDeadFE')
        ),
        killDeadChannels = cms.bool(True),
        laserCorrection = cms.bool(True),
        logWarningEtThreshold_EB_FE = cms.double(50.0),
        logWarningEtThreshold_EE_FE = cms.double(50.0),
        recoverEBFE = cms.bool(True),
        recoverEBIsolatedChannels = cms.bool(False),
        recoverEBVFE = cms.bool(False),
        recoverEEFE = cms.bool(True),
        recoverEEIsolatedChannels = cms.bool(False),
        recoverEEVFE = cms.bool(False),
        singleChannelRecoveryMethod = cms.string('NeuralNetworks'),
        singleChannelRecoveryThreshold = cms.double(8.0),
        skipTimeCalib = cms.bool(True),
        sum8ChannelRecoveryThreshold = cms.double(0.0),
        triggerPrimitiveDigiCollection = cms.InputTag("unused")
    )
)


process.hltEcalUncalibRecHit = SwitchProducerCUDA(
    cpu = cms.EDProducer("EcalUncalibRecHitProducer",
        EBdigiCollection = cms.InputTag("hltEcalDigis","ebDigis"),
        EBhitCollection = cms.string('EcalUncalibRecHitsEB'),
        EEdigiCollection = cms.InputTag("hltEcalDigis","eeDigis"),
        EEhitCollection = cms.string('EcalUncalibRecHitsEE'),
        algo = cms.string('EcalUncalibRecHitWorkerMultiFit'),
        algoPSet = cms.PSet(
            EBamplitudeFitParameters = cms.vdouble(1.138, 1.652),
            EBtimeConstantTerm = cms.double(0.6),
            EBtimeFitLimits_Lower = cms.double(0.2),
            EBtimeFitLimits_Upper = cms.double(1.4),
            EBtimeFitParameters = cms.vdouble(
                -2.015452, 3.130702, -12.3473, 41.88921, -82.83944,
                91.01147, -50.35761, 11.05621
            ),
            EBtimeNconst = cms.double(28.5),
            EEamplitudeFitParameters = cms.vdouble(1.89, 1.4),
            EEtimeConstantTerm = cms.double(1.0),
            EEtimeFitLimits_Lower = cms.double(0.2),
            EEtimeFitLimits_Upper = cms.double(1.4),
            EEtimeFitParameters = cms.vdouble(
                -2.390548, 3.553628, -17.62341, 67.67538, -133.213,
                140.7432, -75.41106, 16.20277
            ),
            EEtimeNconst = cms.double(31.8),
            EcalPulseShapeParameters = cms.PSet(
                EBCorrNoiseMatrixG01 = cms.vdouble(
                    1.0, 0.73354, 0.64442, 0.58851, 0.55425,
                    0.53082, 0.51916, 0.51097, 0.50732, 0.50409
                ),
                EBCorrNoiseMatrixG06 = cms.vdouble(
                    1.0, 0.70946, 0.58021, 0.49846, 0.45006,
                    0.41366, 0.39699, 0.38478, 0.37847, 0.37055
                ),
                EBCorrNoiseMatrixG12 = cms.vdouble(
                    1.0, 0.71073, 0.55721, 0.46089, 0.40449,
                    0.35931, 0.33924, 0.32439, 0.31581, 0.30481
                ),
                EBPulseShapeCovariance = cms.vdouble(
                    3.001e-06, 1.233e-05, 0.0, -4.416e-06, -4.571e-06,
                    -3.614e-06, -2.636e-06, -1.286e-06, -8.41e-07, -5.296e-07,
                    0.0, 0.0, 1.233e-05, 6.154e-05, 0.0,
                    -2.2e-05, -2.309e-05, -1.838e-05, -1.373e-05, -7.334e-06,
                    -5.088e-06, -3.745e-06, -2.428e-06, 0.0, 0.0,
                    0.0, 0.0, 0.0, 0.0, 0.0,
                    0.0, 0.0, 0.0, 0.0, 0.0,
                    0.0, -4.416e-06, -2.2e-05, 0.0, 8.319e-06,
                    8.545e-06, 6.792e-06, 5.059e-06, 2.678e-06, 1.816e-06,
                    1.223e-06, 8.245e-07, 5.589e-07, -4.571e-06, -2.309e-05,
                    0.0, 8.545e-06, 9.182e-06, 7.219e-06, 5.388e-06,
                    2.853e-06, 1.944e-06, 1.324e-06, 9.083e-07, 6.335e-07,
                    -3.614e-06, -1.838e-05, 0.0, 6.792e-06, 7.219e-06,
                    6.016e-06, 4.437e-06, 2.385e-06, 1.636e-06, 1.118e-06,
                    7.754e-07, 5.556e-07, -2.636e-06, -1.373e-05, 0.0,
                    5.059e-06, 5.388e-06, 4.437e-06, 3.602e-06, 1.917e-06,
                    1.322e-06, 9.079e-07, 6.529e-07, 4.752e-07, -1.286e-06,
                    -7.334e-06, 0.0, 2.678e-06, 2.853e-06, 2.385e-06,
                    1.917e-06, 1.375e-06, 9.1e-07, 6.455e-07, 4.693e-07,
                    3.657e-07, -8.41e-07, -5.088e-06, 0.0, 1.816e-06,
                    1.944e-06, 1.636e-06, 1.322e-06, 9.1e-07, 9.115e-07,
                    6.062e-07, 4.436e-07, 3.422e-07, -5.296e-07, -3.745e-06,
                    0.0, 1.223e-06, 1.324e-06, 1.118e-06, 9.079e-07,
                    6.455e-07, 6.062e-07, 7.217e-07, 4.862e-07, 3.768e-07,
                    0.0, -2.428e-06, 0.0, 8.245e-07, 9.083e-07,
                    7.754e-07, 6.529e-07, 4.693e-07, 4.436e-07, 4.862e-07,
                    6.509e-07, 4.418e-07, 0.0, 0.0, 0.0,
                    5.589e-07, 6.335e-07, 5.556e-07, 4.752e-07, 3.657e-07,
                    3.422e-07, 3.768e-07, 4.418e-07, 6.142e-07
                ),
                EBPulseShapeTemplate = cms.vdouble(
                    0.0113979, 0.758151, 1.0, 0.887744, 0.673548,
                    0.474332, 0.319561, 0.215144, 0.147464, 0.101087,
                    0.0693181, 0.0475044
                ),
                EBdigiCollection = cms.string(''),
                EECorrNoiseMatrixG01 = cms.vdouble(
                    1.0, 0.72698, 0.62048, 0.55691, 0.51848,
                    0.49147, 0.47813, 0.47007, 0.46621, 0.46265
                ),
                EECorrNoiseMatrixG06 = cms.vdouble(
                    1.0, 0.71217, 0.47464, 0.34056, 0.26282,
                    0.20287, 0.17734, 0.16256, 0.15618, 0.14443
                ),
                EECorrNoiseMatrixG12 = cms.vdouble(
                    1.0, 0.71373, 0.44825, 0.30152, 0.21609,
                    0.14786, 0.11772, 0.10165, 0.09465, 0.08098
                ),
                EEPulseShapeCovariance = cms.vdouble(
                    3.941e-05, 3.333e-05, 0.0, -1.449e-05, -1.661e-05,
                    -1.424e-05, -1.183e-05, -6.842e-06, -4.915e-06, -3.411e-06,
                    0.0, 0.0, 3.333e-05, 2.862e-05, 0.0,
                    -1.244e-05, -1.431e-05, -1.233e-05, -1.032e-05, -5.883e-06,
                    -4.154e-06, -2.902e-06, -2.128e-06, 0.0, 0.0,
                    0.0, 0.0, 0.0, 0.0, 0.0,
                    0.0, 0.0, 0.0, 0.0, 0.0,
                    0.0, -1.449e-05, -1.244e-05, 0.0, 5.84e-06,
                    6.649e-06, 5.72e-06, 4.812e-06, 2.708e-06, 1.869e-06,
                    1.33e-06, 9.186e-07, 6.446e-07, -1.661e-05, -1.431e-05,
                    0.0, 6.649e-06, 7.966e-06, 6.898e-06, 5.794e-06,
                    3.157e-06, 2.184e-06, 1.567e-06, 1.084e-06, 7.575e-07,
                    -1.424e-05, -1.233e-05, 0.0, 5.72e-06, 6.898e-06,
                    6.341e-06, 5.347e-06, 2.859e-06, 1.991e-06, 1.431e-06,
                    9.839e-07, 6.886e-07, -1.183e-05, -1.032e-05, 0.0,
                    4.812e-06, 5.794e-06, 5.347e-06, 4.854e-06, 2.628e-06,
                    1.809e-06, 1.289e-06, 9.02e-07, 6.146e-07, -6.842e-06,
                    -5.883e-06, 0.0, 2.708e-06, 3.157e-06, 2.859e-06,
                    2.628e-06, 1.863e-06, 1.296e-06, 8.882e-07, 6.108e-07,
                    4.283e-07, -4.915e-06, -4.154e-06, 0.0, 1.869e-06,
                    2.184e-06, 1.991e-06, 1.809e-06, 1.296e-06, 1.217e-06,
                    8.669e-07, 5.751e-07, 3.882e-07, -3.411e-06, -2.902e-06,
                    0.0, 1.33e-06, 1.567e-06, 1.431e-06, 1.289e-06,
                    8.882e-07, 8.669e-07, 9.522e-07, 6.717e-07, 4.293e-07,
                    0.0, -2.128e-06, 0.0, 9.186e-07, 1.084e-06,
                    9.839e-07, 9.02e-07, 6.108e-07, 5.751e-07, 6.717e-07,
                    7.911e-07, 5.493e-07, 0.0, 0.0, 0.0,
                    6.446e-07, 7.575e-07, 6.886e-07, 6.146e-07, 4.283e-07,
                    3.882e-07, 4.293e-07, 5.493e-07, 7.027e-07
                ),
                EEPulseShapeTemplate = cms.vdouble(
                    0.116442, 0.756246, 1.0, 0.897182, 0.686831,
                    0.491506, 0.344111, 0.245731, 0.174115, 0.123361,
                    0.0874288, 0.061957
                ),
                EEdigiCollection = cms.string(''),
                ESdigiCollection = cms.string(''),
                EcalPreMixStage1 = cms.bool(False),
                EcalPreMixStage2 = cms.bool(False),
                UseLCcorrection = cms.untracked.bool(True)
            ),
            activeBXs = cms.vint32(
                -5, -4, -3, -2, -1,
                0, 1, 2, 3, 4
            ),
            addPedestalUncertaintyEB = cms.double(0.0),
            addPedestalUncertaintyEE = cms.double(0.0),
            ampErrorCalculation = cms.bool(False),
            amplitudeThresholdEB = cms.double(10.0),
            amplitudeThresholdEE = cms.double(10.0),
            chi2ThreshEB_ = cms.double(65.0),
            chi2ThreshEE_ = cms.double(50.0),
            doPrefitEB = cms.bool(False),
            doPrefitEE = cms.bool(False),
            dynamicPedestalsEB = cms.bool(False),
            dynamicPedestalsEE = cms.bool(False),
            ebPulseShape = cms.vdouble(
                5.2e-05, -5.26e-05, 6.66e-05, 0.1168, 0.7575,
                1.0, 0.8876, 0.6732, 0.4741, 0.3194
            ),
            ebSpikeThreshold = cms.double(1.042),
            eePulseShape = cms.vdouble(
                5.2e-05, -5.26e-05, 6.66e-05, 0.1168, 0.7575,
                1.0, 0.8876, 0.6732, 0.4741, 0.3194
            ),
            gainSwitchUseMaxSampleEB = cms.bool(True),
            gainSwitchUseMaxSampleEE = cms.bool(False),
            kPoorRecoFlagEB = cms.bool(True),
            kPoorRecoFlagEE = cms.bool(False),
            mitigateBadSamplesEB = cms.bool(False),
            mitigateBadSamplesEE = cms.bool(False),
            outOfTimeThresholdGain12mEB = cms.double(5.0),
            outOfTimeThresholdGain12mEE = cms.double(1000.0),
            outOfTimeThresholdGain12pEB = cms.double(5.0),
            outOfTimeThresholdGain12pEE = cms.double(1000.0),
            outOfTimeThresholdGain61mEB = cms.double(5.0),
            outOfTimeThresholdGain61mEE = cms.double(1000.0),
            outOfTimeThresholdGain61pEB = cms.double(5.0),
            outOfTimeThresholdGain61pEE = cms.double(1000.0),
            prefitMaxChiSqEB = cms.double(25.0),
            prefitMaxChiSqEE = cms.double(10.0),
            selectiveBadSampleCriteriaEB = cms.bool(False),
            selectiveBadSampleCriteriaEE = cms.bool(False),
            simplifiedNoiseModelForGainSwitch = cms.bool(True),
            timealgo = cms.string('None'),
            useLumiInfoRunHeader = cms.bool(False)
        )
    ),
    cuda = cms.EDProducer("EcalUncalibRecHitConvertGPU2CPUFormat",
        mightGet = cms.optional.untracked.vstring,
        recHitsLabelCPUEB = cms.string('EcalUncalibRecHitsEB'),
        recHitsLabelCPUEE = cms.string('EcalUncalibRecHitsEE'),
        recHitsLabelGPUEB = cms.InputTag("hltEcalUncalibRecHitSoA","EcalUncalibRecHitsEB"),
        recHitsLabelGPUEE = cms.InputTag("hltEcalUncalibRecHitSoA","EcalUncalibRecHitsEE")
    )
)


process.hltHbhereco = SwitchProducerCUDA(
    cpu = cms.EDProducer("HBHEPhase1Reconstructor",
        algoConfigClass = cms.string(''),
        algorithm = cms.PSet(
            Class = cms.string('SimpleHBHEPhase1Algo'),
            activeBXs = cms.vint32(
                -3, -2, -1, 0, 1,
                2, 3, 4
            ),
            applyLegacyHBMCorrection = cms.bool(False),
            applyPedConstraint = cms.bool(False),
            applyPulseJitter = cms.bool(False),
            applyTimeConstraint = cms.bool(False),
            applyTimeSlew = cms.bool(True),
            applyTimeSlewM3 = cms.bool(True),
            calculateArrivalTime = cms.bool(False),
            chiSqSwitch = cms.double(-1.0),
            correctForPhaseContainment = cms.bool(True),
            correctionPhaseNS = cms.double(6.0),
            deltaChiSqThresh = cms.double(0.001),
            dynamicPed = cms.bool(False),
            firstSampleShift = cms.int32(0),
            fitTimes = cms.int32(1),
            meanPed = cms.double(0.0),
            meanTime = cms.double(0.0),
            nMaxItersMin = cms.int32(50),
            nMaxItersNNLS = cms.int32(500),
            nnlsThresh = cms.double(1e-11),
            pulseJitter = cms.double(1.0),
            respCorrM3 = cms.double(1.0),
            samplesToAdd = cms.int32(2),
            tdcTimeShift = cms.double(0.0),
            timeMax = cms.double(12.5),
            timeMin = cms.double(-12.5),
            timeSigmaHPD = cms.double(5.0),
            timeSigmaSiPM = cms.double(2.5),
            timeSlewParsType = cms.int32(3),
            ts4Max = cms.vdouble(100.0, 20000.0, 30000.0),
            ts4Min = cms.double(0.0),
            ts4Thresh = cms.double(0.0),
            ts4chi2 = cms.vdouble(15.0, 15.0),
            useM2 = cms.bool(False),
            useM3 = cms.bool(False),
            useMahi = cms.bool(True)
        ),
        digiLabelQIE11 = cms.InputTag("hltHcalDigis"),
        digiLabelQIE8 = cms.InputTag("hltHcalDigis"),
        dropZSmarkedPassed = cms.bool(True),
        flagParametersQIE11 = cms.PSet(

        ),
        flagParametersQIE8 = cms.PSet(
            hitEnergyMinimum = cms.double(1.0),
            hitMultiplicityThreshold = cms.int32(17),
            nominalPedestal = cms.double(3.0),
            pulseShapeParameterSets = cms.VPSet(
                cms.PSet(
                    pulseShapeParameters = cms.vdouble(
                        0.0, 100.0, -50.0, 0.0, -15.0,
                        0.15
                    )
                ),
                cms.PSet(
                    pulseShapeParameters = cms.vdouble(
                        100.0, 2000.0, -50.0, 0.0, -5.0,
                        0.05
                    )
                ),
                cms.PSet(
                    pulseShapeParameters = cms.vdouble(
                        2000.0, 1000000.0, -50.0, 0.0, 95.0,
                        0.0
                    )
                ),
                cms.PSet(
                    pulseShapeParameters = cms.vdouble(
                        -1000000.0, 1000000.0, 45.0, 0.1, 1000000.0,
                        0.0
                    )
                )
            )
        ),
        makeRecHits = cms.bool(True),
        processQIE11 = cms.bool(True),
        processQIE8 = cms.bool(False),
        pulseShapeParametersQIE11 = cms.PSet(

        ),
        pulseShapeParametersQIE8 = cms.PSet(
            LeftSlopeCut = cms.vdouble(5.0, 2.55, 2.55),
            LeftSlopeThreshold = cms.vdouble(250.0, 500.0, 100000.0),
            LinearCut = cms.vdouble(-3.0, -0.054, -0.054),
            LinearThreshold = cms.vdouble(20.0, 100.0, 100000.0),
            MinimumChargeThreshold = cms.double(20.0),
            MinimumTS4TS5Threshold = cms.double(100.0),
            R45MinusOneRange = cms.double(0.2),
            R45PlusOneRange = cms.double(0.2),
            RMS8MaxCut = cms.vdouble(-13.5, -11.5, -11.5),
            RMS8MaxThreshold = cms.vdouble(20.0, 100.0, 100000.0),
            RightSlopeCut = cms.vdouble(5.0, 4.15, 4.15),
            RightSlopeSmallCut = cms.vdouble(1.08, 1.16, 1.16),
            RightSlopeSmallThreshold = cms.vdouble(150.0, 200.0, 100000.0),
            RightSlopeThreshold = cms.vdouble(250.0, 400.0, 100000.0),
            TS3TS4ChargeThreshold = cms.double(70.0),
            TS3TS4UpperChargeThreshold = cms.double(20.0),
            TS4TS5ChargeThreshold = cms.double(70.0),
            TS4TS5LowerCut = cms.vdouble(
                -1.0, -0.7, -0.5, -0.4, -0.3,
                0.1
            ),
            TS4TS5LowerThreshold = cms.vdouble(
                100.0, 120.0, 160.0, 200.0, 300.0,
                500.0
            ),
            TS4TS5UpperCut = cms.vdouble(1.0, 0.8, 0.75, 0.72),
            TS4TS5UpperThreshold = cms.vdouble(70.0, 90.0, 100.0, 400.0),
            TS5TS6ChargeThreshold = cms.double(70.0),
            TS5TS6UpperChargeThreshold = cms.double(20.0),
            TriangleIgnoreSlow = cms.bool(False),
            TrianglePeakTS = cms.uint32(10000),
            UseDualFit = cms.bool(True)
        ),
        recoParamsFromDB = cms.bool(True),
        saveDroppedInfos = cms.bool(False),
        saveEffectivePedestal = cms.bool(True),
        saveInfos = cms.bool(False),
        setLegacyFlagsQIE11 = cms.bool(False),
        setLegacyFlagsQIE8 = cms.bool(False),
        setNegativeFlagsQIE11 = cms.bool(False),
        setNegativeFlagsQIE8 = cms.bool(False),
        setNoiseFlagsQIE11 = cms.bool(False),
        setNoiseFlagsQIE8 = cms.bool(False),
        setPulseShapeFlagsQIE11 = cms.bool(False),
        setPulseShapeFlagsQIE8 = cms.bool(False),
        sipmQNTStoSum = cms.int32(3),
        sipmQTSShift = cms.int32(0),
        tsFromDB = cms.bool(False),
        use8ts = cms.bool(True)
    ),
    cuda = cms.EDAlias(
        hltHbherecoFromGPU = cms.VPSet(cms.PSet(
            type = cms.string('HBHERecHitsSorted')
        ))
    )
)


process.hltPixelTracksSoA = SwitchProducerCUDA(
    cpu = cms.EDProducer("CAHitNtupletCUDA",
        CAThetaCutBarrel = cms.double(0.0020000000949949026),
        CAThetaCutForward = cms.double(0.003000000026077032),
        dcaCutInnerTriplet = cms.double(0.15000000596046448),
        dcaCutOuterTriplet = cms.double(0.25),
        doClusterCut = cms.bool(True),
        doPtCut = cms.bool(True),
        doSharedHitCut = cms.bool(True),
        doZ0Cut = cms.bool(True),
        dupPassThrough = cms.bool(False),
        earlyFishbone = cms.bool(True),
        fillStatistics = cms.bool(True),
        fit5as4 = cms.bool(True),
        hardCurvCut = cms.double(0.03284072249589491),
        idealConditions = cms.bool(False),
        includeJumpingForwardDoublets = cms.bool(True),
        lateFishbone = cms.bool(False),
        maxNumberOfDoublets = cms.uint32(524288),
        mightGet = cms.optional.untracked.vstring,
        minHitsForSharingCut = cms.uint32(5),
        minHitsPerNtuplet = cms.uint32(3),
        onGPU = cms.bool(False),
        pixelRecHitSrc = cms.InputTag("hltSiPixelRecHitSoA"),
        ptmin = cms.double(0.8999999761581421),
        trackQualityCuts = cms.PSet(
            chi2Coeff = cms.vdouble(0.9, 1.8),
            chi2MaxPt = cms.double(10),
            chi2Scale = cms.double(8),
            quadrupletMaxTip = cms.double(0.5),
            quadrupletMaxZip = cms.double(12),
            quadrupletMinPt = cms.double(0.3),
            tripletMaxTip = cms.double(0.3),
            tripletMaxZip = cms.double(12),
            tripletMinPt = cms.double(0.5)
        ),
        useRiemannFit = cms.bool(False),
        useSimpleTripletCleaner = cms.bool(False)
    ),
    cuda = cms.EDProducer("PixelTrackSoAFromCUDA",
        mightGet = cms.optional.untracked.vstring,
        src = cms.InputTag("hltPixelTracksCUDA")
    )
)


process.hltPixelVerticesSoA = SwitchProducerCUDA(
    cpu = cms.EDProducer("PixelVertexProducerCUDA",
        PtMin = cms.double(0.5),
        chi2max = cms.double(9),
        eps = cms.double(0.07),
        errmax = cms.double(0.01),
        mightGet = cms.optional.untracked.vstring,
        minT = cms.int32(2),
        onGPU = cms.bool(False),
        oneKernel = cms.bool(True),
        pixelTrackSrc = cms.InputTag("hltPixelTracksSoA"),
        useDBSCAN = cms.bool(False),
        useDensity = cms.bool(True),
        useIterative = cms.bool(False)
    ),
    cuda = cms.EDProducer("PixelVertexSoAFromCUDA",
        mightGet = cms.optional.untracked.vstring,
        src = cms.InputTag("hltPixelVerticesCUDA")
    )
)


process.hltSiPixelClusters = SwitchProducerCUDA(
    cpu = cms.EDAlias(
        hltSiPixelClustersLegacy = cms.VPSet(cms.PSet(
            type = cms.string('SiPixelClusteredmNewDetSetVector')
        ))
    ),
    cuda = cms.EDProducer("SiPixelDigisClustersFromSoA",
        clusterThreshold_layer1 = cms.int32(2000),
        clusterThreshold_otherLayers = cms.int32(4000),
        mightGet = cms.optional.untracked.vstring,
        produceDigis = cms.bool(False),
        src = cms.InputTag("hltSiPixelDigisSoA"),
        storeDigis = cms.bool(False)
    )
)


process.hltSiPixelDigis = SwitchProducerCUDA(
    cpu = cms.EDAlias(
        hltSiPixelDigisLegacy = cms.VPSet(
            cms.PSet(
                type = cms.string('DetIdedmEDCollection')
            ),
            cms.PSet(
                type = cms.string('SiPixelRawDataErroredmDetSetVector')
            ),
            cms.PSet(
                type = cms.string('PixelFEDChanneledmNewDetSetVector')
            )
        )
    ),
    cuda = cms.EDProducer("SiPixelDigiErrorsFromSoA",
        CablingMapLabel = cms.string(''),
        ErrorList = cms.vint32(29),
        UsePhase1 = cms.bool(True),
        UserErrorList = cms.vint32(40),
        digiErrorSoASrc = cms.InputTag("hltSiPixelDigiErrorsSoA"),
        mightGet = cms.optional.untracked.vstring
    )
)


process.hltSiPixelRecHits = SwitchProducerCUDA(
    cpu = cms.EDProducer("SiPixelRecHitConverter",
        CPE = cms.string('hltESPPixelCPEGeneric'),
        VerboseLevel = cms.untracked.int32(0),
        src = cms.InputTag("hltSiPixelClusters")
    ),
    cuda = cms.EDProducer("SiPixelRecHitFromCUDA",
        mightGet = cms.optional.untracked.vstring,
        pixelRecHitSrc = cms.InputTag("hltSiPixelRecHitsCUDA"),
        src = cms.InputTag("hltSiPixelClusters")
    )
)


process.statusOnGPU = SwitchProducerCUDA(
    cpu = cms.EDProducer("BooleanProducer",
        value = cms.bool(False)
    ),
    cuda = cms.EDProducer("BooleanProducer",
        value = cms.bool(True)
    )
)


process.hltAK4CaloJetsPFEt5 = cms.EDFilter("EtMinCaloJetSelector",
    etMin = cms.double(5.0),
    filter = cms.bool(False),
    src = cms.InputTag("hltAK4CaloJetsPF")
)


process.hltBoolEnd = cms.EDFilter("HLTBool",
    result = cms.bool(True)
)


process.hltBoolFalse = cms.EDFilter("HLTBool",
    result = cms.bool(False)
)


process.hltEG5L1SingleEGOrEtFilter = cms.EDFilter("HLTEgammaEtFilter",
    etcutEB = cms.double(5.0),
    etcutEE = cms.double(5.0),
    inputTag = cms.InputTag("hltEGL1SingleEGOrFilter"),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    ncandcut = cms.int32(1),
    saveTags = cms.bool(True)
)


process.hltEGL1SingleEGOrFilter = cms.EDFilter("HLTEgammaL1TMatchFilterRegional",
    L1SeedFilterTag = cms.InputTag("hltL1sSingleEGor"),
    barrel_end = cms.double(1.4791),
    candIsolatedTag = cms.InputTag("hltEgammaCandidates"),
    candNonIsolatedTag = cms.InputTag(""),
    doIsolated = cms.bool(False),
    endcap_end = cms.double(2.65),
    l1CenJetsTag = cms.InputTag("hltGtStage2Digis","Jet"),
    l1IsolatedTag = cms.InputTag("hltGtStage2Digis","EGamma"),
    l1NonIsolatedTag = cms.InputTag("hltGtStage2Digis","EGamma"),
    l1TausTag = cms.InputTag("hltGtStage2Digis","Tau"),
    ncandcut = cms.int32(1),
    region_eta_size = cms.double(0.522),
    region_eta_size_ecap = cms.double(1.0),
    region_phi_size = cms.double(1.044),
    saveTags = cms.bool(True)
)


process.hltEgammaTriggerFilterObjectWrapper = cms.EDFilter("HLTEgammaTriggerFilterObjectWrapper",
    candIsolatedTag = cms.InputTag("hltEgammaCandidates"),
    candNonIsolatedTag = cms.InputTag("hltEgammaCandidates"),
    doIsolated = cms.bool(False),
    saveTags = cms.bool(True)
)


process.hltEle5DphiFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEgammaTriggerFilterObjectWrapper"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(10.0),
    thrRegularEE = cms.vdouble(10.0),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","Dphi")
)


process.hltEle5WPTightClusterShapeFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEG5L1SingleEGOrEtFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.011),
    thrRegularEE = cms.vdouble(0.0305),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaClusterShape","sigmaIEtaIEta5x5")
)


process.hltEle5WPTightEcalIsoFilter = cms.EDFilter("HLTEgammaGenericQuadraticEtaFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.0, 1.479, 2.1),
    candTag = cms.InputTag("hltEle5WPTightHEFilter"),
    doRhoCorrection = cms.bool(True),
    effectiveAreas = cms.vdouble(0.2, 0.2, 0.25, 0.3),
    energyLowEdges = cms.vdouble(0.0),
    etaBoundaryEB12 = cms.double(1.0),
    etaBoundaryEE12 = cms.double(2.1),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
    saveTags = cms.bool(True),
    thrOverE2EB1 = cms.vdouble(0.0),
    thrOverE2EB2 = cms.vdouble(0.0),
    thrOverE2EE1 = cms.vdouble(0.0),
    thrOverE2EE2 = cms.vdouble(0.0),
    thrOverEEB1 = cms.vdouble(0.03),
    thrOverEEB2 = cms.vdouble(0.03),
    thrOverEEE1 = cms.vdouble(0.025),
    thrOverEEE2 = cms.vdouble(0.025),
    thrRegularEB1 = cms.vdouble(1.75),
    thrRegularEB2 = cms.vdouble(1.75),
    thrRegularEE1 = cms.vdouble(1.0),
    thrRegularEE2 = cms.vdouble(2.0),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaEcalPFClusterIso")
)


process.hltEle5WPTightGsfDetaFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle5WPTightGsfMissingHitsFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.004),
    thrRegularEE = cms.vdouble(0.005),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","DetaSeed")
)


process.hltEle5WPTightGsfDphiFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle5WPTightGsfDetaFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.02),
    thrRegularEE = cms.vdouble(0.023),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","Dphi")
)


process.hltEle5WPTightGsfMissingHitsFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle5WPTightGsfOneOEMinusOneOPFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(999.0),
    thrRegularEE = cms.vdouble(1.0),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","MissingHits")
)


process.hltEle5WPTightGsfOneOEMinusOneOPFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle5WPTightPMS2Filter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.012),
    thrRegularEE = cms.vdouble(0.011),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","OneOESuperMinusOneOP")
)


process.hltEle5WPTightGsfTrackIsoFilter = cms.EDFilter("HLTEgammaGenericQuadraticEtaFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.0, 1.479, 2.1),
    candTag = cms.InputTag("hltEle5DphiFilter"),
    doRhoCorrection = cms.bool(True),
    effectiveAreas = cms.vdouble(0.029, 0.111, 0.114, 0.032),
    energyLowEdges = cms.vdouble(0.0),
    etaBoundaryEB12 = cms.double(1.0),
    etaBoundaryEE12 = cms.double(2.1),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
    saveTags = cms.bool(True),
    thrOverE2EB1 = cms.vdouble(0.0),
    thrOverE2EB2 = cms.vdouble(0.0),
    thrOverE2EE1 = cms.vdouble(0.0),
    thrOverE2EE2 = cms.vdouble(0.0),
    thrOverEEB1 = cms.vdouble(0.03),
    thrOverEEB2 = cms.vdouble(0.03),
    thrOverEEE1 = cms.vdouble(0.025),
    thrOverEEE2 = cms.vdouble(0.025),
    thrRegularEB1 = cms.vdouble(0.838),
    thrRegularEB2 = cms.vdouble(-0.385),
    thrRegularEE1 = cms.vdouble(-0.363),
    thrRegularEE2 = cms.vdouble(0.702),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaEleGsfTrackIso")
)


process.hltEle5WPTightHEFilter = cms.EDFilter("HLTEgammaGenericQuadraticEtaFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.0, 1.479, 2.1),
    candTag = cms.InputTag("hltEle5WPTightClusterShapeFilter"),
    doRhoCorrection = cms.bool(True),
    effectiveAreas = cms.vdouble(0.1, 0.1, 0.3, 0.5),
    energyLowEdges = cms.vdouble(0.0),
    etaBoundaryEB12 = cms.double(1.0),
    etaBoundaryEE12 = cms.double(2.1),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
    saveTags = cms.bool(True),
    thrOverE2EB1 = cms.vdouble(0.0),
    thrOverE2EB2 = cms.vdouble(0.0),
    thrOverE2EE1 = cms.vdouble(0.0),
    thrOverE2EE2 = cms.vdouble(0.0),
    thrOverEEB1 = cms.vdouble(0.03),
    thrOverEEB2 = cms.vdouble(0.03),
    thrOverEEE1 = cms.vdouble(0.03),
    thrOverEEE2 = cms.vdouble(0.03),
    thrRegularEB1 = cms.vdouble(0.75),
    thrRegularEB2 = cms.vdouble(2.25),
    thrRegularEE1 = cms.vdouble(3.0),
    thrRegularEE2 = cms.vdouble(5.0),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaHoverE")
)


process.hltEle5WPTightHcalIsoFilter = cms.EDFilter("HLTEgammaGenericQuadraticEtaFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.0, 1.479, 2.0),
    candTag = cms.InputTag("hltEle5WPTightEcalIsoFilter"),
    doRhoCorrection = cms.bool(True),
    effectiveAreas = cms.vdouble(0.2, 0.2, 0.4, 0.5),
    energyLowEdges = cms.vdouble(0.0),
    etaBoundaryEB12 = cms.double(1.0),
    etaBoundaryEE12 = cms.double(2.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
    saveTags = cms.bool(True),
    thrOverE2EB1 = cms.vdouble(0.0),
    thrOverE2EB2 = cms.vdouble(0.0),
    thrOverE2EE1 = cms.vdouble(0.0),
    thrOverE2EE2 = cms.vdouble(0.0),
    thrOverEEB1 = cms.vdouble(0.03),
    thrOverEEB2 = cms.vdouble(0.03),
    thrOverEEE1 = cms.vdouble(0.03),
    thrOverEEE2 = cms.vdouble(0.03),
    thrRegularEB1 = cms.vdouble(2.5),
    thrRegularEB2 = cms.vdouble(3.0),
    thrRegularEE1 = cms.vdouble(1.0),
    thrRegularEE2 = cms.vdouble(2.0),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaHcalPFClusterIso")
)


process.hltEle5WPTightPMS2Filter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle5WPTightPixelMatchFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(70.0),
    thrRegularEE = cms.vdouble(45.0),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaPixelMatchVars","s2")
)


process.hltEle5WPTightPixelMatchFilter = cms.EDFilter("HLTElectronPixelMatchFilter",
    candTag = cms.InputTag("hltEle5WPTightHcalIsoFilter"),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    l1PixelSeedsTag = cms.InputTag("hltEgammaElectronPixelSeeds"),
    ncandcut = cms.int32(1),
    npixelmatchcut = cms.double(1.0),
    pixelVeto = cms.bool(False),
    s2_threshold = cms.double(0.4),
    s_a_phi1B = cms.double(0.0069),
    s_a_phi1F = cms.double(0.0076),
    s_a_phi1I = cms.double(0.0088),
    s_a_phi2B = cms.double(0.00037),
    s_a_phi2F = cms.double(0.00906),
    s_a_phi2I = cms.double(0.0007),
    s_a_rF = cms.double(0.04),
    s_a_rI = cms.double(0.027),
    s_a_zB = cms.double(0.012),
    saveTags = cms.bool(True),
    tanhSO10BarrelThres = cms.double(0.35),
    tanhSO10ForwardThres = cms.double(1.0),
    tanhSO10InterThres = cms.double(1.0),
    useS = cms.bool(False)
)


process.hltL1sSingleEGor = cms.EDFilter("HLTL1TSeed",
    L1EGammaInputTag = cms.InputTag("hltGtStage2Digis","EGamma"),
    L1EtSumInputTag = cms.InputTag("hltGtStage2Digis","EtSum"),
    L1GlobalInputTag = cms.InputTag("hltGtStage2Digis"),
    L1JetInputTag = cms.InputTag("hltGtStage2Digis","Jet"),
    L1MuonInputTag = cms.InputTag("hltGtStage2Digis","Muon"),
    L1ObjectMapInputTag = cms.InputTag("hltGtStage2ObjectMap"),
    L1SeedsLogicalExpression = cms.string('L1_SingleLooseIsoEG26er2p5 OR L1_SingleLooseIsoEG26er1p5 OR L1_SingleLooseIsoEG28er2p5 OR L1_SingleLooseIsoEG28er2p1 OR L1_SingleLooseIsoEG28er1p5 OR L1_SingleLooseIsoEG30er2p5 OR L1_SingleLooseIsoEG30er1p5 OR L1_SingleEG26er2p5 OR L1_SingleEG38er2p5 OR L1_SingleEG40er2p5 OR L1_SingleEG42er2p5 OR L1_SingleEG45er2p5 OR L1_SingleEG60 OR L1_SingleEG34er2p5 OR L1_SingleEG36er2p5 OR L1_SingleIsoEG24er2p1 OR L1_SingleIsoEG26er2p1 OR L1_SingleIsoEG28er2p1 OR L1_SingleIsoEG30er2p1 OR L1_SingleIsoEG32er2p1 OR L1_SingleIsoEG26er2p5 OR L1_SingleIsoEG28er2p5 OR L1_SingleIsoEG30er2p5 OR L1_SingleIsoEG32er2p5 OR L1_SingleIsoEG34er2p5'),
    L1TauInputTag = cms.InputTag("hltGtStage2Digis","Tau"),
    saveTags = cms.bool(True)
)


process.hltPreEle32WPTightGsf = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtStage2Digis"),
    offset = cms.uint32(0)
)


process.hltTriggerType = cms.EDFilter("HLTTriggerTypeFilter",
    SelectedTriggerType = cms.int32(1)
)


process.statusOnGPUFilter = cms.EDFilter("BooleanFilter",
    src = cms.InputTag("statusOnGPU")
)


process.hltGetRaw = cms.EDAnalyzer("HLTGetRaw",
    RawDataCollection = cms.InputTag("rawDataCollector")
)


process.egOutMod = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('output.root'),
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep *_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep recoRecoEcalCandidates*_*_*_*',
        'keep recoSuperClusters_*_*_*',
        'keep recoCaloClusters_*_*_*',
        'keep *_genParticles_*_*',
        'keep *_addPileupInfo_*_*',
        'keep *_externalLHEProducer_*_*',
        'keep *_generator_*_*',
        'keep *_hltEgammaGsfTracks*_*_*',
        'keep recoElectronSeeds_*_*_*',
        'keep *_hltEgammaHLTExtra_*_*',
        'keep *_hltNrInputEvents_*_*',
        'keep *_hltGtStage2Digis_*_*'
    )
)


process.CUDAService = cms.Service("CUDAService",
    allocator = cms.untracked.PSet(
        devicePreallocate = cms.untracked.vuint32(),
        hostPreallocate = cms.untracked.vuint32()
    ),
    enabled = cms.untracked.bool(True),
    limits = cms.untracked.PSet(
        cudaLimitDevRuntimePendingLaunchCount = cms.untracked.int32(-1),
        cudaLimitDevRuntimeSyncDepth = cms.untracked.int32(-1),
        cudaLimitMallocHeapSize = cms.untracked.int32(-1),
        cudaLimitPrintfFifoSize = cms.untracked.int32(-1),
        cudaLimitStackSize = cms.untracked.int32(-1)
    ),
    verbose = cms.untracked.bool(False)
)


process.DQMStore = cms.Service("DQMStore",
    MEsToSave = cms.untracked.vstring(
        'Muons/MuonRecoAnalyzer/',
        'Muons/MuonIdDQM/GlobalMuons/hDT1Pullx'
    ),
    assertLegacySafe = cms.untracked.bool(False),
    enableMultiThread = cms.untracked.bool(True),
    saveByLumi = cms.untracked.bool(False),
    trackME = cms.untracked.string(''),
    verbose = cms.untracked.int32(0)
)


process.FastTimerService = cms.Service("FastTimerService",
    dqmLumiSectionsRange = cms.untracked.uint32(2500),
    dqmMemoryRange = cms.untracked.double(1000000.0),
    dqmMemoryResolution = cms.untracked.double(5000.0),
    dqmModuleMemoryRange = cms.untracked.double(100000.0),
    dqmModuleMemoryResolution = cms.untracked.double(500.0),
    dqmModuleTimeRange = cms.untracked.double(40.0),
    dqmModuleTimeResolution = cms.untracked.double(0.2),
    dqmPath = cms.untracked.string('HLT/TimerService'),
    dqmPathMemoryRange = cms.untracked.double(1000000.0),
    dqmPathMemoryResolution = cms.untracked.double(5000.0),
    dqmPathTimeRange = cms.untracked.double(100.0),
    dqmPathTimeResolution = cms.untracked.double(0.5),
    dqmTimeRange = cms.untracked.double(2000.0),
    dqmTimeResolution = cms.untracked.double(5.0),
    enableDQM = cms.untracked.bool(True),
    enableDQMTransitions = cms.untracked.bool(False),
    enableDQMbyLumiSection = cms.untracked.bool(True),
    enableDQMbyModule = cms.untracked.bool(False),
    enableDQMbyPath = cms.untracked.bool(False),
    enableDQMbyProcesses = cms.untracked.bool(True),
    jsonFileName = cms.untracked.string('resources.json'),
    printEventSummary = cms.untracked.bool(False),
    printJobSummary = cms.untracked.bool(True),
    printRunSummary = cms.untracked.bool(True),
    writeJSONSummary = cms.untracked.bool(False)
)


process.MessageLogger = cms.Service("MessageLogger",
    CUDAService = cms.untracked.PSet(

    ),
    FastReport = cms.untracked.PSet(

    ),
    HLTrigReport = cms.untracked.PSet(

    ),
    L1GtTrigReport = cms.untracked.PSet(

    ),
    L1TGlobalSummary = cms.untracked.PSet(

    ),
    ThroughputService = cms.untracked.PSet(

    ),
    TriggerSummaryProducerAOD = cms.untracked.PSet(

    ),
    cerr = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            reportEvery = cms.untracked.int32(1)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        noTimeStamps = cms.untracked.bool(False),
        threshold = cms.untracked.string('INFO')
    ),
    debugModules = cms.untracked.vstring(),
    suppressDebug = cms.untracked.vstring(),
    suppressError = cms.untracked.vstring(
        'hltOnlineBeamSpot',
        'hltL3MuonCandidates',
        'hltL3TkTracksFromL2OIState',
        'hltPFJetCtfWithMaterialTracks',
        'hltL3TkTracksFromL2IOHit',
        'hltL3TkTracksFromL2OIHit'
    ),
    suppressFwkInfo = cms.untracked.vstring(),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring(
        'hltOnlineBeamSpot',
        'hltCtf3HitL1SeededWithMaterialTracks',
        'hltL3MuonsOIState',
        'hltPixelTracksForHighMult',
        'hltHITPixelTracksHE',
        'hltHITPixelTracksHB',
        'hltCtfL1SeededWithMaterialTracks',
        'hltRegionalTracksForL3MuonIsolation',
        'hltSiPixelClusters',
        'hltActivityStartUpElectronPixelSeeds',
        'hltLightPFTracks',
        'hltPixelVertices3DbbPhi',
        'hltL3MuonsIOHit',
        'hltPixelTracks',
        'hltSiPixelDigis',
        'hltL3MuonsOIHit',
        'hltL1SeededElectronGsfTracks',
        'hltL1SeededStartUpElectronPixelSeeds',
        'hltBLifetimeRegionalCtfWithMaterialTracksbbPhiL1FastJetFastPV',
        'hltCtfActivityWithMaterialTracks'
    )
)


process.ThroughputService = cms.Service("ThroughputService",
    dqmPath = cms.untracked.string('HLT/Throughput'),
    dqmPathByProcesses = cms.untracked.bool(False),
    enableDQM = cms.untracked.bool(True),
    eventRange = cms.untracked.uint32(10000),
    eventResolution = cms.untracked.uint32(1),
    printEventSummary = cms.untracked.bool(False),
    timeRange = cms.untracked.double(60000.0),
    timeResolution = cms.untracked.double(5.828)
)


process.AnyDirectionAnalyticalPropagator = cms.ESProducer("AnalyticalPropagatorESProducer",
    ComponentName = cms.string('AnyDirectionAnalyticalPropagator'),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('anyDirection')
)


process.CSCChannelMapperESProducer = cms.ESProducer("CSCChannelMapperESProducer",
    AlgoName = cms.string('CSCChannelMapperPostls1')
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    debugV = cms.untracked.bool(False),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useGangedStripsInME1a = cms.bool(False),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.CSCIndexerESProducer = cms.ESProducer("CSCIndexerESProducer",
    AlgoName = cms.string('CSCIndexerPostls1')
)


process.CSCObjectMapESProducer = cms.ESProducer("CSCObjectMapESProducer",
    appendToDataLabel = cms.string('')
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring(
        'HCAL',
        'ZDC',
        'EcalBarrel',
        'EcalEndcap',
        'EcalPreshower',
        'TOWER'
    )
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerConstituentsMapBuilder = cms.ESProducer("CaloTowerConstituentsMapBuilder",
    MapAuto = cms.untracked.bool(False),
    MapFile = cms.untracked.string('Geometry/CaloTopology/data/CaloTowerEEGeometric.map.gz'),
    SkipHE = cms.untracked.bool(False),
    appendToDataLabel = cms.string('')
)


process.CaloTowerGeometryFromDBEP = cms.ESProducer("CaloTowerGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.CaloTowerTopologyEP = cms.ESProducer("CaloTowerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.CastorDbProducer = cms.ESProducer("CastorDbProducer",
    appendToDataLabel = cms.string('')
)


process.ClusterShapeHitFilterESProducer = cms.ESProducer("ClusterShapeHitFilterESProducer",
    ComponentName = cms.string('ClusterShapeHitFilter'),
    PixelShapeFile = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_noL1.par'),
    PixelShapeFileL1 = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_loose.par'),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    )
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    DDDetector = cms.ESInputTag("",""),
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    attribute = cms.string('MuStructure'),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False),
    value = cms.string('MuonBarrelDT')
)


process.DTObjectMapESProducer = cms.ESProducer("DTObjectMapESProducer",
    appendToDataLabel = cms.string('')
)


process.EcalBarrelGeometryFromDBEP = cms.ESProducer("EcalBarrelGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryFromDBEP = cms.ESProducer("EcalEndcapGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService",
    appendToDataLabel = cms.string(''),
    maxExtrapolationTimeInSec = cms.uint32(0)
)


process.EcalPreshowerGeometryFromDBEP = cms.ESProducer("EcalPreshowerGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.GlobalParameters = cms.ESProducer("StableParametersTrivialProducer",
    IfCaloEtaNumberBits = cms.uint32(4),
    IfMuEtaNumberBits = cms.uint32(6),
    NumberChips = cms.uint32(1),
    NumberConditionChips = cms.uint32(1),
    NumberL1CenJet = cms.uint32(4),
    NumberL1EGamma = cms.uint32(12),
    NumberL1ForJet = cms.uint32(4),
    NumberL1IsoEG = cms.uint32(4),
    NumberL1Jet = cms.uint32(12),
    NumberL1JetCounts = cms.uint32(12),
    NumberL1Mu = cms.uint32(4),
    NumberL1Muon = cms.uint32(8),
    NumberL1NoIsoEG = cms.uint32(4),
    NumberL1Tau = cms.uint32(12),
    NumberL1TauJet = cms.uint32(4),
    NumberPhysTriggers = cms.uint32(512),
    NumberPhysTriggersExtended = cms.uint32(64),
    NumberPsbBoards = cms.int32(7),
    NumberTechnicalTriggers = cms.uint32(64),
    OrderConditionChip = cms.vint32(1),
    OrderOfChip = cms.vint32(1),
    PinsOnChip = cms.uint32(512),
    PinsOnConditionChip = cms.uint32(512),
    TotalBxInEvent = cms.int32(5),
    UnitLength = cms.int32(8),
    WordLength = cms.int32(64),
    appendToDataLabel = cms.string('')
)


process.HcalGeometryFromDBEP = cms.ESProducer("HcalGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.HcalTopologyIdealEP = cms.ESProducer("HcalTopologyIdealEP",
    Exclude = cms.untracked.string(''),
    MergePosition = cms.untracked.bool(True),
    appendToDataLabel = cms.string('')
)


process.MaterialPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterial'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.MaterialPropagatorForHI = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialForHI'),
    Mass = cms.double(0.139),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.MaterialPropagatorParabolicMF = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialParabolicMf'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.OppositeMaterialPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialOpposite'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.OppositeMaterialPropagatorForHI = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialOppositeForHI'),
    Mass = cms.double(0.139),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.OppositeMaterialPropagatorParabolicMF = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.OppositePropagatorWithMaterialForMixedStep = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialForMixedStepOpposite'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(0.1),
    useRungeKutta = cms.bool(False)
)


process.ParametrizedMagneticFieldProducer = cms.ESProducer("AutoParametrizedMagneticFieldProducer",
    label = cms.untracked.string('ParabolicMf'),
    valueOverride = cms.int32(-1),
    version = cms.string('Parabolic')
)


process.PixelCPEFastESProducer = cms.ESProducer("PixelCPEFastESProducer",
    Alpha2Order = cms.bool(True),
    ClusterProbComputationFlag = cms.int32(0),
    ComponentName = cms.string('PixelCPEFast'),
    EdgeClusterErrorX = cms.double(50),
    EdgeClusterErrorY = cms.double(85),
    LoadTemplatesFromDB = cms.bool(True),
    MagneticFieldRecord = cms.ESInputTag("",""),
    TruncatePixelCharge = cms.bool(True),
    UseErrorsFromTemplates = cms.bool(True),
    appendToDataLabel = cms.string(''),
    doLorentzFromAlignment = cms.bool(False),
    lAOffset = cms.double(0),
    lAWidthBPix = cms.double(0),
    lAWidthFPix = cms.double(0),
    useLAFromDB = cms.bool(True),
    useLAWidthFromDB = cms.bool(True),
    xerr_barrel_l1 = cms.vdouble(0.00115, 0.0012, 0.00088),
    xerr_barrel_l1_def = cms.double(0.0103),
    xerr_barrel_ln = cms.vdouble(0.00115, 0.0012, 0.00088),
    xerr_barrel_ln_def = cms.double(0.0103),
    xerr_endcap = cms.vdouble(0.002, 0.002),
    xerr_endcap_def = cms.double(0.002),
    yerr_barrel_l1 = cms.vdouble(
        0.00375, 0.0023, 0.0025, 0.0025, 0.0023,
        0.0023, 0.0021, 0.0021, 0.0024
    ),
    yerr_barrel_l1_def = cms.double(0.0021),
    yerr_barrel_ln = cms.vdouble(
        0.00375, 0.0023, 0.0025, 0.0025, 0.0023,
        0.0023, 0.0021, 0.0021, 0.0024
    ),
    yerr_barrel_ln_def = cms.double(0.0021),
    yerr_endcap = cms.vdouble(0.0021),
    yerr_endcap_def = cms.double(0.00075)
)


process.PropagatorWithMaterialForLoopers = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialForLoopers'),
    Mass = cms.double(0.1396),
    MaxDPhi = cms.double(4.0),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.PropagatorWithMaterialForMixedStep = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialForMixedStep'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(0.1),
    useRungeKutta = cms.bool(False)
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.untracked.bool(False),
    fromDDD = cms.untracked.bool(False)
)


process.SiStripClusterizerConditionsESProducer = cms.ESProducer("SiStripClusterizerConditionsESProducer",
    Label = cms.string(''),
    QualityLabel = cms.string(''),
    appendToDataLabel = cms.string('')
)


process.SiStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    APVGain = cms.VPSet(
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGainRcd')
        ),
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGain2Rcd')
        )
    ),
    AutomaticNormalization = cms.bool(False),
    appendToDataLabel = cms.string(''),
    printDebug = cms.untracked.bool(False)
)


process.SiStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiStripDetVOffRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        )
    ),
    PrintDebugOutput = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0),
    PreFilter = cms.bool(False)
)


process.SiStripRegionConnectivity = cms.ESProducer("SiStripRegionConnectivity",
    EtaDivisions = cms.untracked.uint32(20),
    EtaMax = cms.untracked.double(2.5),
    PhiDivisions = cms.untracked.uint32(20)
)


process.SimpleSecondaryVertex3TrkComputer = cms.ESProducer("SimpleSecondaryVertexESProducer",
    minTracks = cms.uint32(3),
    minVertices = cms.uint32(1),
    unBoost = cms.bool(False),
    use3d = cms.bool(True),
    useSignificance = cms.bool(True)
)


process.SteppingHelixPropagatorAny = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('SteppingHelixPropagatorAny'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('anyDirection'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.TrackerAdditionalParametersPerDetESModule = cms.ESProducer("TrackerAdditionalParametersPerDetESModule",
    appendToDataLabel = cms.string('')
)


process.TrackerDigiGeometryESModule = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.TrackerGeometricDetESModule = cms.ESProducer("TrackerGeometricDetESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder')
)


process.VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducerFromDB",
    debugBuilder = cms.untracked.bool(False),
    label = cms.untracked.string(''),
    valueOverride = cms.int32(-1)
)


process.ZdcGeometryFromDBEP = cms.ESProducer("ZdcGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.caloDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('CaloDetIdAssociator'),
    etaBinSize = cms.double(0.087),
    hcalRegion = cms.int32(2),
    includeBadChambers = cms.bool(False),
    includeGEM = cms.bool(False),
    includeME0 = cms.bool(False),
    nEta = cms.int32(70),
    nPhi = cms.int32(72)
)


process.cosmicsNavigationSchoolESProducer = cms.ESProducer("NavigationSchoolESProducer",
    ComponentName = cms.string('CosmicNavigationSchool'),
    SimpleMagneticField = cms.string('')
)


process.ecalDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('EcalDetIdAssociator'),
    etaBinSize = cms.double(0.02),
    hcalRegion = cms.int32(2),
    includeBadChambers = cms.bool(False),
    includeGEM = cms.bool(False),
    includeME0 = cms.bool(False),
    nEta = cms.int32(300),
    nPhi = cms.int32(360)
)


process.ecalElectronicsMappingGPUESProducer = cms.ESProducer("EcalElectronicsMappingGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalGainRatiosGPUESProducer = cms.ESProducer("EcalGainRatiosGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalIntercalibConstantsGPUESProducer = cms.ESProducer("EcalIntercalibConstantsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalLaserAPDPNRatiosGPUESProducer = cms.ESProducer("EcalLaserAPDPNRatiosGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalLaserAPDPNRatiosRefGPUESProducer = cms.ESProducer("EcalLaserAPDPNRatiosRefGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalLaserAlphasGPUESProducer = cms.ESProducer("EcalLaserAlphasGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalLinearCorrectionsGPUESProducer = cms.ESProducer("EcalLinearCorrectionsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalPedestalsGPUESProducer = cms.ESProducer("EcalPedestalsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalPulseCovariancesGPUESProducer = cms.ESProducer("EcalPulseCovariancesGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalPulseShapesGPUESProducer = cms.ESProducer("EcalPulseShapesGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalRechitADCToGeVConstantGPUESProducer = cms.ESProducer("EcalRechitADCToGeVConstantGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalRechitChannelStatusGPUESProducer = cms.ESProducer("EcalRechitChannelStatusGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalSamplesCorrelationGPUESProducer = cms.ESProducer("EcalSamplesCorrelationGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalSeverityLevel = cms.ESProducer("EcalSeverityLevelESProducer",
    dbstatusMask = cms.PSet(
        kBad = cms.vstring(
            'kNonRespondingIsolated',
            'kDeadVFE',
            'kDeadFE',
            'kNoDataNoTP'
        ),
        kGood = cms.vstring('kOk'),
        kProblematic = cms.vstring(
            'kDAC',
            'kNoLaser',
            'kNoisy',
            'kNNoisy',
            'kNNNoisy',
            'kNNNNoisy',
            'kNNNNNoisy',
            'kFixedG6',
            'kFixedG1',
            'kFixedG0'
        ),
        kRecovered = cms.vstring(),
        kTime = cms.vstring(),
        kWeird = cms.vstring()
    ),
    flagMask = cms.PSet(
        kBad = cms.vstring(
            'kFaultyHardware',
            'kDead',
            'kKilled'
        ),
        kGood = cms.vstring('kGood'),
        kProblematic = cms.vstring(
            'kPoorReco',
            'kPoorCalib',
            'kNoisy',
            'kSaturated'
        ),
        kRecovered = cms.vstring(
            'kLeadingEdgeRecovered',
            'kTowerRecovered'
        ),
        kTime = cms.vstring('kOutOfTime'),
        kWeird = cms.vstring(
            'kWeird',
            'kDiWeird'
        )
    ),
    timeThresh = cms.double(2.0)
)


process.ecalTimeBiasCorrectionsGPUESProducer = cms.ESProducer("EcalTimeBiasCorrectionsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalTimeCalibConstantsGPUESProducer = cms.ESProducer("EcalTimeCalibConstantsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.hcalChannelPropertiesESProd = cms.ESProducer("HcalChannelPropertiesEP")


process.hcalChannelQualityGPUESProducer = cms.ESProducer("HcalChannelQualityGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.hcalConvertedEffectivePedestalWidthsGPUESProducer = cms.ESProducer("HcalConvertedEffectivePedestalWidthsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label0 = cms.string('withTopoEff'),
    label1 = cms.string('withTopoEff'),
    label2 = cms.string(''),
    label3 = cms.string('')
)


process.hcalConvertedEffectivePedestalsGPUESProducer = cms.ESProducer("HcalConvertedEffectivePedestalsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label0 = cms.string('withTopoEff'),
    label1 = cms.string(''),
    label2 = cms.string('')
)


process.hcalConvertedPedestalWidthsGPUESProducer = cms.ESProducer("HcalConvertedPedestalWidthsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label0 = cms.string(''),
    label1 = cms.string(''),
    label2 = cms.string(''),
    label3 = cms.string('')
)


process.hcalConvertedPedestalsGPUESProducer = cms.ESProducer("HcalConvertedPedestalsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label0 = cms.string(''),
    label1 = cms.string(''),
    label2 = cms.string('')
)


process.hcalDDDRecConstants = cms.ESProducer("HcalDDDRecConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalDDDSimConstants = cms.ESProducer("HcalDDDSimConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('HcalDetIdAssociator'),
    etaBinSize = cms.double(0.087),
    hcalRegion = cms.int32(2),
    includeBadChambers = cms.bool(False),
    includeGEM = cms.bool(False),
    includeME0 = cms.bool(False),
    nEta = cms.int32(70),
    nPhi = cms.int32(72)
)


process.hcalElectronicsMappingGPUESProducer = cms.ESProducer("HcalElectronicsMappingGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.hcalGainWidthsGPUESProducer = cms.ESProducer("HcalGainWidthsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.hcalGainsGPUESProducer = cms.ESProducer("HcalGainsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.hcalLUTCorrsGPUESProducer = cms.ESProducer("HcalLUTCorrsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.hcalQIECodersGPUESProducer = cms.ESProducer("HcalQIECodersGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.hcalQIETypesGPUESProducer = cms.ESProducer("HcalQIETypesGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.hcalRecAlgos = cms.ESProducer("HcalRecAlgoESProducer",
    DropChannelStatusBits = cms.vstring(
        'HcalCellMask',
        'HcalCellOff',
        'HcalCellDead'
    ),
    RecoveredRecHitBits = cms.vstring(),
    SeverityLevels = cms.VPSet(
        cms.PSet(
            ChannelStatus = cms.vstring(),
            Level = cms.int32(0),
            RecHitFlags = cms.vstring('TimingFromTDC')
        ),
        cms.PSet(
            ChannelStatus = cms.vstring('HcalCellCaloTowerProb'),
            Level = cms.int32(1),
            RecHitFlags = cms.vstring()
        ),
        cms.PSet(
            ChannelStatus = cms.vstring('HcalCellExcludeFromHBHENoiseSummary'),
            Level = cms.int32(5),
            RecHitFlags = cms.vstring()
        ),
        cms.PSet(
            ChannelStatus = cms.vstring(),
            Level = cms.int32(8),
            RecHitFlags = cms.vstring(
                'HBHEHpdHitMultiplicity',
                'HBHEIsolatedNoise',
                'HBHEFlatNoise',
                'HBHESpikeNoise',
                'HBHETS4TS5Noise',
                'HBHENegativeNoise',
                'HBHEPulseFitBit',
                'HBHEOOTPU'
            )
        ),
        cms.PSet(
            ChannelStatus = cms.vstring(),
            Level = cms.int32(11),
            RecHitFlags = cms.vstring(
                'HFLongShort',
                'HFS8S1Ratio',
                'HFPET',
                'HFSignalAsymmetry'
            )
        ),
        cms.PSet(
            ChannelStatus = cms.vstring('HcalCellHot'),
            Level = cms.int32(15),
            RecHitFlags = cms.vstring()
        ),
        cms.PSet(
            ChannelStatus = cms.vstring(
                'HcalCellOff',
                'HcalCellDead'
            ),
            Level = cms.int32(20),
            RecHitFlags = cms.vstring()
        )
    ),
    appendToDataLabel = cms.string(''),
    phase = cms.uint32(1)
)


process.hcalRecoParamsWithPulseShapesGPUESProducer = cms.ESProducer("HcalRecoParamsWithPulseShapesGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.hcalRespCorrsGPUESProducer = cms.ESProducer("HcalRespCorrsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.hcalSiPMCharacteristicsGPUESProducer = cms.ESProducer("HcalSiPMCharacteristicsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.hcalSiPMParametersGPUESProducer = cms.ESProducer("HcalSiPMParametersGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.hcalTimeCorrsGPUESProducer = cms.ESProducer("HcalTimeCorrsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer")


process.hltBoostedDoubleSecondaryVertexAK8Computer = cms.ESProducer("CandidateBoostedDoubleSecondaryVertexESProducer",
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SecondaryVertex/data/BoostedDoubleSV_AK8_BDT_v4.weights.xml.gz')
)


process.hltCombinedSecondaryVertex = cms.ESProducer("CombinedSecondaryVertexESProducer",
    SoftLeptonFlip = cms.bool(False),
    calibrationRecords = cms.vstring(
        'CombinedSVRecoVertex',
        'CombinedSVPseudoVertex',
        'CombinedSVNoVertex'
    ),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    recordLabel = cms.string('HLT'),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(3),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5.0),
        maxDistToAxis = cms.double(0.07),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0)
    ),
    trackSelection = cms.PSet(
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5.0),
        maxDistToAxis = cms.double(0.07),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.hltCombinedSecondaryVertexV2 = cms.ESProducer("CombinedSecondaryVertexESProducer",
    SoftLeptonFlip = cms.bool(False),
    calibrationRecords = cms.vstring(
        'CombinedSVIVFV2RecoVertex',
        'CombinedSVIVFV2PseudoVertex',
        'CombinedSVIVFV2NoVertex'
    ),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    recordLabel = cms.string('HLT'),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(3),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5.0),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500.0),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3.0),
        min_pT = cms.double(120.0),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5.0),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500.0),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3.0),
        min_pT = cms.double(120.0),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.hltDisplacedDijethltESPPromptTrackCountingESProducer = cms.ESProducer("PromptTrackCountingESProducer",
    deltaR = cms.double(-1.0),
    deltaRmin = cms.double(0.0),
    impactParameterType = cms.int32(1),
    maxImpactParameter = cms.double(0.1),
    maxImpactParameterSig = cms.double(999999.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(999999.0),
    minimumImpactParameter = cms.double(-1.0),
    nthTrack = cms.int32(-1),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True)
)


process.hltDisplacedDijethltESPTrackCounting2D1st = cms.ESProducer("TrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(1),
    max_pT = cms.double(500.0),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(9999999.0),
    min_pT = cms.double(120.0),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(0.05),
    nthTrack = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(False),
    useVariableJTA = cms.bool(False)
)


process.hltESPAnalyticalPropagator = cms.ESProducer("AnalyticalPropagatorESProducer",
    ComponentName = cms.string('hltESPAnalyticalPropagator'),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum')
)


process.hltESPBwdAnalyticalPropagator = cms.ESProducer("AnalyticalPropagatorESProducer",
    ComponentName = cms.string('hltESPBwdAnalyticalPropagator'),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum')
)


process.hltESPBwdElectronPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('hltESPBwdElectronPropagator'),
    Mass = cms.double(0.000511),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.hltESPChi2ChargeLooseMeasurementEstimator16 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeLooseMeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPChi2ChargeMeasurementEstimator16 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPChi2ChargeMeasurementEstimator2000 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeMeasurementEstimator2000'),
    MaxChi2 = cms.double(2000.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPChi2ChargeMeasurementEstimator30 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    MaxChi2 = cms.double(30.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPChi2ChargeMeasurementEstimator9 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeMeasurementEstimator9'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(15.0)
)


process.hltESPChi2ChargeMeasurementEstimator9ForHI = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeMeasurementEstimator9ForHI'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutForHI')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(15.0)
)


process.hltESPChi2ChargeTightMeasurementEstimator16 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeTightMeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPChi2MeasurementEstimator100 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2MeasurementEstimator100'),
    MaxChi2 = cms.double(40.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(4.0)
)


process.hltESPChi2MeasurementEstimator16 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2MeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3.0)
)


process.hltESPChi2MeasurementEstimator30 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2MeasurementEstimator30'),
    MaxChi2 = cms.double(30.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3.0)
)


process.hltESPChi2MeasurementEstimator9 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2MeasurementEstimator9'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3.0)
)


process.hltESPCloseComponentsMerger5D = cms.ESProducer("CloseComponentsMergerESProducer5D",
    ComponentName = cms.string('hltESPCloseComponentsMerger5D'),
    DistanceMeasure = cms.string('hltESPKullbackLeiblerDistance5D'),
    MaxComponents = cms.int32(12)
)


process.hltESPDetachedQuadStepChi2ChargeMeasurementEstimator9 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPDetachedQuadStepChi2ChargeMeasurementEstimator9'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPDetachedQuadStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPDetachedQuadStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.13)
)


process.hltESPDetachedStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPDetachedStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.13)
)


process.hltESPDetachedTripletStepChi2ChargeMeasurementEstimator9 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPDetachedTripletStepChi2ChargeMeasurementEstimator9'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPDetachedTripletStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPDetachedTripletStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.13)
)


process.hltESPDisplacedDijethltPromptTrackCountingESProducer = cms.ESProducer("PromptTrackCountingESProducer",
    deltaR = cms.double(-1.0),
    deltaRmin = cms.double(0.0),
    impactParameterType = cms.int32(1),
    maxImpactParameter = cms.double(0.1),
    maxImpactParameterSig = cms.double(999999.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(999999.0),
    minimumImpactParameter = cms.double(-1.0),
    nthTrack = cms.int32(-1),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True)
)


process.hltESPDisplacedDijethltPromptTrackCountingESProducerLong = cms.ESProducer("PromptTrackCountingESProducer",
    deltaR = cms.double(-1.0),
    deltaRmin = cms.double(0.0),
    impactParameterType = cms.int32(1),
    maxImpactParameter = cms.double(0.2),
    maxImpactParameterSig = cms.double(999999.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(999999.0),
    minimumImpactParameter = cms.double(-1.0),
    nthTrack = cms.int32(-1),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True)
)


process.hltESPDisplacedDijethltTrackCounting2D1st = cms.ESProducer("TrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(1),
    max_pT = cms.double(500.0),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(9999999.0),
    min_pT = cms.double(120.0),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(0.05),
    nthTrack = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(False),
    useVariableJTA = cms.bool(False)
)


process.hltESPDisplacedDijethltTrackCounting2D2ndLong = cms.ESProducer("TrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(1),
    max_pT = cms.double(500.0),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(9999999.0),
    min_pT = cms.double(120.0),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(0.2),
    nthTrack = cms.int32(2),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.hltESPDummyDetLayerGeometry = cms.ESProducer("DetLayerGeometryESProducer",
    ComponentName = cms.string('hltESPDummyDetLayerGeometry')
)


process.hltESPEcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.hltESPElectronMaterialEffects = cms.ESProducer("GsfMaterialEffectsESProducer",
    BetheHeitlerCorrection = cms.int32(2),
    BetheHeitlerParametrization = cms.string('BetheHeitler_cdfmom_nC6_O5.par'),
    ComponentName = cms.string('hltESPElectronMaterialEffects'),
    EnergyLossUpdator = cms.string('GsfBetheHeitlerUpdator'),
    Mass = cms.double(0.000511),
    MultipleScatteringUpdator = cms.string('MultipleScatteringUpdator')
)


process.hltESPFastSteppingHelixPropagatorAny = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('hltESPFastSteppingHelixPropagatorAny'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('anyDirection'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(True)
)


process.hltESPFastSteppingHelixPropagatorOpposite = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('hltESPFastSteppingHelixPropagatorOpposite'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(True)
)


process.hltESPFittingSmootherIT = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('hltESPFittingSmootherIT'),
    EstimateCut = cms.double(-1.0),
    Fitter = cms.string('hltESPTrajectoryFitterRK'),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(3),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPTrajectorySmootherRK'),
    appendToDataLabel = cms.string('')
)


process.hltESPFittingSmootherRK = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('hltESPFittingSmootherRK'),
    EstimateCut = cms.double(-1.0),
    Fitter = cms.string('hltESPTrajectoryFitterRK'),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(False),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPTrajectorySmootherRK'),
    appendToDataLabel = cms.string('')
)


process.hltESPFlexibleKFFittingSmoother = cms.ESProducer("FlexibleKFFittingSmootherESProducer",
    ComponentName = cms.string('hltESPFlexibleKFFittingSmoother'),
    appendToDataLabel = cms.string(''),
    looperFitter = cms.string('hltESPKFFittingSmootherForLoopers'),
    standardFitter = cms.string('hltESPKFFittingSmootherWithOutliersRejectionAndRK')
)


process.hltESPFwdElectronPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('hltESPFwdElectronPropagator'),
    Mass = cms.double(0.000511),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.hltESPGlobalDetLayerGeometry = cms.ESProducer("GlobalDetLayerGeometryESProducer",
    ComponentName = cms.string('hltESPGlobalDetLayerGeometry')
)


process.hltESPGlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.hltESPGsfElectronFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('hltESPGsfElectronFittingSmoother'),
    EstimateCut = cms.double(-1.0),
    Fitter = cms.string('hltESPGsfTrajectoryFitter'),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPGsfTrajectorySmoother'),
    appendToDataLabel = cms.string('')
)


process.hltESPGsfTrajectoryFitter = cms.ESProducer("GsfTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPGsfTrajectoryFitter'),
    GeometricalPropagator = cms.string('hltESPAnalyticalPropagator'),
    MaterialEffectsUpdator = cms.string('hltESPElectronMaterialEffects'),
    Merger = cms.string('hltESPCloseComponentsMerger5D'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry')
)


process.hltESPGsfTrajectorySmoother = cms.ESProducer("GsfTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPGsfTrajectorySmoother'),
    ErrorRescaling = cms.double(100.0),
    GeometricalPropagator = cms.string('hltESPBwdAnalyticalPropagator'),
    MaterialEffectsUpdator = cms.string('hltESPElectronMaterialEffects'),
    Merger = cms.string('hltESPCloseComponentsMerger5D'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry')
)


process.hltESPHighPtTripletStepChi2ChargeMeasurementEstimator30 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPHighPtTripletStepChi2ChargeMeasurementEstimator30'),
    MaxChi2 = cms.double(30.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(15.0)
)


process.hltESPInitialStepChi2ChargeMeasurementEstimator30 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPInitialStepChi2ChargeMeasurementEstimator30'),
    MaxChi2 = cms.double(30.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(15.0)
)


process.hltESPInitialStepChi2MeasurementEstimator36 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPInitialStepChi2MeasurementEstimator36'),
    MaxChi2 = cms.double(36.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3.0)
)


process.hltESPKFFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('hltESPKFFittingSmoother'),
    EstimateCut = cms.double(-1.0),
    Fitter = cms.string('hltESPKFTrajectoryFitter'),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(False),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPKFTrajectorySmoother'),
    appendToDataLabel = cms.string('')
)


process.hltESPKFFittingSmootherForL2Muon = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('hltESPKFFittingSmootherForL2Muon'),
    EstimateCut = cms.double(-1.0),
    Fitter = cms.string('hltESPKFTrajectoryFitterForL2Muon'),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(False),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPKFTrajectorySmootherForL2Muon'),
    appendToDataLabel = cms.string('')
)


process.hltESPKFFittingSmootherForLoopers = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('hltESPKFFittingSmootherForLoopers'),
    EstimateCut = cms.double(20.0),
    Fitter = cms.string('hltESPKFTrajectoryFitterForLoopers'),
    LogPixelProbabilityCut = cms.double(-14.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(3),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPKFTrajectorySmootherForLoopers'),
    appendToDataLabel = cms.string('')
)


process.hltESPKFFittingSmootherWithOutliersRejectionAndRK = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('hltESPKFFittingSmootherWithOutliersRejectionAndRK'),
    EstimateCut = cms.double(20.0),
    Fitter = cms.string('hltESPRKTrajectoryFitter'),
    LogPixelProbabilityCut = cms.double(-14.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(3),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPRKTrajectorySmoother'),
    appendToDataLabel = cms.string('')
)


process.hltESPKFTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPKFTrajectoryFitter'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectoryFitterForL2Muon = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPKFTrajectoryFitterForL2Muon'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectoryFitterForLoopers = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPKFTrajectoryFitterForLoopers'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialForLoopers'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPKFTrajectorySmoother'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectorySmootherForL2Muon = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPKFTrajectorySmootherForL2Muon'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPFastSteppingHelixPropagatorOpposite'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectorySmootherForLoopers = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPKFTrajectorySmootherForLoopers'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialForLoopers'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectorySmootherForMuonTrackLoader = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPSmartPropagatorAnyOpposite'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(3)
)


process.hltESPKFUpdator = cms.ESProducer("KFUpdatorESProducer",
    ComponentName = cms.string('hltESPKFUpdator')
)


process.hltESPKullbackLeiblerDistance5D = cms.ESProducer("DistanceBetweenComponentsESProducer5D",
    ComponentName = cms.string('hltESPKullbackLeiblerDistance5D'),
    DistanceMeasure = cms.string('KullbackLeibler')
)


process.hltESPL3MuKFTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPL3MuKFTrajectoryFitter'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPSmartPropagatorAny'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.hltESPLowPtQuadStepChi2ChargeMeasurementEstimator9 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPLowPtQuadStepChi2ChargeMeasurementEstimator9'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPLowPtQuadStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPLowPtQuadStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.16)
)


process.hltESPLowPtStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPLowPtStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.16)
)


process.hltESPLowPtTripletStepChi2ChargeMeasurementEstimator9 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPLowPtTripletStepChi2ChargeMeasurementEstimator9'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPLowPtTripletStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPLowPtTripletStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.16)
)


process.hltESPMeasurementTracker = cms.ESProducer("MeasurementTrackerESProducer",
    ComponentName = cms.string('hltESPMeasurementTracker'),
    DebugPixelModuleQualityDB = cms.untracked.bool(False),
    DebugPixelROCQualityDB = cms.untracked.bool(False),
    DebugStripAPVFiberQualityDB = cms.untracked.bool(False),
    DebugStripModuleQualityDB = cms.untracked.bool(False),
    DebugStripStripQualityDB = cms.untracked.bool(False),
    HitMatcher = cms.string('StandardMatcher'),
    MaskBadAPVFibers = cms.bool(True),
    Phase2StripCPE = cms.string(''),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    SiStripQualityLabel = cms.string(''),
    StripCPE = cms.string('hltESPStripCPEfromTrackAngle'),
    UsePixelModuleQualityDB = cms.bool(True),
    UsePixelROCQualityDB = cms.bool(True),
    UseStripAPVFiberQualityDB = cms.bool(True),
    UseStripModuleQualityDB = cms.bool(True),
    UseStripStripQualityDB = cms.bool(True),
    appendToDataLabel = cms.string(''),
    badStripCuts = cms.PSet(
        TEC = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        ),
        TIB = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        ),
        TID = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        ),
        TOB = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        )
    )
)


process.hltESPMixedStepClusterShapeHitFilter = cms.ESProducer("ClusterShapeHitFilterESProducer",
    ComponentName = cms.string('hltESPMixedStepClusterShapeHitFilter'),
    PixelShapeFile = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_noL1.par'),
    PixelShapeFileL1 = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_loose.par'),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    )
)


process.hltESPMixedStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPMixedStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.11)
)


process.hltESPMixedTripletStepChi2ChargeMeasurementEstimator16 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPMixedTripletStepChi2ChargeMeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPMixedTripletStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPMixedTripletStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.11)
)


process.hltESPMuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.hltESPMuonTransientTrackingRecHitBuilder = cms.ESProducer("MuonTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('hltESPMuonTransientTrackingRecHitBuilder')
)


process.hltESPPixelCPEGeneric = cms.ESProducer("PixelCPEGenericESProducer",
    Alpha2Order = cms.bool(True),
    ClusterProbComputationFlag = cms.int32(0),
    ComponentName = cms.string('hltESPPixelCPEGeneric'),
    DoCosmics = cms.bool(False),
    EdgeClusterErrorX = cms.double(50.0),
    EdgeClusterErrorY = cms.double(85.0),
    IrradiationBiasCorrection = cms.bool(True),
    LoadTemplatesFromDB = cms.bool(True),
    MagneticFieldRecord = cms.ESInputTag("",""),
    NoTemplateErrorsWhenNoTrkAngles = cms.bool(False),
    SmallPitch = cms.bool(False),
    TruncatePixelCharge = cms.bool(True),
    Upgrade = cms.bool(False),
    UseErrorsFromTemplates = cms.bool(True),
    appendToDataLabel = cms.string(''),
    doLorentzFromAlignment = cms.bool(False),
    eff_charge_cut_highX = cms.double(1.0),
    eff_charge_cut_highY = cms.double(1.0),
    eff_charge_cut_lowX = cms.double(0.0),
    eff_charge_cut_lowY = cms.double(0.0),
    inflate_all_errors_no_trk_angle = cms.bool(False),
    inflate_errors = cms.bool(False),
    lAOffset = cms.double(0.0),
    lAWidthBPix = cms.double(0.0),
    lAWidthFPix = cms.double(0.0),
    size_cutX = cms.double(3.0),
    size_cutY = cms.double(3.0),
    useLAFromDB = cms.bool(True),
    useLAWidthFromDB = cms.bool(False),
    xerr_barrel_l1 = cms.vdouble(0.00115, 0.0012, 0.00088),
    xerr_barrel_l1_def = cms.double(0.0103),
    xerr_barrel_ln = cms.vdouble(0.00115, 0.0012, 0.00088),
    xerr_barrel_ln_def = cms.double(0.0103),
    xerr_endcap = cms.vdouble(0.002, 0.002),
    xerr_endcap_def = cms.double(0.002),
    yerr_barrel_l1 = cms.vdouble(
        0.00375, 0.0023, 0.0025, 0.0025, 0.0023,
        0.0023, 0.0021, 0.0021, 0.0024
    ),
    yerr_barrel_l1_def = cms.double(0.0021),
    yerr_barrel_ln = cms.vdouble(
        0.00375, 0.0023, 0.0025, 0.0025, 0.0023,
        0.0023, 0.0021, 0.0021, 0.0024
    ),
    yerr_barrel_ln_def = cms.double(0.0021),
    yerr_endcap = cms.vdouble(0.0021),
    yerr_endcap_def = cms.double(0.00075)
)


process.hltESPPixelCPETemplateReco = cms.ESProducer("PixelCPETemplateRecoESProducer",
    Alpha2Order = cms.bool(True),
    ClusterProbComputationFlag = cms.int32(0),
    ComponentName = cms.string('hltESPPixelCPETemplateReco'),
    LoadTemplatesFromDB = cms.bool(True),
    UseClusterSplitter = cms.bool(False),
    appendToDataLabel = cms.string(''),
    barrelTemplateID = cms.int32(0),
    directoryWithTemplates = cms.int32(0),
    doLorentzFromAlignment = cms.bool(False),
    forwardTemplateID = cms.int32(0),
    lAOffset = cms.double(0.0),
    lAWidthBPix = cms.double(0.0),
    lAWidthFPix = cms.double(0.0),
    speed = cms.int32(-2),
    useLAFromDB = cms.bool(True),
    useLAWidthFromDB = cms.bool(True)
)


process.hltESPPixelLessStepChi2ChargeMeasurementEstimator16 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPPixelLessStepChi2ChargeMeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPPixelLessStepClusterShapeHitFilter = cms.ESProducer("ClusterShapeHitFilterESProducer",
    ComponentName = cms.string('hltESPPixelLessStepClusterShapeHitFilter'),
    PixelShapeFile = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_noL1.par'),
    PixelShapeFileL1 = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_loose.par'),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    )
)


process.hltESPPixelLessStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPPixelLessStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.11)
)


process.hltESPPixelPairStepChi2ChargeMeasurementEstimator9 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPPixelPairStepChi2ChargeMeasurementEstimator9'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(15.0)
)


process.hltESPPixelPairStepChi2MeasurementEstimator25 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPPixelPairStepChi2MeasurementEstimator25'),
    MaxChi2 = cms.double(25.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3.0)
)


process.hltESPPixelPairTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPPixelPairTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.19)
)


process.hltESPRKTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPRKTrajectoryFitter'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.hltESPRKTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPRKTrajectorySmoother'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3)
)


process.hltESPRungeKuttaTrackerPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('hltESPRungeKuttaTrackerPropagator'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(True)
)


process.hltESPSmartPropagator = cms.ESProducer("SmartPropagatorESProducer",
    ComponentName = cms.string('hltESPSmartPropagator'),
    Epsilon = cms.double(5.0),
    MuonPropagator = cms.string('hltESPSteppingHelixPropagatorAlong'),
    PropagationDirection = cms.string('alongMomentum'),
    TrackerPropagator = cms.string('PropagatorWithMaterial')
)


process.hltESPSmartPropagatorAny = cms.ESProducer("SmartPropagatorESProducer",
    ComponentName = cms.string('hltESPSmartPropagatorAny'),
    Epsilon = cms.double(5.0),
    MuonPropagator = cms.string('SteppingHelixPropagatorAny'),
    PropagationDirection = cms.string('alongMomentum'),
    TrackerPropagator = cms.string('PropagatorWithMaterial')
)


process.hltESPSmartPropagatorAnyOpposite = cms.ESProducer("SmartPropagatorESProducer",
    ComponentName = cms.string('hltESPSmartPropagatorAnyOpposite'),
    Epsilon = cms.double(5.0),
    MuonPropagator = cms.string('SteppingHelixPropagatorAny'),
    PropagationDirection = cms.string('oppositeToMomentum'),
    TrackerPropagator = cms.string('PropagatorWithMaterialOpposite')
)


process.hltESPSoftLeptonByDistance = cms.ESProducer("LeptonTaggerByDistanceESProducer",
    distance = cms.double(0.5)
)


process.hltESPSteppingHelixPropagatorAlong = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('hltESPSteppingHelixPropagatorAlong'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('alongMomentum'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.hltESPSteppingHelixPropagatorOpposite = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('hltESPSteppingHelixPropagatorOpposite'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.hltESPStripCPEfromTrackAngle = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('hltESPStripCPEfromTrackAngle'),
    ComponentType = cms.string('StripCPEfromTrackAngle'),
    parameters = cms.PSet(
        mLC_P0 = cms.double(-0.326),
        mLC_P1 = cms.double(0.618),
        mLC_P2 = cms.double(0.3),
        mTEC_P0 = cms.double(-1.885),
        mTEC_P1 = cms.double(0.471),
        mTIB_P0 = cms.double(-0.742),
        mTIB_P1 = cms.double(0.202),
        mTID_P0 = cms.double(-1.427),
        mTID_P1 = cms.double(0.433),
        mTOB_P0 = cms.double(-1.026),
        mTOB_P1 = cms.double(0.253),
        maxChgOneMIP = cms.double(6000.0),
        useLegacyError = cms.bool(False)
    )
)


process.hltESPTTRHBWithTrackAngle = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('hltESPTTRHBWithTrackAngle'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    StripCPE = cms.string('hltESPStripCPEfromTrackAngle')
)


process.hltESPTTRHBuilderAngleAndTemplate = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('hltESPTTRHBuilderAngleAndTemplate'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    PixelCPE = cms.string('hltESPPixelCPETemplateReco'),
    StripCPE = cms.string('hltESPStripCPEfromTrackAngle')
)


process.hltESPTTRHBuilderPixelOnly = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('hltESPTTRHBuilderPixelOnly'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    StripCPE = cms.string('Fake')
)


process.hltESPTTRHBuilderWithoutAngle4PixelTriplets = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('hltESPTTRHBuilderWithoutAngle4PixelTriplets'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    StripCPE = cms.string('Fake')
)


process.hltESPTobTecStepChi2ChargeMeasurementEstimator16 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPTobTecStepChi2ChargeMeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPTobTecStepClusterShapeHitFilter = cms.ESProducer("ClusterShapeHitFilterESProducer",
    ComponentName = cms.string('hltESPTobTecStepClusterShapeHitFilter'),
    PixelShapeFile = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_noL1.par'),
    PixelShapeFileL1 = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_loose.par'),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    )
)


process.hltESPTobTecStepFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('hltESPTobTecStepFitterSmoother'),
    EstimateCut = cms.double(30.0),
    Fitter = cms.string('hltESPTobTecStepRKFitter'),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(7),
    NoInvalidHitsBeginEnd = cms.bool(False),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPTobTecStepRKSmoother'),
    appendToDataLabel = cms.string('')
)


process.hltESPTobTecStepFittingSmootherForLoopers = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('hltESPTobTecStepFitterSmootherForLoopers'),
    EstimateCut = cms.double(30.0),
    Fitter = cms.string('hltESPTobTecStepRKFitterForLoopers'),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(7),
    NoInvalidHitsBeginEnd = cms.bool(False),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPTobTecStepRKSmootherForLoopers'),
    appendToDataLabel = cms.string('')
)


process.hltESPTobTecStepFlexibleKFFittingSmoother = cms.ESProducer("FlexibleKFFittingSmootherESProducer",
    ComponentName = cms.string('hltESPTobTecStepFlexibleKFFittingSmoother'),
    appendToDataLabel = cms.string(''),
    looperFitter = cms.string('hltESPTobTecStepFitterSmootherForLoopers'),
    standardFitter = cms.string('hltESPTobTecStepFitterSmoother')
)


process.hltESPTobTecStepRKTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPTobTecStepRKFitter'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(7)
)


process.hltESPTobTecStepRKTrajectoryFitterForLoopers = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPTobTecStepRKFitterForLoopers'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialForLoopers'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(7)
)


process.hltESPTobTecStepRKTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPTobTecStepRKSmoother'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(7)
)


process.hltESPTobTecStepRKTrajectorySmootherForLoopers = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPTobTecStepRKSmootherForLoopers'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialForLoopers'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(7)
)


process.hltESPTobTecStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPTobTecStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.09)
)


process.hltESPTrackAlgoPriorityOrder = cms.ESProducer("TrackAlgoPriorityOrderESProducer",
    ComponentName = cms.string('hltESPTrackAlgoPriorityOrder'),
    algoOrder = cms.vstring(),
    appendToDataLabel = cms.string('')
)


process.hltESPTrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer",
    appendToDataLabel = cms.string(''),
    trackerGeometryLabel = cms.untracked.string(''),
    usePhase2Stacks = cms.bool(False)
)


process.hltESPTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(0.0),
    ValidHitBonus = cms.double(100.0),
    allowSharedFirstHit = cms.bool(False),
    fractionShared = cms.double(0.5)
)


process.hltESPTrajectoryFitterRK = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPTrajectoryFitterRK'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.hltESPTrajectorySmootherRK = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPTrajectorySmootherRK'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3)
)


process.hltPixelTracksCleanerBySharedHits = cms.ESProducer("PixelTrackCleanerBySharedHitsESProducer",
    ComponentName = cms.string('hltPixelTracksCleanerBySharedHits'),
    appendToDataLabel = cms.string(''),
    useQuadrupletAlgo = cms.bool(False)
)


process.hltTrackCleaner = cms.ESProducer("TrackCleanerESProducer",
    ComponentName = cms.string('hltTrackCleaner'),
    appendToDataLabel = cms.string('')
)


process.hoDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('HODetIdAssociator'),
    etaBinSize = cms.double(0.087),
    hcalRegion = cms.int32(2),
    includeBadChambers = cms.bool(False),
    includeGEM = cms.bool(False),
    includeME0 = cms.bool(False),
    nEta = cms.int32(30),
    nPhi = cms.int32(72)
)


process.multipleScatteringParametrisationMakerESProducer = cms.ESProducer("MultipleScatteringParametrisationMakerESProducer",
    appendToDataLabel = cms.string('')
)


process.muonDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('MuonDetIdAssociator'),
    etaBinSize = cms.double(0.125),
    hcalRegion = cms.int32(2),
    includeBadChambers = cms.bool(False),
    includeGEM = cms.bool(False),
    includeME0 = cms.bool(False),
    nEta = cms.int32(48),
    nPhi = cms.int32(48)
)


process.muonSeededTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('muonSeededTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(1.0),
    ValidHitBonus = cms.double(1000.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.1)
)


process.navigationSchoolESProducer = cms.ESProducer("NavigationSchoolESProducer",
    ComponentName = cms.string('SimpleNavigationSchool'),
    SimpleMagneticField = cms.string('ParabolicMf')
)


process.preshowerDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('PreshowerDetIdAssociator'),
    etaBinSize = cms.double(0.1),
    hcalRegion = cms.int32(2),
    includeBadChambers = cms.bool(False),
    includeGEM = cms.bool(False),
    includeME0 = cms.bool(False),
    nEta = cms.int32(60),
    nPhi = cms.int32(30)
)


process.siPixelGainCalibrationForHLTGPU = cms.ESProducer("SiPixelGainCalibrationForHLTGPUESProducer",
    appendToDataLabel = cms.string('')
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    siPixelQualityLabel = cms.string('')
)


process.siPixelROCsStatusAndMappingWrapperESProducer = cms.ESProducer("SiPixelROCsStatusAndMappingWrapperESProducer",
    CablingMapLabel = cms.string(''),
    ComponentName = cms.string(''),
    UseQualityInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.siPixelTemplateDBObjectESProducer = cms.ESProducer("SiPixelTemplateDBObjectESProducer")


process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer("SiStripBackPlaneCorrectionDepESProducer",
    BackPlaneCorrectionDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    )
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripLorentzAngleRcd')
    ),
    LorentzAnglePeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripLorentzAngleRcd')
    )
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.trackerTopology = cms.ESProducer("TrackerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.CSCChannelMapperESSource = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('CSCChannelMapperRecord')
)


process.CSCINdexerESSource = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('CSCIndexerRecord')
)


process.GlobalParametersRcdSource = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('L1TGlobalParametersRcd')
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string('.'),
        connectionRetrialPeriod = cms.untracked.int32(10),
        connectionRetrialTimeOut = cms.untracked.int32(60),
        connectionTimeOut = cms.untracked.int32(0),
        enableConnectionSharing = cms.untracked.bool(True),
        enablePoolAutomaticCleanUp = cms.untracked.bool(False),
        enableReadOnlySessionOnUpdateConnection = cms.untracked.bool(False),
        idleConnectionCleanupPeriod = cms.untracked.int32(10),
        messageLevel = cms.untracked.int32(0)
    ),
    DumpStat = cms.untracked.bool(False),
    ReconnectEachRun = cms.untracked.bool(False),
    RefreshAlways = cms.untracked.bool(False),
    RefreshEachRun = cms.untracked.bool(False),
    RefreshOpenIOVs = cms.untracked.bool(False),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string('121X_mcRun3_2021_realistic_v10'),
    pfnPostfix = cms.untracked.string('None'),
    snapshotTime = cms.string(''),
    toGet = cms.VPSet()
)


process.HcalTimeSlewEP = cms.ESSource("HcalTimeSlewEP",
    appendToDataLabel = cms.string('HBHE'),
    timeSlewParametersM2 = cms.VPSet(
        cms.PSet(
            slope = cms.double(-3.178648),
            tmax = cms.double(16.0),
            tzero = cms.double(23.960177)
        ),
        cms.PSet(
            slope = cms.double(-1.5610227),
            tmax = cms.double(10.0),
            tzero = cms.double(11.977461)
        ),
        cms.PSet(
            slope = cms.double(-1.075824),
            tmax = cms.double(6.25),
            tzero = cms.double(9.109694)
        )
    ),
    timeSlewParametersM3 = cms.VPSet(
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ),
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(15.5),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-3.2),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(32.0),
            tspar2_siPM = cms.double(0.0)
        ),
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ),
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        )
    )
)


process.HepPDTESSource = cms.ESSource("HepPDTESSource",
    pdtFileName = cms.FileInPath('SimGeneral/HepPDTESSource/data/pythiaparticle.tbl')
)


process.ecalMultifitParametersGPUESProducer = cms.ESSource("EcalMultifitParametersGPUESProducer",
    EBamplitudeFitParameters = cms.vdouble(1.138, 1.652),
    EBtimeFitParameters = cms.vdouble(
        -2.015452, 3.130702, -12.3473, 41.88921, -82.83944,
        91.01147, -50.35761, 11.05621
    ),
    EEamplitudeFitParameters = cms.vdouble(1.89, 1.4),
    EEtimeFitParameters = cms.vdouble(
        -2.390548, 3.553628, -17.62341, 67.67538, -133.213,
        140.7432, -75.41106, 16.20277
    ),
    appendToDataLabel = cms.string(''),
    pulseOffsets = cms.vint32(
        -3, -2, -1, 0, 1,
        2, 3, 4
    )
)


process.ecalRecHitParametersGPUESProducer = cms.ESSource("EcalRecHitParametersGPUESProducer",
    ChannelStatusToBeExcluded = cms.vstring(
        'kDAC',
        'kNoisy',
        'kNNoisy',
        'kFixedG6',
        'kFixedG1',
        'kFixedG0',
        'kNonRespondingIsolated',
        'kDeadVFE',
        'kDeadFE',
        'kNoDataNoTP'
    ),
    appendToDataLabel = cms.string(''),
    flagsMapDBReco = cms.PSet(
        kDead = cms.vstring('kNoDataNoTP'),
        kGood = cms.vstring(
            'kOk',
            'kDAC',
            'kNoLaser',
            'kNoisy'
        ),
        kNeighboursRecovered = cms.vstring(
            'kFixedG0',
            'kNonRespondingIsolated',
            'kDeadVFE'
        ),
        kNoisy = cms.vstring(
            'kNNoisy',
            'kFixedG6',
            'kFixedG1'
        ),
        kTowerRecovered = cms.vstring('kDeadFE')
    )
)


process.eegeom = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd')
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    fromDDD = cms.untracked.bool(False),
    toGet = cms.untracked.vstring('GainWidths')
)


process.hcalMahiPulseOffsetsGPUESProducer = cms.ESSource("HcalMahiPulseOffsetsGPUESProducer",
    appendToDataLabel = cms.string(''),
    pulseOffsets = cms.vint32(
        -3, -2, -1, 0, 1,
        2, 3, 4
    )
)


process.hltESSBTagRecord = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('JetTagComputerRecord')
)


process.hltESSEcalSeverityLevel = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalSeverityLevelAlgoRcd')
)


process.hltESSHcalSeverityLevel = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('HcalSeverityLevelComputerRcd')
)


process.HLTDoLocalPixelTask = cms.Task(process.hltOnlineBeamSpotToCUDA, process.hltSiPixelClusters, process.hltSiPixelClustersCUDA, process.hltSiPixelClustersCache, process.hltSiPixelClustersLegacy, process.hltSiPixelDigiErrorsSoA, process.hltSiPixelDigis, process.hltSiPixelDigisLegacy, process.hltSiPixelDigisSoA, process.hltSiPixelRecHits, process.hltSiPixelRecHitsCUDA)


process.HLTRecoPixelTracksTask = cms.Task(process.hltPixelTracks, process.hltPixelTracksCUDA, process.hltPixelTracksSoA, process.hltPixelTracksTrackingRegions, process.hltSiPixelRecHitSoA)


process.HLTRecopixelvertexingTask = cms.Task(process.HLTRecoPixelTracksTask, process.hltPixelVertices, process.hltPixelVerticesCUDA, process.hltPixelVerticesSoA, process.hltTrimmedPixelVertices)


process.HLTDoFullUnpackingEgammaEcalWithoutPreshowerTask = cms.Task(process.hltEcalDetIdToBeRecovered, process.hltEcalDigis, process.hltEcalDigisGPU, process.hltEcalDigisLegacy, process.hltEcalRecHit, process.hltEcalUncalibRecHit, process.hltEcalUncalibRecHitGPU, process.hltEcalUncalibRecHitSoA)


process.HLTPreshowerTask = cms.Task(process.hltEcalPreshowerDigis, process.hltEcalPreshowerRecHit)


process.HLTDoFullUnpackingEgammaEcalTask = cms.Task(process.HLTDoFullUnpackingEgammaEcalWithoutPreshowerTask, process.HLTPreshowerTask)


process.HLTDoLocalHcalTask = cms.Task(process.hltHbhereco, process.hltHbherecoFromGPU, process.hltHbherecoGPU, process.hltHcalDigis, process.hltHcalDigisGPU, process.hltHfprereco, process.hltHfreco, process.hltHoreco)


process.HLTL1UnpackerSequence = cms.Sequence(process.hltGtStage2Digis+process.hltGtStage2ObjectMap)


process.HLTBeamSpot = cms.Sequence(process.hltScalersRawToDigi+process.hltOnlineBeamSpot)


process.HLTBeginSequence = cms.Sequence(process.hltTriggerType+process.HLTL1UnpackerSequence+process.HLTBeamSpot)


process.HLTPFClusteringForEgamma = cms.Sequence(process.hltRechitInRegionsECAL+process.hltRechitInRegionsES+process.hltParticleFlowRecHitECALL1Seeded+process.hltParticleFlowRecHitPSL1Seeded+process.hltParticleFlowClusterPSL1Seeded+process.hltParticleFlowClusterECALUncorrectedL1Seeded+process.hltParticleFlowClusterECALL1Seeded+process.hltParticleFlowSuperClusterECALL1Seeded)


process.HLTFastJetForEgamma = cms.Sequence(process.hltTowerMakerForAll+process.hltFixedGridRhoFastjetAllCaloForMuons)


process.HLTPFHcalClustering = cms.Sequence(process.hltParticleFlowRecHitHBHE+process.hltParticleFlowClusterHBHE+process.hltParticleFlowClusterHCAL)


process.HLTDoLocalStripSequence = cms.Sequence(process.hltSiStripExcludedFEDListProducer+process.hltSiStripRawToClustersFacility+process.hltSiStripClusters)


process.HLTGsfElectronSequence = cms.Sequence(process.hltEgammaCkfTrackCandidatesForGSF+process.hltEgammaGsfTracks+process.hltEgammaGsfElectrons+process.hltEgammaGsfTrackVars)


process.HLTEndSequence = cms.Sequence(process.hltBoolEnd)


process.HLTDoLocalPixelSequence = cms.Sequence(process.HLTDoLocalPixelTask)


process.HLTRecopixelvertexingSequence = cms.Sequence(process.hltPixelTracksFitter+process.hltPixelTracksFilter, process.HLTRecopixelvertexingTask)


process.HLTDoFullUnpackingEgammaEcalWithoutPreshowerSequence = cms.Sequence(process.HLTDoFullUnpackingEgammaEcalWithoutPreshowerTask)


process.HLTDoFullUnpackingEgammaEcalSequence = cms.Sequence(process.HLTDoFullUnpackingEgammaEcalTask)


process.HLTDoLocalHcalSequence = cms.Sequence(process.HLTDoLocalHcalTask)


process.HLTIterativeTrackingIteration0Task = cms.Sequence(process.hltIter0PFLowPixelSeedsFromPixelTracks+process.hltIter0PFlowCkfTrackCandidates+process.hltIter0PFlowCtfWithMaterialTracks+process.hltIter0PFlowTrackCutClassifier+process.hltMergedTracks)


process.HLTIterativeTrackingIteration0 = cms.Sequence(process.HLTIterativeTrackingIteration0Task)


process.HLTIterativeTrackingIter02 = cms.Sequence(process.HLTIterativeTrackingIteration0)


process.HLTElePixelMatchSequence = cms.Sequence(process.HLTDoLocalPixelSequence+process.HLTDoLocalStripSequence+process.hltPixelLayerPairs+process.hltPixelLayerTriplets+process.hltEgammaHoverE+process.hltEgammaSuperClustersToPixelMatch+process.hltEleSeedsTrackingRegions+process.hltElePixelHitDoublets+process.hltElePixelHitDoubletsForTriplets+process.hltElePixelHitTriplets+process.hltElePixelSeedsDoublets+process.hltElePixelSeedsTriplets+process.hltElePixelSeedsCombined+process.hltEgammaElectronPixelSeeds+process.hltEgammaPixelMatchVars)


process.HLTDoCaloSequencePF = cms.Sequence(process.HLTDoFullUnpackingEgammaEcalWithoutPreshowerSequence+process.HLTDoLocalHcalSequence+process.hltTowerMakerForAll)


process.HLTAK4CaloJetsPrePFRecoSequence = cms.Sequence(process.HLTDoCaloSequencePF+process.hltAK4CaloJetsPF)


process.HLTPreAK4PFJetsRecoSequence = cms.Sequence(process.HLTAK4CaloJetsPrePFRecoSequence+process.hltAK4CaloJetsPFEt5)


process.HLTTrackReconstructionForPFNoMu = cms.Sequence(process.HLTDoLocalPixelSequence+process.HLTRecopixelvertexingSequence+process.HLTDoLocalStripSequence+process.HLTIterativeTrackingIter02)


process.HLTTrackReconstructionForIsoElectronIter02 = cms.Sequence(process.HLTPreAK4PFJetsRecoSequence+process.HLTTrackReconstructionForPFNoMu)


process.HLTEle5WPTightGsfSequence = cms.Sequence(process.HLTDoFullUnpackingEgammaEcalSequence+process.HLTPFClusteringForEgamma+process.hltEgammaCandidates+process.hltEgammaTriggerFilterObjectWrapper+cms.ignore(process.hltEGL1SingleEGOrFilter)+cms.ignore(process.hltEG5L1SingleEGOrEtFilter)+process.hltEgammaClusterShape+cms.ignore(process.hltEle5WPTightClusterShapeFilter)+process.HLTDoLocalHcalSequence+process.HLTFastJetForEgamma+process.hltEgammaHoverE+cms.ignore(process.hltEle5WPTightHEFilter)+process.hltEgammaEcalPFClusterIso+cms.ignore(process.hltEle5WPTightEcalIsoFilter)+process.HLTPFHcalClustering+process.hltEgammaHcalPFClusterIso+cms.ignore(process.hltEle5WPTightHcalIsoFilter)+process.HLTElePixelMatchSequence+cms.ignore(process.hltEle5WPTightPixelMatchFilter)+cms.ignore(process.hltEle5WPTightPMS2Filter)+process.HLTGsfElectronSequence+cms.ignore(process.hltEle5WPTightGsfOneOEMinusOneOPFilter)+cms.ignore(process.hltEle5WPTightGsfMissingHitsFilter)+cms.ignore(process.hltEle5WPTightGsfDetaFilter)+cms.ignore(process.hltEle5WPTightGsfDphiFilter)+process.hltEle5DphiFilter+process.HLTTrackReconstructionForIsoElectronIter02+process.hltEgammaEleGsfTrackIso+cms.ignore(process.hltEle5WPTightGsfTrackIsoFilter))


process.HLTriggerFirstPath = cms.Path(process.hltGetRaw+process.hltPSetMap+process.hltBoolFalse)


process.HLT_Ele32_WPTight_Gsf_v15 = cms.Path(process.HLTBeginSequence+cms.ignore(process.hltL1sSingleEGor)+process.hltPreEle32WPTightGsf+process.HLTEle5WPTightGsfSequence+process.HLTEndSequence)


process.HLTriggerFinalPath = cms.Path(process.hltGtStage2Digis+process.hltScalersRawToDigi+process.hltFEDSelector+process.hltTriggerSummaryAOD+process.hltTriggerSummaryRAW+process.hltBoolFalse)


process.Status_OnCPU = cms.Path(process.statusOnGPU+~process.statusOnGPUFilter)


process.Status_OnGPU = cms.Path(process.statusOnGPU+process.statusOnGPUFilter)


process.hltEgHLTOut = cms.EndPath(process.hltEgammaHLTExtra+process.egOutMod)



