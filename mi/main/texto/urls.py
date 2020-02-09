from django.conf.urls import url,re_path
from django.urls import path, include
from texto import views

urlpatterns =[

url(r'primero/',views.primero,name="primero"),
url(r'segundo/',views.segundo,name="segundo"),
url(r'tercero/',views.tercero,name="tercero"),
url(r'cuarto/',views.cuarto,name="cuarto"),
url(r'quinto/',views.quinto,name="quinto"),
url(r'escapa/',views.escapa,name="escapa"),
url(r'final/',views.final,name="final"),

]