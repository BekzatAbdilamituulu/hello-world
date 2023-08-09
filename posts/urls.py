from django.urls import path
from .views import *

app_name = 'posts'

urlpatterns = [
    path('', HomePageView.as_view(), name='home_p'),
]