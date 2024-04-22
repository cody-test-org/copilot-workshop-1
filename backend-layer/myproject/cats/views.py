#from django.http import JsonResponse
#from django.db import connection

#def cats(request):
#    with connection.cursor() as cursor:
#        cursor.execute("SELECT * FROM cats")
#        row = cursor.fetchall()
#    return JsonResponse({'cats': cats})

from rest_framework import viewsets
from .models import Cat
from .serializers import CatSerializer

class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    
# Insert Cat into Database with User Defined Parameters
def insert_cat(request):
    if request.method == 'POST':
        cat_name = request.POST.get('name')
        cat_breed = request.POST.get('breed')
        cat_age = request.POST.get('age')
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO cats(name, breed, age) VALUES (%s, %s, %s)", [cat_name, cat_breed, cat_age])
    return JsonResponse({'status': 'success'})