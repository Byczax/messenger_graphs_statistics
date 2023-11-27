#!/bin/bash

shopt -s globstar

declare -A dates

function rename_file {
    file="$1"
    newest_timestamp=$(jq -r '.messages | sort_by(.timestamp_ms) | reverse | .[0].timestamp_ms' "$file")
    newest_date=$(date -d @$((newest_timestamp / 1000)) '+%Y-%m-%d_%H-%M-%S')
    if [[ -z "${dates[$newest_date]}" ]]; then
        dates[$newest_date]=$file
        new_filename="$(dirname "$file")/message_$newest_date.json"
        # mv "$file" "$new_filename"
        echo "Renamed file $file to $new_filename"
        # echo "File: $file, Newest date: $newest_date"
    else
        echo "Duplicate date found: $newest_date in files ${dates[$newest_date]} and $file"
    fi
}

for file in messages/**/*.json; do
    rename_file "$file" &
done
wait
