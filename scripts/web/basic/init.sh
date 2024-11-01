# script.sh
#!/bin/bash

current_path=$(pwd)
fourth_component=$(echo $current_path | cut -d'/' -f5) # 4 for root, 5 for -a
NOTIFY_ID=$fourth_component

while true; do
    source "./script.sh"

    main &

    PID=$!

    wait $PID

    sleep 1800
done
