from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MessageViewSet, UserViewSet, LoginView, LogoutView

router = DefaultRouter()
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserViewSet.as_view({'post': 'create'}), name='register'),
]

