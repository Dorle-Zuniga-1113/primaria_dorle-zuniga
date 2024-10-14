from django.urls import path, include
from alumno_app import views
urlpatterns = [
    path('', views.index_vista,name="index_vista"),
]