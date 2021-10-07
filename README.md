# pixel-track-validation

- Step - 1: Get configuration file
- Step - 2: Run the configuration file using `cmsRun`
    - Step - 2(a): Submit the crab jobs with large statistics
- Step - 3: Analyze the output

# Crab job submission

```bash
cmsenv
voms-proxy-init --voms cms --valid 168:00
source /cvmfs/cms.cern.ch/crab3/crab.sh
crab-dev submit crab_config_default.py
crab-dev submit crab_config_petatrk.py
```

```bash
crab-dev status -d crab_ZprimeToEE_M6000_TuneCP5_14TeV_defaultv1/crab_crab_ZprimeToEE_M6000_TuneCP5_14TeV_defaultv1
crab-dev status -d crab_ZprimeToEE_M6000_TuneCP5_14TeV_PetaTrkv1/crab_crab_ZprimeToEE_M6000_TuneCP5_14TeV_PetaTrkv1
```