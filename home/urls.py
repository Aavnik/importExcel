from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
   path('',views.excelfile),
   path('export_excel', views.export_excel, name='export_excel')
]