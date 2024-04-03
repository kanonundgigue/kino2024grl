# Supporting program for “Synoptic Moisture Intrusion Provided Heavy Isotope Precipitations in Inland Antarctica during the Last Glacial Maximum” (Version 1.0). Github. Retrieved from https://github.com/kanonundgigue/kino2024grl

## Scripts and Data Summary
- Source codes for analyses used in Kino et al. (2024, GRL) [https://doi.org/xxx](https://doi.org/xxx)
- Data (in gtool and csv formats) are available from [Kino et al. (2024, Zenodo)](https://doi.org/10.5281/zenodo.10867605)
- The python environment has been build by using [this package](https://github.com/kanonundgigue/virtual_env.git).

### Jupyter Notebooks
- `Ant_proxy_model_comparison.ipynb`
    - Figures 1i–j and S4.
- `Ant_zonalmean.ipynb`
    - Figure S5.
- `Calc_Eady_growth_rate.ipynb`
    - Calculation for Figure S7 based on ESMValTool [(Righi et al., 2020, GMD)](https://gmd.copernicus.org/articles/13/1179/2020/). 
- `Filtering_3D.ipynb`
    - Calculation for the analysis described in Section 2.4 based on [Newman et al. (2012, JC)](https://journals.ametsoc.org/view/journals/clim/25/21/jcli-d-11-00665.1.xml).
- `global_model-data_comparison_LGM_G.ipynb`
    - Figure S2.
- `global_model-data_comparison_LGM_M.ipynb`
    - Figure S3.
- `global_seasurface_LGM-PI.ipynb`
    - Figure S1.
- `Spatial_maps.ipynb`
    - Figures 1a–h, S6–S13.

### Miscellaneous
#### Additional Data
- `grlndfglac1d.t42`: Symbolic link to the LGM topography file.
- `Antarctica_LGM_Proxies.csv`: Ice core data described in Section 2.3. (Available from [Kino et al. (2024, Zenodo)](https://zenodo.org/doi/10.5281/zenodo.7582875))
- `model_outputs`: Directory for model data (Contents are available from [Kino et al. (2024, Zenodo)](https://zenodo.org/doi/10.5281/zenodo.7582875))
- `IceCores_LGM_PI.csv`: Symbolic link to the global ice core data described in Section 2.3. (Original data is available from [https://www.ncdc.noaa.gov/data-access/paleoclimatology-data](https://www.ncdc.noaa.gov/data-access/paleoclimatology-data) and described by [Cauquoin et al. (2019, EPSL)](https://www.sciencedirect.com/science/article/pii/S0012821X19304236?via%3Dihub))
- `SISALv2_d18O_LGM_PI.csv`: Symbolic link to the global speleothem data described in Section 2.3. (Original data is available from [Comas-Bru et al. (2020, URRDA)](https://researchdata.reading.ac.uk/256/).
- The Sea surface temperature and sea ice concentration data of GLOMAP is available at [Paul et al. (2020, PANGAEA)](https://doi.pangaea.de/10.1594/PANGAEA.923262).
- The Sea surface temperature and sea ice concentration outputs from MIROC4m-AOGCM are available from the authors of [Sherriff-Tadano et al. (2023,CP)](https://journals.ametsoc.org/view/journals/clim/aop/JCLI-D-22-0221.1/JCLI-D-22-0221.1.xml).
  
### Scripts and Utilities
- `zenodo_upload.sh`: Symbolic link to a script provided by [https://github.com/jhpoelen/zenodo-upload](https://github.com/jhpoelen/zenodo-upload)
- `execute_upload.py`: Python script to execute `zenodo_upload.sh`.
- `get_path.py`: Python script to locate necessary files for executing the Jupyter notebooks.
- `file_paths.txt`: Output file from `get_path.py`.

## How to cite
Kino, K. (2024). Supporting program for “Synoptic Moisture Intrusion Provided Heavy Isotope Precipitations in Inland Antarctica during the Last Glacial Maximum” (Version 1.0). [Software] https://github.com/kanonundgigue/kino2024grl
