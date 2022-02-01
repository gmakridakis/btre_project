from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing

def index(request):
    listings = Listing.objects.all().order_by("-list_date").filter(is_published=True)

    #if listings:
    #    return render(request, "pages/index.html", listings)
    #else:
    return render(request, "pages/index.html")

def about(request):
    return render(request, "pages/about.html")