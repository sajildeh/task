from django.urls import path, include
from django.conf.urls import url
from .views import CPUAvgView
from .views import MemoryAvgView
from .views import DiskAvgView
from .views import CPUView

urlpatterns = [
    url(r'CPU/', CPUAvgView.as_view({'get': 'list'})),
    url(r'Memory/', MemoryAvgView.as_view({'get': 'list'})),
    url(r'Disk/', DiskAvgView.as_view({'get': 'list'})),
    url(r'CPUOnline/', CPUView.as_view()),
    
    
]
