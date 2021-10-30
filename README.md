***pixel-track-validation***
---

- Step - 1: Get configuration file
- Step - 2: Run the configuration file using `cmsRun`
    - Step - 2(a): Submit the crab jobs with large statistics
- Step - 3: Analyze the output, make plots, etc.

# Get Configuration

## New configuration from Mario

Detailed instructions given [here](https://its.cern.ch/jira/plugins/servlet/mobile#issue/CMSHLT-2187).

- General settings:
   ```bash
   cmsrel CMSSW_12_1_0_pre4
   pushd CMSSW_12_1_0_pre4/src/
   cmsenv
   git cms-init
   git cms-addpkg HLTrigger/Configuration
   git cms-remote add mmasciov
   git fetch mmasciov
   git cherry-pick 91909330a10724646b4aed0596d62fc30a56a024
   scram b -j 12
   ```
- Get hlt configuration:
    ```bash
    hltGetConfiguration /users/swmukher/egm_ele5_open/V16 --setup /dev/CMSSW_12_0_0/GRun/V6 --globaltag auto:phase1_2021_realistic --input root://cms-xrd-global.cern.ch///store/mc/Run3Winter21DRMiniAOD/DYToLL_M-50_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/270024/a5adba3d-a6b2-46c0-b690-04e9462fad11.root --mc --process MYHLT --prescale none --max-events 50 --eras Run3 --output none --customise HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaMenuDev,HLTrigger/Configuration/customizeHLTforRun3Tracking.customizeHLTforRun3Tracking > hlt_PataTrack_CustomTracking.py

    hltGetConfiguration /users/swmukher/egm_ele5_open/V16 --setup /dev/CMSSW_12_0_0/GRun/V6 --globaltag auto:phase1_2021_realistic --input root://cms-xrd-global.cern.ch///store/mc/Run3Winter21DRMiniAOD/DYToLL_M-50_TuneCP5_14TeV-pythia8/GEN-SIM-DIGI-RAW/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/270024/a5adba3d-a6b2-46c0-b690-04e9462fad11.root --mc --process MYHLT --prescale none --max-events 50 --eras Run3 --output none --customise HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaMenuDev > hlt_Default_CustomTracking.py

    edmConfigDump --prune hlt_12_1_0pre4_Default_CustomTracking.py > hlt_12_1_0pre4_Default_CustomTracking_dump.py
    edmConfigDump --prune hlt_12_1_0pre4_PataTrack_CustomTracking.py > hlt_12_1_0pre4_PataTrack_CustomTracking_dump.py
    ```

# Crab job submission

```bash
cd /afs/cern.ch/work/r/rasharma/EGamma-POG/HLT_tasks/CPUtoGPUTransition/CMSSW_12_0_1/src/pixel-track-validation
cmsenv
voms-proxy-init --voms cms --valid 168:00
source /cvmfs/cms.cern.ch/crab3/crab.sh
crab-dev submit crab_config_default.py
crab-dev submit crab_config_petatrk.py
crab-dev submit crab_config_petatrk_QCD.py
crab-dev submit crab_config_default_QCD.py
```

# Analysis

- Used Sam's analyzer: https://gitlab.cern.ch/sharper/HLTAnalyserPy
- Command used for getting the reduced ntuples:

    ```bash
    python3 Analysis/HLTAnalyserPy/test/runMultiThreaded.py  -o ZPrime_petaTrkv3.root  /eos/cms/store/group/phys_egamma/Run3TriggerStudies/PixelTrackValidation/PetaTrkv3/ZprimeToEE_M-6000_TuneCP5_14TeV-pythia8/crab_crab_ZprimeToEE_M6000_TuneCP5_14TeV_PetaTrkv3/211022_191312/0000/output*.root --cmd "python3 Analysis/HLTAnalyserPy/test/makeRun3Ntup.py -r 1000" --hadd
    python3 Analysis/HLTAnalyserPy/test/runMultiThreaded.py  -o ZPrime_defaultv3.root  /eos/cms/store/group/phys_egamma/Run3TriggerStudies/PixelTrackValidation/defaultv3/ZprimeToEE_M-6000_TuneCP5_14TeV-pythia8/crab_crab_ZprimeToEE_M6000_TuneCP5_14TeV_defaultv3/211022_191301/0000/output*.root --cmd "python3 Analysis/HLTAnalyserPy/test/makeRun3Ntup.py -r 1000" --hadd
    python3 Analysis/HLTAnalyserPy/test/runMultiThreaded.py  -o QCD_PetaTrkv3.root  /eos/cms/store/group/phys_egamma/Run3TriggerStudies/PixelTrackValidation/PetaTrkv3/QCD_Pt-30To50_EMEnriched_TuneCP5_14TeV-pythia8/crab_crab_QCD_Pt30To50_EMEnriched_TuneCP5_14TeV_PetaTrkv3/211022_191322/0000/output*.root --cmd "python3 Analysis/HLTAnalyserPy/test/makeRun3Ntup.py -r 1000" --hadd
    python3 Analysis/HLTAnalyserPy/test/runMultiThreaded.py  -o QCD_defaultv3.root  /eos/cms/store/group/phys_egamma/Run3TriggerStudies/PixelTrackValidation/defaultv3/QCD_Pt-30To50_EMEnriched_TuneCP5_14TeV-pythia8/crab_crab_QCD_Pt30To50_EMEnriched_TuneCP5_14TeV_defaultv3/211022_191328/0000/output*.root --cmd "python3 Analysis/HLTAnalyserPy/test/makeRun3Ntup.py -r 1000" --hadd
    ```

# Plotting

```bash
cd $CMSSW_BASE/src/pixel-track-validation/Plotting-Macro
# Update input file paths in plotter.C then run
root -l -b -q plotter.C
```