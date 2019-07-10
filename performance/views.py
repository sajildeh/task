from django.shortcuts import render
from rest_framework import viewsets

from .models import CPUAvg
from .serializers import CPUAvgSerializer

from .models import MemoryAvg
from .serializers import MemoryAvgSerializer

from .models import DiskAvg
from .serializers import DiskAvgSerializer

from django.shortcuts import render
import os
from rest_framework.views import APIView, Response
import psutil
import subprocess

class CPUAvgView(viewsets.ModelViewSet):
    queryset = CPUAvg.objects.all()
    serializer_class = CPUAvgSerializer
   
class MemoryAvgView(viewsets.ModelViewSet):
    queryset = MemoryAvg.objects.all()
    serializer_class = MemoryAvgSerializer

class DiskAvgView(viewsets.ModelViewSet):
    queryset = DiskAvg.objects.all()
    serializer_class = DiskAvgSerializer
    
#class CPUView(APIView):
#    def get(self, request, format=None):
#        cpuU=round(float(os.popen('''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' ''').readline()),2)
#        memoryU=psutil.virtual_memory()[3]
#        diskU=psutil.disk_usage('/')[1]
#        outputData={
#          "CPU usage": cpuU,
#          "Memory used": memoryU, 
#          "Disk used": diskU
#          }
#        return Response(str(outputData))

class CPUView(APIView):
    
    def get(self, request, format=None):
           
        outputData={
        
            "CPU usage": "{0:.2f}".format(100.0-float(os.popen("(mpstat | head -4 | tail -1 | awk '{print $13}')").read())),
            "Memory used": "{0:.5f}".format(int(os.popen("(free | head -2 | tail -1 | awk '{print $3}')").read()) /(1024.0 ** 3)), 
            "Disk used": "{0:.5f}".format(int(os.popen("(df --total | tail -n 1 | awk '{print $3}')").read()) /(1024.0 ** 3))
            }
        return Response(str(outputData))
      
      
      

