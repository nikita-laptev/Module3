from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import CosmicObject
from .serializers import CosmicObjectSerializer

class CosmicObjectListView(generics.ListCreateAPIView):
    serializer_class = CosmicObjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CosmicObject.objects.filter(user=self.request.user)  # Фильтр по пользователю

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Сохраняем пользователя при создании

class CosmicObjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CosmicObject.objects.all()
    serializer_class = CosmicObjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)  # Ограничиваем доступ только к объектам текущего пользователя

