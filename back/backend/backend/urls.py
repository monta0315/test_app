from django.urls import path, include

urlpatterns = [
    path('', include('back_app.urls')),
]
