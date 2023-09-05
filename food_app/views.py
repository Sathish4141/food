from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ItemSerializer
from .models import Items
from rest_framework import status,serializers
# Create your views here.

@api_view(['GET'])
def index(request):
    data = {"message":"index page working successfully"}

    return Response(data)

@api_view(['POST'])
def create(request):
    item = ItemSerializer(data = request.data)
    
    if Items.objects.filter(**request.data).exists():
        raise serializers.ValidationError('data already present')

    if item.is_valid():
        item.save()
        return Response(item.data)

    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

    

@api_view(['GET'])
def view_all(request):
    
    if request.query_params:
        item = Items.objects.filter(**request.query_params.dict())
        serializer = ItemSerializer(item,many = True)
        return Response(serializer.data)
    else:
        item = Items.objects.all()
    if item:
        serializer = ItemSerializer(item,many = True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['PUT'])
def update(request,id):
    item = Items.objects.get(id = id)
    data = ItemSerializer(instance=item,data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

@api_view(["DELETE"])
def delete(request,id):
    item = get_object_or_404(Items,id = id)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

