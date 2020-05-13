from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from api import views

urlpatterns = [
    path('api/pcs/', views.PcList.as_view()),
    path('api/pcs/<int:pk>/', views.PcDetail.as_view()),

    path('api/user/', include(('user.urls', 'user'))),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
