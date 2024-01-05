#!/bin/bash

zenodo_repo_id=10444172
filename="file_list.txt"
experiments=(PI.AMIP_t42.20230831 LGM.miroc_glomapice_anomtopo_t42.20230831 LGM.miroc_anomtopo_t42.20230831 LGM.glomap_anomtopo_t42.20230831)

for exp in "${experiments[@]}"
do
    if ! test -e "${exp}.zip" ; then
        file_to_zip=()
        while IFS= read -r line
        do
            if [[ $line == *"$exp"* ]]; then
                file_to_zip+=("model_outputs/$line")
            fi
        done < "$filename"
    
        zip "${exp}.zip" "${file_to_zip[@]}" &
    fi
    ./zenodo_upload.sh ${zenodo_repo_id} ${exp}.zip
done


