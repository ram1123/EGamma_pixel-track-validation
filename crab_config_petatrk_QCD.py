from CRABClient.UserUtilities import config
config = config()

# config.section_('General')
config.General.requestName = 'crab_QCD_Pt30To50_EMEnriched_TuneCP5_14TeV_PetaTrkv2'
config.General.workArea = 'crab_QCD_Pt30To50_EMEnriched_TuneCP5_14TeV_PetaTrkv2'
config.General.transferOutputs = True
config.General.transferLogs = True

# config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'hlt_12_0_1_patatrack.py'
config.JobType.numCores = 4

# config.Data.inputDBS = 'phys03'
config.JobType.allowUndistributedCMSSW = True
# config.JobType.maxMemoryMB = 1000

# config.JobType.numCores = 8
config.Data.inputDataset ='/QCD_Pt-30To50_EMEnriched_TuneCP5_14TeV-pythia8/Run3Winter21DRMiniAOD-FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/GEN-SIM-DIGI-RAW'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1

config.Data.outLFNDirBase = '/store/group/phys_egamma/Run3TriggerStudies/PixelTrackValidation/PetaTrkv2'
config.Data.publication = False
config.Site.storageSite = 'T2_CH_CERN'