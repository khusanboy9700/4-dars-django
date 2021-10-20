from django.urls import path
from .views import HomapageView

urlpatterns = [
    path('', HomapageView.as_view(), name='home')
]
