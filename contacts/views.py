from django.shortcuts import redirect, render
from django.contrib import messages
from btre.settings import EMAIL_HOST_USER
from contacts.models import Contact
from django.core.mail import send_mail

# Create your views here.


def contact(request):
    if request.method == "POST":
        
        listing_id = request.POST["listing_id"]
        listing = request.POST["listing"]
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]
        user_id = request.POST["user_id"]
        realtor_email = request.POST["realtor_email"]

        if request.user.is_authenticated:
            user_id=request.POST["user_id"] #request.user_id

            if Contact.objects.all().filter(user_id=user_id, listing_id=listing_id).exists():
                print("You have already made an inquiry for this listing")
                messages.error(request, "You have already made an inquiry for this listing")
                return redirect("/listings/"+listing_id)

        contact=Contact(
            listing=listing,
            listing_id=listing_id,
            name=name,
            email=email,
            phone=phone,
            message=message,
            user_id=user_id
        )

        contact.save()

        send_mail(
            subject="Property listing inquiry",
            message="Your request has been sumbitted!",
            from_email=EMAIL_HOST_USER,
            recipient_list=[email]
        )

        print("Your request has been sumbitted!")
        messages.success(request, "Your request has been sumbitted!")
        return redirect("/listings/"+listing_id)
