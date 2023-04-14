from django.urls import path
from .import views

urlpatterns = [
    path('resume/', views.profileview.as_view(), name='resume'),
    path('list/', views.profileview.as_view(), name='list'),
    path('all/', views.profileview.as_view(), name='all'),
   
]