from django.urls import path 
from  .views import profile_upload

urlpatterns = [
    
    path('upload/', profile_upload, name="profile_upload"),
]