#!/bin/bash
rm -rf fixed_messages
mkdir -p fixed_messages
# iterate every folder in messages
for folder in ./messages/*; do
    {
        if [[ -d "$folder" ]]; then
            mkdir -p "fixed_messages/${folder##*/}"
            # iterate every file in given folder
            for file in "$folder"/*; do
                printf -- "%s--- ./fixed_%s\n" "$file" "${file#*/}"
                python3 "./fix_stupid_facebook_unicode_encoding.py" "$file" "./fixed_${file#*/}"
            done
        else
            printf -- "%s is not a folder, this file should be there?\n" "$folder"
        fi
    } &
done
wait
