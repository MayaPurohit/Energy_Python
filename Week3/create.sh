#!/bin/bash
sleep 10
python3 create_file.py 10
scp -r /dev/shm/transfer_files/ cc@129.114.108.102:/dev/shm/
rm -r /dev/shm/transfer_files/