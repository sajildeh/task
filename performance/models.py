from django.conf import settings
from django.db import models
from django.urls import reverse

from rest_framework.reverse import reverse as api_reverse

import pymysql.cursors 
import os
import subprocess


import psutil

class CPUAvg(models.Model):
  db_table = 'CPUAvg'
  id=models.AutoField(primary_key=True,null=False);
  date=models.CharField(max_length=100,default=0);
  cpuAvgColumn=models.FloatField(default=0)
  
  class Meta:
        verbose_name = "CPUAvg"
        verbose_name_plural = "CPUAvgs"
        db_table = 'CPUAvg'
        
  def __unicode__(self):
        return  self.id


class MemoryAvg(models.Model):
  db_table = 'MemoryAvg'
  id=models.AutoField(primary_key=True,null=False);
  date=models.CharField(max_length=100,default=0);
  AvgMemoryAvailable=models.FloatField(default=0)
  AvgMemoryFree=models.FloatField(default=0)
  
  class Meta:
        verbose_name = "MemoryAvg"
        verbose_name_plural = "MemoryAvgs"
        db_table = 'MemoryAvg'
        
  def __unicode__(self):
        return  self.id

class DiskAvg(models.Model):
  db_table = 'DiskAvg'
  id=models.AutoField(primary_key=True,null=False);
  date=models.CharField(max_length=100,default=0);
  AvgDiskAvailable=models.FloatField(default=0)
  AvgDiskFree=models.FloatField(default=0)
  
  class Meta:
        verbose_name = "DiskAvg"
        verbose_name_plural = "DiskAvgs"
        db_table = 'DiskAvg'
        
  def __unicode__(self):
        return  self.id 
        

  


















