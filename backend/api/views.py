from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, get_object_or_404
from .models import House, OrderBrick, get_stats
from rest_framework.response import Response
from .serializers import HomeCreateSerializer, AddBricksSerializer


class BaseView(APIView):
    """ Вьюха отлавливает все неотловленные ошибки."""

    def dispatch(self, request, *args, **kwargs):
        try:
            response = super().dispatch(request, *args, **kwargs)
        except Exception as e:
            return self._response({'errorMassege': str(e)}, status=400)

        if isinstance(response, (dict, list)):
            return self._response(response)
        else:
            return response

    @staticmethod
    def _response(data, *, status=200):
        return JsonResponse(data=data, status=status)


class HomeCreateView(BaseView, CreateAPIView):
    """Вью для создание дома в базе."""
    http_method_names = ['post']
    serializer_class = HomeCreateSerializer


class AddBricksView(BaseView):
    """ Положить N кирпичей в дом с pk=id в момент времени T."""
    serializer_class = AddBricksSerializer

    def post(self, request, pk):
        serializer = AddBricksSerializer(data=request.POST)
        house = get_object_or_404(House, id=pk)

        if serializer.is_valid(raise_exception=True):

            order_created_at, brick_quantity = serializer.data['created_at'], serializer.data['brick_quantity']

            if order_created_at < str(house.release_date):
                data = {'errorMassege': 'Введите дату задания, которая будет позже даты создания дома!'}
                return Response(status=400, data=data)

            OrderBrick.objects.create(house=house, brick_quantity=brick_quantity, created_at=order_created_at)
            return Response(status=200)


class StatusListView(BaseView):
    """Статистику по всем существующим домам.
    Показывает сколько в каждом лежит кирпичей с группировкой по датам. Также необходимо вывести адрес дома.
    """

    def get(self, request):
        data = get_stats()
        return Response(status=200, data=data)


