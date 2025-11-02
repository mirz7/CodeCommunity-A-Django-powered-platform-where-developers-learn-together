from django.shortcuts import render,redirect
from .models import Room,Topic
from .form import Roomform
from django.db.models import Q
# rooms = [
#     {'id':1,'name':'Lets learn Python!'},
#     {'id':2,'name':'Design with me'},
#     {'id':3,'name':'Frontend Developers'},  ]

def home(request):
    q = request.GET.get('q') if request.GET.get('q')!= None else ''

    rooms = Room.objects.filter(Q(topic__name__icontains=q)|
                                Q(name__icontains=q) |
                                Q(description__icontains=q) )
    topics = Topic.objects.all()
    room_count = rooms.count()
    context = {'rooms':rooms,'topics':topics ,'room_count':room_count}
    

    
    return render(request,'base/home.html',context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    
    context = {'room':room}

    return render(request,'base/room.html',context)
def createRoom(request):
    if request.method == 'POST':
        print(request.POST)
        form = Roomform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = Roomform()
    context = {'form': form}

    return render(request,'base/room_form.html',context)

def updateRoom(request,pk):
    
    room = Room.objects.get(id=pk)
    form = Roomform(instance=room)
    context = {'form':form}

    if request.method =='POST':
        print(request.POST)
        form = Roomform(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')


    return render(request,'base/room_form.html',context)

def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request,'base/delete.html',{'obj':room})
