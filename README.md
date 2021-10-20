# pixel-track-validation

- Step - 1: Get configuration file
    - https://mattermost.web.cern.ch/cmseg/pl/7dt6srgmttnqdkug95by8n7f9a
- Step - 2: Run the configuration file using `cmsRun`
    - Step - 2(a): Submit the crab jobs with large statistics
    - Submit crab jobs over two jobs:

- Step - 3: Analyze the output

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