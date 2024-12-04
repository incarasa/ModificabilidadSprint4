from django.urls import path
from . import views

urlpatterns = [
    path('cronogramas-con-pagos/', views.cronogramas_con_pagos, name='cronogramas_con_pagos'),
    path('estudiantes-con-cronogramas/', views.estudiantes_con_cronogramas, name='estudiantes_con_cronogramas'),
]