from django.urls import path
from .views import InputValueView

urlpatterns = [
    path('', InputValueView.as_view(), name='input_value'),
]
