from CRABClient.UserUtilities import config
config = config()

# config.section_('General')
config.General.requestName = 'crab_ZprimeToEE_M6000_TuneCP5_14TeV_default'
config.General.workArea = 'crab_ZprimeToEE_M6000_TuneCP5_14TeV_default'
config.General.transferOutputs = True
config.General.transferLogs = True

# config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'hlt_12_0_1_default.py'
config.JobType.numCores = 4

# config.Data.inputDBS = 'phys03'
config.JobType.allowUndistributedCMSSW = True
config.JobType.maxMemoryMB = 1000

# config.JobType.numCores = 8
config.Data.inputDataset ='/ZprimeToEE_M-6000_TuneCP5_14TeV-pythia8/Run3Winter21DRMiniAOD-FlatPU0to80FEVT_112X_mcRun3_2021_realistic_v16-v2/GEN-SIM-DIGI-RAW'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1

config.Data.outLFNDirBase = '/store/group/phys_egamma/Run3TriggerStudies/PixelTrackValidation/default'
config.Data.publication = False
config.Site.storageSite = 'T2_CH_CERN'