
from django.contrib import admin
from django.urls import path , include, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    # Your stuff: custom urls includes go here
    path('', include('dashboard.urls', namespace = 'dashboard') ),
    path('user/', include('users.urls', namespace = 'user') ),
    path('notifications/', include('notifications.urls', namespace = 'notifications') ),
    # Media files
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]

if settings.DEBUG:
    
    if 'rosetta' in settings.INSTALLED_APPS:
        urlpatterns += [
            re_path(r'^rosetta/', include('rosetta.urls')),
        ]

    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [
            path("__debug__/", include(debug_toolbar.urls)),
            *urlpatterns,
        ]
