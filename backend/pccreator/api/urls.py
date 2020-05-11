from django.urls import path
from api import views

urlpatterns = [
    path('pcs/', views.pc_list),
    # path('pcs/<int:pk>/', views.snippet_detail),
]