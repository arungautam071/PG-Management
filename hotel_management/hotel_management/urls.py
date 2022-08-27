#--------django default imports--------#

from os import stat
from re import template
from django.contrib import admin
from django.urls import path, include

#--------View import--------#

from user_management import views as user_views
from user_management.views import (
    ComplaintDetailView,
    ComplaintUpdateView,
    ComplaintDeleteView,
    UserComplainListView,
)
from user_request.views import WashingDetailView,WashingDeleteView,WashingUpdateView
#--------Lgoin & Logout--------#
from django.contrib.auth import views as auth_views

#--------For Media Static Files--------#
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',user_views.index,name='index-page'),
    path('home/',user_views.home,name='home-page'),
    path('price/',user_views.pricing,name='room-price'),
    path('user/<str:username>', UserComplainListView.as_view(), name='user-complain'),
    path('complaint/<int:pk>/', ComplaintDetailView.as_view(), name='Complaint-detail'),
    path('complaint/<int:pk>/update/', ComplaintUpdateView.as_view(), name='Complaint-update'),
    path('complaint/<int:pk>/delete/', ComplaintDeleteView.as_view(), name='Complaint-delete'),
    path('washing_request_manage/<int:pk>/', WashingDetailView.as_view(), name='washing-detail'),
    path('washing_request_manage/<int:pk>/update/', WashingUpdateView.as_view(), name='washing-update'),
    path('washing_request_manage/<int:pk>/delete/', WashingDeleteView.as_view(), name='washing-delete'),
    path('register/',user_views.register,name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/',auth_views.LoginView.as_view(template_name='user_management/login.html'),name='Login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='user_management/logout.html'),name='Logout'),
    path('', include('services_management.urls')),
    path('user/', include('user_request.urls')),
    path('user/', include('room_management.urls')),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)