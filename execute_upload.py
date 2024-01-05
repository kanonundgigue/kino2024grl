import os
import subprocess

def main():
    zenodo_repo_id = "10461149"
    filename = "file_paths.txt"
    experiments = ["PI.AMIP_t42.20230831", "LGM.miroc_glomapice_anomtopo_t42.20230831", 
                   "LGM.miroc_anomtopo_t42.20230831", "LGM.glomap_anomtopo_t42.20230831"]
    current_dir = os.getcwd()

    for exp in experiments:
        print(f"Experiment: {exp}")
        zip_filename = f"{exp}.zip"

        if not os.path.exists(zip_filename):
            file_to_zip = []

            with open(filename, 'r') as file:
                for line in file:
                    line = line.strip()
                    # filepath = f"/data44/kanon/kino2023grl/{line}"
                    if exp in line:
                        print(f"Checking line: {line}")
                        file_to_zip.append(line)
                        print(file_to_zip)

            file_to_zip_str = " ".join(file_to_zip)
            print(f"Files to zip for {exp}:\n{file_to_zip_str}")

            # Zip the files
            os.system(f"zip {zip_filename} {file_to_zip_str} &")

        # Upload to Zenodo
        subprocess.run(["./zenodo_upload.sh", zenodo_repo_id, zip_filename])

if __name__ == "__main__":
    main()
