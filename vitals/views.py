from django.http import HttpResponse
from django.shortcuts import render

from .models import Vitals


def index(request):
    latest_vitals_list = Vitals.objects.order_by('-date_time')[:10]
    context = {'latest_vitals_list': latest_vitals_list}
    return render(request, 'vitals/index.html', context)


def detail(request, vitals_id):
    return HttpResponse(f"Vitals {vitals_id}")


def enter_vitals(request, vitals_id):
    return HttpResponse(f"Entering {vitals_id}")
