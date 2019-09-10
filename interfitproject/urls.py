from django.contrib import admin
from django.urls import path, include
import resumeapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',resumeapp.views.resume_index, name='resume_index'),
    path('resume_input/',resumeapp.views.resume_input, name='resume_input'),
    path('resumelist/create/',resumeapp.views.create, name="create"),
    path('accounts/' , include('accounts.urls')),
]
