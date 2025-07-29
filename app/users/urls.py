from django.urls import path
from .views import login_, logout_, userProfileEdit, changePassword

app_name = 'user'

urlpatterns = [
    path('login/', login_, name='login'),
    path('logout/', logout_, name='logout'),
    path('profile/', userProfileEdit, name='profile'),
    path('password/', changePassword, name='changePassword'),
]