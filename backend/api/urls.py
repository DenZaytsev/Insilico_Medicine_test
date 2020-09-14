from django.urls import path
from .views import HomeCreateView, AddBricksView, StatusListView


urlpatterns = [
    path('building/', HomeCreateView.as_view()),
    path('building/<int:pk>/add-bricks/', AddBricksView.as_view()),
    path('status/', StatusListView.as_view()),

]