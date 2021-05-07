from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead
from .forms import LeadModelForm
from django.shortcuts import redirect

def leads_list(request):
    leads = Lead.objects.all()
    context = {"leads":leads}
    return render(request, "leads/leads_list.html", context)

def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead":lead
    }
    return render(request, "leads/lead_detail.html", context)

def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "form":form
    }            
    return render(request,"leads/lead_create.html",context)