from django.urls import path
from .views import DayListView

urlpatterns = [
    path("", DayListView.as_view(), name="home")
]