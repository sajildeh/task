#!/bin/bash

cd /root/task2/Memory/
cat * > temp.txt
sed 'n; d' temp.txt > MUsed.txt
sed '1d; n; d' temp.txt > MFree.txt

count=0;
total=0;
for i in $( awk '{ print $1; }' MUsed.txt )
   do
     total=$(echo $total+$i | bc )
     ((count++))
   done
#echo -n "Average memory available=" > "/root/task2/MemoryAvg/$(date).txt"
AMAvg=$(echo "scale=2; $total / $count" | bc)
#echo "scale=2; $total / $count" | bc >> "/root/task2/MemoryAvg/$(date).txt"

count=0;
total=0;
for i in $( awk '{ print $1; }' MFree.txt )
   do
     total=$(echo $total+$i | bc )
     ((count++))
   done
#echo -n "Average free memory=" >> "/root/task2/MemoryAvg/$(date).txt"
FMAvg=$(echo "scale=2; $total / $count" | bc)
#echo "scale=2; $total / $count" | bc >> "/root/task2/MemoryAvg/$(date).txt"

mysql --user=root --password=Saji@1234 myproject7 << EOF
INSERT INTO MemoryAvg (date,AvgMemoryAvailable,AvgMemoryFree) VALUES ('$(date)','$AMAvg','$FMAvg');
EOF
rm temp.txt MUsed.txt MFree.txt

