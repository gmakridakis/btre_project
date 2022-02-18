from django.shortcuts import redirect, render
from django.contrib import messages
from contacts.models import Contact

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

            import pdb; pdb.set_trace()
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

        print("Your request has been sumbitted!")
        messages.success(request, "Your request has been sumbitted!")
        return redirect("/listings/"+listing_id)
