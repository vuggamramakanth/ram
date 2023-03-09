from app.views import *
from django.urls import path
app_name='sai'
urlpatterns=[
    path('kanth/',kanth,name='kanth'),
]