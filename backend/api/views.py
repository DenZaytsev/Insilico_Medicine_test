from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, get_object_or_404
from .models import House, OrderBrick
from rest_framework.response import Response
from .serializers import HomeCreateSerializer, AddBricksSerializer


class BaseView(APIView):
    pass


class HomeCreateView(BaseView, CreateAPIView):
    http_method_names = ['post']
    serializer_class = HomeCreateSerializer


class AddBricksView(BaseView):
    serializer_class = AddBricksSerializer

    def post(self, request, pk):
        serializer = AddBricksSerializer(data=request.POST)
        house = get_object_or_404(House, id=pk)

        if serializer.is_valid(raise_exception=True):
            clean_data = serializer.data
            order_created_at = clean_data['created_at']
            brick_quantity = clean_data['brick_quantity']
            if order_created_at < str(house.release_date):
                data = {'message': 'Введите дату задания, которая будет позже даты создания дома!'}
                return Response(status=400, data=data)
            OrderBrick.objects.create(house=house, brick_quantity=brick_quantity, created_at=order_created_at)
            return Response(status=200)







class StatusListView(BaseView):
    pass