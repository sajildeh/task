#!/bin/bash

cd /root/task2/CPU 
CPUUtilization=$(mpstat | head -4 | tail -1 | awk '{print $13}')
cpu=$(echo "scale=2; 100 -$CPUUtilization" | bc)
echo "scale=2; 100 -$CPUUtilization" | bc >> cpuUtil.txt

mysql --user=root --password=Saji@1234 myproject7 << EOF
INSERT INTO CPUTable (date, cpuColumn) VALUES ('$(date)','$cpu');
EOF