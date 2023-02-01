from django.urls import path
from .views import InputValueView, OutputValueView

urlpatterns = [
    # path('', index, name='index'),
    # path('last_input/', InputValueView.as_view(), name='get_last_input')
    path('', InputValueView.as_view(), name='input_value'),
    path('output', OutputValueView.as_view(), name='output_value')
]
