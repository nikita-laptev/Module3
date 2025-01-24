from django.urls import path
from .views import LunarMissionsView

urlpatterns = [
    path('lunar-missions', LunarMissionsView.as_view(), name='lunar_missions'),
    path('lunar-missions/<int:mission_id>', LunarMissionsView.as_view(), name='delete_lunar_mission'),
]
