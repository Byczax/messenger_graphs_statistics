#!/bin/bash

mkdir -p img
# iterate every folder in messages
for folder in ./fixed_messages/*;do
    mkdir -p "img/${folder##*/}"
    # year=2019
    # month=10
    # day=1
    previous=
    current=
    next=
    number=1
    mkdir -p "img/${folder##*/}/all/"
    python3 "./src/main.py" $folder "[2000,01,01]" "[2222,01,01]" "xD" "True" "../img/${folder##*/}/all/"
    for date in 20{18,19,20,21},{03,10},01;do
        previous=$current
        current=$next
        next=$date
        # echo $current $next
        if [ -n "$next" -a -n "$current" ];then
            month_next=($(echo $next | tr "," "\n"))
            month_current=($(echo $current | tr "," "\n"))
            semester="zima"
            if [ ${month_next[0]} -eq ${month_current[0]} ];then
                semester="lato"
                fi
            # echo $folder
            mkdir -p "img/${folder##*/}/$number-$semester-${month_current[0]}"
            python3 "./src/main.py" $folder "[$current]" "[$next]" "xD" "True" "../img/${folder##*/}/$number-$semester-${month_current[0]}/"
            number=$((number+1))
        fi
    # for date in 20{19,20,21},{01,02,03,04,05,06,07,08,09,10,11,12},01;do
    #     echo $date
        # printf -- "python3 ./src/main.py $folder "
    done
    # echo
done
