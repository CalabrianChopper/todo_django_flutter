from django.urls import path
from .views import TodoGetCreate, TodoUpdateOrDelete

urlpatterns = [
    path("", TodoGetCreate.as_view()),
    path("<int:pk>/", TodoUpdateOrDelete.as_view()),
]
