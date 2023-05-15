from django.urls import path
from . import views
app_name = "app"
urlpatterns = [
    path('', views.index , name='index'),
    path('generate/', views.generate, name='generate'),
    path('edit/', views.edit, name='edit'),
]
