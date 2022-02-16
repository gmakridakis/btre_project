from django.shortcuts import render
import contacts

from contacts.models import Contact

# Create your views here.


def contact(request):
    if request.method == "POST":
        listing_id = request.POST["listing_id"]
        listing = request.POST["listing"]
        #name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]
        user_id = request.POST["user_id"]
        realtor_email = request.POST["realtor_email"]

        contact=Contact(
            listing=listing,
            listing_id=listing_id,
            name="TEST",
            email=email,
            phone=phone,
            message=message,
            user_id=user_id
        )

        contact.save()

        print("Contact IS N O W saved")