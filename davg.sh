#!/bin/bash

cd /root/task2/Disk/
cat * > temp.txt
sed 'n; d' temp.txt > DUsed.txt
sed '1d; n; d' temp.txt > DFree.txt

count=0;
total=0;
for i in $( awk '{ print $1; }' DUsed.txt )
   do
     total=$(echo $total+$i | bc )
     ((count++))
   done
#echo -n "Average disk available=" > "/root/task2/DiskAvg/$(date).txt"
ADAvg=$(echo "scale=2; $total / $count" | bc)
#echo "scale=2; $total / $count" | bc >> "/root/task2/DiskAvg/$(date).txt"

count=0;
total=0;
for i in $( awk '{ print $1; }' DFree.txt )
   do
     total=$(echo $total+$i | bc )
     ((count++))
   done
#echo -n "Average free disk=" >> "/root/task2/DiskAvg/$(date).txt"
FDAvg=$(echo "scale=2; $total / $count" | bc)
#echo "scale=2; $total / $count" | bc >> "/root/task2/DiskAvg/$(date).txt"

mysql --user=root --password=Saji@1234 myproject7 << EOF
INSERT INTO DiskAvg (date,AvgDiskAvailable,AvgDiskFree) VALUES ('$(date)','$ADAvg','$FDAvg');
EOF
rm temp.txt DUsed.txt DFree.txt

