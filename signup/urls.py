from django.urls import path
from .views import signupview   
urlpatterns = [
    path('signup/', signupview.as_view(), name='signup'),
]
