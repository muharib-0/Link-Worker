from django.urls import path
from .views import loginview, signupview   
urlpatterns = [
    path('signup/', signupview.as_view(), name='signup'),
    path('login/', loginview.as_view(), name='login'),
]
