# Scripts and Data Summary
- Source codes for analyses used in Kino et al. (2024, GRL) [https://doi.org/xxx](https://doi.org/xxx)
- Data (in gtool and csv formats) are available from Kino et al. (2024, Zenodo) [https://doi.org/10.5281/zenodo.7582876](https://doi.org/10.5281/zenodo.7582876)

## Jupyter Notebooks
- `Ant_proxy_model_comparison.ipynb`
    - Figures 1i–j and S4.
- `Ant_zonalmean.ipynb`
    - Figures 1a–h, S6, and S7.
- `Calc_Eady_growth_rate.ipynb`
    - Calculation for Figure S8.
- `Filtering_3D.ipynb`
    - Calculation for the analysis described in Section 2.4.
- `global_model-data_comparison_LGM_G.ipynb`
    - Figure S2.
- `global_model-data_comparison_LGM_M.ipynb`
    - Figure S3.
- `global_seasurface_LGM-PI.ipynb`
    - Figure S1.
- `Spatial_maps.ipynb`
    - Figures 2, S5, S8, and S9.

## Miscellaneous
### Additional Data
- `grlndfglac1d.t42`: Symbolic link to the LGM topography file.
- `Antarctica_LGM_Proxies.csv`: Ice core data described in Section 2.3. (Available from the Zenodo repository)
- `model_outputs`: Directory for model data (Contents are available from the Zenodo repository)

### Scripts and Utilities
- `zenodo_upload.sh`: Symbolic link to a script provided by [https://github.com/jhpoelen/zenodo-upload](https://github.com/jhpoelen/zenodo-upload)
- `execute_upload.sh`: Shell script to execute `zenodo_upload.sh`.
- `get_path.py`: Python script to locate necessary files for executing the Jupyter notebooks.
- `file_paths.csv`: Output file from `get_path.py`.