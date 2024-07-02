#!/bin/bash


# sudo powerstat -a -RDH 1 120 >powerstat_log.csv &
# sudo turbostat --show PkgWatt,RAMWatt --interval 1 >turbostatVals_write.csv &
# ps_pid=$!
sleep 10
# sudo iostat -cd 1 >io.txt &
# is_pid=$!
# echo $is_pid
python3 create_file.py 10
scp -r /run/user/1000/transfer_files/* cc@129.114.108.83:/run/user/1000/transfer_files
# kill ${ps_pid}
rm -r /run/user/1000/transfer_files/*