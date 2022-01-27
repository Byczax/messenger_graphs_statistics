#!/bin/bash

mkdir -p img
# iterate every folder in messages
for folder in ./fixed_messages/*;do
    mkdir -p "img/${folder##*/}"
    current=
    next=
    number=1
    mkdir -p "img/${folder##*/}/all/"
    python3 "./src/main.py" "$folder" "[2000,01,01]" "[2222,01,01]" "xD" "True" "../img/${folder##*/}/all/" &
    for date in 20{18,19,20,21,22},{03,10},01;do
        current=$next
        next=$date
        if [[ -n "$next" && -n "$current" ]];then
            mapfile -t month_next < <(echo "$next" | tr "," "\n")
            mapfile -t month_current < <(echo "$current" | tr "," "\n")
            semester="zima"
            if [ "${month_next[0]}" -eq "${month_current[0]}" ];then
                semester="lato"
            fi
            mkdir -p "img/${folder##*/}/$number-$semester-${month_current[0]}"
            python3 "./src/main.py" "$folder" "[$current]" "[$next]" "xD" "True" "../img/${folder##*/}/$number-$semester-${month_current[0]}/" &
            number=$((number+1))
        fi
    done
done
wait
