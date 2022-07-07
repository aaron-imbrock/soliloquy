from django.views.generic import ListView
from .models import DayView, Task

# Create your views here.


class TodayListView(ListView):
    model = DayView
    template_name = "home.html"
