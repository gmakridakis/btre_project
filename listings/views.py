import keyword
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from listings.models import Listing
from listings.choices import bedroom_choices, state_choices, price_choices

def index(request):
    listings = Listing.objects.order_by("-price")
    paginator = Paginator(listings, 3)
    page = request.GET.get("page")
    paginated_listing = paginator.get_page(page)
    context = {"listings": paginated_listing}

    return render(request, 'listings/listings.html', context)

def listing(request ,listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {"listing": listing}
    return render(request, 'listings/listing.html', context)

def search(request):

    queryset = Listing.objects.order_by("-list_date")

    if "keywords" in request.GET and request.GET["keywords"]:
        queryset = queryset.filter(description__icontains=request.GET["keywords"])


    if "bedrooms" in request.GET and request.GET["bedrooms"]:
        queryset = queryset.filter(bedrooms__lte=request.GET["bedrooms"])



    listings = queryset

    context = {
        "listings": listings,
        "state_choices": state_choices,
        "bedroom_choices": bedroom_choices,
        "price_choices": price_choices
    }

    return render(request, 'listings/search.html', context)