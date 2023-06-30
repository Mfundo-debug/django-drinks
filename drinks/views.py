from .models import Drink
from .serializers import DrinkSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



@api_view(['GET', 'POST'])
def drink_list(request, format=None):
    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return JsonResponse({"drinks": serializer.data}, safe=False)
    
    elif request.method == 'POST':
        drink = request.data.get('drink')
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            drink_saved = serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, pk, format=None):
    try:
        drink = Drink.objects.get(pk=pk)
    except Drink.DoesNotExist:
        return JsonResponse({'message': 'The drink does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return JsonResponse(serializer.data)
    
    
    elif request.method == 'DELETE':
        drink.delete()
        return JsonResponse({'message': 'Drink was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)