#!/bin/bash
cd /root/task2/CPUAvg/ 
sudo tail -n 60 "/root/task2/CPU/cpuUtil.txt" > CAvg.txt
count=0;
total=0;

for i in $( awk '{ print $1; }' CAvg.txt )
   do
     total=$(echo $total+$i | bc )
     ((count++))
   done
cpuAvg=$(echo "scale=2; $total / $count" | bc)
#echo "scale=2; $total / $count" | bc > "$(date).txt"
mysql --user=root --password=Saji@1234 myproject7 << EOF
INSERT INTO CPUAvg (date, cpuAvgColumn) VALUES ('$(date)','$cpuAvg');
EOF
rm CAvg.txt
