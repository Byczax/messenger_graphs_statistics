#!/bin/bash

printf "\n=========== Fixing stupid facebook files ===========\n\n"
bash ./fix_stupid_files.sh
printf "\n=========== Generating images ===========\n\n"
bash ./generate_all.sh
printf "\n=========== Done! ===========\n\n"
