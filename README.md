***pixel-track-validation***
---

- Step - 1: Get configuration file
    - https://mattermost.web.cern.ch/cmseg/pl/7dt6srgmttnqdkug95by8n7f9a
- Step - 2: Run the configuration file using `cmsRun`
    - Step - 2(a): Submit the crab jobs with large statistics
    - Submit crab jobs over two jobs:
- Step - 3: Analyze the output, make efficiency plots, etc.

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

```bash
crab-dev status -d crab_ZprimeToEE_M6000_TuneCP5_14TeV_defaultv2/crab_crab_ZprimeToEE_M6000_TuneCP5_14TeV_defaultv2 --verboseErrors
crab-dev status -d crab_ZprimeToEE_M6000_TuneCP5_14TeV_PetaTrkv2/crab_crab_ZprimeToEE_M6000_TuneCP5_14TeV_PetaTrkv2 --verboseErrors
crab-dev status -d crab_QCD_Pt30To50_EMEnriched_TuneCP5_14TeV_PetaTrkv2/crab_crab_QCD_Pt30To50_EMEnriched_TuneCP5_14TeV_PetaTrkv2 --verboseErrors
crab-dev status -d crab_QCD_Pt30To50_EMEnriched_TuneCP5_14TeV_defaultv2/crab_crab_QCD_Pt30To50_EMEnriched_TuneCP5_14TeV_defaultv2 --verboseErrors
```


```bash
crab-dev resubmit -d crab_ZprimeToEE_M6000_TuneCP5_14TeV_defaultv2/crab_crab_ZprimeToEE_M6000_TuneCP5_14TeV_defaultv2
crab-dev resubmit -d crab_ZprimeToEE_M6000_TuneCP5_14TeV_PetaTrkv2/crab_crab_ZprimeToEE_M6000_TuneCP5_14TeV_PetaTrkv2
```


# Analysis

```bash
cd /afs/cern.ch/user/r/rasharma/work/EGamma-POG/HLT_tasks/CPUtoGPUTransition/analyzer/CMSSW_12_0_1/src
cmsenv
python3 Analysis/HLTAnalyserPy/test/makeRun3Ntup.py /eos/cms/store/group/phys_egamma/Run3TriggerStudies/PixelTrackValidation/PetaTrk/ZprimeToEE_M-6000_TuneCP5_14TeV-pythia8/crab_crab_ZprimeToEE_M6000_TuneCP5_14TeV_PetaTrkv1/211007_140711/0000/output_111*.root  -o test.root -r 1000
# Using multithread
python3 Analysis/HLTAnalyserPy/test/runMultiThreaded.py  -o ZPrime_petaTrk.root  /eos/cms/store/group/phys_egamma/Run3TriggerStudies/PixelTrackValidation/PetaTrk/ZprimeToEE_M-6000_TuneCP5_14TeV-pythia8/crab_crab_ZprimeToEE_M6000_TuneCP5_14TeV_PetaTrkv1/211007_140711/0000/output*.root --cmd "python3 Analysis/HLTAnalyserPy/test/makeRun3Ntup.py -r 1000" --hadd
python3 Analysis/HLTAnalyserPy/test/runMultiThreaded.py  -o ZPrime_default.root  /eos/cms/store/group/phys_egamma/Run3TriggerStudies/PixelTrackValidation/default/ZprimeToEE_M-6000_TuneCP5_14TeV-pythia8/crab_crab_ZprimeToEE_M6000_TuneCP5_14TeV_defaultv1/211007_140700/0000/output*.root --cmd "python3 Analysis/HLTAnalyserPy/test/makeRun3Ntup.py -r 1000" --hadd
python3 Analysis/HLTAnalyserPy/test/runMultiThreaded.py  -o QCD_default.root  /eos/cms/store/group/phys_egamma/Run3TriggerStudies/PixelTrackValidation/default/QCD_Pt-30To50_EMEnriched_TuneCP5_14TeV-pythia8/crab_crab_QCD_Pt30To50_EMEnriched_TuneCP5_14TeV_defaultv1/211007_203255/0000/output*.root --cmd "python3 Analysis/HLTAnalyserPy/test/makeRun3Ntup.py -r 1000" --hadd
python3 Analysis/HLTAnalyserPy/test/runMultiThreaded.py  -o QCD_PetaTrk.root  /eos/cms/store/group/phys_egamma/Run3TriggerStudies/PixelTrackValidation/PetaTrk/QCD_Pt-30To50_EMEnriched_TuneCP5_14TeV-pythia8/crab_crab_QCD_Pt30To50_EMEnriched_TuneCP5_14TeV_PetaTrkv1/211007_203246/0000/output*.root --cmd "python3 Analysis/HLTAnalyserPy/test/makeRun3Ntup.py -r 1000" --hadd


# Using multithread v2
python3 Analysis/HLTAnalyserPy/test/runMultiThreaded.py  -o ZPrime_petaTrkv2.root  /eos/cms/store/group/phys_egamma/Run3TriggerStudies/PixelTrackValidation/PetaTrkv2/ZprimeToEE_M-6000_TuneCP5_14TeV-pythia8/crab_crab_ZprimeToEE_M6000_TuneCP5_14TeV_PetaTrkv2/211019_124543/0000/output*.root --cmd "python3 Analysis/HLTAnalyserPy/test/makeRun3Ntup.py -r 1000" --hadd
python3 Analysis/HLTAnalyserPy/test/runMultiThreaded.py  -o ZPrime_defaultv2.root  /eos/cms/store/group/phys_egamma/Run3TriggerStudies/PixelTrackValidation/defaultv2/ZprimeToEE_M-6000_TuneCP5_14TeV-pythia8/crab_crab_ZprimeToEE_M6000_TuneCP5_14TeV_defaultv2/211019_124536/0000/output*.root --cmd "python3 Analysis/HLTAnalyserPy/test/makeRun3Ntup.py -r 1000" --hadd
python3 Analysis/HLTAnalyserPy/test/runMultiThreaded.py  -o QCD_PetaTrkv2.root  /eos/cms/store/group/phys_egamma/Run3TriggerStudies/PixelTrackValidation/PetaTrkv2/QCD_Pt-30To50_EMEnriched_TuneCP5_14TeV-pythia8/crab_crab_QCD_Pt30To50_EMEnriched_TuneCP5_14TeV_PetaTrkv2/211019_124548/0000/output*.root --cmd "python3 Analysis/HLTAnalyserPy/test/makeRun3Ntup.py -r 1000" --hadd
python3 Analysis/HLTAnalyserPy/test/runMultiThreaded.py  -o QCD_defaultv2.root  /eos/cms/store/group/phys_egamma/Run3TriggerStudies/PixelTrackValidation/defaultv2/QCD_Pt-30To50_EMEnriched_TuneCP5_14TeV-pythia8/crab_crab_QCD_Pt30To50_EMEnriched_TuneCP5_14TeV_defaultv2/211019_124554/0000/output*.root --cmd "python3 Analysis/HLTAnalyserPy/test/makeRun3Ntup.py -r 1000" --hadd
```