from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Cliente
from .serializers import ClienteSerializer

# Create your views here.
@csrf_exempt
def clientes_list(request):
    if request.method == 'GET':
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return JsonResponse(serializer.data, safe=False)
