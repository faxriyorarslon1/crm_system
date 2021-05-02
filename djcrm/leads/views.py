from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead


def index(request):
    leads = Lead.objects.all()
    context = {"leads":leads}
    return render(request, "leads/leads_list.html", context)