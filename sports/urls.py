from django.urls import path
from .views import SportListView, SportDetailView, SportCreateView, SportUpdateView, SportDeleteView

urlpatterns = [
    path('', SportListView.as_view(), name='sport_list'),
    path('<int:pk>/', SportDetailView.as_view(), name='sport_detail'),
    path('create/', SportCreateView.as_view(), name='sport_create'),
    path('<int:pk>/update/', SportUpdateView.as_view(), name='sport_update'),
    path('<int:pk>/delete/', SportDeleteView.as_view(), name='sport_delete'),

]