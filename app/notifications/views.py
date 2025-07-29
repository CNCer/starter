from django.shortcuts import render, redirect
from .models import Msg


def getmessagesforuser(user):
    totalMsg = 0
    unreadMsg = 0
    msgs = Msg.objects.filter(user = user).order_by( '-seen', '-timestamp')
    if msgs is not None:
        for msg in msgs:
            totalMsg += 1
            if msg.seen ==False:
                unreadMsg += 1

    return totalMsg, unreadMsg, msgs


def notifications_get (request):
    totalMsg, unreadMsg, msgs = getmessagesforuser(request.user)
    contest = {
        'totalmsg':totalMsg,
        'unread':unreadMsg,
        'msgs':msgs,
    }
    return render(request, 'notifications/notification.html', contest)

def notification_delete (request,pk):
    try:
        msg = Msg.objects.get(pk = pk)
        msg.delete()
    except Msg.DoesNotExist:
        pass
    return render(request, 'common/empty.html')
    #return redirect("notifications:index")
    


def notification_markRead (request,pk):
    try:
        msg = Msg.objects.get(pk = pk)
        msg.seen = True
        msg.save()
    except Msg.DoesNotExist:
        pass
    return render(request, 'notifications/notificationlistelement.html', {'msg':msg})

def notification_markUnread (request,pk):
    try:
        msg = Msg.objects.get(pk = pk)
        msg.seen = False
        msg.save()
    except Msg.DoesNotExist:
        pass
    return render(request, 'notifications/notificationlistelement.html', {'msg':msg})


