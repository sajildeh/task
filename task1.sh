#!/bin/bash

cd /root/task2/Memory
memoryUsed=$(free | head -2 | tail -1 | awk '{print $3}')
freeMemory=$(free | head -2 |tail -1 | awk '{print $4}')
echo -e "$memoryUsed \t$freeMemory" > "$(date).txt"

mysql --user=root --password=Saji@1234 myproject7 << EOF
INSERT INTO MemoryTable (date,MemoryAvailable,MemoryUsed) VALUES ('$(date)','$freeMemory','$memoryUsed');
EOF




