from rest_framework import serializers

from .models import CPUAvg
from .models import MemoryAvg
from .models import DiskAvg




class CPUAvgSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPUAvg
        fields = '__all__'

class MemoryAvgSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemoryAvg
        fields = '__all__'

class DiskAvgSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiskAvg
        fields = '__all__'

class CPUSerializer(serializers.Serializer):

   cpuC = serializers.IntegerField()