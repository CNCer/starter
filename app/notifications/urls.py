from django.urls import path
from .views import notifications_get, notification_delete, notification_markRead, notification_markUnread

app_name = 'notifications'

urlpatterns = [
    path('', notifications_get, name='index'),
    path('delete/<int:pk>/', notification_delete, name='delete'),
    path('markread/<int:pk>/', notification_markRead, name='markread'),
    path('markunread/<int:pk>/', notification_markUnread, name='markunread'),

]