from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello")


def detail(request, vitals_id):
    return HttpResponse(f"Vitals {vitals_id}")


def enter_vitals(request, vitals_id):
    return HttpResponse(f"Entering {vitals_id}")
