from django.shortcuts import render
from .models import ChatRoom,CharMessage

# Create your views here.

def index(request):
    chatrooms = ChatRoom.objects.all()
    return render(request,'chatapp/index.html',{"chatrooms":chatrooms})


def chatRoom(request,slug):
    chat = ChatRoom.objects.get(slug=slug)
    message = CharMessage.objects.filter(room=chat)[0:30]
    return render(request,'chatapp/room.html',{"chat":chat,'message':message})