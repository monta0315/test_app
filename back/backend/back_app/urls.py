from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from back_app import views

urlpatterns = [
    path('luck/', views.res_luck),
]

urlpatterns = format_suffix_patterns(urlpatterns)
