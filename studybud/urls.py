from django.contrib import admin
# from django.http import HttpResponse
from django.urls import include, path

# def home(request):
#     return HttpResponse('Home page')

# def room(request):
#     return HttpResponse('ROOM')


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home),
    # path('room/', room),
    path('', include('base.urls'))
]
