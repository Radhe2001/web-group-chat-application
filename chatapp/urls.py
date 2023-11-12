from django.urls import path,include
from .views import index,chatRoom

urlpatterns = [
    path('',index,name='index'),
    path('<slug:slug>/',chatRoom,name="chatRoom")
]
