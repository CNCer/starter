from django.shortcuts import render
from notifications.views import getmessagesforuser 

# Create your views here.
def home (request):
    totalMsg, unreadMsg, msgs = getmessagesforuser(request.user)
    contest = {
        'totalmsg':totalMsg,
        'unread':unreadMsg,
        'msgs':msgs,
    }
    return render(request, 'dashboard/dashboard.html', contest)


