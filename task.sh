#!/bin/bash

cd /root/task2/Disk
diskUsed=$(df --total | tail -n 1 | awk '{print $3}')
availableDisk=$(df --total | tail -n 1 | awk '{print $4}')
echo -e "$diskUsedk \t$availableDisk" > "$(date).txt"

mysql --user=root --password=Saji@1234 myproject7 << EOF
INSERT INTO DiskTable (date,DiskAvailable,DiskUsed) VALUES ('$(date)','$availableDisk','$diskUsed');
EOF

