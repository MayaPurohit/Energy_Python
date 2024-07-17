#!/bin/bash

# Write CSV header
echo "Timestamp,Sensor,Value" > "ipmi_log.csv"

while true; do
    # Get current timestamp
    TIMESTAMP=$(date "+%H:%M:%S")
    
    # Collect IPMI sensor data
    IPMI_DATA=$(sudo ipmi-dcmi --get-system-power-statistics)
    
    # Parse and format data for CSV
    echo "$IPMI_DATA" | while read line; do

        SENSOR=$(echo $line | awk '{print $1}')
        VALUE=$(echo $line | awk '{print $(NF-1)}')
        if [ $SENSOR != "Power" ] && [ $SENSOR != "Time" ] && [ $SENSOR != "Statistics" ]; then
            echo "$TIMESTAMP,$SENSOR,$VALUE" >> "ipmi_log.csv"
        fi
    done
    
    # Wait for the next interval (e.g., 60 seconds)
    sleep 0.1
done