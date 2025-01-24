from django.urls import path
from .views import MissionSearchView

urlpatterns = [
    path('search', MissionSearchView.as_view(), name='mission_search'),
]
