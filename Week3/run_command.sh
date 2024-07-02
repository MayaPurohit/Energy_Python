#!/bin/bash

sudo powerstat -a -RDH 1 120 >receive_times.csv &
ps_pid=$!
# sudo iostat -cd 1 >io.csv &
# is_pid=$!
# echo $is_pid

# mkdir /run/user/1000/transfer_files

destination_dir="/run/user/1000/transfer_files"

destination_files=$(ls "$destination_dir" | wc -l )

while [ $destination_files -ne 11 ];
do
    destination_files=$(ls "$destination_dir" | wc -l )
done; 

python3 read_file.py "/run/user/1000/transfer_files"

kill ${ps_pid}
kill ${is_pid}
rm -r /run/user/1000/transfer_files/*
