from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chat.urls')),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get_messages/<int:recipient_id>/', views.get_messages, name='get_messages'),
]

from django.urls import path
from . import views

urlpatterns = [
    path("chat/<str:room_name>/", views.chat_room, name="chat_room"),
]






