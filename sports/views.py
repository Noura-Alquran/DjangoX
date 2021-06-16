from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Sport


class SportListView(ListView):
    template_name = "sports/sport-list.html"
    model = Sport


class SportDetailView(DetailView):
    template_name = "sports/sport-detail.html"
    model = Sport


class SportCreateView(CreateView):
    template_name = "sports/sport-create.html"
    model = Sport
    fields = ['player_name','coach_s_name','description']


class SportUpdateView(UpdateView):
    template_name = "sports/sport-update.html"
    model = Sport
    fields = ['description']


class SportDeleteView(DeleteView):
    template_name = "sports/sport-delete.html"
    model = Sport
    success_url = reverse_lazy("sport_list")
