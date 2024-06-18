#!/bin/bash

sudo powerstat -a -RDH 1 80 >receive_times.csv &
ps_pid=$!
sudo iostat -cd 1 >io.csv &
is_pid=$!
echo $is_pid
destination_dir="/home/cc/Energy_Python/transfer_files"

destination_files=$(ls "$destination_dir" | wc -l )

while [ $destination_files -ne 11 ];
do
    destination_files=$(ls "$destination_dir" | wc -l )
done; 

python3 read_file.py "/home/cc/Energy_Python/transfer_files"

kill ${ps_pid}
kill ${is_pid}
rm -r /home/cc/Energy_Python/transfer_files/*


