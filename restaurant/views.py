from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FoodCategory
from .serializers import FoodListSerializer


class FoodsListView(APIView):
    def get(self, request):
        try:
            categories = FoodCategory.objects.filter(foods__is_publish=True).prefetch_related('foods').distinct()
            serializer = FoodListSerializer(categories, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
