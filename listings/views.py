from django.core.paginator import Paginator
from django.shortcuts import render
from listings.models import Listing

def index(request):
    listings = Listing.objects.order_by("-price")
    paginator = Paginator(listings, 3)
    page = request.GET.get("page")
    paginated_listing = paginator.get_page(page)
    context = {"listings": paginated_listing}

    return render(request, 'listings/listings.html', context)

def listing(request ,listing_id):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')