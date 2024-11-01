# script.sh
#!/bin/bash

while true; do
    source "./script.sh"

    main &

    PID=$!

    wait $PID

    sleep 1800
done
