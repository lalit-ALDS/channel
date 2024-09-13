from django.shortcuts import render


def index(request):
    return render(request, template_name='index.html')


def room(request, room_name):
    return render(request, template_name='chatroom.html', context={
        'room_name': room_name
    })