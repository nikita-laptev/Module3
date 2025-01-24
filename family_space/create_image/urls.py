from django.urls import path
from .views import LunarWatermarkView

urlpatterns = [
    path('lunar-watermark/', LunarWatermarkView.as_view(), name='lunar_watermark'),
]
