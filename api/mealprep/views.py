from rest_framework import viewsets

# Create your views here.
from .models import MealPlan
from .serializers import MealPlanSerializer


class MealPlanViewSet(viewsets.ModelViewSet):
    queryset = MealPlan.objects.all().order_by('-date')
    serializer_class = MealPlanSerializer
