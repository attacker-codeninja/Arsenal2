#!/bin/bash

while true; do
    source "./script.sh"

    main &

    PID=$!

    sleep 1800

    kill $PID 2>/dev/null

    wait $PID 2>/dev/null
done
