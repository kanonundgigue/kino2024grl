import csv

# 定義された変数と実験
variables_to_draw = ["grsst", "gricr", "precwtot", "precw_d18O", "u250", "T2", "prcp_d18O", "sstgrad", "sens", "evap", "prcp", "vflow", "vprecwtot","vprecw"]
experiments = {
    "PI": "PI.AMIP_t42.20230831",
    "LGM_Mw/Gice": "LGM.miroc_glomapice_anomtopo_t42.20230831",
    "LGM_M": "LGM.miroc_anomtopo_t42.20230831",
    "LGM_G": "LGM.glomap_anomtopo_t42.20230831",
}
filter_types = ["1y_lp", "10d_lp", "10d_lp_residual"]

# CSVファイルに書き込むためのファイルパスのリストを生成
file_paths = []

# experimentsとvariables_to_drawの組み合わせからパスを生成
for exp_key, exp_path in experiments.items():
    for var in variables_to_draw:
        if var not in ["vprecw"]:
            file_paths.append(f"model_outputs/{exp_path}/clm/{var}")

# filter_typesと特定の変数の組み合わせから追加のパスを生成
for exp_key, exp_path in experiments.items():
    for filter_type in filter_types:
        for var in ["vprecw"]:
            if var in variables_to_draw:
                if filter_type == "1y_lp":
                    file_paths.append(f"model_outputs/{exp_path}/clm/ann/uvqt_clm.npz")
                elif filter_type == "10d_lp":
                    file_paths.append(f"model_outputs/{exp_path}/clm/ann/uvqt_10d_lp_clmanom.npz")
                else:
                    file_paths.append(f"model_outputs/{exp_path}/clm/ann/uvqt_10d_lp_clmanom_residual.npz")

# CSVファイルに書き込み
with open('file_paths.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for path in file_paths:
        writer.writerow([path])

print("CSVファイルが生成されました。")

