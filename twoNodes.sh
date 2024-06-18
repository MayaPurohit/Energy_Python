#!/bin/bash


#sudo powerstat -a -RDH 1 120 >graph_filesize.txt &
sudo turbostat --show PkgWatt,RAMWatt --interval 1 >turbostatVals_write.csv &
ps_pid=$!
sleep 10
# sudo iostat -cd 1 >io.txt &
# is_pid=$!
# echo $is_pid
python3 create_file.py 10
scp -r /home/cc/Energy_Python/transfer_files/* cc@129.114.108.8:/home/cc/Energy_Python/transfer_files
kill ${ps_pid}
# kill ${is_pid}
rm -r "/home/cc/Energy_Python/transfer_files"