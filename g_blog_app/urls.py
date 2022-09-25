from django.urls import path
from .views import *

#url patterns

urlpatterns = [
    path('detail/<slug:slug>/', detailPage, name='detailPage'),
    path('', indexPage.as_view(), name='index'),
]
