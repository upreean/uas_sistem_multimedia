from django.urls import path

from . import views

urlpatterns = [
    path("discreatecosine/", views.dct),
    path("discreateforier/", views.dft),
    path("", views.index),
    # path("resize/", views.resize)
]