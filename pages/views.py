# pages/views.py
from django.http import HttpResponse


def home_page_view(request):
    return HttpResponse("Hello from the Platform.sh project!!!")