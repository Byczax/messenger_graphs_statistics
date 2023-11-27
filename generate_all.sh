#!/bin/bash
rm -rf img
mkdir -p img

# iterate every folder in messages
for folder in ./fixed_messages/*; do
    folder_name="${folder##*/}"
    mkdir -p "img/${folder_name:5}"
    current=
    next=
    number=0
    mkdir -p "img/${folder_name:5}/all/"

    python3 "./src/main.py" "$folder" "[2000,01,01]" "[2222,01,01]" "xD" "True" "../img/${folder_name:5}/all/" &

    start_year=$(expr "${folder_name:0:4}")
    current_year=$(date +%Y)
    years=()

    while [[ $start_year -le $current_year ]]; do
        years+=($start_year)
        start_year=$((start_year + 1))
    done

    for year in "${years[@]}"; do
        for date in $year,{03,10},01; do
            current=$next
            next=$date

            if [[ -n "$next" && -n "$current" ]]; then
                mapfile -t month_next < <(echo "$next" | tr "," "\n")
                mapfile -t month_current < <(echo "$current" | tr "," "\n")
                semester="zima"

                if [[ "${month_next[0]}" -eq "${month_current[0]}" ]]; then
                    semester="lato"
                fi
                mkdir -p "img/${folder_name:5}/$number-$semester-${month_current[0]}"
                # python3 "./src/main.py" "$folder" "[$current]" "[$next]" "xD" "True" "../img/${folder_name:5}/$number-$semester-${month_current[0]}/" &
                number=$((number + 1))
            fi
        done
    done
done
wait
