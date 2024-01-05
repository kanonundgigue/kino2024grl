#!/bin/bash

zenodo_repo_id=10444172
filename="file_paths.txt"
experiments=(PI.AMIP_t42.20230831 LGM.miroc_glomapice_anomtopo_t42.20230831 LGM.miroc_anomtopo_t42.20230831 LGM.glomap_anomtopo_t42.20230831)
current_dir=`pwd -P`
for exp in "${experiments[@]}"
do
    echo "Experiment: $exp"
    if ! test -e "${exp}.zip" ; then
        file_to_zip=()
        while IFS= read -r line
        do
            
#             filepath=/data44/kanon/kino2023grl/"$line"
             
            if [[ $line == *"$exp"* ]]; then
                echo "Checking line: $line"
                file_to_zip+=("$line")
                echo ${file_to_zip[@]}
            fi
        done < "$filename"

        # 配列の要素をスペース区切りの文字列に結合
        file_to_zip_str=""
        for item in "${file_to_zip[@]}"; do
            file_to_zip_str+="$item "
        done

        # 末尾の余分なスペースを削除
        file_to_zip_str="${file_to_zip_str% }"
        
        echo "Files to zip for $exp:"
        printf '%s\n' "${file_to_zip_str}"

#        zip ${exp}.zip ${file_to_zip_str} &
    fi
#    ./zenodo_upload.sh ${zenodo_repo_id} ${exp}.zip
done


