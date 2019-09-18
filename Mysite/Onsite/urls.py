from django.urls import path
from . import views


urlpatterns =[
    path('home/',views.home),
    path('index/',views.index),
    path('show/',views.show),
    path('Manju/',views.Manju),
    path('edit/',views.edit),
    path('form1/',views.form1),
    path('Bhumi/',views.Bhumi),
    path('info/',views.req),
    path('setsession/',views.setsession),
    path('getsession/',views.getsession),
    path('csv/',views.getfile),
    path('cs/',views.getfile),
    path('pdf/',views.pdffile),
    path('boot/',views.boot),
]