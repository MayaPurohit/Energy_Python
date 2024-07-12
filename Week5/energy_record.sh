#!/bin/bash

# sudo powerstat -a -RDH 1 1000 > powerstat_memory_read.csv 
# sudo turbostat --show RAMWatt --enable "Time_Of_Day_Seconds" --interval 1 >turbostat_memory_write.csv  &
# python3 read_file.py /dev/shm/transfer_files

echo "Timestamp,Sensor,Value" > "ipmi_idle.csv"

while true; do

    TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")

    IPMI_DATA=$(sudo ipmi-dcmi --get-system-power-statistics)
    
    # Parse and format data for CSV
    echo "$IPMI_DATA" | while read line; do

        SENSOR=$(echo $line | awk '{print $1}')
        VALUE=$(echo $line | awk '{print $(NF-1)}')
        if [ $SENSOR == "Current" ]; then
            echo "$TIMESTAMP,$SENSOR,$VALUE" >> "ipmi_idle.csv"
        fi
    done
    

    sleep 1

done