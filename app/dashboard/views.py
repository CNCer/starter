from django.shortcuts import render
from notifications.views import getmessagesforuser 

import logging
db_logger = logging.getLogger('db')

# Create your views here.
def home (request):
    totalMsg, unreadMsg, msgs = getmessagesforuser(request.user)
    contest = {
        'totalmsg':totalMsg,
        'unread':unreadMsg,
        'msgs':msgs,
    }
    db_logger.info("site visited - info")
    db_logger.warning("site visited - warnning")
    db_logger.error ("site visited - error")
    return render(request, 'dashboard/dashboard.html', contest)


