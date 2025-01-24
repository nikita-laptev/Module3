from django.urls import path
from .views import CosmicObjectListView, CosmicObjectDetailView

urlpatterns = [
    path('api/cosmic-objects/', CosmicObjectListView.as_view(), name='cosmic-object-list'),
    path('api/cosmic-objects/<int:pk>/', CosmicObjectDetailView.as_view(), name='cosmic-object-detail'),
]
